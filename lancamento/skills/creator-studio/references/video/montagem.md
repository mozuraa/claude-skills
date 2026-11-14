# Montar, verificar e renderizar

Como passar do `plano.md` para os ficheiros de vídeo, com o motor mais leve que serve. Lê também `audio.md` para o som.

## Índice

1. Ver o que existe (e instalar só com autorização)
2. Motor ⚡ Rápido — só ffmpeg
3. Motor 🎨 Estúdio — HTML + browser + ffmpeg
4. Motor 🧩 Hyperframes — se já estiver instalado
5. Plano B sem instalar nada
6. Verificar antes de renderizar
7. Rascunho e render final
8. Capa cozida no fotograma 0
9. Legendas (.srt e gravadas na imagem)
10. Exportações especiais
11. Respeitar o computador

---

## 1. Ver o que existe

```bash
command -v ffmpeg && ffmpeg -hide_banner -version | head -1
ffmpeg -hide_banner -filters 2>/dev/null | grep -E " (drawtext|subtitles|xfade|loudnorm|sidechaincompress) "
command -v node && node -v
node -e "require.resolve('playwright-core')" 2>/dev/null && echo "playwright-core aqui"
npx --no-install hyperframes --version 2>/dev/null     # não instala nada se não existir
python3 --version
ls -d "/Applications/Google Chrome.app" "/Applications/Brave Browser.app" "/Applications/Microsoft Edge.app" "/Applications/Chromium.app" 2>/dev/null
xcrun simctl list devices booted 2>/dev/null | head -5
command -v adb && adb devices
```

Se faltar algo, explica **o que é, para que serve, quanto ocupa** e pergunta. Sugestões (o utilizador corre as que pedem palavra-passe; tu nunca escreves palavras-passe):

| Falta | macOS | Windows | Linux |
|---|---|---|---|
| ffmpeg | `brew install ffmpeg` (precisa do Homebrew) | `winget install Gyan.FFmpeg` | `sudo apt install ffmpeg` |
| Node.js | `brew install node` ou o instalador de nodejs.org | `winget install OpenJS.NodeJS.LTS` | `sudo apt install nodejs npm` |
| Playwright | `npm i playwright-core` dentro de `launch-output/work/` (~8 MB) **e** usar o Chrome/Brave/Edge que já existe. Só se não houver nenhum: `npx playwright install chromium` (~150–250 MB) | idem | idem |

Instala sempre de forma isolada (dentro de `launch-output/work/`), nunca nas dependências do projeto do utilizador.

## 2. Motor ⚡ Rápido — só ffmpeg

Para vídeos feitos de capturas e gravações reais, com texto e transições simples. Cada cena vira um clipe com o mesmo tamanho, fps e formato de cor; no fim juntam-se e mistura-se o som.

### Cena a partir de uma captura (fundo da marca + zoom lento)

```bash
D=2.5   # duração da cena em segundos
ffmpeg -y -f lavfi -i "color=c=0x0F1115:s=1080x1920:r=30:d=$D" \
  -i work/capturas/01-inicio-9x16.png \
  -filter_complex "[1:v]scale=900:-2[shot];[0:v][shot]overlay=(W-w)/2:(H-h)/2+80,\
scale=w='trunc(1080*(1+0.04*t/$D)/2)*2':h=-2:eval=frame,crop=1080:1920,setsar=1,format=yuv420p[v]" \
  -map "[v]" -t $D -r 30 -c:v libx264 -crf 18 -preset medium work/cenas/01.mp4
```

- O zoom de 4% ao longo da cena dá vida sem enjoar. Para um deslize em vez de zoom, anima o `x`/`y` do `overlay` com `t`.
- Os cantos arredondados, sombras e molduras ficam melhor no motor 🎨 Estúdio; aqui mantém simples.

### Cena a partir de uma gravação (cortar, acelerar, encaixar)

```bash
ffmpeg -y -ss 3.2 -t 3 -i work/gravacoes/fluxo.mov \
  -f lavfi -i "color=c=0x0F1115:s=1080x1920:r=30:d=2" \
  -filter_complex "[0:v]setpts=PTS/1.5,fps=30,scale=900:-2[rec];\
[1:v][rec]overlay=(W-w)/2:(H-h)/2+80:shortest=1,setsar=1,format=yuv420p[v]" \
  -map "[v]" -an -t 2 -c:v libx264 -crf 18 -preset medium work/cenas/02.mp4
```

