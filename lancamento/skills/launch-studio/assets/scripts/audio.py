#!/usr/bin/env python3
"""
launch-studio · audio.py
Música original, efeitos sonoros e grelha de batida — só com Python 3, sem instalar nada.
Original music, sound effects and beat grid — Python 3 standard library only.

Subcomandos / subcommands:
  batida  gera uma base musical original (WAV estéreo 48 kHz)
  sons    gera efeitos sonoros originais (clique, toque, pop, whoosh, ding, tecla, impacto, sucesso)
  pista   coloca sons (ou frases de voz) nos tempos certos numa só pista, opcionalmente sobre a música
  grelha  imprime a grelha de batidas e compassos (segundos e fotogramas)

Exemplos / examples:
  python3 audio.py batida --estilo pop --bpm 120 --compassos 10 --tom la --modo menor --saida musica.wav
  python3 audio.py sons --saida sons/
  python3 audio.py pista --duracao 20 --eventos "0.5:pop,2:whoosh:-6" --pasta sons --saida sons-pista.wav
  python3 audio.py grelha --bpm 120 --duracao 20 --fps 30

Tudo o que este script gera é original e pode ser usado livremente (MIT, como o resto da skill).
Everything this script generates is original and free to use (MIT, like the rest of the skill).
"""

import argparse
import array
import math
import os
import random
import sys
import wave

SR = 48000
TAU = 2.0 * math.pi

# ---------------------------------------------------------------- utilidades


def zeros(n):
    return array.array("d", bytes(8 * max(0, int(n))))


def db(x):
    return 10.0 ** (x / 20.0)


def midi_hz(m):
    return 440.0 * 2.0 ** ((m - 69) / 12.0)


class Mix:
    """Buffer estéreo em float."""

    def __init__(self, seconds):
        self.n = int(round(seconds * SR))
        self.L = zeros(self.n)
        self.R = zeros(self.n)

    def add(self, sig, t, gain=1.0, pan=0.0):
        """Soma um sinal mono em t segundos. pan: -1 esquerda, 0 centro, 1 direita."""
        o = int(round(t * SR))
        if o >= self.n:
            return
        a = (pan + 1.0) * math.pi / 4.0
        gl, gr = math.cos(a) * gain * 1.4142, math.sin(a) * gain * 1.4142
        L, R = self.L, self.R
        start = max(0, -o)
        end = min(len(sig), self.n - o)
        for i in range(start, end):
            s = sig[i]
            L[o + i] += s * gl
            R[o + i] += s * gr

    def add_stereo(self, sl, sr_, t, gain=1.0):
        o = int(round(t * SR))
        L, R = self.L, self.R
        start = max(0, -o)
        end = min(len(sl), self.n - o)
        for i in range(start, end):
            L[o + i] += sl[i] * gain
            R[o + i] += sr_[i] * gain

    def fade_out(self, seconds):
        k = int(seconds * SR)
        for i in range(max(0, self.n - k), self.n):
            g = (self.n - i) / float(k)
            self.L[i] *= g
            self.R[i] *= g

    def fade_in(self, seconds):
        k = int(seconds * SR)
        for i in range(min(k, self.n)):
            g = i / float(k)
            self.L[i] *= g
            self.R[i] *= g


def peak(*chans):
    p = 0.0
    for c in chans:
        for s in c:
            a = s if s >= 0 else -s
            if a > p:
                p = a
    return p


def dc_block(c):
    """Filtro passa-alto muito baixo (~4 Hz): tira desvios de corrente contínua."""
    prev_x, prev_y = 0.0, 0.0
    for i in range(len(c)):
        x = c[i]
        y = x - prev_x + 0.9995 * prev_y
        prev_x, prev_y = x, y
        c[i] = y


def finish(L, R, peak_db=-1.0, drive=1.0):
    """Corta o desvio DC, aplica saturação suave e normaliza o pico."""
    dc_block(L)
    dc_block(R)
    if drive > 0:
        for c in (L, R):
            for i in range(len(c)):
                c[i] = math.tanh(c[i] * drive)
    p = peak(L, R)
    if p > 0:
        g = db(peak_db) / p
        for c in (L, R):
            for i in range(len(c)):
                c[i] *= g


