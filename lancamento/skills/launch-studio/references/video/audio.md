# Som: música, efeitos e voz

O som é metade da sensação de "isto é profissional", mas o vídeo tem de funcionar sem ele. Música, efeitos e voz soam como **uma só peça**: no mesmo andamento, na mesma grelha, misturados com cuidado.

## Índice

1. De onde pode vir a música (e as licenças)
2. Música gerada pela skill (`audio.py batida`)
3. Efeitos sonoros (`audio.py sons` e `audio.py pista`)
4. Voz-off (opcional)
5. Misturar
6. Créditos

---

## 1. De onde pode vir a música

Só há três origens aceitáveis. Pergunta ao utilizador qual prefere (com a tua recomendação) e regista a escolha em `creditos.md`.

### a) A música do utilizador
A melhor opção se ele a compôs ou tem licença para a usar. Pergunta: "É tua ou tens licença para a usar em vídeos promocionais?" Se ele não souber, não uses.

### b) Música gerada pela skill
`audio.py batida` compõe uma base original a partir de regras simples (acordes, baixo, percussão, arpejos), no andamento e duração do plano. É do utilizador, sem licença a gerir. É simples — honesta, limpa, no ritmo certo — mas não substitui um produtor. Diz-lho.

### c) Faixas *royalty-free* com licença verificada
Antes de usar qualquer faixa, confirma e escreve em `creditos.md`:

- [ ] **Uso comercial / promocional** permitido?
- [ ] **Atribuição** obrigatória? Em que formato exato?
- [ ] **Modificações** permitidas (cortar, fazer loop, misturar)? Licenças "ND" (sem derivados) não servem.
- [ ] **Não comercial** ("NC")? Não serve para promover um produto pago.
- [ ] A faixa está registada em sistemas de identificação de conteúdo (ex.: Content ID) que podem reclamar o vídeo?
- [ ] Restrições de plataforma (ex.: só para o YouTube)?
- [ ] O link da página da faixa e a data em que a licença foi lida.

Origens habituais (as regras mudam — lê sempre a licença da faixa concreta):

| Origem | Licença típica | Atenção |
|---|---|---|
| Biblioteca de Áudio do YouTube | gratuita para vídeos; algumas faixas pedem atribuição | pensada para vídeos no YouTube — confirma os termos antes de usar noutras plataformas |
| Pixabay Music | licença própria da Pixabay: uso comercial, sem atribuição | algumas faixas estão registadas em sistemas de identificação e podem gerar reclamações; guarda a página da faixa |
| incompetech (Kevin MacLeod) | CC BY 4.0 | atribuição obrigatória, no formato pedido pelo autor |
| ende.app (Sascha Ende) | licença padrão gratuita com atribuição (CC BY 4.0) | atribuição obrigatória |
| Free Music Archive, ccMixter | Creative Commons, faixa a faixa | evita NC e ND; confirma cada faixa |
| Uppbeat e semelhantes | gratuita com crédito, com limites | precisa de conta — o utilizador cria-a, tu não |
| Epidemic Sound, Artlist, Musicbed | subscrição paga | só se o utilizador já tiver; tu nunca compras |
| Serviços de música por IA | depende do plano | muitos planos gratuitos proíbem uso comercial; lê os termos do plano do utilizador |

**Bibliotecas das próprias apps (TikTok, Instagram):** um som escolhido dentro da app fica licenciado para uso **dentro** dessa app (e contas de empresa só têm acesso a um catálogo comercial mais pequeno). Para estas plataformas, entrega também uma versão **sem música** (só efeitos e voz) para o utilizador juntar o som na app.

**Nunca:** músicas comerciais conhecidas, faixas tiradas de outros vídeos, jogos ou apps, "sem direitos de autor" de canais duvidosos, ou sons copiados de outras ferramentas.

## 2. Música gerada pela skill

`<skill-dir>/assets/scripts/audio.py` só usa Python 3 (sem instalar nada). Escreve WAV estéreo 48 kHz.

