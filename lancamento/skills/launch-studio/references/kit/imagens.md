# Imagens, GIF e vídeos para as lojas

Tamanhos e regras revistos em **novembro de 2026**. Para as lojas (App Store, Google Play), confirma sempre a página oficial de especificações antes de enviar — mudam com cada geração de aparelhos.

## Índice

1. Imagem OG (partilhas de links)
2. Imagem social do repositório (GitHub)
3. Miniatura (YouTube e afins) e capas verticais
4. Product Hunt
5. GIF de demonstração para o README
6. App Store: pré-visualização em vídeo e capturas
7. Google Play: gráfico de destaque, capturas e vídeo
8. Como gerar as imagens
9. Verificar

---

## 1. Imagem OG

A imagem que aparece quando alguém partilha o link do site (X, LinkedIn, WhatsApp, Slack, Discord, iMessage…).

- **1200×630** (1,91:1). PNG para texto e interface, JPG para fotografias. Idealmente **< 1 MB**.
- O essencial no centro: algumas apps cortam as margens ou mostram em quadrado.
- Conteúdo: o nome, a frase do produto (curta), uma captura real ou o momento "uau", as cores da marca. Letra grande — vai ser vista pequena.
- **Meta tags** no `<head>` do site (✋ pergunta antes de alterar o projeto):

```html
<meta property="og:title" content="Migalha — divide a conta em 3 toques">
<meta property="og:description" content="Escreve o total, toca em dividir, cada um vê quanto paga.">
<meta property="og:image" content="https://migalha.exemplo/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="O ecrã do Migalha a mostrar 21,15 € por pessoa">
<meta property="og:url" content="https://migalha.exemplo/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
```

- O URL da imagem tem de ser **absoluto** e público. As plataformas guardam a imagem em cache: se a mudares, muda também o nome ou acrescenta `?v=2`.

## 2. Imagem social do repositório (GitHub)

Para projetos no GitHub: **1280×640** (o GitHub recomenda), carregada pelo utilizador em *Settings → General → Social preview*. Pode ser a mesma composição da imagem OG, adaptada.

## 3. Miniatura e capas

- **Miniatura YouTube (16:9):** 1280×720, JPG/PNG, < 2 MB. O produto em grande + 2–4 palavras enormes. Legível em 320×180.
- **Capa vertical (Reels, TikTok, Shorts):** 1080×1920, com o essencial no centro 1080×1440 (a grelha do Instagram mostra 3:4) e longe das zonas da interface. Normalmente é a capa cozida no fotograma 0 (`capa-9x16.jpg`).

## 4. Product Hunt

- **Miniatura:** 240×240 (PNG, JPG ou GIF). Um GIF de 2–3 s em loop chama a atenção na lista.
- **Galeria:** 1270×760. 3–6 imagens; a primeira é a mais vista — o produto a funcionar com uma frase. Pode incluir um vídeo (link do YouTube).
- Mesmo estilo em todas as imagens (fundo, letras, molduras).

## 5. GIF de demonstração para o README

O que mais convence num repositório: o produto a funcionar, em loop, sem som.

- 6–12 s, um só fluxo, em loop limpo (o fim encaixa no início).
- Largura 720–800 px, 10–15 fps. Abaixo de **5 MB** carrega depressa.
- Texto na imagem com pelo menos ~14 px no tamanho final.

```bash
# a partir do vídeo 16:9 (ou de uma gravação), dos 2,0 s aos 10,0 s
ffmpeg -y -ss 2 -t 8 -i video/launch-16x9.mp4 -vf "fps=12,scale=800:-2:flags=lanczos,split[a][b];\
[a]palettegen=max_colors=128:stats_mode=diff[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
  -loop 0 kit/demo.gif
ls -lh kit/demo.gif     # se passar de 5 MB: menos fps (10), menos largura (640) ou max_colors=96
```

No README:

```markdown
<p align="center">
  <img src="docs/demo.gif" width="720" alt="O Migalha a dividir uma conta de 84,60 € por quatro pessoas">
</p>
```

**Alternativa em vídeo:** ao editar o README no site do GitHub, arrastar um `.mp4` para o editor carrega-o e insere um leitor de vídeo (é o utilizador que o faz). Mais leve e nítido do que um GIF, mas não toca sozinho em todas as vistas.

## 6. App Store

### Pré-visualização em vídeo (app preview)

Especificações oficiais (App Store Connect, revistas em novembro de 2026):

| | |
|---|---|
| Duração | **15 a 30 s** |
| Quantidade | até 3 por tamanho de ecrã e por língua |
| Ficheiro | `.mov`, `.m4v` ou `.mp4`, até 500 MB |
| Vídeo | H.264 (alvo 10–12 Mbps, *High Profile* até nível 4.0) ou ProRes 422 HQ; **máx. 30 fps**; progressivo |
| Áudio | estéreo, AAC 256 kbps, 44,1 ou 48 kHz |
| Fotograma de capa | por defeito aos 5 s (pode escolher-se no envio) |
| iPhone com Dynamic Island / Face ID (grande e médio) | **886×1920** vertical · 1920×886 horizontal |
| iPhone com botão Home (grande) | 1080×1920 · 1920×1080 |
| iPad 13" e 11" | **1200×1600** · 1600×1200 |
| Mac / Apple TV | 1920×1080 (só horizontal) |