def limit(L, R, ceiling_db=-1.0):
    """Só baixa se passar do teto (não sobe o volume)."""
    p = peak(L, R)
    c = db(ceiling_db)
    if p > c:
        g = c / p
        for ch in (L, R):
            for i in range(len(ch)):
                ch[i] *= g


def write_wav(path, L, R):
    d = os.path.dirname(os.path.abspath(path))
    os.makedirs(d, exist_ok=True)
    out = array.array("h", bytes(2 * 2 * len(L)))
    j = 0
    for i in range(len(L)):
        a = int(max(-1.0, min(1.0, L[i])) * 32767.0)
        b = int(max(-1.0, min(1.0, R[i])) * 32767.0)
        out[j] = a
        out[j + 1] = b
        j += 2
    if sys.byteorder == "big":
        out.byteswap()
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(out.tobytes())


def read_wav(path):
    """Lê WAV PCM 8/16/24/32 bits, mono ou estéreo; devolve (L, R) a 48 kHz."""
    with wave.open(path, "rb") as w:
        ch, sw, fr, n = w.getnchannels(), w.getsampwidth(), w.getframerate(), w.getnframes()
        raw = w.readframes(n)
    total = n * ch
    vals = zeros(total)
    if sw == 2:
        a = array.array("h")
        a.frombytes(raw)
        if sys.byteorder == "big":
            a.byteswap()
        for i in range(total):
            vals[i] = a[i] / 32768.0
    elif sw == 1:
        for i in range(total):
            vals[i] = (raw[i] - 128) / 128.0
    elif sw == 3:
        for i in range(total):
            b = raw[3 * i:3 * i + 3]
            v = int.from_bytes(b, "little", signed=True)
            vals[i] = v / 8388608.0
    elif sw == 4:
        a = array.array("i")
        a.frombytes(raw)
        if sys.byteorder == "big":
            a.byteswap()
        for i in range(total):
            vals[i] = a[i] / 2147483648.0
    else:
        raise SystemExit("Formato WAV não suportado: %s" % path)
    L = zeros(n)
    R = zeros(n)
    for i in range(n):
        L[i] = vals[i * ch]
        R[i] = vals[i * ch + (1 if ch > 1 else 0)]
    if fr != SR:
        L, R = resample(L, fr), resample(R, fr)
    return L, R


def resample(x, fr):
    ratio = fr / float(SR)
    m = int(len(x) / ratio)
    y = zeros(m)
    for i in range(m):
        p = i * ratio
        k = int(p)
        f = p - k
        a = x[k] if k < len(x) else 0.0
        b = x[k + 1] if k + 1 < len(x) else a
        y[i] = a + (b - a) * f
    return y


# ---------------------------------------------------------------- instrumentos


def env_exp(n, decay):
    """Envolvente exponencial (decay em segundos até ~-60 dB)."""
    k = math.log(1000.0) / max(1e-4, decay * SR)
    return [math.exp(-k * i) for i in range(n)]


def kick(dur=0.38, f0=150.0, f1=45.0, drive=1.0):
    n = int(dur * SR)
    s = zeros(n)
    ph = 0.0
    for i in range(n):
        t = i / SR
        f = f1 + (f0 - f1) * math.exp(-t * 28.0)
        ph += TAU * f / SR
        a = math.exp(-t * 9.0)
        s[i] = math.tanh(math.sin(ph) * a * (1.0 + drive))
    for i in range(min(n, 120)):  # pequeno clique de ataque
        s[i] += (1 - i / 120.0) * 0.25
    return s


def noise_burst(dur, decay, rng, hp=0, color=0.0):
    """Ruído com decaimento; hp = nº de diferenciações (agudos); color = suavização (graves)."""
    n = int(dur * SR)
    s = zeros(n)
    k = math.log(1000.0) / max(1e-4, decay * SR)
    prev = 0.0
    for i in range(n):
        x = rng.uniform(-1, 1)
        if color > 0:
            prev = prev + (x - prev) * (1.0 - color)
            x = prev
        s[i] = x * math.exp(-k * i)
    for _ in range(hp):
        last = 0.0
        for i in range(n):
            cur = s[i]
            s[i] = cur - last
            last = cur
    return s