(3 s de gravação a 1,5× = 2 s de cena.) Acelera as partes aborrecidas (esperas, carregamentos), nunca o momento do resultado.

### Texto por cima

Escreve cada texto num ficheiro (evita problemas com aspas e dois pontos) e usa `drawtext`:

```bash
printf '%s' "Quem ficou de pagar o quê?" > work/textos/01-pt.txt
# acrescenta ao fim do filtro da cena:
drawtext=fontfile=/caminho/para/Fonte-Bold.ttf:textfile=work/textos/01-pt.txt:\
fontsize=96:fontcolor=0xF5F5F7:x=(w-text_w)/2:y='260+40*(1-min(1,(t-0.2)/0.3))':\
alpha='min(1,(t-0.2)/0.3)':enable='gte(t,0.2)'
```

Entra aos 0,2 s, sobe 40 px e aparece em 0,3 s, e fica. Usa a fonte do projeto (`.ttf`/`.otf`); no Mac, se não houver, `/System/Library/Fonts/SFNS.ttf` ou `/System/Library/Fonts/Helvetica.ttc`. Uma linha por `drawtext` (para duas linhas, dois filtros ou `\n` no ficheiro com `line_spacing`).

### Juntar as cenas

**Cortes secos** (tudo codificado igual):
```bash
printf "file '%s'\n" work/cenas/*.mp4 > work/cenas/lista.txt
ffmpeg -y -f concat -safe 0 -i work/cenas/lista.txt -c copy work/video-mudo.mp4
```

**Com transições** (`xfade`): se cada clipe (menos o último) durar a sua duração planeada **mais** a duração da transição `T`, então cada transição começa exatamente no tempo de corte do plano: `offset` da transição *k* = soma das durações **planeadas** das cenas antes dela.

```bash
# cenas planeadas: 2,0 s · 2,5 s · 3,0 s ; T = 0,4 ; clipes com 2,4 · 2,9 · 3,0 s
ffmpeg -y -i work/cenas/01.mp4 -i work/cenas/02.mp4 -i work/cenas/03.mp4 -filter_complex \
"[0:v][1:v]xfade=transition=slideleft:duration=0.4:offset=2.0[a];\
 [a][2:v]xfade=transition=fadeblack:duration=0.4:offset=4.5,format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -crf 18 -preset medium work/video-mudo.mp4
```

Transições úteis: `fade`, `fadeblack`/`fadewhite` (mergulho pela cor — bom entre ecrãs cheios), `slideleft`/`slideup`, `smoothleft`, `circleopen`, `zoomin`. Uma ou duas por vídeo; o resto cortes na batida.

### Juntar o som

Ver `audio.md` (secção "Misturar"). O resultado final:
```bash
ffmpeg -y -i work/video-mudo.mp4 -i work/audio-final.wav -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart video/launch-9x16.mp4
```

### Os outros formatos

Repete as cenas com as dimensões e posições de cada formato (`1080x1080`, `1920x1080`, `1080x1350`) e as capturas certas para cada um. O som (`audio-final.wav`) é o mesmo para todos.

## 3. Motor 🎨 Estúdio — HTML + browser + ffmpeg

Para cenas desenhadas: cartões, molduras de telemóvel, toques simulados, texto a escrever-se, contadores, legendas com estilo. Usa o modelo em `<skill-dir>/assets/compositor/`.

1. **Copia** o modelo para o trabalho: `cp -R <skill-dir>/assets/compositor launch-output/work/compositor`.
2. **Edita** `work/compositor/cena.html`: no topo do `<script>`, o objeto `COMPOSICAO` tem as cores e fontes do projeto, a duração, as cenas e os elementos (texto, imagem, cartão, toque, contador), com tempos tirados do plano e posições por formato. As imagens são as capturas reais (`../capturas/...`). Textos em `{ pt: "...", en: "..." }`.
3. **Pré-visualiza** no browser integrado: abre `cena.html?formato=9x16&play=1` (corre em tempo real e encaixa na janela) ou `?formato=16x9&t=3.2` (um fotograma). `&guias=1` mostra as zonas seguras; `&lingua=en` troca a língua; `&legendas=1` liga as legendas.
4. **Captura** os fotogramas (Node + `playwright-core` em `work/`, e o Chrome/Brave/Edge que já existe):

```bash
cd launch-output/work && npm i playwright-core     # só da primeira vez, com autorização
nice -n 10 node compositor/capturar.mjs --formato 9x16 --fps 30 --lingua pt --saida frames-9x16
```

