# Exemplo — 🎬 Vídeo

Projeto fictício: **Migalha**, uma app web que divide a conta do jantar. Pasta com `index.html`, `app.js`, `styles.css` e um `README.md`.

---

**Utilizador:** /launch-studio

**Claude:** Vou fazer o vídeo de lançamento do Migalha. Antes, quatro escolhas rápidas:

1. **Foco** — (a) o fluxo principal: total → dividir → quanto paga cada um *(recomendo)* · (b) a gorjeta e os arredondamentos · (c) o produto todo
2. **Tom** — (a) `natural`, leve e claro *(recomendo: é uma utilidade simpática)* · (b) `lancamento-serio`, a "revolução" da divisão de contas · (c) `tutorial`, em 3 passos
3. **Formatos** — (a) os três: 9:16, 1:1 e 16:9 *(recomendo)* · (b) só vertical · (c) só horizontal
4. **Som e língua** — (a) música gerada por mim, sem voz, PT e EN *(recomendo)* · (b) música tua · (c) com a tua voz

**Utilizador:** tudo o recomendado, mas experimenta o tom `lancamento-serio`.

---

**Claude:** *(lê o código e o README, arranca o servidor local, explora no browser integrado, guarda capturas 9:16 e 16:9 com o browser sem janela)*

**As 10 perguntas**

1. Divide a conta do jantar em 3 toques, gorjeta incluída.
2. Grupos de amigos; acaba com os cinco minutos de contas no telemóvel no fim do jantar.
3. Não precisa de conta nem de instalar nada; funciona offline depois de aberto.
4. "Ninguém sai a dever 3 cêntimos." (da página inicial)
5. O número final a contar até 21,15 € com o fundo a mudar para verde.
6. Escrever 84,60 € → escolher 4 pessoas → tocar em "Dividir" → "Cada um paga 21,15 €".
7. migalha.exemplo
8. `lancamento-serio` — "a apresentação solene de uma calculadora"
9. Base séria e lenta, um impacto grave no nome e no remate.
10. "Durante séculos, a humanidade dividiu contas à mão. Até hoje."

Dados de demonstração: os valores são inventados; não há nomes nem dados pessoais no ecrã.

**Plano** (`launch-output/plano.md`) — 20 s, 90 BPM (batida 0,667 s = 20 fotogramas; compasso 2,67 s), 7,5 compassos

| # | Cena | Tempo | O que se vê | Texto PT / EN |
|---|---|---|---|---|
| 1 | Gancho | 0,0–2,7 s | fundo preto, texto solene a escrever-se | "Durante séculos, a humanidade dividiu contas à mão." / "For centuries, humanity split the bill by hand." |
| 2 | O problema | 2,7–5,3 s | gravação acelerada de alguém a fazer contas na calculadora do telemóvel | "Com resultados variáveis." / "With mixed results." |
| 3 | A revelação | 5,3–8,0 s | corte seco para a cor da marca; nome enorme | "Migalha." |
| 4 | O produto | 8,0–14,7 s | captura real em moldura de telemóvel; o total escreve-se, toque em "Dividir", o valor conta até 21,15 € | "84,60 € · 4 pessoas · 1 toque" |
| 5 | A prova | 14,7–17,3 s | o ecrã final parado, zoom lento | "Ninguém sai a dever 3 cêntimos." / "Nobody owes 3 cents." |
| 6 | Remate | 17,3–20,0 s | nome + URL em pílula | "migalha.exemplo" |

Arrumação: 9:16 empilhado (texto em cima, telemóvel ao centro) · 1:1 telemóvel à esquerda, texto à direita · 16:9 idem, com mais ar.

**A minha opinião:** o tom sério funciona porque o produto é pequeno e simpático — a graça está no contraste. O risco é a cena 2: se a gravação da calculadora parecer encenada, perde-se a graça. Proponho mantê-la curta (2,6 s) e acelerada. A cena 4 é a mais forte: é o produto a funcionar. Avanço para o rascunho?

**Utilizador:** avança.

---

**Claude:** Vejo o que existe: `ffmpeg` sim, Node sim, Brave sim, Playwright não. Uso o motor 🎨 Estúdio — preciso de instalar `playwright-core` (≈8 MB) dentro de `launch-output/work/`, sem mexer no teu projeto. Posso?

**Utilizador:** sim.

**Claude:** *(gera a música: `audio.py batida --estilo epico --bpm 90 --compassos 7 --tom re --modo menor --final` — o acorde final cai aos 18,7 s, dentro do remate, e o som é cortado aos 20 s com desvanecimento; os efeitos com `audio.py sons`; monta a pista com o impacto aos 5,3 s (o nome); edita `cena.html`; tira uma folha de contacto com guias nos três formatos)*

Encontrei e corrigi dois problemas na folha de contacto: em 9:16 o "Ninguém sai a dever 3 cêntimos." ficava na zona que o TikTok tapa em baixo (subi-o 180 px) e, em inglês, o gancho partia em três linhas (reduzi para duas, mudando a quebra). Aqui está o rascunho 9:16 (540×960, 15 fps): `launch-output/work/rascunho-9x16.mp4`. Ouve a música — eu não a consigo ouvir. Faço o render final dos três formatos, um de cada vez?

**Utilizador:** sim.

---

**Claude:** Pronto.

```
launch-output/
├── plano.md
├── video/
│   ├── launch-9x16.mp4 · launch-1x1.mp4 · launch-16x9.mp4   (20,0 s, 30 fps, H.264 + AAC)
│   ├── launch-9x16-legendado.mp4
│   ├── capa-9x16.jpg · capa-1x1.jpg · capa-16x9.jpg          (fotograma da cena 3, também no fotograma 0)
│   └── legendas-pt.srt · legendas-en.srt
├── partilhar.txt
└── creditos.md     (música e efeitos originais, gerados; fonte do sistema)
```

**Ângulo:** a apresentação mais solene do mundo para uma calculadora de contas — e o produto a funcionar no centro.

**Verifiquei:** duração e tamanho de cada ficheiro (`ffprobe`), fotogramas de todas as cenas e transições nos três formatos, legendas sem avisos. **Não verifiquei:** como soa a música (não ouço), nem como fica no telemóvel real.

`partilhar.txt`:
> Durante séculos, a humanidade dividiu contas à mão. Hoje, isso acaba. Migalha: divide a conta em 3 toques. migalha.exemplo

Quer que refaça alguma cena, experimente o tom `natural`, ou passe ao 📣 Kit de lançamento?