def snare(rng, dur=0.22):
    n = int(dur * SR)
    s = noise_burst(dur, 0.16, rng, hp=1)
    ph = 0.0
    for i in range(n):
        ph += TAU * 185.0 / SR
        s[i] = s[i] * 0.7 + math.sin(ph) * math.exp(-i / SR * 30.0) * 0.5
    return s


def clap(rng):
    n = int(0.25 * SR)
    s = zeros(n)
    for off in (0.0, 0.011, 0.022):
        b = noise_burst(0.2 - off, 0.12 if off == 0.022 else 0.02, rng, hp=1)
        o = int(off * SR)
        for i in range(len(b)):
            if o + i < n:
                s[o + i] += b[i] * 0.6
    return s


def hat(rng, dur=0.06, open_=False):
    return noise_burst(0.3 if open_ else dur, 0.22 if open_ else dur * 0.8, rng, hp=3)


def tone(freq, dur, wave_="sine", attack=0.005, decay=0.3, sustain=0.0, release=0.05,
         harmonics=None, detune=0.0, vibrato=0.0):
    """Nota sintetizada com envolvente ADSR simples."""
    n = int((dur + release) * SR)
    s = zeros(n)
    na, nd, nr = max(1, int(attack * SR)), max(1, int(decay * SR)), max(1, int(release * SR))
    nsus = int(dur * SR)

    def level(i):
        if i < na:
            return i / na
        if i < na + nd:
            return 1.0 - (1.0 - sustain) * (i - na) / nd
        return sustain

    rel_level = level(nsus)
    ph, ph2 = 0.0, 0.0
    f2 = freq * (1.0 + detune)
    for i in range(n):
        t = i / SR
        f = freq * (1.0 + vibrato * math.sin(TAU * 5.0 * t))
        ph += TAU * f / SR
        ph2 += TAU * f2 / SR
        if wave_ == "sine":
            v = math.sin(ph)
            if harmonics:
                for h, amp in harmonics:
                    v += amp * math.sin(ph * h)
        elif wave_ == "tri":
            x = (ph / TAU) % 1.0
            v = 4.0 * abs(x - 0.5) - 1.0
        elif wave_ == "square":
            v = 1.0 if (ph / TAU) % 1.0 < 0.5 else -1.0
            v *= 0.5
        else:  # saw (aproximada por harmónicos para não serrilhar)
            v = 0.0
            for h in range(1, 7):
                if freq * h > 12000:
                    break
                v += math.sin(ph * h) / h
            v *= 0.6
        if detune:
            v = 0.5 * v + 0.5 * math.sin(ph2)
        if i < nsus:
            e = level(i)
        else:
            e = rel_level * max(0.0, 1.0 - (i - nsus) / nr)
        s[i] = v * e
    return s


def pluck(freq, dur, rng, bright=0.5):
    """Karplus-Strong: corda dedilhada barata e bonita."""
    p = max(2, int(SR / freq))
    buf = [rng.uniform(-1, 1) for _ in range(p)]
    n = int(dur * SR)
    s = zeros(n)
    damp = 0.496 + 0.0035 * bright
    idx = 0
    for i in range(n):
        a = buf[idx]
        b = buf[(idx + 1) % p]
        buf[idx] = (a + b) * damp
        s[i] = a
        idx = (idx + 1) % p
    lp = 0.0
    for i in range(n):  # suaviza
        lp += (s[i] - lp) * (0.35 + 0.5 * bright)
        s[i] = lp
    return s


def lowpass(s, amount):
    lp = 0.0
    for i in range(len(s)):
        lp += (s[i] - lp) * amount
        s[i] = lp
    return s


# ---------------------------------------------------------------- harmonia

NOTES = {"do": 0, "c": 0, "do#": 1, "c#": 1, "reb": 1, "db": 1, "re": 2, "d": 2, "re#": 3, "d#": 3,
         "mib": 3, "eb": 3, "mi": 4, "e": 4, "fa": 5, "f": 5, "fa#": 6, "f#": 6, "solb": 6, "gb": 6,
         "sol": 7, "g": 7, "sol#": 8, "g#": 8, "lab": 8, "ab": 8, "la": 9, "a": 9, "la#": 10, "a#": 10,
         "sib": 10, "bb": 10, "si": 11, "b": 11}