Opções: `--escala 0.5 --fps 15` para rascunhos; `--tempos 0.8,2.6,5.1` para tirar só alguns fotogramas (verificação); `--legendas` para gravar as legendas; `--browser <caminho>` para escolher o browser.

5. **Codifica** com o som:

```bash
nice -n 10 ffmpeg -y -framerate 30 -i frames-9x16/%05d.png -i audio-final.wav \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart ../video/launch-9x16.mp4
```

Regras do modelo (se o alterares, mantém-nas): cada fotograma é **função pura do tempo** (nada de `setTimeout`, `Math.random()` sem semente, ou animações CSS a correr sozinhas); `window.seek(t)` espera por fontes e imagens antes de responder; tudo local (sem fontes ou imagens de URLs externos no momento da captura — descarrega-as para `work/` primeiro, se a licença o permitir); se usares HTML do próprio site, tira os `<script>`.

## 4. Motor 🧩 Hyperframes

Só se `npx --no-install hyperframes --version` responder (nunca instales sem perguntar). A skill continua dona da história; o Hyperframes faz a composição e o render.

1. Escreve `launch-output/brief.md` a partir do `plano.md`: objetivo e público; formato, tamanho, fps e duração; o material real (caminhos das capturas e gravações); identidade (cores exatas, fontes); o guião cena a cena com textos, tempos e transições; o som **já preparado e licenciado** (caminhos dos ficheiros, BPM, tempos dos cortes) e a regra "não acrescentar música nem sons de outras origens"; as leis criativas e o tempo de leitura.
2. Segue a documentação e as skills do Hyperframes que estiverem instaladas para compor em `launch-output/work/hyperframes/`, correr a verificação dele e renderizar para `video/launch-<formato>.mp4`.
3. Volta a esta skill para a verificação (secção 6), a capa, as legendas, os créditos e a entrega.

## 5. Plano B sem instalar nada

Sem ffmpeg e sem autorização para instalar: entrega o `plano.md`, a composição HTML pronta e estas instruções ao utilizador — abrir `cena.html?formato=9x16&play=1` no browser em ecrã inteiro e gravar com o gravador do sistema (macOS: ⇧⌘5 → "Gravar parte do ecrã"; Windows: Ferramenta de Recorte → Gravar). O som junta-se num editor de vídeo (iMovie, CapCut, Clipchamp) com o `audio-final.wav` gerado por `audio.py` (só precisa de Python). Diz claramente que este caminho tem menos qualidade e mais trabalho manual.

## 6. Verificar antes de renderizar

Nunca renderizes o final sem ver. Tira fotogramas de **cada cena já assente** e de **meio de cada transição**, em cada formato:

```bash
# motor Estúdio: só os tempos que interessam, com as guias
node compositor/capturar.mjs --formato 9x16 --tempos 1.0,1.9,3.5,4.4,6.8 --guias --escala 0.5 --saida verificar-9x16
# juntar numa folha de contacto
ffmpeg -y -pattern_type glob -i 'verificar-9x16/*.png' -vf "scale=360:-2,tile=5x1:padding=12:color=white" folha-9x16.png
# a partir de um vídeo já feito (motor Rápido): 2 fotogramas por segundo
ffmpeg -y -i work/video-mudo.mp4 -vf "fps=2,scale=270:-2,tile=8x5:padding=6:color=white" -frames:v 1 work/folha.png
```

Abre a folha e procura:
- [ ] texto cortado, a sair do ecrã ou dentro das zonas que as apps tapam;
- [ ] texto sobre imagem sem contraste (mínimo 4,5:1 para texto pequeno, 3:1 para títulos grandes);
- [ ] elementos que se sobrepõem por engano;
- [ ] transições turvas (dois ecrãs cheios em cruzamento) — troca por saída-entrada ou mergulho pela cor;
- [ ] fotogramas vazios ou com imagens por carregar;
- [ ] dados reais ou pessoais que tenham escapado;
- [ ] o mesmo em cada língua (o português é mais comprido).

Mostra a folha ao utilizador quando ajudar a decidir.

## 7. Rascunho e render final

- **Rascunho:** um só formato (o principal), metade da resolução, 15 fps, codificação rápida (`-preset veryfast -crf 28`). ✋ Mostra-o e pergunta se avanças.
- **Final:** um formato de cada vez, em segundo plano, `-crf 18`, `-preset medium` (ou `slow` se a máquina estiver folgada), H.264 High, `yuv420p`, 30 fps, AAC 192 kbps 48 kHz estéreo, `-movflags +faststart` (começa a tocar antes de descarregar tudo).
- Confirma cada ficheiro: `ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate -of compact video/launch-9x16.mp4`.

