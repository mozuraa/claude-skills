---
name: design-vocabulary
description: Dicionário prático de 25 termos de design de interfaces que todo o designer e programador deve conhecer — kerning, tracking, leading, x-height, optical centre, tabular numbers, line length, orphan, widow, OKLCH, tinted neutral, layout shift, optimistic update, touch target, safe area, affordance, combobox, progressive disclosure, skeleton screen, empty state, stagger, ease-out, origin-aware animation, interruptible animation, shared element transition. Usa sempre que o utilizador perguntar "o que é X" sobre design/UI, quando precisares de nomear um problema numa revisão de design (ex.: "o texto salta quando carrega" = layout shift), quando escreveres feedback de design ou prompts de design para uma IA e quiseres usar o termo certo, ou quando o utilizador disser "não sei como se chama isto" a descrever um detalhe visual.
---

# Design Vocabulary

Skill extraída de dois reels de [@charles.unemployed](https://www.instagram.com/charles.unemployed/):
- **"20 Design Terms You Should Know (in under 30 seconds)"** — [reel](https://www.instagram.com/reel/Dfh24cUh4KF/) (nov. 2026), com a lista dos 20 termos no ecrã.
- A legenda do mesmo reel acrescenta **5 termos extra** com definição do autor (marcados com ✱).

> A lista de termos vem do reel. As definições sem ✱, os exemplos e a secção "Como aplicar" foram escritos para tornar a skill útil.

Responde na língua do utilizador. Quando explicares um termo: definição numa frase → exemplo visual concreto → como corrigir/aplicar (com código se ajudar).

## Tipografia

| Termo | O que é | Como aplicar |
|---|---|---|
| **Kerning** | Ajuste do espaço entre **dois caracteres específicos** (ex.: "AV", "To"). | Em títulos grandes, ativa `font-kerning: normal` e corrige pares feios à mão em logótipos. |
| **Tracking** | Espaço **uniforme** entre todas as letras de um bloco (`letter-spacing`). | Títulos grandes: tracking ligeiramente negativo (-0.01 a -0.03em). Texto em maiúsculas pequenas: positivo (+0.05 a +0.1em). |
| **Leading** | Espaço entre linhas (`line-height`). | Corpo de texto 1.4–1.6; títulos 1.05–1.2. Quanto maior a letra, menor o leading relativo. |
| **x-height** | Altura das minúsculas (a altura do "x"). Fontes com x-height alta parecem maiores e leem-se melhor em tamanhos pequenos. | Ao misturar fontes, alinha pela x-height, não pelo tamanho em px. |
| **Optical centre** | O centro que o olho *percebe*, ligeiramente acima do centro geométrico. | Num botão com ícone ▶ ou num título num cartão, sobe 1–2 px / desloca o triângulo para a direita para *parecer* centrado. |
| **Tabular numbers** | Números com largura igual (monoespaçados), para colunas e valores que mudam. | `font-variant-numeric: tabular-nums;` em tabelas, preços, timers e contadores — evita que o texto "dance". |
| **Line length** | Número de caracteres por linha. | Ideal 45–75 caracteres (`max-width: 65ch`). Linhas longas cansam; curtas partem o ritmo. |
| **Orphan** ✱ | A última linha solitária de um parágrafo que fica isolada no topo da coluna/página seguinte. | Em web: `orphans`/`widows` no CSS de impressão; em layout, ajusta a altura do bloco. |
| **Widow** | Uma palavra sozinha na última linha de um parágrafo ou título. | `text-wrap: pretty;` (parágrafos) e `text-wrap: balance;` (títulos), ou `&nbsp;` entre as duas últimas palavras. |

## Cor

| Termo | O que é | Como aplicar |
|---|---|---|
| **OKLCH** | Espaço de cor perceptualmente uniforme: Lightness, Chroma, Hue. Mudar a luminosidade não altera o "tom" percebido. | Gera escalas de cor consistentes: `oklch(62% 0.19 255)` e varia só o L. Ótimo para temas claro/escuro. |
| **Tinted neutral** ✱ | Um cinzento com um toque de cor, para parecer escolhido em vez de default. | Em vez de `#888`, usa um cinzento puxado para a cor da marca: `oklch(60% 0.01 255)`. |

## Layout e comportamento

| Termo | O que é | Como aplicar |
|---|---|---|
| **Layout shift** | O conteúdo salta de sítio enquanto a página carrega (métrica CLS). | Reserva espaço: `width`/`height` ou `aspect-ratio` em imagens, skeletons do mesmo tamanho, fontes com `size-adjust`. |
| **Optimistic update** | A UI mostra o resultado **antes** de o servidor confirmar, e reverte se falhar. | Likes, toggles, mover cartões. Guarda o estado anterior para rollback e mostra erro discreto. |
| **Touch target** | A área tocável de um elemento. | Mínimo 44×44 pt (iOS) / 48×48 dp (Android); aumenta com padding sem mudar o visual. |
| **Safe area** | Zona do ecrã livre de notch, Dynamic Island, cantos arredondados e barra de gestos. | `padding: env(safe-area-inset-top)` etc. com `viewport-fit=cover`; `SafeAreaView` / `.safeAreaInset` no nativo. |
| **Affordance** | Pistas visuais que dizem *como* um elemento se usa (um botão parece clicável, uma pega parece arrastável). | Sombra/relevo em botões, cursor `pointer`, sublinhado em links, "grabber" em sheets. |
| **Combobox** | Campo de texto + lista de sugestões filtrável (autocomplete com seleção). | Usa para listas longas (países, cidades) em vez de `<select>` gigante; segue o padrão ARIA `combobox`. |
| **Progressive disclosure** | Mostrar só o essencial e revelar o avançado quando é pedido. | "Opções avançadas", passos num formulário, "Ver mais". Reduz a carga de decisão (lei de Hick). |
| **Skeleton screen** ✱ | Formas cinzentas de placeholder que seguram o layout enquanto o conteúdo carrega. | Mesmo tamanho do conteúdo final, shimmer subtil; melhor que um spinner para listas e cartões. |
| **Empty state** ✱ | O que um ecrã mostra antes de haver conteúdo. | Explica o que vai aparecer ali + uma ação clara ("Criar primeiro projeto"). Nunca um ecrã vazio sem texto. |

## Animação

| Termo | O que é | Como aplicar |
|---|---|---|
| **Stagger** | Elementos de uma lista animam com um pequeno atraso em cascata. | 20–40ms entre itens, máximo ~8 itens em cascata (o resto aparece junto). |
| **Ease-out** ✱ | Começa rápido e abranda até parar — o padrão para tudo o que *entra* no ecrã. | `cubic-bezier(0.16, 1, 0.3, 1)`; saídas usam ease-in. |
| **Origin-aware animation** | A animação parte do sítio de onde foi acionada (um menu cresce a partir do botão que o abriu). | `transform-origin` igual à posição do gatilho; Radix expõe `--radix-popover-content-transform-origin`. |
| **Interruptible animation** | Uma animação que pode ser interrompida e invertida a meio, sem saltar nem esperar que acabe. | Usa transições CSS (não keyframes) ou springs, que partem do estado atual. Essencial em gestos e toggles rápidos. |
| **Shared element transition** | Um elemento "viaja" entre dois ecrãs (miniatura → imagem em detalhe). | View Transitions API (`view-transition-name`), Framer Motion `layoutId`, SwiftUI `matchedGeometryEffect`, Flutter `Hero`. |

Ver também a skill `ui-motion-ux` (princípios de animação e leis de UX) do mesmo autor.