```bash
python3 <skill-dir>/assets/scripts/audio.py batida --estilo pop --bpm 120 --compassos 10 \
  --tom la --modo menor --semente 7 --saida launch-output/work/musica.wav
```

| `--estilo` | Para os tons | Como soa |
|---|---|---|
| `pop` | natural, loja, tutorial | bombo e palmas, baixo marcado, acordes em pulsação, arpejo leve |
| `calmo` | premium, acolhedor, seco | *pad* suave, notas espaçadas, quase sem percussão |
| `epico` | trailer, lancamento-serio | graves longos, tambores que crescem, impacto no fim |
| `retro` | retro | ondas quadradas, arpejos rápidos, ruído como percussão |
| `caos` | caos | rápido e denso, baixo distorcido, chimbal constante |
| `lofi` | devlog | batida lenta e arrastada, acordes de sétima, um pouco de ruído de fundo |

- `--compassos` × (240 / BPM) = duração. 10 compassos a 120 BPM = 20 s. Arredonda para cima e corta no fim com um desvanecimento.
- `--semente` muda a melodia e os arpejos mantendo o estilo: gera 2–3 versões e escolhe a melhor (ou deixa o utilizador ouvir).
- `--final` acrescenta um acorde final a soar 1 compasso (bom para o remate com o nome).
- `audio.py grelha --bpm 120 --duracao 20` mostra a grelha para o plano.

Não ouves o resultado. Diz ao utilizador que tem de o ouvir antes do render final, e oferece outra semente ou estilo se não gostar.

## 3. Efeitos sonoros

Gera efeitos originais:

```bash
python3 <skill-dir>/assets/scripts/audio.py sons --saida launch-output/work/sons/
# cria: clique.wav, toque.wav, pop.wav, whoosh.wav, ding.wav, tecla.wav, impacto.wav, sucesso.wav
```

Depois coloca-os no tempo certo numa só pista (e, se quiseres, por cima da música):

```bash
python3 <skill-dir>/assets/scripts/audio.py pista --duracao 20 \
  --eventos "0.5:pop,2.0:whoosh:-6,4.0:toque,4.5:toque,6.0:sucesso,19.0:impacto" \
  --pasta launch-output/work/sons --saida launch-output/work/sons-pista.wav
```

Cada evento é `tempo:som[:ganho_em_dB]`; `som` é um nome da pasta ou o caminho de qualquer WAV (por exemplo, uma frase de voz).

**Que som para que momento:**

| Momento no ecrã | Som | Nota |
|---|---|---|
| toque num botão | `toque` ou `clique` | no fotograma do toque, não antes |
| cartão ou elemento a aparecer | `pop` | baixo; em sequência, só nos primeiros 2–3 |
| mudança de cena com movimento | `whoosh` | começa ~0,1 s antes do corte |
| texto a escrever-se | `tecla` | uma tecla a cada 2–3 letras, não em todas |
| resultado, sucesso | `sucesso` ou `ding` | o efeito mais "alto" do vídeo |
| nome do produto / remate | `impacto` | um só, no primeiro tempo de um compasso |

**Densidade por tom:** `seco` e `premium` — 0 a 2 efeitos; `natural`, `loja`, `tutorial` — 3 a 6; `caos` e `retro` — muitos, mas baixos. Os efeitos ficam **por baixo** da música (6–12 dB abaixo dos picos dela), nada estridente, repetições discretas. Ou caem numa batida da grelha, ou exatamente no fotograma do que acontece no ecrã — nunca entre os dois.

## 4. Voz-off (opcional)

Desligada por defeito. Só com `--voz` ou se o utilizador pedir.

**Escrever o texto:**
- Complementa a imagem; não lê o texto que já está no ecrã.
- ~2,5 palavras por segundo em português (~2,7 em inglês): 20 s ≈ 40–50 palavras, já contando pausas.
- Deixa ~0,5 s sem voz no início e ~1 s no fim; cada frase cabe dentro da sua cena.
- Natural, como se falasse a um amigo; frases curtas; o nome do produto dito com clareza.

