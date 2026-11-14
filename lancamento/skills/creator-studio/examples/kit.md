# Exemplo — 📣 Kit de lançamento

Projeto fictício: **Pausa**, uma app para iPhone de exercícios de respiração de 1 minuto. Paga (2,99 €), sem versão gratuita. Já tem vídeo de lançamento feito com o modo 🎬 Vídeo.

---

**Utilizador:** prepara o lançamento da Pausa. Sai na App Store dia 17.

**Claude:** Três perguntas:

1. **Plataformas** (escolhe várias) — (a) TikTok + Reels + Shorts *(recomendo: o vídeo vertical é o teu melhor trunfo)* · (b) X · (c) Product Hunt · (d) Reddit · (e) LinkedIn · (f) Show HN
2. **Público e língua** — (a) português e inglês *(recomendo)* · (b) só português · (c) só inglês
3. **App Store** — (a) também a pré-visualização em vídeo e as capturas *(recomendo)* · (b) só os posts

**Utilizador:** a, b, c, d, f. PT e EN. Sim à App Store.

**Claude:** Uma opinião antes de começar: **o Show HN não encaixa** — as regras pedem algo que as pessoas possam experimentar já, e a Pausa é paga sem versão grátis. Publicar lá arrisca ser removido ou mal recebido. Proponho tirar o Show HN, ou criar um código promocional para os primeiros 50 leitores (aí já há forma de experimentar). E o **Product Hunt** costuma dar menos tração a apps só para iPhone — vale a pena, mas com expectativas baixas. Sigo sem o Show HN?

**Utilizador:** sim, sem Show HN.

---

**Claude:** *(lê o plano do vídeo, as capturas e o README; grava no simulador do maior iPhone com a barra de estado limpa; prepara as imagens a partir de `og-image.html`; escreve os textos e conta os caracteres)*

Excerto de `kit/copy.md`:

**X** (203/280)
> Fiz uma app para quando o dia aperta: a Pausa.
>
> Um minuto, um círculo que cresce e encolhe, e respiras com ele. Sem contas, sem anúncios, sem notificações a pedir atenção.
>
> Na App Store a partir de hoje.

Anexo `video/launch-16x9.mp4` · texto alternativo: "Um círculo laranja cresce e encolhe ao ritmo da respiração no ecrã da Pausa." · link na primeira resposta.

**Product Hunt**

| Campo | Texto | Contagem |
|---|---|---|
| Tagline | Breathe for one minute, guided by a circle | 42/60 |
| Descrição | A tiny iPhone app for the moment the day gets heavy: one minute, one circle, no accounts, no ads, no streaks to keep. | 117 |
| Tópicos | Health & Fitness · iOS · Meditation | 3 |

**Reddit** — r/iOSProgramming só aceita apps no "App Saturday" (confirmado nas regras da comunidade hoje); r/SideProject aceita todos os dias. Título: "I made a one-minute breathing app with no accounts, no ads and no streaks — feedback welcome".

**Pré-visualização da App Store:** `kit/app-preview-886x1920.mp4` — 24 s, só gravações do ecrã da app (o círculo, a escolha da duração, o ecrã final), texto por cima ao centro, música gerada, 886×1920, 30 fps, AAC 256 kbps. Não usei as cenas desenhadas do vídeo de lançamento: a diretriz 2.3.4 só aceita gravações do ecrã da app.

**Imagens:** `kit/og-image.png` (1200×630, 412 KB) · `kit/ph-miniatura.gif` (240×240, o círculo a respirar, 380 KB) · `kit/ph-1.png` … `ph-4.png` (1270×760) · `kit/miniatura.png` (1280×720).

Excerto de `kit/checklist.md` (hora de Lisboa):

| Quando | O quê |
|---|---|
| sex 13 | ✋ confirmar que a versão está aprovada e com lançamento manual marcado para dia 17 |
| seg 16 | testar o link da App Store no telemóvel; ver o vídeo com e sem som |
| ter 17, 08:01 | ✋ Product Hunt ativo; primeiro comentário do criador |
| ter 17, 09:00 | ✋ carregar em "Publicar" na App Store Connect; mensagens pessoais a 20 pessoas |
| ter 17, 13:00 | ✋ X (PT e EN) |
| ter 17, 19:00 | ✋ Reels, TikTok e Shorts (`launch-9x16-sem-musica.mp4` no TikTok, com um som da biblioteca) |
| sáb 21 | ✋ r/iOSProgramming (App Saturday) |
| ter 24 | post "o que aprendi numa semana" |

`kit/calendario.ics` com estes momentos, para importares no teu calendário.

**A minha opinião:** começa pelos vídeos verticais — é onde uma app visual e calma se destaca. O X e o Reddit servem para conversas com quem faz apps. Não esperes milhares de downloads no primeiro dia; o objetivo é as primeiras 100 pessoas e as opiniões delas. **Nada foi publicado:** todos os passos com ✋ são teus.
