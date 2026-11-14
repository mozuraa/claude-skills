# Compositor (motor 🎨 Estúdio)

Um modelo de composição em HTML/CSS em que **cada fotograma é função do tempo**. Serve para pré-visualizar no browser e para capturar fotograma a fotograma.

| Ficheiro | O que é |
|---|---|
| `cena.html` | a composição: edita o objeto `COMPOSICAO` no topo (cores, fontes, cenas, elementos, legendas) |
| `capturar.mjs` | captura os fotogramas em PNG com Playwright e o Chrome/Brave/Edge que já existe |

## Usar

```bash
cp -R <skill-dir>/assets/compositor launch-output/work/compositor
# edita launch-output/work/compositor/cena.html a partir do plano.md
```

Pré-visualizar (no browser integrado ou em qualquer browser):

- `cena.html?formato=9x16&play=1` — reproduz em tempo real, ajustado à janela
- `cena.html?formato=16x9&t=6.2&guias=1` — um instante, com as zonas seguras
- `&lingua=en` troca a língua · `&legendas=1` mostra as legendas

Capturar (com autorização para `npm i playwright-core` dentro de `launch-output/work/`):

```bash
cd launch-output/work
node compositor/capturar.mjs --formato 9x16 --fps 30 --saida frames-9x16
node compositor/capturar.mjs --formato 9x16 --tempos 1.0,3.2,6.3,10 --guias --escala 0.5 --saida verificar-9x16
```

## Elementos

Todos aceitam `em` (quando entra), `ate` (quando começa a sair; por defeito, o fim da cena), `entrada` / `saida` (`sobe`, `desce`, `esquerda`, `direita`, `zoom`, `pop`, `aparece`, `escreve`, `nenhuma`), `durEntrada` / `durSaida`, `estilo` e `pos` por formato (`"9x16"`, `"1x1"`, `"16x9"`, `"4x5"` ou `"*"`), com `x`, `y`, `w`, `h` em px ou `"%"`, `ancora` (`centro`, `topo`, `base`, `esquerda`, `direita`) e qualquer propriedade de `estilo` para afinar nesse formato.

| `tipo` | Para quê | Campos próprios |
|---|---|---|
| `texto` | títulos, frases, etiquetas | `texto` (`"..."` ou `{ pt, en }`); `estilo`: `tamanho`, `peso`, `cor`, `fonte` (`titulos`/`corpo`), `alinhar`, `fundo`, `raio`, `padding`, `maiusculas` |
| `imagem` | capturas e fotogramas reais | `src`, `moldura` (`telemovel`, `browser` + `url`, ou nada), `camara: { de, para }` (zoom lento) |
| `cartao` | cartões de funcionalidade e resultados | `titulo`, `valor`, `contador`, `src`; `estilo`: `fundo`, `cor`, `raio`, `padding`, `tamanho`, `tamanhoValor` |
| `contador` | números a subir | `contador: { de, para, casas, prefixo, sufixo, atraso, dur }` (formato de número da língua) |
| `toque` | dedo/cursor a mover e a tocar | `caminho` por formato: `[{ t, x, y, toque: true }]` |
| `forma` | blocos de cor, círculos | `estilo`: `fundo`, `raio`, `circulo` |

Cores podem ser nomes de `COMPOSICAO.cores` (`"destaque"`) ou valores (`"#FF6B4A"`). Cada cena tem `fundo` e, opcionalmente, `fundoTransicao` (segundos).

## Regras

- Nada de `setTimeout`, animações CSS a correr sozinhas, vídeos a tocar ou `Math.random()` — tudo depende de `t`.
- Tudo local: fontes e imagens copiadas para `work/` (só se a licença o permitir). Nada carregado da internet durante a captura.
- Se reutilizares HTML do próprio site, tira os `<script>`.
- Uma imagem em falta aparece como um quadro às riscas com o caminho — não passa despercebida.