**Regras de conteúdo (diretriz 2.3.4 da App Review):** a pré-visualização só pode usar **gravações do ecrã da própria app**; podes acrescentar narração e texto por cima para explicar o que não fica claro. Por isso **não é** o vídeo de lançamento redimensionado — não leves cenas desenhadas, molduras de aparelho, mãos nem conteúdo de fora da app. Mostra funcionalidades que existem, nesta versão.

Como fazer:
1. Grava no simulador do maior iPhone (`xcrun simctl io booted recordVideo --codec=h264 …`, com a barra de estado limpa — ver `references/video/inspecionar.md`).
2. Monta 15–30 s só com essas gravações (cortes, acelerações suaves, texto por cima na zona central) com o motor ⚡ Rápido.
3. Exporta no tamanho aceite:

```bash
ffmpeg -y -i work/app-preview-montado.mp4 -f lavfi -i anullsrc=r=48000:cl=stereo \
  -vf "scale=886:1920:force_original_aspect_ratio=increase,crop=886:1920,fps=30,format=yuv420p" \
  -map 0:v -map 1:a -c:v libx264 -profile:v high -level 4.0 -b:v 11M -maxrate 12M -bufsize 24M \
  -c:a aac -b:a 256k -ar 48000 -ac 2 -shortest -movflags +faststart kit/app-preview-886x1920.mp4
```

(A segunda entrada é silêncio: garante **uma** pista de áudio estéreo mesmo que a montagem não tenha som. Se a montagem já tiver som, retira `-f lavfi -i anullsrc=…` e troca `-map 1:a` por `-map 0:a` — nunca fiques com duas pistas.) Confirma com `ffprobe` que a duração está entre 15 e 30 s e o tamanho é exatamente 886×1920.

4. O utilizador carrega-o no App Store Connect (pode demorar até 24 h a processar).

### Capturas de ecrã

O App Store Connect pede as capturas do **maior iPhone** (e do maior iPad, se a app for para iPad) e reduz para os outros. Tira-as no simulador desse aparelho com a barra de estado limpa. Até 10 por língua; as 3 primeiras são as que aparecem na pesquisa — põe lá o fluxo principal e o resultado. Texto por cima é permitido; mantém-no curto e verdadeiro. Confirma os tamanhos exatos na página oficial antes de exportar.

## 7. Google Play

- **Gráfico de destaque (feature graphic):** 1024×500, JPG ou PNG sem transparência. Obrigatório para mostrar o vídeo promocional.
- **Ícone:** 512×512, PNG.
- **Capturas de telemóvel:** pelo menos 2; lado menor ≥ 320 px e maior ≤ 3840 px, proporção até 2:1. 4 ou mais, com 1080 px ou mais, ajudam a aparecer em recomendações.
- **Vídeo promocional:** um **link do YouTube** (público ou não listado, sem anúncios, sem restrição de idade, incorporável). O utilizador carrega o vídeo no canal dele; tu dás-lhe o ficheiro (16:9 funciona bem) e o título e descrição.
- Confirma as regras atuais na Ajuda da Play Console.

## 8. Como gerar as imagens

**A partir de um modelo HTML** (`assets/kit/og-image.html`): edita as cores, o nome, a frase e a captura; depois captura no tamanho certo com o browser sem janela (sem Node):

```bash
"$CHROME" --headless=new --hide-scrollbars --window-size=1200,630 --virtual-time-budget=2000 \
  --screenshot="launch-output/kit/og-image.png" "file:///caminho/para/launch-output/work/og-image.html"
# miniatura 1280×720: ?formato=miniatura e --window-size=1280,720 · GitHub 1280×640: ?formato=github
# Product Hunt 1270×760: ?formato=ph · Google Play 1024×500: ?formato=play
```

(`$CHROME` como em `references/video/inspecionar.md`. Com Node, o `capturar.mjs` também serve, com uma página própria.)

**A partir de um fotograma do vídeo** (a capa já é forte): `ffmpeg -ss 3.4 -i video/launch-16x9.mp4 -frames:v 1 -vf "scale=1200:630:force_original_aspect_ratio=increase,crop=1200:630" kit/og-image.png`.

## 9. Verificar

- [ ] Abre cada imagem em tamanho real **e** reduzida (como aparece numa lista): o nome lê-se?
- [ ] Nada importante perto das margens (OG, capas) nem nas zonas da interface (capas verticais).
- [ ] Contraste suficiente; nada de texto fino sobre fotografias.
- [ ] Tamanhos exatos (`sips -g pixelWidth -g pixelHeight ficheiro.png` no Mac, ou `ffprobe`).
- [ ] Pesos: OG < 1 MB, miniatura < 2 MB, GIF < 5 MB.
- [ ] Texto alternativo escrito para cada imagem (vai no `copy.md`).
- [ ] Depois de publicar o site, o utilizador pode confirmar a pré-visualização do link nas ferramentas de inspeção de partilhas das próprias plataformas.