**Quem fala** (pergunta, com a tua recomendação):

| Opção | Como | Notas |
|---|---|---|
| **A voz do utilizador** (recomendado) | grava no telemóvel ou com o QuickTime / Gravador de Voz, num sítio calmo, a ~15 cm do microfone, uma frase de cada vez | a mais autêntica; cada frase num WAV |
| **Voz do sistema (macOS)** | `say -v Joana -r 175 --file-format=WAVE --data-format=LEI16@48000 -o work/voz/01.wav "Frase."` | sem instalar nada; `say -v '?'` lista as vozes (Joana = português de Portugal). Vozes "Melhorada"/"Premium" soam melhor: o utilizador descarrega-as em Definições do Sistema → Acessibilidade → Conteúdo falado |
| **Voz local aberta** (ex.: Kokoro, licença Apache-2.0) | biblioteca Python que corre no computador | pesada de instalar (modelos e bibliotecas de IA) — ✋ pergunta; nem todas têm português de Portugal |
| **Serviço de voz na nuvem** | só com a conta e a chave do utilizador | nunca crias contas nem escreves chaves; respeita os termos dele |

Gera **uma frase por ficheiro** e mede cada uma (`afinfo work/voz/01.wav | grep duration` no Mac, ou `python3 -c "import wave,sys; w=wave.open(sys.argv[1]); print(w.getnframes()/w.getframerate())" work/voz/01.wav`). Com as durações reais, ajusta os tempos do plano e as legendas.

**Regras:** nunca clones nem imites a voz de uma pessoa real sem o consentimento dela. Se a voz sintética puder passar por humana, várias plataformas pedem que o conteúdo seja marcado como gerado por IA — lembra o utilizador de usar essa opção ao publicar.

## 5. Misturar

Objetivo para redes sociais: volume integrado de ~-14 LUFS, picos abaixo de -1,5 dBTP, voz sempre clara (música 10–15 dB abaixo enquanto há voz), efeitos por baixo da música.

**Música + efeitos:**
```bash
ffmpeg -y -i work/musica.wav -i work/sons-pista.wav -filter_complex \
"[0:a][1:a]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=18.5:d=1.5,\
loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map "[a]" -ar 48000 work/audio-final.wav
```

**Música + efeitos + voz (a música baixa sozinha quando há voz):** primeiro junta as frases numa pista com `audio.py pista` (eventos `1.0:work/voz/01.wav,...`) e depois:
```bash
ffmpeg -y -i work/musica.wav -i work/sons-pista.wav -i work/voz-pista.wav -filter_complex \
"[2:a]asplit=2[voz][chave];\
[0:a][chave]sidechaincompress=threshold=0.03:ratio=10:attack=15:release=350[musica];\
[musica][1:a][voz]amix=inputs=3:normalize=0:duration=first,afade=t=out:st=18.5:d=1.5,\
loudnorm=I=-14:TP=-1.5:LRA=11[a]" -map "[a]" -ar 48000 work/audio-final.wav
```

**Sem ffmpeg:** `audio.py pista --base work/musica.wav --eventos ...` mistura os efeitos (e a voz) por cima da música e normaliza os picos — chega para o plano B.

A música começa no fotograma 0 com o primeiro tempo forte; se a faixa tiver introdução, corta-a (`-ss`) para alinhar. Termina com desvanecimento de 1–1,5 s ou com o acorde final (`--final`) a coincidir com o remate.

## 6. Créditos

`creditos.md` (modelo em `assets/creditos-template.md`) regista, para cada som e fonte tipográfica: origem, autor, licença, link e data em que foi verificada, e o texto de atribuição pronto a colar na descrição do post, quando obrigatório. Música gerada pela skill: "Música original gerada com launch-studio (sem licença de terceiros)". Diz ao utilizador onde colar a atribuição.
