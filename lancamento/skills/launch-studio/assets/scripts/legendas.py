#!/usr/bin/env python3
"""
launch-studio · legendas.py
Converte uma tabela simples de tempos e textos num ficheiro .srt e verifica a legibilidade.
Turns a simple timing table into an .srt file and checks readability. Python 3, no dependencies.

Entrada (uma legenda por linha; linhas vazias e começadas por # são ignoradas):
    inicio | fim | texto
    0.3 | 2.0 | Quem ficou de pagar o quê?
    2,2 | 4,5 | Escreve o total. Toca em dividir.
Também aceita tabulações em vez de "|" e a tabela Markdown do plano (| 0.3 | 2.0 | texto |).
Use "\\n" no texto para forçar a mudança de linha.

Uso:
    python3 legendas.py legendas-pt.txt legendas-pt.srt
    python3 legendas.py legendas-en.txt legendas-en.srt --max-cps 17 --max-linha 42 --deslocar 0.0
"""

import argparse
import re
import sys


def parse_time(x):
    x = x.strip().replace(",", ".")
    if ":" in x:  # mm:ss.ms ou hh:mm:ss.ms
        parts = [float(p) for p in x.split(":")]
        t = 0.0
        for p in parts:
            t = t * 60 + p
        return t
    return float(x)


def fmt(t):
    t = max(0.0, t)
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return "%02d:%02d:%02d,%03d" % (h, m, s, ms)


def wrap(text, max_line):
    """Parte em até 2 linhas equilibradas, sem cortar palavras."""
    if "\\n" in text:
        return [p.strip() for p in text.split("\\n")]
    if len(text) <= max_line:
        return [text]
    words = text.split()
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        score = max(len(a), len(b))
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best[1] if best else [text]


def read_rows(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
            if re.match(r"^\|?\s*:?-{2,}", raw):  # separador de tabela Markdown
                continue
            parts = [p.strip() for p in (raw.strip("|").split("|") if "|" in raw else raw.split("\t"))]
            if len(parts) < 3:
                print("aviso: linha %d ignorada (precisa de inicio | fim | texto): %s" % (n, raw), file=sys.stderr)
                continue
            try:
                a, b = parse_time(parts[0]), parse_time(parts[1])
            except ValueError:
                continue  # cabeçalho da tabela
            text = " | ".join(parts[2:]).strip()
            rows.append((n, a, b, text))
    return rows


def main():
    p = argparse.ArgumentParser(description="Tabela de tempos → .srt, com verificação de legibilidade.")
    p.add_argument("entrada")
    p.add_argument("saida")
    p.add_argument("--max-cps", type=float, default=17.0, help="caracteres por segundo (por defeito 17)")
    p.add_argument("--max-linha", type=int, default=42, help="caracteres por linha (por defeito 42)")
    p.add_argument("--min-dur", type=float, default=1.0, help="duração mínima em segundos (por defeito 1,0)")
    p.add_argument("--deslocar", type=float, default=0.0, help="soma este valor a todos os tempos")
    a = p.parse_args()

    rows = read_rows(a.entrada)
    if not rows:
        raise SystemExit("Nenhuma legenda encontrada em %s" % a.entrada)
    rows.sort(key=lambda r: r[1])
    warnings = 0
    out = []
    prev_end = None
    for i, (line_no, start, end, text) in enumerate(rows, 1):
        start += a.deslocar
        end += a.deslocar
        lines = wrap(text, a.max_linha)
        dur = end - start
        chars = len(" ".join(lines))
        problems = []
        if dur <= 0:
            problems.append("fim antes do início")
        elif dur < a.min_dur:
            problems.append("curta demais (%.2f s < %.1f s)" % (dur, a.min_dur))
        if dur > 0 and chars / dur > a.max_cps:
            problems.append("rápida demais (%.1f car./s > %.0f) — encurta o texto ou dá mais tempo"
                            % (chars / dur, a.max_cps))
        if len(lines) > 2:
            problems.append("%d linhas (máximo 2)" % len(lines))
        for ln in lines:
            if len(ln) > a.max_linha:
                problems.append("linha com %d car. (máximo %d): %r" % (len(ln), a.max_linha, ln))
        if prev_end is not None and start < prev_end - 1e-6:
            problems.append("sobrepõe-se à anterior (começa %.2f s antes de ela acabar)" % (prev_end - start))
        for pr in problems:
            warnings += 1
            print("aviso: legenda %d (linha %d): %s" % (i, line_no, pr), file=sys.stderr)
        out.append("%d\n%s --> %s\n%s\n" % (i, fmt(start), fmt(end), "\n".join(lines)))
        prev_end = end

    with open(a.saida, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("OK %s — %d legendas, %d avisos" % (a.saida, len(out), warnings))


if __name__ == "__main__":
    main()
