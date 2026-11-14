---
name: depth-backgrounds
description: Catálogo de 22 tipos de fundo para tornar designs menos planos — felt texture, fluted glass, thermal gradients, water ripples, speckled graphite, single-hue landscapes, blueprint grids, halftone, grainy gradients, grass texture, dithered images, paper texture, contour lines, cloud sky, pixel mosaics, lens distortion, stippled gradients, square-dot grids, blurred photos, iridescent shapes, impressionist paintings, ASCII e pixels — com receitas em CSS/SVG/canvas e quando usar cada um. Usa sempre que o utilizador disser que um site, hero, landing page, cartão ou app "está plano", "sem graça", "genérico", "parece feito por IA", pedir um fundo, textura, gradiente, padrão, "hero mais interessante", ou quiser dar profundidade/personalidade visual a uma interface.
---

# Depth Backgrounds

Skill extraída do reel **"22 Backgrounds to Make Designs Less Flat (in under 30 seconds)"** de [@charles.unemployed](https://www.instagram.com/reel/DffEWqKhKWo/) (nov. 2026). No vídeo, cada fundo aparece aplicado por trás de um cartão de UI (widget de tempo/música).

> A lista dos 22 fundos é a do reel. As descrições, receitas e regras de uso foram acrescentadas.

Responde na língua do utilizador.

## Regras de uso

1. **O fundo serve o conteúdo.** Texto por cima tem de ter contraste ≥ 4.5:1 — põe um véu (`background: rgb(0 0 0 / .35)`), um cartão sólido/vidro, ou escolhe uma zona calma do fundo.
2. **Um só fundo expressivo por ecrã** (normalmente o hero). O resto do site fica calmo.
3. **Combina com a marca:** escolhe pela personalidade (técnico → blueprint/contour/ASCII; artesanal → paper/felt/stippled; premium → fluted glass/iridescent; natural → cloud/water/grass).
4. **Performance:** prefere CSS/SVG leve; imagens em AVIF/WebP com `loading="lazy"` fora do ecrã; shaders/canvas só no hero e pausados fora de vista; respeita `prefers-reduced-motion` em fundos animados.
5. **Ruído evita banding:** qualquer gradiente grande fica melhor com uma camada de grão a 3–8 % de opacidade.

## Os 22 fundos

| # | Fundo | Sensação | Receita rápida |
|---|---|---|---|
| 1 | **Felt texture** | Tátil, acolhedor, físico | Foto/textura de feltro em tom único + `background-blend-mode: multiply` sobre a cor da marca. |
| 2 | **Fluted glass** | Premium, arquitetónico | Imagem/gradiente por trás + faixas verticais: `repeating-linear-gradient(90deg, rgb(255 255 255/.12) 0 2px, transparent 2px 24px)` com `backdrop-filter: blur(12px)`; ou SVG `feDisplacementMap`. |
| 3 | **Thermal gradients** | Energia, tecnologia, calor | Gradiente mapa-de-calor (azul→verde→amarelo→vermelho) com blobs: vários `radial-gradient` + `filter: blur(60px)`. |
| 4 | **Water ripples** | Calma, fluidez | SVG `feTurbulence` (baseFrequency baixa) + `feDisplacementMap` sobre uma foto de água; ou shader de ondas. |
| 5 | **Speckled graphite** | Sóbrio, editorial | Cinza escuro + grão denso (`feTurbulence` com `numOctaves=3`, opacidade 15 %). |
| 6 | **Single-hue landscapes** | Sereno, cinematográfico | Foto de paisagem convertida a monocromático na cor da marca (`filter: grayscale(1)` + overlay `mix-blend-mode: color`). |
| 7 | **Blueprint grids** | Técnico, engenharia | `background: linear-gradient(#fff2 1px, transparent 1px) 0 0/24px 24px, linear-gradient(90deg, #fff2 1px, transparent 1px) 0 0/24px 24px, #0b3a6e;` |
| 8 | **Halftone** | Retro, impressão, pop | `radial-gradient(circle, #000 35%, transparent 36%) 0 0/8px 8px` com máscara em gradiente para variar o tamanho dos pontos. |
| 9 | **Grainy gradients** | Moderno, quente, "anti-IA" | Gradiente suave + camada de ruído SVG (`feTurbulence type="fractalNoise"`) com `mix-blend-mode: overlay`. |
| 10 | **Grass texture** | Natural, orgânico, lúdico | Foto macro de relva com profundidade de campo, desaturada e escurecida para texto. |
| 11 | **Dithered images** | Retro-digital, indie | Foto convertida com dithering (Floyd–Steinberg/Bayer) em 2–4 cores; `image-rendering: pixelated`. |
| 12 | **Paper texture** | Artesanal, editorial, humano | Textura de papel com fibras + `multiply`; combina com tipografia serif. |
| 13 | **Contour lines** | Exploração, dados, mapa | SVG de linhas topográficas (gerador ou `d3-contour`), traço fino 1px a 10–20 % de opacidade. |
| 14 | **Cloud sky** | Leve, sonhador, otimista | Foto de céu com nuvens, ou gradiente azul + nuvens via `feTurbulence` com máscara. |
| 15 | **Pixel mosaics** | Jogo, nostalgia, criativo | Grelha de quadrados com cores amostradas de uma imagem (canvas) ou padrão SVG. |
| 16 | **Lens distortion** | Ótico, experimental | Shader ou SVG `feDisplacementMap` com mapa radial — distorce a imagem como por uma lente. |
| 17 | **Stippled gradients** | Ilustrado, manual | Gradiente feito de pontos de densidade variável (canvas ou SVG gerado). |
| 18 | **Square-dot grids** | Minimal, produto, Figma-like | `radial-gradient(#0002 1px, transparent 1px) 0 0/16px 16px` (pontos) ou quadrados de 2px. |
| 19 | **Blurred photos** | Ambiente, foco no conteúdo | Foto relevante com `filter: blur(40px) saturate(1.2)` e `scale(1.1)` para esconder bordas. |
| 20 | **Iridescent shapes** | Futurista, holográfico, luxo | `conic-gradient` multicolor em formas 3D/blobs + `blur`; ou render 3D com material iridescente. |
| 21 | **Impressionist paintings** | Cultura, elegância, intemporal | Pintura de domínio público (ex.: Monet, Museu Met/Rijksmuseum) recortada e escurecida. Confirma a licença. |
| 22 | **ASCII and pixels** | Hacker, dev-tool, retro-computing | Imagem convertida para caracteres ASCII (canvas) em monospace a baixa opacidade, ou animação de caracteres. |

## Como escolher (atalho)

- **SaaS / dev tool:** blueprint grids, square-dot grids, ASCII, contour lines.
- **App de consumo / lifestyle:** grainy gradients, blurred photos, cloud sky, single-hue landscapes.
- **Marca premium / produto físico:** fluted glass, iridescent shapes, felt/paper texture.
- **Portfólio / criativo:** halftone, dithered, pixel mosaics, impressionist paintings, stippled.

## Exemplo — grainy gradient pronto a usar

```css
.hero {
  position: relative;
  isolation: isolate;
  background:
    radial-gradient(60% 80% at 20% 20%, oklch(75% .15 30), transparent),
    radial-gradient(60% 80% at 80% 70%, oklch(65% .18 280), transparent),
    oklch(20% .03 270);
}
.hero::after {               /* camada de grão por cima do gradiente, por baixo do texto */
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  opacity: .12;
  mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```