SCALES = {"maior": [0, 2, 4, 5, 7, 9, 11], "menor": [0, 2, 3, 5, 7, 8, 10]}

STYLES = {
    #        bpm  progressão maior   progressão menor   sétimas
    "pop":   (120, [0, 4, 5, 3], [0, 5, 2, 6], False),
    "calmo": (72, [0, 3, 5, 4], [0, 5, 3, 4], True),
    "epico": (90, [0, 5, 3, 4], [0, 5, 2, 6], False),
    "retro": (150, [0, 5, 3, 4], [0, 6, 5, 4], False),
    "caos":  (150, [0, 4, 5, 3], [0, 0, 5, 6], False),
    "lofi":  (75, [1, 4, 0, 0], [0, 3, 6, 2], True),
}


def chord_notes(root_midi, scale, degree, sevenths):
    out = []
    for k in (0, 2, 4, 6) if sevenths else (0, 2, 4):
        d = degree + k
        out.append(root_midi + scale[d % 7] + 12 * (d // 7))
    return out


# ---------------------------------------------------------------- batida


def cmd_batida(a):
    style = a.estilo
    if style not in STYLES:
        raise SystemExit("Estilo desconhecido. Usa: " + ", ".join(STYLES))
    bpm_default, prog_maj, prog_min, sevenths = STYLES[style]
    bpm = a.bpm or bpm_default
    mode = a.modo or ("maior" if style in ("pop", "retro", "calmo") else "menor")
    if mode not in SCALES:
        raise SystemExit("Modo: maior ou menor")
    key = a.tom.lower()
    if key not in NOTES:
        raise SystemExit("Tom desconhecido: %s (ex.: do, re, mi, fa, sol, la, si, ou c d e f g a b, com # ou b)" % a.tom)
    scale = SCALES[mode]
    prog = prog_maj if mode == "maior" else prog_min
    root = 48 + NOTES[key]  # oitava 3
    rng = random.Random(a.semente)
    beat = 60.0 / bpm
    bar = 4 * beat
    bars = a.compassos
    extra = bar * (1.25 if a.final else 0.25)
    mix = Mix(bars * bar + extra)

    # one-shots
    K = kick(drive=1.6 if style == "caos" else 0.8, f0=170 if style == "epico" else 150)
    S = snare(rng)
    C = clap(rng)
    H = hat(rng)
    HO = hat(rng, open_=True)
    TOM = kick(dur=0.6, f0=140, f1=70, drive=0.3)

    swing = beat / 6.0 if style == "lofi" else 0.0

    for b in range(bars):
        t0 = b * bar
        degree = prog[b % len(prog)]
        notes = chord_notes(root, scale, degree, sevenths)
        bass_note = notes[0] - 12 if style != "epico" else notes[0] - 24
        last_bar = (b == bars - 1)
        build = b / max(1, bars - 1)  # 0..1 ao longo do tema

        # ------------------------- percussão
        if style in ("pop", "caos"):
            for q in range(4):
                mix.add(K, t0 + q * beat, 0.9)
            for q in (1, 3):
                mix.add(C if style == "pop" else S, t0 + q * beat, 0.45, 0.05)
            step = 4 if style == "caos" else 2
            for e in range(4 * step):
                mix.add(H, t0 + e * beat / step, 0.16 if e % 2 else 0.22, 0.35)
        elif style == "lofi":
            mix.add(K, t0, 0.7)
            mix.add(K, t0 + 2.5 * beat, 0.55)
            mix.add(S, t0 + beat, 0.28)
            mix.add(S, t0 + 3 * beat, 0.28)
            for e in range(8):
                mix.add(H, t0 + e * beat / 2 + (swing if e % 2 else 0), 0.10, 0.3)
        elif style == "retro":
            for q in (0, 2):
                mix.add(noise_burst(0.12, 0.08, rng, color=0.85), t0 + q * beat, 0.5)
            for q in (1, 3):
                mix.add(noise_burst(0.15, 0.1, rng, hp=1), t0 + q * beat, 0.35)
            for e in range(8):
                mix.add(noise_burst(0.03, 0.02, rng, hp=2), t0 + e * beat / 2, 0.12, -0.3)
        elif style == "epico":
            mix.add(K, t0, 0.9)
            if build > 0.3:
                mix.add(TOM, t0 + 2 * beat, 0.6, -0.2)
            if build > 0.6:
                for q in range(4):
                    mix.add(TOM, t0 + q * beat + beat / 2, 0.35, 0.2)
                mix.add(S, t0 + 3 * beat, 0.35)
        elif style == "calmo":
            if b % 2 == 1:
                mix.add(noise_burst(0.5, 0.4, rng, hp=3), t0 + 2 * beat, 0.05, 0.4)

        # ------------------------- baixo
        if style in ("pop", "lofi"):
            for q in (0, 2.5) if style == "lofi" else (0, 1.5, 2, 3.5):
                n = tone(midi_hz(bass_note), beat * 0.9, "sine", 0.005, 0.25, 0.6, 0.06,
                         harmonics=[(2, 0.3), (3, 0.1)])
                mix.add(n, t0 + q * beat, 0.42)
        elif style == "caos":
            for e in range(8):
                n = tone(midi_hz(bass_note + (12 if e % 4 == 3 else 0)), beat * 0.45, "saw", 0.003, 0.1, 0.5, 0.03)
                for i in range(len(n)):
                    n[i] = math.tanh(n[i] * 3.0) * 0.5
                mix.add(n, t0 + e * beat / 2, 0.38)
        elif style == "retro":
            for e in range(8):
                n = tone(midi_hz(bass_note + (7 if e % 4 == 2 else 0)), beat * 0.4, "tri", 0.002, 0.1, 0.7, 0.02)
                mix.add(n, t0 + e * beat / 2, 0.45)
        elif style == "epico":
            n = tone(midi_hz(bass_note), bar * 0.95, "saw", 0.08, 0.5, 0.7, 0.3)
            mix.add(lowpass(n, 0.04), t0, 0.7)
        elif style == "calmo":
            n = tone(midi_hz(bass_note), bar * 0.9, "sine", 0.3, 0.6, 0.6, 0.5)
            mix.add(n, t0, 0.32)

        # ------------------------- acordes
        if style in ("calmo", "epico", "lofi", "pop"):
            for k, m in enumerate(notes):
                if style == "lofi":
                    for q in (0, 1.5):
                        n = tone(midi_hz(m + 12), beat * 1.2, "sine", 0.01, 0.6, 0.35, 0.2,
                                 harmonics=[(2, 0.15)], vibrato=0.002)
                        mix.add(n, t0 + q * beat, 0.11, -0.4 + 0.27 * k)
                elif style == "pop":
                    for q in range(8):
                        if q in (0, 3, 4, 6):
                            n = tone(midi_hz(m + 12), beat * 0.35, "tri", 0.004, 0.15, 0.3, 0.05)
                            mix.add(n, t0 + q * beat / 2, 0.07, -0.3 + 0.3 * k)
                else:
                    n = tone(midi_hz(m + 12), bar, "tri", 0.5 if style == "calmo" else 0.25, 0.8, 0.7,
                             0.6, detune=0.004)
                    mix.add(n, t0, 0.12 if style == "calmo" else 0.10, -0.5 + 0.33 * k)

        # ------------------------- arpejos / melodia
        if style in ("pop", "retro", "caos"):
            per = 8 if style == "pop" else 16
            pattern = rng.choice(["up", "down", "updown", "random"])
            pool = [n + 24 for n in notes] + [notes[0] + 36]
            for e in range(per):
                if style == "pop" and rng.random() < 0.25:
                    continue
                if pattern == "up":
                    m = pool[e % len(pool)]
                elif pattern == "down":
                    m = pool[-1 - (e % len(pool))]
                elif pattern == "updown":
                    cyc = pool + pool[-2:0:-1]
                    m = cyc[e % len(cyc)]
                else:
                    m = rng.choice(pool)
                dt = bar / per
                if style == "retro":
                    n = tone(midi_hz(m), dt * 0.8, "square", 0.002, 0.05, 0.6, 0.01)
                    mix.add(n, t0 + e * dt, 0.10, 0.2 if e % 2 else -0.2)
                elif style == "caos":
                    n = tone(midi_hz(m), dt * 0.7, "saw", 0.002, 0.05, 0.4, 0.01)
                    mix.add(n, t0 + e * dt, 0.06, 0.4 if e % 2 else -0.4)
                else:
                    n = pluck(midi_hz(m), dt * 2.5, rng, bright=0.6)
                    mix.add(n, t0 + e * dt, 0.22, 0.25 if e % 2 else -0.25)
        elif style in ("calmo", "lofi"):
            pool = [n + 24 for n in notes]
            for q in range(0, 4, 2 if style == "calmo" else 1):
                if rng.random() < (0.5 if style == "calmo" else 0.35):
                    m = rng.choice(pool)
                    n = pluck(midi_hz(m), beat * 2.5, rng, bright=0.3)
                    mix.add(n, t0 + q * beat + (swing if style == "lofi" else 0), 0.2, rng.uniform(-0.4, 0.4))

        # ------------------------- subida antes do fim (épico, caos, pop)
        if last_bar and style in ("epico", "caos", "pop") and not a.final:
            sw = noise_burst(bar, bar * 4, rng, hp=1)
            for i in range(len(sw)):
                sw[i] *= (i / len(sw)) ** 2
            mix.add(sw, t0, 0.12)

    # ---------------------------------------------- acorde final
    if a.final:
        t0 = bars * bar
        notes = chord_notes(root, scale, 0, sevenths)
        mix.add(kick(dur=1.2, f0=120, f1=38, drive=0.5), t0, 0.9)
        mix.add(noise_burst(0.8, 0.6, rng, color=0.6), t0, 0.12)
        for k, m in enumerate(notes):
            n = tone(midi_hz(m + 12), bar * 0.8, "tri", 0.01, 1.2, 0.5, 0.6, detune=0.004)
            mix.add(n, t0, 0.12, -0.4 + 0.3 * k)
            mix.add(pluck(midi_hz(m + 24), bar, rng, bright=0.5), t0 + k * 0.03, 0.18, -0.3 + 0.3 * k)
        mix.add(tone(midi_hz(notes[0] - 12), bar * 0.8, "sine", 0.01, 1.0, 0.5, 0.6), t0, 0.4)

    if style == "lofi":  # crepitar de disco
        for i in range(0, mix.n, 7):
            if rng.random() < 0.004:
                v = rng.uniform(-0.25, 0.25)
                mix.L[i] += v
                mix.R[i] += v * 0.8
            mix.L[i] += rng.uniform(-0.004, 0.004)

    mix.fade_in(0.01)
    mix.fade_out(0.35 if a.final else min(1.5, bar / 2))
    finish(mix.L, mix.R, peak_db=-1.0, drive=1.1)
    write_wav(a.saida, mix.L, mix.R)
    total = mix.n / SR
    print("OK %s — estilo %s, %s %s, %d BPM, %d compassos%s, %.2f s"
          % (a.saida, style, a.tom, mode, bpm, bars, " + final" if a.final else "", total))
    print("Batida = %.3f s · compasso = %.3f s · a 30 fps: %.2f fotogramas por batida"
          % (beat, bar, 30 * beat))


# ---------------------------------------------------------------- sons


def cmd_sons(a):
    rng = random.Random(a.semente)
    out = a.saida
    os.makedirs(out, exist_ok=True)
    made = {}

    # clique: curto e seco
    s = noise_burst(0.012, 0.004, rng, hp=2)
    t = tone(2200, 0.01, "sine", 0.0005, 0.008, 0, 0.002)
    for i in range(len(t)):
        if i < len(s):
            s[i] = s[i] * 0.5 + t[i] * 0.5
    made["clique"] = s

    # toque: tap suave, ligeiramente descendente
    n = int(0.06 * SR)
    s = zeros(n)
    ph = 0.0
    for i in range(n):
        tt = i / SR
        ph += TAU * (900 - 3000 * tt) / SR
        s[i] = math.sin(ph) * math.exp(-tt * 70)
    nb = noise_burst(0.01, 0.004, rng, hp=1)
    for i in range(len(nb)):
        s[i] += nb[i] * 0.2
    made["toque"] = s

    # pop: bolha a subir
    n = int(0.12 * SR)
    s = zeros(n)
    ph = 0.0
    for i in range(n):
        tt = i / SR
        f = 320 + 900 * (1 - math.exp(-tt * 60))
        ph += TAU * f / SR
        s[i] = math.sin(ph) * math.exp(-tt * 35) * min(1.0, i / 60.0)
    made["pop"] = s

    # whoosh: ruído com filtro a abrir e fechar (estéreo, da esquerda para a direita)
    dur = 0.5
    n = int(dur * SR)
    wl, wr = zeros(n), zeros(n)
    lp = 0.0
    for i in range(n):
        x = i / n
        envv = math.sin(math.pi * x) ** 2
        cut = 0.01 + 0.25 * math.sin(math.pi * x) ** 3
        lp += (rng.uniform(-1, 1) - lp) * cut
        v = lp * envv * 3.0
        wl[i] = v * math.cos(x * math.pi / 2)
        wr[i] = v * math.sin(x * math.pi / 2)
    made["whoosh"] = (wl, wr)

    # ding: sino
    n = int(1.4 * SR)
    s = zeros(n)
    for f, amp, dec in ((1318.5, 1.0, 1.3), (1318.5 * 2.76, 0.4, 0.5), (1318.5 * 5.4, 0.15, 0.25), (659.25, 0.3, 1.0)):
        ph = 0.0
        k = math.log(1000.0) / (dec * SR)
        for i in range(n):
            ph += TAU * f / SR
            s[i] += math.sin(ph) * amp * math.exp(-k * i)
    made["ding"] = s

    # tecla: teclado
    s = noise_burst(0.03, 0.008, rng, hp=2)
    th = tone(140, 0.02, "sine", 0.001, 0.02, 0, 0.005)
    for i in range(len(th)):
        if i < len(s):
            s[i] = s[i] * 0.6 + th[i] * 0.5
    made["tecla"] = s

    # impacto: boom grave + ar
    s = kick(dur=1.4, f0=110, f1=36, drive=0.6)
    nb = noise_burst(0.9, 0.7, rng, color=0.75)
    for i in range(len(nb)):
        s[i] += nb[i] * 0.35
    made["impacto"] = s

    # sucesso: duas notas a subir (dó6 → sol6)
    s = zeros(int(0.9 * SR))
    for k, (m, off) in enumerate(((84, 0.0), (91, 0.09))):
        p = pluck(midi_hz(m), 0.8, rng, bright=0.8)
        o = int(off * SR)
        for i in range(len(p)):
            if o + i < len(s):
                s[o + i] += p[i] * 0.8
        tn = tone(midi_hz(m), 0.3, "sine", 0.002, 0.4, 0.0, 0.2)
        for i in range(len(tn)):
            if o + i < len(s):
                s[o + i] += tn[i] * 0.3
    made["sucesso"] = s

    for name, sig in made.items():
        if isinstance(sig, tuple):
            L, R = sig
        else:
            L, R = array.array("d", sig), array.array("d", sig)
        finish(L, R, peak_db=-9.0, drive=0.0)  # ficam por baixo da música
        write_wav(os.path.join(out, name + ".wav"), L, R)
    print("OK %d sons em %s: %s" % (len(made), out, ", ".join(sorted(made))))
    print("Gerados a -9 dBFS de pico, para ficarem por baixo da música. Originais — uso livre.")


# ---------------------------------------------------------------- pista


def parse_num(x):
    return float(str(x).replace(",", "."))


def cmd_pista(a):
    mix = Mix(a.duracao)
    if a.base:
        bl, br = read_wav(a.base)
        mix.add_stereo(bl, br, 0.0, db(a.ganho_base))
    cache = {}
    count = 0
    for item in [e.strip() for e in a.eventos.split(",") if e.strip()] if a.eventos else []:
        # tempo:som[:ganho_dB] — tempos com ponto decimal (0.5), porque a vírgula separa eventos
        parts = item.split(":")
        if len(parts) < 2:
            raise SystemExit("Evento inválido: %r (usa tempo:som[:ganho_dB])" % item)
        t = parse_num(parts[0])
        name = parts[1]
        gain = parse_num(parts[2]) if len(parts) > 2 else 0.0
        path = name if (os.sep in name or name.lower().endswith(".wav")) else os.path.join(a.pasta, name + ".wav")
        if not os.path.exists(path):
            raise SystemExit("Som não encontrado: %s" % path)
        if path not in cache:
            cache[path] = read_wav(path)
        L, R = cache[path]
        mix.add_stereo(L, R, t, db(gain))
        count += 1
    if a.base:
        finish(mix.L, mix.R, peak_db=-1.0, drive=1.0)
    else:
        limit(mix.L, mix.R, -1.0)
    write_wav(a.saida, mix.L, mix.R)
    print("OK %s — %d eventos, %.2f s%s" % (a.saida, count, a.duracao, " sobre " + a.base if a.base else ""))


# ---------------------------------------------------------------- grelha


def cmd_grelha(a):
    beat = 60.0 / a.bpm
    fpb = a.fps * beat
    print("BPM %g · batida %.3f s · compasso %.3f s · %g fps → %.3f fotogramas por batida%s"
          % (a.bpm, beat, 4 * beat, a.fps, fpb,
             "" if abs(fpb - round(fpb)) < 1e-9 else "  (não é inteiro: os cortes vão arredondar)"))
    print("%-9s %-8s %-10s %s" % ("compasso", "batida", "segundos", "fotograma"))
    i = 0
    while True:
        t = i * beat
        if t > a.duracao + 1e-9:
            break
        bar, b = divmod(i, 4)
        mark = "  ◀ início de compasso" if b == 0 else ""
        print("%-9d %-8d %-10.3f %d%s" % (bar + 1, b + 1, t, int(round(t * a.fps)), mark))
        i += 1


# ---------------------------------------------------------------- main


def main():
    p = argparse.ArgumentParser(description="launch-studio · música, efeitos e grelha (só Python 3).")
    sub = p.add_subparsers(dest="cmd")

    b = sub.add_parser("batida", help="gera uma base musical original")
    b.add_argument("--estilo", default="pop", help="pop, calmo, epico, retro, caos, lofi")
    b.add_argument("--bpm", type=float, default=0, help="andamento (por defeito, o do estilo)")
    b.add_argument("--compassos", type=int, default=10, help="nº de compassos de 4 tempos")
    b.add_argument("--tom", default="la", help="do, re, mi, fa, sol, la, si (ou c..b), com # ou b")
    b.add_argument("--modo", default="", help="maior ou menor (por defeito, o do estilo)")
    b.add_argument("--semente", type=int, default=1, help="muda a melodia mantendo o estilo")
    b.add_argument("--final", action="store_true", help="acrescenta um compasso com acorde final")
    b.add_argument("--saida", default="musica.wav")

    s = sub.add_parser("sons", help="gera efeitos sonoros originais")
    s.add_argument("--saida", default="sons")
    s.add_argument("--semente", type=int, default=1)

    t = sub.add_parser("pista", help="coloca sons nos tempos certos")
    t.add_argument("--duracao", type=float, required=True)
    t.add_argument("--eventos", default="", help='"tempo:som[:ganho_dB],..." ex.: "0.5:pop,2:whoosh:-6"')
    t.add_argument("--pasta", default="sons", help="pasta dos sons (nome sem .wav)")
    t.add_argument("--base", default="", help="WAV por baixo (ex.: a música) — opcional")
    t.add_argument("--ganho-base", dest="ganho_base", type=float, default=0.0)
    t.add_argument("--saida", default="pista.wav")

    g = sub.add_parser("grelha", help="mostra a grelha de batidas")
    g.add_argument("--bpm", type=float, required=True)
    g.add_argument("--duracao", type=float, default=20)
    g.add_argument("--fps", type=float, default=30)

    a = p.parse_args()
    if a.cmd == "batida":
        cmd_batida(a)
    elif a.cmd == "sons":
        cmd_sons(a)
    elif a.cmd == "pista":
        cmd_pista(a)
    elif a.cmd == "grelha":
        cmd_grelha(a)
    else:
        p.print_help()


if __name__ == "__main__":
    main()
