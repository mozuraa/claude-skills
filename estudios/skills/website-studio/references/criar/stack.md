# Escolher a tecnologia, o alojamento e os serviços

A regra: **a tecnologia mais simples que resolve o problema e que o utilizador consegue manter.** Explica a escolha numa frase e diz quanto custa. Os preços são indicativos e mudam — confirma no site do serviço antes de os prometer.

## Índice

- [Decisão rápida](#decisão-rápida)
- [Opções em detalhe](#opções-em-detalhe)
- [Alojamento](#alojamento)
- [Formulários](#formulários)
- [Editar conteúdo sem programar (CMS)](#editar-conteúdo-sem-programar-cms)
- [Estatísticas sem cookies](#estatísticas-sem-cookies)
- [Outros serviços comuns](#outros-serviços-comuns)
- [Custos típicos](#custos-típicos)

---

## Decisão rápida

| Situação | Recomendação |
|---|---|
| 1–10 páginas, muda pouco, o Claude ou um programador faz as alterações | **HTML + CSS** (site-base da skill) |
| Site com muitas páginas parecidas, blog em Markdown, várias línguas | **Astro** |
| Precisa de área de cliente, login, dados dinâmicos, painel | **Next.js** (ou SvelteKit/Nuxt) + base de dados (Supabase, etc.) |
| O utilizador quer editar tudo sozinho, sem código, com frequência | **WordPress** (alojado) ou **Astro + CMS** (Decap, Sanity); ou um construtor (Squarespace, Wix, Framer) |
| Loja com muitos produtos, stock, envios | **Shopify** ou **WooCommerce** |
| 1–5 produtos ou serviços pagos | Site simples + **links de pagamento** (Stripe Payment Links, etc.) |
| Página de uma app | **HTML + CSS** ou **Astro** |

**Opinião franca a dar:** se o utilizador não programa e não vai ter ajuda para manter o site, um construtor visual pode ser melhor do que código — mesmo que o Claude consiga fazer um site mais rápido em código. Diz-lhe as vantagens e as desvantagens das duas opções e deixa-o escolher.

## Opções em detalhe

**HTML + CSS (+ um pouco de JS)**
- ✅ Mais rápido possível, zero dependências, aloja-se grátis em qualquer lado, dura décadas sem manutenção.
- ❌ Repetir cabeçalho/rodapé em cada página (aceitável até ~10 páginas); editar exige mexer em HTML.
- Usa o `assets/starter/`.

**Astro**
- ✅ Componentes (cabeçalho escrito uma vez), Markdown para conteúdo, gera HTML estático rápido, ótimo para blogs e várias línguas, integra CMS.
- ❌ Precisa de Node e de um passo de build.
- Criar: `npm create astro@latest`. Imagens: `astro:assets`. Sitemap: `@astrojs/sitemap`.

**Next.js**
- ✅ Para sites com partes dinâmicas: contas, painéis, dados em tempo real, APIs.
- ❌ Mais complexo; mais coisas para manter e proteger. Não usar só para um site de apresentação.
- Criar: `npx create-next-app@latest`. Cuidado: variáveis `NEXT_PUBLIC_*` são públicas.

**WordPress**
- ✅ O utilizador edita tudo num painel; enorme ecossistema.
- ❌ Precisa de atualizações constantes (núcleo, temas, plugins) — é o CMS mais atacado; plugins a mais tornam-no lento. Recomendar alojamento gerido com atualizações e cópias automáticas.

**Construtores (Squarespace, Wix, Framer, Webflow)**
- ✅ Edição visual, alojamento incluído, sem manutenção técnica.
- ❌ Custo mensal, menos controlo sobre velocidade e privacidade, difícil sair da plataforma.

**Shopify / WooCommerce**
- ✅ Pagamentos, impostos, envios, stock e faturas resolvidos.
- ❌ Custo mensal (Shopify) ou manutenção (WooCommerce).

## Alojamento

Para sites estáticos (HTML ou Astro), todos estes têm plano gratuito com HTTPS e domínio próprio:

| Serviço | Bom para | Notas |
|---|---|---|
| **GitHub Pages** | Sites simples, projetos já no GitHub | Sem cabeçalhos HTTP personalizados (não dá para pôr CSP/HSTS próprios). Sem formulários. |
| **Netlify** | Sites estáticos com formulários | `_headers` para cabeçalhos; Netlify Forms (com limite gratuito); deploy ao ligar o repositório. |
| **Cloudflare Pages** | Velocidade e tráfego ilimitado | `_headers`; CDN global; bom se o domínio já está na Cloudflare. |
| **Vercel** | Next.js, Astro com partes de servidor | `vercel.json` para cabeçalhos; plano gratuito é para uso não comercial — confirmar os termos para negócios. |

Para WordPress: alojamento gerido em Portugal/UE (dados na UE ajudam no RGPD).

## Formulários

Um site estático não envia emails sozinho. Opções:

- **Netlify Forms** (se alojado na Netlify): basta um atributo no `<form>`.
- **Formspree, Web3Forms, Basin** e semelhantes: o formulário envia para o serviço, que encaminha por email. Plano gratuito com limite mensal.
- **Função/rota própria** (Vercel/Netlify/Cloudflare Functions, ou Next.js) + serviço de email (Resend, Postmark, Brevo): mais controlo. A chave do serviço de email fica **só no servidor**.
- **Proteção anti-spam**: campo *honeypot* escondido + validação no servidor; CAPTCHA acessível (Cloudflare Turnstile) se o spam continuar.
- **Privacidade**: pedir só os dados precisos, link para a política de privacidade junto ao botão, e escolher um serviço com dados na UE quando possível.

## Editar conteúdo sem programar (CMS)

- **Decap CMS** (grátis, guarda o conteúdo no próprio repositório Git; bom com Netlify/Astro).
- **Sanity, Storyblok, Contentful** (CMS alojados; planos gratuitos com limites; editor muito bom).
- **WordPress** (ver acima).
- Às vezes basta **um ficheiro de dados simples** (`precos.json`, `menu.md`) e o guia `COMO-EDITAR.md` — pergunta se o utilizador está à vontade com isto antes de propor um CMS.

## Estatísticas sem cookies

Se o utilizador quer saber quantas visitas tem, propõe primeiro uma opção **sem cookies** (dispensa banner de consentimento para isso): **Plausible**, **Umami** (pode ser alojado gratuitamente), **Simple Analytics**, **Cloudflare Web Analytics**, **GoatCounter**. Google Analytics só se ele precisar mesmo — e então com banner de consentimento e carregado apenas depois de aceitar.

## Outros serviços comuns

| Precisa de | Opções | Atenção |
|---|---|---|
| Mapa | Link para Google Maps/Apple Maps com imagem estática; OpenStreetMap | Mapa do Google incorporado carrega cookies → carregar só depois de clicar |
| Vídeo | `youtube-nocookie.com`, Vimeo com `dnt=1`, ou ficheiro próprio (`<video>`) | Carregar só ao clicar (fachada com imagem) para não pesar |
| Reservas/marcações | Calendly, Cal.com, SimplyBook, TheFork (restaurantes) | Ver onde ficam os dados; política de privacidade |
| Newsletter | Buttondown, Brevo, MailerLite | Consentimento explícito, sem caixa pré-marcada |
| Pagamentos | Stripe (Payment Links/Checkout), SumUp, PayPal | Nunca guardar dados de cartão no site |
| Fontes | Ficheiros WOFF2 alojados no próprio site (ex.: via Fontsource) | Não carregar do Google Fonts (envia IPs dos visitantes) |
| Ícones | SVG inline, conjuntos abertos (Lucide, Phosphor, Tabler) | Não carregar bibliotecas inteiras de ícones por 5 ícones |

## Custos típicos

| Item | Valor indicativo |
|---|---|
| Domínio `.pt` / `.com` | ~10–25 € por ano |
| Alojamento estático (GitHub Pages, Netlify, Cloudflare) | 0 € (planos gratuitos) |
| Email no domínio (Google Workspace, Microsoft 365, Zoho, Proton) | ~1–7 € por utilizador/mês (Zoho tem plano gratuito limitado) |
| Formulários (Formspree e semelhantes) | 0 € até um limite mensal |
| Estatísticas sem cookies | 0 € (Umami/GoatCounter/Cloudflare) a ~9 €/mês (Plausible) |
| WordPress alojado e gerido | ~5–30 €/mês |
| Construtores (Squarespace, Wix...) | ~15–40 €/mês |
| Shopify | ~30 €/mês + comissões |

Apresenta sempre ao utilizador uma tabela com **o que vai pagar, quanto e quando renova**.