## 8. Capa cozida no fotograma 0

A maioria das plataformas usa o primeiro fotograma como miniatura. Escolhe o fotograma mais forte **já assente** (o gancho ou o remate com o nome), guarda-o como capa e põe-no no lugar do fotograma 0 — só esse fotograma muda; a duração e o som ficam iguais (1/30 s não se nota a ver).

- **Motor Estúdio (sem perdas):** antes de codificar, copia o fotograma escolhido por cima de `frames-9x16/00000.png` e guarda-o também como capa:
  ```bash
  cp frames-9x16/00102.png ../video/capa-9x16.png && cp frames-9x16/00102.png frames-9x16/00000.png
  ```
- **Vídeo já feito:**
  ```bash
  ffmpeg -y -ss 3.4 -i video/launch-9x16.mp4 -frames:v 1 -q:v 2 video/capa-9x16.jpg
  ffmpeg -y -i video/launch-9x16.mp4 -i video/capa-9x16.jpg \
    -filter_complex "[0:v][1:v]overlay=0:0:enable='eq(n,0)',format=yuv420p[v]" \
    -map "[v]" -map 0:a? -c:v libx264 -crf 18 -preset medium -c:a copy -movflags +faststart work/capa-tmp.mp4 \
    && mv work/capa-tmp.mp4 video/launch-9x16.mp4
  ```

Guarda as capas: servem para as plataformas que deixam carregar uma capa (Instagram, TikTok, YouTube, LinkedIn) e para `<video poster="...">` num site.

## 9. Legendas

- **`.srt`** por língua, a partir do texto no ecrã e da voz, com `python3 <skill-dir>/assets/scripts/legendas.py` (lê uma tabela simples, escreve o `.srt` e avisa se alguma legenda é rápida ou comprida demais). Regras: até 2 linhas, ~42 caracteres por linha, no máximo ~17 caracteres por segundo, mínimo ~1 s no ecrã.
- **Sem voz**, o texto no ecrã já é a "legenda"; gera o `.srt` na mesma (acessibilidade e plataformas que o aceitam).
- **Gravadas na imagem:** no motor Estúdio, `--legendas` desenha-as com o estilo do vídeo, dentro da zona segura. No motor Rápido, com o filtro `subtitles` (precisa de libass):
  ```bash
  ffmpeg -y -i video/launch-9x16.mp4 -vf "subtitles=video/legendas-pt.srt:force_style='FontName=Helvetica Neue,FontSize=15,Bold=1,PrimaryColour=&H00FFFFFF,BorderStyle=3,OutlineColour=&H99000000,Outline=4,Shadow=0,Alignment=2,MarginV=70'" \
    -c:v libx264 -crf 18 -preset medium -c:a copy -movflags +faststart video/launch-9x16-legendado.mp4
  ```
  (`FontSize` e `MarginV` são relativos a uma altura de 288: 15 ≈ 100 px e 70 ≈ 470 px num vídeo de 1920.)
- Onde a plataforma aceita carregar o `.srt` (YouTube, LinkedIn, Facebook...), carrega o ficheiro em vez de gravar — fica pesquisável e desligável.

## 10. Exportações especiais

- **Pré-visualização da App Store:** não é o vídeo de lançamento redimensionado — só pode usar gravações do ecrã da app e tem tamanhos próprios. Ver `references/kit/imagens.md`.
- **GIF para o README:** ver `references/kit/imagens.md`.
- **Versão sem música** (`launch-9x16-sem-musica.mp4`, só efeitos e voz): para quem quer juntar um som da biblioteca da própria app (TikTok, Instagram).
- **Ficheiro mais leve** para mensagens: `-crf 26 -preset medium` e AAC 128 kbps.

## 11. Respeitar o computador

- Um render de cada vez. Comandos longos em segundo plano, com `nice -n 10` e, numa máquina carregada, `-threads 2` no ffmpeg.
- Rascunho pequeno primeiro; final só depois do "sim".
- Fotogramas PNG ocupam muito (1080×1920 ≈ 1–3 MB cada; 20 s a 30 fps ≈ 600 ficheiros): apaga cada pasta de fotogramas depois de codificar e verificar o vídeo — com autorização, se for fora de `work/`.
- Diz ao utilizador quanto tempo esperas que demore e avisa quando acabar.
