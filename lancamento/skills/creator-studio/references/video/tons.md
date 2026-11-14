# Tons

Um tom muda o ritmo, a escrita, as letras, as transições e o som. Os tons são pontos de partida: uma direção livre do utilizador ("como um anúncio de perfume", "lançamento falso de 2016", "documentário sobre a natureza") **afina ou substitui** o tom. Nesse caso escolhe o tom mais próximo para o ritmo e a estrutura, e guarda a frase do utilizador no plano.

Aceita os nomes em português, em inglês e os do /brag.

| Tom | Também aceita | Numa frase | Cenas em ~20 s |
|---|---|---|---|
| `natural` | `default` | alegre, limpo, fácil de partilhar | 4–5 |
| `premium` | `polished`, `elegant` | sério, contido, confiante | 3–4 |
| `lancamento-serio` | `yc-parody`, `keynote` | uma ideia pequena apresentada como um marco da humanidade | 4–5 |
| `caos` | `chaotic`, `hype` | rápido, alto, exagerado | 6–8 |
| `seco` | `deadpan`, `dry` | calmo, frio, nada é uma piada | 3–4 |
| `trailer` | `cinematic`, `epic` | escala de cinema, frases grandes | 4–5 |
| `loja` | `app-store`, `clean` | cartões de funcionalidades, polido | 4–6 |
| `devlog` | `indie`, `behind-the-scenes` | honesto, de quem fez, com bastidores | 4–5 |
| `tutorial` | `how-to` | "faz assim", três passos e o resultado | 4–5 |
| `retro` | `8-bit`, `vhs`, `arcade` | nostalgia de pixel, VHS ou arcada | 5–6 |
| `acolhedor` | `cozy`, `calm` | suave, quente, sem pressa | 3–4 |

Escolher sem indicação: produto sério ou pago → `premium` ou `loja`; projeto engraçado ou absurdo → `lancamento-serio` ou `seco`; jogo → `trailer`, `retro` ou `caos` conforme o jogo; ferramenta de programadores → `tutorial` ou `devlog`; bem-estar, crianças, hobbies → `acolhedor`; na dúvida → `natural`.

---

## `natural`
- **Sensação:** um amigo a mostrar uma coisa boa que fez. Confiante sem se armar.
- **Ritmo:** médio (100–120 BPM); cenas de 3–5 s; entradas rápidas, pausas para ler.
- **Letras:** as do projeto; títulos em negrito, frases curtas, minúsculas permitidas.
- **Transições:** deslizes suaves, zooms curtos, cortes na batida.
- **Som:** base alegre e leve (`audio.py batida --estilo pop`); 2–4 efeitos discretos (toque, aparecer, final).
- **Texto:** frases do próprio produto; verbos concretos.
- **Evitar:** exageros, maiúsculas a gritar, emojis em todas as cenas.

## `premium`
- **Sensação:** filme de produto discreto. Menos é mais.
- **Ritmo:** lento (72–90 BPM); planos longos, muito espaço vazio; uma frase por ecrã.
- **Letras:** finas ou serifadas elegantes, muito espaço entre letras nos títulos curtos.
- **Transições:** desvanecimentos lentos, movimentos de câmara muito suaves.
- **Som:** piano ou *pad* com pouca percussão (`--estilo calmo`); um efeito no remate, ou nenhum.
- **Evitar:** piadas, cortes rápidos, cores saturadas que o produto não usa.

## `lancamento-serio`
- **Sensação:** a apresentação mais solene do mundo para algo pequeno ou absurdo. A graça está em nunca piscar o olho.
- **Ritmo:** estruturado (90–100 BPM); uma afirmação por cena, pausa dramática antes do nome.
- **Letras:** sóbrias, centradas, grandes.
- **Transições:** cortes secos, ecrãs de texto branco sobre preto ou sobre a cor da marca.
- **Som:** base séria, um "impacto" grave no nome e no remate.
- **Texto:** frases solenes e verdadeiras ("Durante séculos, a humanidade dividiu contas à mão.") — o exagero está no tom, nunca em factos inventados.
- **Evitar:** números falsos de investimento, logótipos de investidores ou de imprensa.

## `caos`
- **Sensação:** anúncio de jogo para telemóvel com café a mais. TUDO EM MAIÚSCULAS.
- **Ritmo:** muito rápido (140–150 BPM); algumas cenas com menos de 2 s; cortes em cada batida.
- **Letras:** pesadas, enormes, inclinadas; contorno ou sombra dura.
- **Transições:** *flashes*, zooms bruscos, tremer de câmara curto.
- **Som:** batida densa (`--estilo caos`), efeitos frequentes mas baixos na mistura.
- **Cuidado:** mesmo aqui, o texto tem de se ler — entra a gritar e fica parado. Evita *flashes* intensos repetidos (sensibilidade à luz): nunca mais de 3 por segundo.

