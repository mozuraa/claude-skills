# Design — sistema visual e componentes

Um bom site parece **feito para aquela marca**, é fácil de ler no telemóvel e guia o visitante para uma ação. Define primeiro o sistema (tokens), depois os componentes, e só então as páginas.

## Índice

- [1. Da marca para o estilo](#1-da-marca-para-o-estilo)
- [2. Tokens](#2-tokens)
- [3. Tipografia](#3-tipografia)
- [4. Cor](#4-cor)
- [5. Espaçamento e grelha](#5-espaçamento-e-grelha)
- [6. Componentes](#6-componentes)
- [7. Imagens](#7-imagens)
- [8. Movimento](#8-movimento)
- [9. Modo escuro](#9-modo-escuro)
- [10. Evitar o aspeto genérico](#10-evitar-o-aspeto-genérico)
- [11. Erros comuns a evitar](#11-erros-comuns-a-evitar)

---

## 1. Da marca para o estilo

Transforma as 3 palavras da marca em decisões concretas e mostra-as ao utilizador no plano:

| Palavra | Tipografia | Cor | Forma | Imagens |
|---|---|---|---|---|
| Artesanal, acolhedor | Serifa humanista ou letra com personalidade nos títulos | Tons quentes, terra, creme | Cantos suaves, texturas leves | Fotografias reais, luz natural, mãos e processo |
| Confiável, profissional | Sem serifa sóbria | Azuis/verdes profundos, neutros | Linhas direitas, muito espaço | Pessoas reais da equipa, espaços limpos |
| Jovem, divertido | Sem serifa redonda e grossa | Cores saturadas, contrastes fortes | Formas orgânicas, ilustrações | Ilustrações, cores vivas, movimento |
| Luxo, elegante | Serifa fina e contrastada | Preto, branco, um dourado/acento discreto | Muito espaço, pouca coisa | Fotografia editorial, grande |
| Técnico, moderno | Sem serifa geométrica ou monoespaçada nos detalhes | Neutros frios + um acento vivo | Grelha visível, cantos pequenos | Capturas do produto, diagramas |

## 2. Tokens

Tudo o que se repete vira variável CSS no `:root` (o site-base já tem esta estrutura):

```css
:root {
  /* cor */
  --cor-fundo: #fffdf8;  --cor-superficie: #ffffff;  --cor-texto: #1d1b18;
  --cor-texto-suave: #5c574f;  --cor-primaria: #b5482a;  --cor-primaria-texto: #ffffff;
  --cor-borda: #e7e1d6;  --cor-foco: #1f6feb;
  /* tipografia */
  --fonte-titulos: "Fraunces", Georgia, serif;
  --fonte-texto: "Inter", system-ui, sans-serif;
  /* espaço (escala de 4/8) */
  --e-1: .25rem; --e-2: .5rem; --e-3: .75rem; --e-4: 1rem; --e-6: 1.5rem; --e-8: 2rem; --e-12: 3rem; --e-16: 4rem; --e-24: 6rem;
  /* forma */
  --raio: .75rem;  --sombra: 0 1px 2px rgb(0 0 0 / .06), 0 4px 16px rgb(0 0 0 / .06);
  /* layout */
  --largura-max: 72rem;  --largura-texto: 42rem;
}
```

Nunca escrevas cores ou tamanhos soltos nos componentes — usa os tokens. Assim, mudar a cor da marca é mudar uma linha.

## 3. Tipografia

- **1 ou 2 famílias**, no máximo (uma para títulos, outra para texto — ou a mesma para tudo). Máximo 3–4 ficheiros de fonte (pesos).
- **Alojadas no próprio site**, em WOFF2, com `font-display: swap` e `preload` da fonte principal. Fontes variáveis poupam ficheiros.
- **Fontes do sistema** (`system-ui`) são uma escolha válida e a mais rápida.
- Texto do corpo: **16–18 px** (1–1.125 rem) no telemóvel, altura de linha **1.5–1.7**, linhas de **45–75 caracteres** (`max-width: var(--largura-texto)`).
- Escala de títulos fluida com `clamp()`:

```css
h1 { font-size: clamp(2.25rem, 1.6rem + 3vw, 4rem); line-height: 1.1; }
h2 { font-size: clamp(1.75rem, 1.4rem + 1.6vw, 2.75rem); line-height: 1.15; }
h3 { font-size: clamp(1.25rem, 1.1rem + .6vw, 1.5rem); line-height: 1.25; }
```

- Hierarquia por **tamanho, peso e espaço** — não por cores diferentes em cada título.
- `text-wrap: balance` nos títulos e `text-wrap: pretty` nos parágrafos evitam palavras sozinhas.

## 4. Cor

- Paleta: **1 cor primária** (ações e destaques), **neutros** (fundo, superfícies, texto, bordas), **1 acento** opcional, e cores de estado (sucesso, erro, aviso).
- A cor primária é usada com parcimónia: botões principais, links, pequenos destaques. Se tudo é colorido, nada se destaca.
- **Contraste verificado**: texto normal ≥ **4,5:1**, texto grande e ícones/bordas de campos ≥ **3:1**. Texto branco sobre a cor primária também tem de passar — se não passar, escurece a primária.
- Nunca transmitir informação só pela cor (erros também em texto/ícone).
- Fundos muito brancos (#fff) cansam; um branco-quente ou cinza muito claro é mais confortável. Texto #000 puro em fundo branco é duro; usar um quase-preto.

## 5. Espaçamento e grelha

- Escala única de espaçamento (4/8 px). Espaços **entre secções** grandes (64–128 px no desktop, 48–80 no telemóvel); espaços **dentro** de grupos pequenos. A proximidade mostra o que pertence a quê.
- Contentor centrado: `width: min(100% - 2rem, var(--largura-max)); margin-inline: auto;` — margens laterais de 16 px no telemóvel.
- Layouts com **CSS Grid** e **Flexbox**, `gap` em vez de margens soltas; grelhas que se adaptam sem *media queries*:

```css
.grelha { display: grid; gap: var(--e-6); grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); }
```

- **Alinhamentos**: tudo alinhado ao mesmo eixo esquerdo dentro do contentor; texto longo alinhado à esquerda (não justificado, não centrado em parágrafos longos).

## 6. Componentes

**Cabeçalho e navegação**
- Logótipo (link para o início) + 3–6 links + 1 botão de ação principal.
- No telemóvel: botão de menu com `aria-expanded`, `aria-controls`, nome acessível ("Menu"), fecha com Esc e ao escolher um link. O site-base já faz isto.
- Cabeçalho fixo só se for baixo (≤ 64 px) e não tapar conteúdo; `scroll-margin-top` nas âncoras.

**Topo (hero)**
- Título com o **benefício** (não "Bem-vindo"), subtítulo de 1–2 frases, **um** botão principal (+ um secundário opcional), imagem relevante.
- Visível sem scroll em telemóvel: título + botão. Imagem do topo com `fetchpriority="high"` e sem *lazy loading*.
- Sem carrosséis automáticos (ninguém vê o segundo slide e prejudicam a acessibilidade).

**Botões e links**
- Botão principal cheio (cor primária), secundário com contorno; texto com verbo ("Marcar consulta", não "Clique aqui").
- Altura ≥ 44 px, área de toque generosa; estados `:hover`, `:focus-visible` (contorno bem visível), `:active`, desativado.
- Links dentro de texto sublinhados.

**Cartões**
- Imagem com proporção fixa (`aspect-ratio`), título, 1–2 linhas, ação. Cartão inteiro clicável só com um único link (técnica do pseudo-elemento), nunca links dentro de links.

**Formulários**
- `<label>` visível em cada campo (não só *placeholder*), campos ≥ 44 px de altura, texto 16 px+ (evita zoom no iOS).
- `autocomplete` correto (`name`, `email`, `tel`), `type` correto (`email`, `tel`), `inputmode` quando útil.
- Erros junto do campo, em texto, ligados com `aria-describedby`; mensagem de sucesso clara; nada se perde se houver erro.
- Pedir só o essencial; link para a privacidade junto ao botão.

**Rodapé**
- Contactos, horário, links principais, redes sociais, links legais (privacidade, cookies, termos, livro de reclamações), © ano atual (gerado, para não ficar desatualizado).

**Outros**: testemunhos (reais, com nome e contexto), FAQ (`<details>`/`<summary>` é acessível e sem JS), tabelas de preços (destacar uma opção), galeria (grelha + `loading="lazy"`; *lightbox* acessível ou só abrir a imagem).

## 7. Imagens

- **Formato**: AVIF ou WebP para fotografias (com JPEG de recurso se necessário via `<picture>`); SVG para logótipos e ícones; PNG só para casos especiais.
- **Tamanho**: gerar 2–4 larguras (ex.: 480, 960, 1440, 1920) e usar `srcset` + `sizes`. Peso alvo: < 200 KB por fotografia, < 300 KB a do topo.
- **Sempre** `width` e `height` (evita saltos), `alt` descritivo (ou `alt=""` se decorativa), `decoding="async"`, `loading="lazy"` abaixo da dobra.
- **Recorte**: `object-fit: cover` + `aspect-ratio` consistente nas grelhas.
- **Ferramentas** (se disponíveis): `cwebp`/`avifenc`, `sharp` (Node), `sips` (macOS) para redimensionar; Squoosh no browser para o utilizador.
- Remover metadados GPS das fotografias do utilizador.
- Licença: só imagens do utilizador, de bancos com licença livre, ou criadas por ele.

```html
<picture>
  <source type="image/avif" srcset="/img/loja-960.avif 960w, /img/loja-1600.avif 1600w" sizes="(min-width: 64rem) 50vw, 100vw">
  <img src="/img/loja-960.webp" srcset="/img/loja-960.webp 960w, /img/loja-1600.webp 1600w" sizes="(min-width: 64rem) 50vw, 100vw"
       width="1600" height="1067" alt="Interior da padaria com pão acabado de sair do forno" loading="lazy" decoding="async">
</picture>
```

## 8. Movimento

- Pouco e com propósito: transições de 150–250 ms em estados (hover, abrir menu), aparecimento suave de secções opcional.
- Só animar `transform` e `opacity`.
- Respeitar sempre `prefers-reduced-motion: reduce` (o site-base já desliga animações nesse caso).
- Sem parallax pesado, sem vídeo automático com som, nada a piscar.

## 9. Modo escuro

- Se o site tiver modo escuro, redefine os tokens em `@media (prefers-color-scheme: dark)` — não reescrevas componentes.
- Verifica contraste nos dois modos; logótipos e ilustrações escuras precisam de versão clara; sombras quase não se veem no escuro (usar bordas subtis).
- É opcional: um site só claro, bem feito, é melhor do que um modo escuro mal feito. Pergunta ao utilizador.

## 10. Evitar o aspeto genérico

Sites feitos à pressa parecem todos iguais (gradiente roxo, ícones genéricos em três colunas, "Bem-vindo ao nosso site"). Para fugir disso:

- Um **elemento de assinatura** derivado da marca: uma forma, uma textura, um padrão no fundo, uma forma de recortar fotografias, uma cor inesperada.
- **Fotografias reais** do negócio valem mais do que qualquer ilustração de stock.
- **Texto específico**: "Pão de fermentação lenta, cozido às 6h em Campo de Ourique" em vez de "Os melhores produtos de qualidade".
- **Ritmo**: alternar secções (texto+imagem, faixa de cor, grelha, citação grande) em vez de blocos iguais em sequência.
- Uma tipografia de títulos com caráter, usada com confiança e em tamanho grande.

## 11. Erros comuns a evitar

- Texto sobre fotografias sem sobreposição escura (contraste ilegível).
- Botões com texto vago, ou três botões "principais" lado a lado.
- *Placeholders* em vez de etiquetas nos formulários.
- Ícones sem texto em navegação.
- Menus com mais de 7 itens.
- Pop-ups no primeiro segundo (newsletter, chat a abrir sozinho).
- Fundo com vídeo pesado no telemóvel.
- Larguras fixas em px que rebentam no telemóvel; `100vh` no iOS (usar `100svh`/`100dvh`).
