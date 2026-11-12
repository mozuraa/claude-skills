# Modelos — imagem, vídeo e música

Prompts descritivas: descreve o que se vê ou ouve, não dês ordens. Detalhes por ferramenta em `references/destinos.md`.

---

## 🖼️ Imagem

**Linguagem natural** (geradores integrados nos assistentes, Imagen, Firefly, Midjourney recente):

```
[Tipo de imagem e meio] de [sujeito com detalhes concretos], [ação], [cenário e momento].
[Composição: enquadramento, ângulo, onde fica o sujeito, espaço livre].
[Luz]. [Paleta e ambiente]. [Detalhes técnicos: lente, profundidade de campo, textura].
[Proporção].
```

Exemplo:
```
Fotografia de produto de uma caneca de cerâmica artesanal azul-petróleo, com vidrado
irregular, pousada numa mesa de madeira clara ao lado de um livro aberto. Manhã, luz
suave de janela vinda da esquerda, vapor leve a sair da caneca. Enquadramento a meia
altura, caneca no terço direito, espaço livre à esquerda para texto. Tons quentes e
naturais, ambiente calmo e acolhedor. Profundidade de campo curta, fundo desfocado.
Proporção 4:5.
```

**Midjourney** — a mesma descrição, mais parâmetros no fim (confirma na documentação atual):
```
[descrição] --ar 4:5 --no texto, logótipos
```

**Stable Diffusion e semelhantes** — palavras-chave e prompt negativa:
```
Prompt: product photo, handmade teal ceramic mug, irregular glaze, light wooden table,
open book, soft window light from left, morning, steam, shallow depth of field,
warm natural tones, cozy
Negativa: blurry, text, watermark, logo, distorted, extra handles
```

---

## 🎬 Vídeo (um plano)

```
[Plano e movimento de câmara]. [Sujeito] [ação do início ao fim].
[Cenário, luz, ambiente]. [Estilo]. [Som, se a ferramenta gerar áudio].
Duração [5–10 s], proporção [16:9 / 9:16].
```

Exemplo:
```
Grande plano, câmara fixa. Mãos de uma ceramista moldam uma caneca no torno; a peça
sobe lentamente e ganha forma; no fim as mãos afastam-se e a caneca continua a girar.
Atelier com luz de fim de tarde a entrar pela janela, pó a flutuar no ar. Estilo
documental, cores quentes. Som: zumbido suave do torno e água. 8 segundos, 9:16.
```

---

## 🎵 Música

**Estilo** (campo de estilo da ferramenta):
```
[género e subgénero], [época], [ambiente], [instrumentos], [voz ou instrumental], [ritmo/BPM]
```

Exemplo: `indie folk acústico, anos 70, nostálgico e quente, guitarra dedilhada e violino suave, voz masculina grave, 85 BPM`

**Letra** (original — escrita pelo utilizador ou contigo):
```
[Intro]

[Verso 1]
...

[Refrão]
...

[Verso 2]
...

[Refrão]
...

[Final]
```
