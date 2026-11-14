---
name: ui-motion-ux
description: Aplica e revê 20 princípios de UX e animação de interfaces — os 12 princípios de animação da Disney adaptados a UI (squash & stretch, antecipação, staging, pose to pose, follow through, slow in/slow out, arcos, ação secundária, timing, exagero, volume, appeal) e 8 leis de UX (Fitts, áreas de toque maiores, Hick, Miller, limiar de Doherty, Postel, Jakob, frequência de uso). Usa sempre que o utilizador pedir para animar um componente, criar micro-interações, transições, hover/press states, "dar vida" ou "polish" a uma interface, perguntar que duração ou easing usar, porque é que uma animação parece lenta/robótica/barata, ou rever a UX de um ecrã (botões pequenos, demasiadas opções, formulários rígidos, app lenta a responder) — em CSS, Tailwind, Framer Motion/Motion, React Native Reanimated, SwiftUI, Flutter ou Compose, mesmo que não diga "animação" nem "UX".
---

# UI Motion & UX Laws

Skill extraída do reel **"20 Principles of UX & Animation (in under 30 seconds)"** de [@charles.unemployed](https://www.instagram.com/reel/DfphRvFBx54/) (nov. 2026). No vídeo, cada princípio aparece com uma legenda curta e uma demo **Antes / Depois** (ex.: notificação a 500ms → 150ms).

**Fontes citadas pelo autor:** Raphael Salaja — *userinterface.wiki*; Disney — *The Illusion of Life* (os 12 princípios); Jon Yablonski — *Laws of UX*; Emil Kowalski — regra da frequência de uso.

> As definições abaixo (em **negrito**) são as do reel. As secções "Na prática" e os valores concretos são orientações de implementação acrescentadas para tornar a skill acionável.

Responde na língua do utilizador.

## Como usar esta skill

1. **Ao criar** animação ou UI: escolhe só os princípios que servem o momento (não aplicar os 20 a tudo). Começa sempre por *Frequência de uso*, *Timing* e *Slow in & slow out* — são os que mais pesam.
2. **Ao rever**: percorre a checklist no fim, aponta cada problema com o princípio violado, o porquê e a correção concreta (com valores).
3. Respeita sempre `prefers-reduced-motion` / "Reduzir movimento": substitui movimento por fade curto ou nada.
4. Anima de preferência `transform` e `opacity` (GPU); evita animar `width`, `height`, `top`, `left`, `box-shadow` pesados.

---

## Parte 1 — 12 princípios de animação aplicados a UI

### 1. Squash & stretch
**As coisas achatam no impacto e esticam em movimento, o que lhes dá peso.**
- No vídeo: "Things squish on impact to show weight" — ícones de uma dock que comprimem ao serem tocados.
- Na prática: no `:active`/press, `scale(0.95–0.97)`; ao aterrar (bounce de um badge, toggle), um ligeiro `scaleY(0.9) scaleX(1.05)` e volta. Mantém o volume (se achata num eixo, alarga no outro). Subtil em UI — 2–8 %, nunca cartoon.

### 2. Anticipation (wind-up)
**Um pequeno recuo antes do movimento grande, para as pessoas o verem chegar.**
- No vídeo: "A small wind-up before the big move" — ícone de enviar (avião de papel) que recua antes de disparar.
- Na prática: antes de uma saída rápida, recua 2–4 px ou `scale(0.96)` durante ~60–100ms, depois parte. Usa em ações com consequência (enviar, apagar, lançar). Easing tipo `cubic-bezier(0.36, 0, 0.66, -0.56)` (back-in) faz isto de graça.

### 3. Staging the focus
**Dirige o olhar para uma coisa de cada vez.**
- No vídeo: "Direct the eye to one thing at a time" — grelha de cartões → o cartão escolhido destaca-se e o resto recua.
- Na prática: quando algo abre (modal, cartão expandido), escurece/desfoca o fundo, reduz a opacidade do resto e anima só o elemento principal. Nunca dois movimentos importantes ao mesmo tempo no mesmo sítio.

### 4. Pose to pose
**Define as poses-chave e deixa o browser preencher os frames entre elas.**
- No vídeo: "Set the key poses, let the rest fill in" — elemento com início, pose-chave e fim numa timeline.
- Na prática: declara estados (início/fim, ou poucos `@keyframes`) e deixa transições/interpolação fazer o resto: `transition`, `@keyframes`, Framer Motion `animate`, SwiftUI `withAnimation`, layout animations (FLIP). Não animes frame a frame em JS.

### 5. Follow through
**Partes continuam a mexer depois de o corpo principal parar, e depois assentam.**
- Na prática: depois de um painel parar, o conteúdo interno assenta 40–80ms mais tarde; um pequeno overshoot (1–3 %) com retorno. Springs com algum bounce (`damping` moderado) dão isto naturalmente. Também: stagger de filhos (20–40ms entre itens).

### 6. Slow in & slow out
**Acelera e desacelera — nunca te movas a velocidade constante.**
- Na prática: nunca `linear` em movimento (só em loaders/rotações contínuas e progress bars).
  - Entrada no ecrã → **ease-out** (`cubic-bezier(0.16, 1, 0.3, 1)` ou `(0.22, 1, 0.36, 1)`).
  - Saída → **ease-in**, mais curta que a entrada.
  - Movimento dentro do ecrã → **ease-in-out** (`cubic-bezier(0.65, 0, 0.35, 1)`).
  - Gestos/arrastos → springs.

### 7. Moving in arcs
**Move ao longo de curvas, não em linhas retas.**
- Na prática: objetos que viajam longe (item a voar para o carrinho, FAB que se transforma em ecrã) seguem curva: anima X e Y com easings diferentes, ou usa `offset-path` / motion paths. Em movimentos curtos e retos (dropdown), não é preciso.

### 8. Secondary action
**Um pequeno floreado que reforça a ação principal.**
- Na prática: ao dar "like", o coração cresce (ação principal) e soltam-se partículas/um anel (secundária); ao copiar, o ícone troca para ✓. A secundária nunca compete com a principal: menor, mais rápida, opcional.

### 9. Snappy timing
**A duração define a sensação — mantém as animações de UI abaixo de 300ms.**
- No vídeo: "Duration sets the feel. Keep UI under 300ms" — notificação: **Antes 500ms → Depois 150ms**.
- Na prática (referência):
  | Tipo | Duração |
  |---|---|
  | Hover, press, toggle, cor | 100–150ms |
  | Tooltips, dropdowns, pequenos elementos | 150–200ms |
  | Modais, sheets, cartões a expandir | 200–300ms |
  | Transições de ecrã inteiro / elementos grandes | até ~400ms (exceção, não regra) |
  - Saídas ~20–30 % mais rápidas que entradas. Distâncias maiores → um pouco mais de tempo.

### 10. Exaggerated feedback
**Leva-o além do real para que o momento tenha impacto.**
- Na prática: momentos raros e importantes (compra concluída, objetivo cumprido, erro de password com shake) merecem exagero: confetti, bounce maior, shake de 3 oscilações de ±6 px. Momentos frequentes **não** (ver regra 20).

### 11. Solid drawing in 3D
**Dá profundidade e volume a coisas planas.**
- Na prática: sombras em camadas que crescem com a elevação (elemento levantado = sombra maior e mais difusa), `perspective` + `rotateX/Y` leve em flips e tilt, highlight subtil no topo. Elementos em cima devem parecer em cima.

### 12. Overall appeal
**A soma de todos os detalhes, feita com cuidado.**
- Na prática: consistência (mesmos easings e durações em todo o produto, definidos como tokens), nada a saltar/piscar, estados de loading/vazio/erro também animados com cuidado, 60 fps reais. Se um detalhe chama atenção por ser estranho, está errado.

---

## Parte 2 — Leis de UX

### 13. Lei de Fitts
**Alvos maiores e mais próximos são mais rápidos de acertar.**
- Na prática: ação principal grande e perto de onde o polegar/cursor já está; ações destrutivas longe das frequentes; cantos e bordas do ecrã são alvos "infinitos" no desktop.

### 14. Áreas de clique maiores
**A área clicável pode ser maior do que parece.**
- Na prática: mínimo **44×44 pt** (iOS) / **48×48 dp** (Android) / 24×24 px CSS (WCAG 2.2 AA, recomendado 44). Ícone pequeno → aumenta a área com `padding` ou um pseudo-elemento (`::before { inset: -8px }`) sem mudar o visual. Espaço entre alvos para evitar toques errados.

### 15. Lei de Hick
**Mais escolhas significam decisões mais lentas.**
- Na prática: uma ação primária por ecrã; esconde opções avançadas ("Mais…"); divide fluxos longos em passos; destaca a opção recomendada.

### 16. Lei de Miller
**Guardamos cerca de 7 coisas na cabeça de cada vez, por isso agrupa a informação.**
- Na prática: agrupa (chunking) — números de telefone/cartões em blocos, menus em secções, formulários em grupos. Não é um limite rígido de 7 itens num menu; é sobre carga de memória.

### 17. Limiar de Doherty
**Responde em menos de 400ms ou parece lento.**
- Na prática: feedback visual imediato (<100ms) a qualquer toque; UI otimista (mostra o resultado antes de o servidor confirmar); skeletons em vez de spinners; se demorar >1s, mostra progresso.

### 18. Lei de Postel
**Aceita input desarrumado, devolve output limpo.**
- Na prática: aceita telefone com espaços, traços ou `+351`; datas em vários formatos; emails com espaços à volta (faz `trim`); não obrigues a maiúsculas/minúsculas. Depois normaliza e mostra formatado.

### 19. Lei de Jakob
**As pessoas esperam que a tua app funcione como as apps que já usam.**
- Na prática: segue as convenções da plataforma (HIG / Material) — logo leva à home, swipe-back no iOS, carrinho no canto superior direito, pull-to-refresh. Inova no produto, não nos padrões básicos.

### 20. Frequência de uso
**Quanto mais vezes algo é usado, menos deve animar.**
- Na prática:
  - Centenas de vezes por dia (atalhos de teclado, command palette, mudar de tab, menus de contexto) → **sem animação** ou instantânea.
  - Várias vezes por dia (abrir modal, sidebar) → rápida e discreta (≤200ms).
  - Rara (onboarding, primeira vez, celebração) → pode ser expressiva (regra 10).
  - Ações por teclado devem ser instantâneas mesmo que o clique equivalente anime.

---

## Checklist de revisão

Para cada animação/ecrã, verifica:

- [ ] **Frequência:** isto é usado muitas vezes? Então anima menos ou nada.
- [ ] **Duração:** < 300ms (exceto transições grandes); saída mais curta que entrada.
- [ ] **Easing:** nada de `linear` em movimento; ease-out a entrar, ease-in a sair, springs em gestos.
- [ ] **Foco:** só uma coisa importante a mexer de cada vez.
- [ ] **Física:** press com `scale` subtil; overshoot/settle onde faz sentido; arcos em trajetos longos.
- [ ] **Propósito:** a animação explica algo (de onde veio, para onde foi, o que mudou)? Se é só decoração, corta ou encurta.
- [ ] **Performance:** só `transform`/`opacity`; 60 fps; sem layout thrashing.
- [ ] **Acessibilidade:** respeita `prefers-reduced-motion`; nada a piscar >3×/s.
- [ ] **Alvos:** ≥44 pt / 48 dp; áreas de clique alargadas em ícones pequenos.
- [ ] **Escolhas:** uma ação primária clara; opções secundárias escondidas/agrupadas.
- [ ] **Resposta:** feedback <100ms; UI otimista ou skeleton se a operação demora.
- [ ] **Input:** formulários tolerantes a formatos; output normalizado.
- [ ] **Convenções:** comporta-se como as apps da plataforma?

## Tokens de movimento recomendados (ponto de partida)

```css
:root {
  --duration-instant: 100ms;
  --duration-fast: 150ms;
  --duration-base: 200ms;
  --duration-slow: 300ms;

  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);      /* entradas */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);       /* saídas */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);  /* movimento no ecrã */
  --ease-back: cubic-bezier(0.34, 1.56, 0.64, 1); /* overshoot / follow through */
}

.button { transition: transform var(--duration-instant) var(--ease-out); }
.button:active { transform: scale(0.97); }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Equivalentes: Framer Motion/Motion `transition={{ type: "spring", stiffness: 400, damping: 30 }}`; SwiftUI `.spring(response: 0.3, dampingFraction: 0.8)` / `.snappy`; Reanimated `withSpring(v, { damping: 18, stiffness: 220 })`; Flutter `Curves.easeOutCubic` com `Duration(milliseconds: 200)`.

## Formato de resposta numa revisão

Para cada problema: **Princípio violado** → o que está mal (com ficheiro:linha se for código) → porque importa → correção concreta com valores. Termina com as 3 mudanças de maior impacto, por ordem.