## `seco`
- **Sensação:** humor de cara séria. Calmo, quase aborrecido de propósito.
- **Ritmo:** lento (72–90 BPM); planos longos, uma palavra de cada vez, muito vazio.
- **Letras:** simples, pequenas para o tamanho do ecrã, alinhadas à esquerda.
- **Transições:** cortes secos ou desvanecimentos lentos.
- **Som:** quase nada — uma base baixíssima ou silêncio e um único efeito seco no fim.
- **Texto:** frases factuais, curtas, sem pontos de exclamação. "Isto divide contas. Só isso."

## `trailer`
- **Sensação:** trailer de cinema. Frases curtas e épicas, câmara a mover.
- **Ritmo:** começa lento e cresce (90–120 BPM, com subida); ecrãs pretos entre frases.
- **Letras:** grandes, condensadas ou serifadas de cinema, espaçadas.
- **Transições:** cortes para preto, revelações com luz, zooms lentos que aceleram.
- **Som:** `--estilo epico` (graves longos, tambores a crescer, impacto no título).
- **Texto:** "Este verão..." só se for verdade e com graça. O remate é o título + onde jogar/descarregar.

## `loja`
- **Sensação:** página da App Store em movimento. Limpo, claro, útil.
- **Ritmo:** médio (100–120 BPM); um cartão por funcionalidade, cada um com captura real.
- **Letras:** as do sistema (SF Pro, Roboto) ou as do produto; títulos curtos em negrito.
- **Transições:** deslizes laterais, cartões que entram uns sobre os outros.
- **Som:** base alegre e limpa; um toque suave por cartão.
- **Bom para:** reaproveitar como vídeo de pré-visualização (se só usar gravações do ecrã da app).

## `devlog`
- **Sensação:** "fiz isto em 3 semanas — eis como ficou". Autêntico, com bastidores.
- **Ritmo:** médio; mistura código ou esboços com o resultado final.
- **Letras:** monoespaçada para notas, a do produto para o resultado.
- **Transições:** cortes simples, "antes / depois" lado a lado.
- **Som:** base leve (`--estilo lofi`), som de teclado discreto.
- **Texto:** primeira pessoa, números reais (dias, linhas, versões) só se o utilizador os confirmar.
- **Pergunta antes:** se o utilizador quer aparecer (cara, voz, nome) — por defeito, não.

## `tutorial`
- **Sensação:** "em 15 segundos aprendes a usar isto".
- **Ritmo:** claro e regular (100–120 BPM); passos numerados; cada passo com tempo de leitura folgado.
- **Letras:** legíveis, números grandes (1, 2, 3).
- **Transições:** deslizes na mesma direção (a avançar), destaque do sítio onde se toca.
- **Som:** base discreta, um clique por passo.
- **Bom para:** ferramentas, CLIs (com o terminal reconstruído), extensões.

## `retro`
- **Sensação:** cartucho de 8 bits, cassete VHS ou máquina de arcada — escolhe uma época e mantém-na.
- **Ritmo:** animado (120–150 BPM); texto a piscar com moderação.
- **Letras:** pixel ou de época (confirma a licença da fonte).
- **Transições:** varrimentos de linhas, "glitch" leve, ecrã de "PRESS START".
- **Som:** `--estilo retro` (ondas quadradas, arpejos, ruído para percussão).
- **Bom para:** jogos e projetos com estética de pixel. Não imites ecrãs, personagens ou sons de jogos existentes.

## `acolhedor`
- **Sensação:** uma manta e um chá. Suave, quente, sem pressa.
- **Ritmo:** lento (72–90 BPM); entradas suaves, nada brusco.
- **Letras:** arredondadas, amigáveis; cores quentes do produto.
- **Transições:** desvanecimentos, movimentos lentos, pequenas ilustrações a aparecer.
- **Som:** `--estilo calmo` (pad, notas suaves), efeitos muito baixos ou nenhum.
- **Bom para:** bem-estar, hábitos, crianças, jogos calmos.

---

## Texto para partilhar, por tom

Sempre específico, 1–3 frases, pronto a publicar, sem "estou muito entusiasmado". Estruturas de partida:

- **natural:** "Fiz o [nome]: [o que faz, com as palavras do projeto]. [A melhor frase do produto.]"
- **premium:** "[Nome]. [A frase de apresentação do projeto.] [Onde.]"
- **lancamento-serio:** "Durante demasiado tempo, [problema dito com toda a seriedade]. Hoje, isso acaba. [Nome]."
- **caos:** "[AFIRMAÇÃO VERDADEIRA EM MAIÚSCULAS]. [Nome] faz [o que faz]. Link em baixo."
- **seco:** "Fiz o [nome]. Faz [uma coisa]."
- **trailer:** "[Nome]. [Frase de apresentação.] [Data ou onde.]"
- **loja:** "O [nome] já está disponível: [funcionalidade 1], [2] e [3]."
- **devlog:** "[N] semanas depois, o [nome] está cá fora. [O que aprendi numa frase.]"
- **tutorial:** "Como [resultado] em 3 passos com o [nome]:"
- **retro:** "PRESS START: o [nome] já se pode jogar. [Plataforma.]"
- **acolhedor:** "Fiz o [nome] para [momento calmo]. [O que faz, com suavidade.]"
