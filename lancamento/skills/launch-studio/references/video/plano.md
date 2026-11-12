# Planear o vídeo

O `plano.md` é o contrato do vídeo: o que tem de dizer, com que material, em quanto tempo, e como se arruma em cada formato. Escreve-o a partir de `assets/plano-template.md`. Uma página focada; o detalhe técnico fica para a montagem.

## Índice

1. Escolher o ângulo
2. Formas de história
3. O gancho
4. Tempo de leitura e quantidade de texto
5. A grelha de batida
6. Um plano, vários formatos (zonas seguras)
7. Duas línguas
8. Guião cena a cena
9. Antes de mostrar o plano

---

## 1. Escolher o ângulo

O ângulo é a ideia que faz este vídeo ser deste projeto. Parte das 10 perguntas da inspeção e escreve uma frase: *"Mostrar que dividir a conta deixa de ser o momento constrangedor do jantar."* Bons ângulos vêm de:

- **O resultado** que a pessoa ganha (tempo, dinheiro, calma, riso).
- **O contraste** antes / depois.
- **O absurdo** do próprio projeto, levado a sério.
- **A sensação** de usar (um jogo satisfatório, uma app calma).
- **A história de quem fez** (para devlogs e projetos indie — se o utilizador quiser aparecer).

Se o utilizador pediu `--foco`, o ângulo gira à volta disso e o resto do produto fica de fora ou numa cena só.

## 2. Formas de história

Escolhe uma e diz qual no plano. São pontos de partida, não moldes.

| Forma | Esqueleto | Serve para |
|---|---|---|
| **Problema → solução** | dor reconhecível → o produto entra → resolvido → onde arranjar | utilidades, ferramentas |
| **Antes / depois** | o caos de antes → o mesmo momento com o produto | apps de organização, edição, automação |
| **Demonstração contínua** | um só fluxo real, do primeiro toque ao resultado, acelerado onde aborrece | apps com um fluxo forte e rápido |
| **Três coisas** | gancho → 3 momentos, um por cena → remate | produtos com várias funcionalidades de peso igual |
| **Lançamento a sério** | uma ideia pequena ou absurda apresentada como um grande lançamento | projetos divertidos, paródias |
| **Tutorial em 3 passos** | "faz assim" → passo 1, 2, 3 → resultado | ferramentas, CLIs, extensões |
| **Teaser** | um pormenor, uma pergunta, uma data — mostra pouco | antes de lançar, listas de espera |
| **Jogo: momento a momento** | o plano mais bonito → a mecânica → o momento tenso → o título | jogos |

## 3. O gancho

Os primeiros 2 segundos. Escreve-o antes de tudo o resto, e escreve três alternativas para escolher a melhor.

**Ganchos que funcionam:**
- **Resultado primeiro:** abrir no ecrã final ("Cada um paga 21,15 €") e depois mostrar como lá se chegou.
- **Pergunta concreta** que o público faz a si próprio ("Quem ficou de pagar o quê?").
- **Ação a meio:** o dedo já a deslizar, o texto já a escrever-se.
- **Contraste:** duas imagens lado a lado, antes e depois.
- **A frase mais forte do projeto**, em letra enorme.
- **Um número real** do produto (nunca inventado).
- **POV / situação reconhecível:** "Quando o grupo diz 'depois fazemos as contas'".
- **Movimento ou som inesperado** que pertença ao produto (a animação de vitória do jogo).

**Ganchos a evitar:** o logótipo a abrir · fundo preto a desvanecer · "Olá, eu sou..." · "Apresentamos..." · texto pequeno demais para ler no telemóvel · começar pelo nome sem dizer o que é.

## 4. Tempo de leitura e quantidade de texto

O ritmo vem de cortes e movimento; o texto fica parado o tempo suficiente.

- **Linha curta (1–3 palavras):** ~0,8–1 s parada.
- **Frase:** ~0,3 s por palavra, mínimo 1,2 s. O gancho fica mais tempo.
- Conta a partir do momento em que a linha está **toda** visível e parada, até começar a sair.
- **Máximo por ecrã:** uma ideia; em 9:16, até ~7 palavras por linha e 2–3 linhas.
- Uma cena de 3 s aguenta duas leituras curtas, não seis. Se o texto não cabe, corta texto ou divide a cena — não aceleres.
- Itens que aparecem em sequência (cartões, linhas de lista) ao ritmo da batida rápida (~0,5 s) servem para acentos, não para texto que é para ler: mostra-os depressa e deixa o conjunto parado no fim, ou usa uma batida sim, outra não.
- Tamanho mínimo de letra para telemóvel: ~48 px num vídeo 1080×1920 para texto secundário, 80–140 px para títulos.

## 5. A grelha de batida

Escolhe o andamento (BPM) **no plano** e corta tudo sobre a grelha — cenas, entradas de texto, efeitos.

- Uma batida dura `60 / BPM` segundos. Um compasso (4 batidas) dura `240 / BPM`.
- A 30 fps, uma batida tem `1800 / BPM` fotogramas. Escolhe um BPM que dê um número inteiro, para que os cortes caiam sempre num fotograma certo:

| BPM | Batida | Fotogramas (30 fps) | Compasso | Sensação |
|---|---|---|---|---|
| 72 | 0,833 s | 25 | 3,33 s | lento, calmo |
| 90 | 0,667 s | 20 | 2,67 s | descontraído |
| 100 | 0,600 s | 18 | 2,40 s | médio, confiante |
| 120 | 0,500 s | 15 | 2,00 s | animado (o mais fácil de contar) |
| 150 | 0,400 s | 12 | 1,60 s | rápido, energético |

- Durações de cena em compassos ou meios compassos: a 120 BPM, um vídeo de 20 s são 10 compassos (ex.: gancho 1 · revelação 2 · momentos 2+2+2 · remate 1).
- `python3 <skill-dir>/assets/scripts/audio.py grelha --bpm 120 --duracao 20` imprime os tempos e fotogramas de cada batida e compasso.
- Os cortes grandes caem no início de um compasso; os acentos (cartões, toques, efeitos) nas batidas.
- Se a música vier de fora, mede o BPM dela (ou pede ao utilizador) e alinha o primeiro tempo forte ao fotograma 0 — corta o início da faixa se for preciso.

## 6. Um plano, vários formatos

O guião, os tempos e o som são **iguais** em todos os formatos. Muda a **arrumação**. Desenha primeiro o 9:16 (o mais exigente) e depois diz, cena a cena, como se adapta.

| Formato | Tamanho | Onde se usa | Margens / zonas seguras (aprox.) |
|---|---|---|---|
| **9:16** | 1080×1920 | TikTok, Reels, Shorts, Stories | deixa livres ~250 px em cima, ~420 px em baixo (legendas e botões da app) e ~140 px à direita (gostos, partilhar). Texto importante no centro ~900×1250 |
| **4:5** | 1080×1350 | feed do Instagram e do LinkedIn | margem ~80 px; no Instagram a grelha do perfil corta para 3:4 ao centro |
| **1:1** | 1080×1080 | feed, X, LinkedIn | margem ~80 px |
| **16:9** | 1920×1080 | YouTube, X, sites, README, apresentações | margem ~96 px (área segura de título ~90%) |

Regras de adaptação:
- **9:16:** empilhado — texto em cima, produto (ecrã do telemóvel ou página) grande no meio.
- **1:1 / 4:5:** produto um pouco mais pequeno, texto por cima ou por baixo.
- **16:9:** lado a lado — produto num lado, texto no outro; capturas de telemóvel ficam ao centro com espaço para texto à volta, capturas de site ocupam a largura.
- Usa capturas do formato certo quando existem (captura vertical para 9:16, horizontal para 16:9) em vez de cortar uma só.
- As zonas seguras exatas mudam com as apps; no motor 🎨 Estúdio, `?guias=1` mostra-as por cima para verificares.

## 7. Duas línguas

- O guião tem o texto de cada cena em todas as línguas pedidas (`pt` / `en`). Os tempos são os mesmos.
- O português ocupa ~20–30% mais espaço do que o inglês: verifica que cabe nos dois, e se não couber encurta (não reduzas a letra abaixo do mínimo).
- Não traduzas palavra a palavra os ganchos e as piadas — adapta-os. Mantém os nomes próprios do produto.
- Cada língua gera o seu vídeo, as suas legendas `.srt` e o seu texto para partilhar.

## 8. Guião cena a cena

Para cada cena, no `plano.md`:

- **Nome e duração** (em segundos e em compassos) e o intervalo exato (ex.: `0,0–2,0 s`).
- **O que se vê**, com o material real usado (ficheiro de captura ou gravação).
- **Texto no ecrã**, por língua, e quanto tempo fica parado.
- **Movimento / interação:** o que aparece um a um, o toque ou deslize simulado, a câmara (zoom lento, deslize).
- **Arrumação** em 9:16, 1:1 e 16:9 (uma linha cada).
- **Som:** o que a música faz; efeitos (moment → som) e se cai na batida.
- **Voz** (se ligada): a frase desta cena.
- **Transição** para a seguinte: corte seco, deslize, zoom, mergulho pela cor de fundo. Cruzamentos simples entre dois ecrãs cheios ficam turvos — faz sair o antigo e entrar o novo, ou passa pela cor de fundo.

As durações somam o alvo. Conta-as.

## 9. Antes de mostrar o plano

- [ ] O gancho funciona sem som e sem saber nada do produto?
- [ ] Pelo menos metade do tempo mostra o produto real a funcionar?
- [ ] O fim diz onde se arranja?
- [ ] Todas as linhas de texto têm tempo de leitura?
- [ ] As durações somam o alvo e caem na grelha?
- [ ] Cada cena tem arrumação para cada formato pedido?
- [ ] Nenhuma alegação é inventada; nenhum dado é real e pessoal?
- [ ] A música e os sons têm origem e licença definidas?

Depois mostra ao utilizador um resumo (ângulo, gancho, tabela de cenas, tom, som) com a tua opinião — o que é mais forte, o que é risco — e pergunta se avanças para o rascunho.
