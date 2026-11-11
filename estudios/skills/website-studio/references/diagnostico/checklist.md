# Checklist completo — websites

Tudo o que examinar num site. Cada item diz **o que verificar** e, quando útil, **o valor certo**. Os comandos para verificar estão em `como-verificar.md`. Nem tudo se aplica a todos os sites (um site estático não tem login nem base de dados) — salta o que não faz sentido e diz que saltaste.

## Índice

1. [Funcionamento](#1-funcionamento)
2. [Layout e alinhamentos](#2-layout-e-alinhamentos)
3. [Imagens e media](#3-imagens-e-media)
4. [Desempenho](#4-desempenho)
5. [Segurança](#5-segurança)
6. [Privacidade e RGPD](#6-privacidade-e-rgpd)
7. [Acessibilidade](#7-acessibilidade)
8. [SEO e partilha](#8-seo-e-partilha)
9. [Conteúdo](#9-conteúdo)
10. [Compatibilidade](#10-compatibilidade)
11. [Domínio, alojamento e email](#11-domínio-alojamento-e-email)
12. [Qualidade do código](#12-qualidade-do-código)

---

## 1. Funcionamento

- [ ] Nenhum erro na consola do browser em nenhuma página principal (erros JS, recursos que não carregam, avisos de CORS).
- [ ] Nenhum pedido de rede falhado (4xx/5xx) para ficheiros do próprio site.
- [ ] Todos os links internos funcionam; links externos importantes funcionam.
- [ ] Existe uma página 404 personalizada, útil (com link para o início), e devolve mesmo o código 404 (não 200).
- [ ] Redirecionamentos: http → https, e www ↔ sem www num só sentido, com 301, sem cadeias de vários saltos.
- [ ] Formulários: enviam, mostram confirmação, mostram erros compreensíveis, não perdem o que foi escrito em caso de erro, o email chega mesmo (testar).
- [ ] Botões e menus funcionam com rato, toque e teclado; o menu móvel abre e fecha.
- [ ] Funcionalidades principais (comprar, reservar, pesquisar, login) funcionam de ponta a ponta.
- [ ] Estados vazios e de erro existem (pesquisa sem resultados, carrinho vazio, falha de rede).
- [ ] Nada depende de estar com sessão iniciada como administrador para funcionar.
- [ ] Páginas carregam sem JavaScript o mínimo indispensável (ou pelo menos mostram uma mensagem).

## 2. Layout e alinhamentos

- [ ] Testado em 320, 375, 768, 1024, 1440 e 1920 px de largura.
- [ ] **Sem scroll horizontal** em nenhuma largura (procurar elementos mais largos que o ecrã: imagens, tabelas, `100vw`, margens negativas, palavras longas/URLs sem quebra).
- [ ] Elementos alinhados numa grelha consistente; margens laterais iguais em todas as secções.
- [ ] Espaçamentos consistentes (usar uma escala: 4/8/16/24/32...), sem valores aleatórios.
- [ ] Nada sobreposto ou cortado (textos por cima de imagens, botões fora do ecrã, menus atrás de outros elementos — `z-index`).
- [ ] Texto longo e traduções não partem o layout (nomes compridos, botões com texto maior).
- [ ] Altura em telemóvel: cuidado com `100vh` no iOS Safari (usar `100dvh`/`svh`); teclado no ecrã não esconde campos.
- [ ] Áreas seguras de iPhone (notch/Dynamic Island) respeitadas quando o site é em ecrã inteiro (`env(safe-area-inset-*)`).
- [ ] Tipografia: tamanho de texto ≥ 16 px em telemóvel (evita zoom automático nos campos no iOS), linhas com 45–80 caracteres, altura de linha ~1.4–1.6, hierarquia clara.
- [ ] Fontes carregam sem saltos visíveis (`font-display: swap` + fallback com métricas próximas).
- [ ] Modo escuro (se existir): contraste correto, sem texto escuro em fundo escuro, imagens/logos visíveis.
- [ ] Impressão (se relevante: faturas, receitas) — página imprimível sem menus.
- [ ] Sem saltos de layout ao carregar (imagens e anúncios com espaço reservado).
- [ ] Favicon e cor do tema (`theme-color`) definidos.

## 3. Imagens e media

- [ ] Formatos modernos: WebP ou AVIF para fotografias, SVG para ícones e logos, PNG só quando precisa de transparência sem perdas.
- [ ] Peso: fotografias normalmente < 200 KB; imagem principal (hero) < 300 KB; nada acima de 1 MB sem razão.
- [ ] Tamanho certo: a imagem não é muito maior do que o espaço onde aparece (usar `srcset`/`sizes` ou o componente de imagem do framework).
- [ ] `width` e `height` (ou `aspect-ratio`) definidos para não haver saltos de layout.
- [ ] `loading="lazy"` nas imagens abaixo da dobra; **não** na imagem principal (essa leva `fetchpriority="high"`).
- [ ] Sem imagens deformadas (proporção errada) — usar `object-fit: cover/contain`.
- [ ] Texto alternativo (`alt`) descritivo nas imagens com significado; `alt=""` nas decorativas.
- [ ] Imagens nítidas em ecrãs retina (2x) sem serem enormes.
- [ ] Vídeos: comprimidos, com `poster`, sem autoplay com som, `playsinline` no iOS, legendas se tiverem fala.
- [ ] Imagens de partilha (`og:image`, 1200×630) e ícones (favicon, `apple-touch-icon` 180×180, manifest) existem e estão certos.
- [ ] Sem metadados sensíveis nas fotografias (localização GPS em EXIF).
- [ ] Direitos: imagens com licença para uso (não tiradas do Google sem autorização).

## 4. Desempenho

- [ ] Core Web Vitals (dados reais ou Lighthouse, em telemóvel): **LCP < 2,5 s**, **INP < 200 ms**, **CLS < 0,1**.
- [ ] Pontuação Lighthouse de desempenho (telemóvel) ≥ 90 como objetivo; < 50 é problema importante.
- [ ] Peso total da página inicial razoável (objetivo < 1,5 MB; JS < 300 KB comprimido).
- [ ] Compressão gzip ou brotli ativa para HTML, CSS, JS, SVG.
- [ ] Cache: ficheiros com hash no nome com `Cache-Control: max-age=31536000, immutable`; HTML com cache curta ou revalidação.
- [ ] HTTP/2 ou HTTP/3; CDN para ficheiros estáticos se o público for internacional.
- [ ] Sem CSS/JS a bloquear a renderização sem necessidade (`defer`/`async`, CSS crítico).
- [ ] Fontes: poucas variantes, WOFF2, `preload` da principal, subset de caracteres se possível.
- [ ] Scripts de terceiros (chat, analytics, anúncios, pixels) contados e justificados — são a causa mais comum de lentidão.
- [ ] Sem bibliotecas enormes para tarefas pequenas (ex.: moment.js inteiro, jQuery só para um efeito).
- [ ] Tempo de resposta do servidor (TTFB) < 800 ms.
- [ ] Sem pedidos repetidos ou em cascata desnecessários.
- [ ] Animações usam `transform`/`opacity` e respeitam `prefers-reduced-motion`.

## 5. Segurança

**Transporte e cabeçalhos**
- [ ] HTTPS em todo o site, certificado válido, sem conteúdo misto (http dentro de https).
- [ ] `Strict-Transport-Security` (HSTS) com `max-age` ≥ 6 meses.
- [ ] `Content-Security-Policy` definida (pelo menos `default-src 'self'` adaptada; sem `unsafe-inline` em scripts se possível); `frame-ancestors` para impedir que o site seja metido num iframe alheio (ou `X-Frame-Options: DENY/SAMEORIGIN`).
- [ ] `X-Content-Type-Options: nosniff`.
- [ ] `Referrer-Policy: strict-origin-when-cross-origin` (ou mais restrita).
- [ ] `Permissions-Policy` a desligar o que não se usa (câmara, microfone, localização).
- [ ] O servidor não anuncia versões (`Server`, `X-Powered-By`).

**Segredos e ficheiros expostos**
- [ ] Nenhuma chave secreta, palavra-passe ou token no código do frontend nem no repositório (chaves "públicas" como as publishable keys do Stripe são aceitáveis; as secretas não).
- [ ] Ficheiros `.env`, `.git/`, backups (`.zip`, `.sql`, `.bak`), `phpinfo`, painéis de admin de desenvolvimento **não** acessíveis publicamente.
- [ ] Source maps de produção não expõem código sensível (ou desligados).
- [ ] `.gitignore` inclui `.env` e ficheiros com credenciais.

**Código e dados**
- [ ] Sem XSS: dados do utilizador nunca inseridos como HTML (`innerHTML`, `dangerouslySetInnerHTML`, `v-html`, `|safe`) sem sanitização.
- [ ] Sem injeção SQL/NoSQL: consultas parametrizadas, nunca texto concatenado.
- [ ] Validação de dados **no servidor**, não só no browser.
- [ ] Proteção CSRF em formulários que alteram dados (tokens ou cookies `SameSite`).
- [ ] Sem redirecionamentos abertos (`?next=https://site-malicioso`).
- [ ] Uploads: tipo e tamanho validados no servidor, ficheiros guardados fora da pasta executável, nomes gerados pelo servidor.
- [ ] Mensagens de erro de produção não mostram stack traces, consultas SQL ou caminhos do servidor.
- [ ] CORS restrito às origens necessárias (não `*` em APIs com dados privados ou com credenciais).
- [ ] Links externos com `target="_blank"` têm `rel="noopener"` (browsers modernos já o fazem, mas confirmar em sites antigos).
- [ ] Scripts de CDN externos com Subresource Integrity (`integrity=`) quando a versão é fixa.

**Contas e acesso** (se houver login)
- [ ] Palavras-passe guardadas com hash forte (bcrypt/argon2), nunca em texto.
- [ ] Limite de tentativas de login / rate limiting; proteção contra bots em formulários (honeypot, CAPTCHA acessível).
- [ ] Cookies de sessão com `Secure`, `HttpOnly`, `SameSite=Lax` ou `Strict`.
- [ ] Recuperação de palavra-passe com token de uso único e expiração.
- [ ] Cada pedido verifica se o utilizador tem permissão para **aquele** recurso (não basta esconder o botão).
- [ ] 2FA disponível para administradores.
- [ ] Regras de acesso das bases de dados de serviços (Firebase rules, Supabase RLS) ativas e restritivas.

**Dependências e plataforma**
- [ ] Sem vulnerabilidades conhecidas altas/críticas nas dependências (`npm audit`, etc.).
- [ ] CMS (WordPress, etc.), temas e plugins atualizados; plugins não usados removidos.
- [ ] Contas de admin com nomes não óbvios e palavras-passe fortes.
- [ ] Existe forma de reportar falhas (`/.well-known/security.txt` — opcional, boa prática).

## 6. Privacidade e RGPD

- [ ] Inventário de **tudo o que recolhe dados**: analytics, pixels (Meta, TikTok, Google Ads), chat, mapas, vídeos incorporados, fontes externas, formulários, newsletters.
- [ ] **Nenhum cookie ou rastreador não essencial é carregado antes do consentimento** (verificar na rede e nos cookies ao abrir o site pela primeira vez, sem aceitar nada).
- [ ] Banner de cookies com "Rejeitar" tão fácil como "Aceitar", sem caixas pré-marcadas, e forma de mudar de ideias depois.
- [ ] Política de privacidade acessível em todas as páginas, em linguagem clara: que dados, para quê, base legal, quanto tempo, com quem são partilhados, direitos do titular, contacto.
- [ ] Política de cookies (pode estar dentro da de privacidade) com a lista real de cookies.
- [ ] Formulários pedem só os dados necessários; consentimento explícito para newsletter/marketing (caixa não pré-marcada).
- [ ] Dados pessoais não vão em URLs (`?email=...`), nem em logs, nem para analytics.
- [ ] Vídeos do YouTube em modo `youtube-nocookie.com` ou carregados só após clique; mapas idem.
- [ ] Google Fonts servidas localmente (carregá-las do Google envia o IP dos visitantes — já deu multas na UE).
- [ ] Analytics: preferir soluções sem cookies/anónimas (ex.: Plausible, Matomo configurado) ou só após consentimento.
- [ ] Dados pessoais guardados no browser (`localStorage`) só se necessário e nunca sensíveis.
- [ ] Forma de pedir acesso/apagamento dos dados (email ou formulário) e de cancelar a newsletter.
- [ ] Transferências para fora da UE identificadas (serviços americanos) e mencionadas na política.
- [ ] Menores: se o público incluir crianças, regras de consentimento parental.
- [ ] Informação legal exigida no país (ex.: identificação da empresa, livro de reclamações eletrónico em Portugal para negócios, termos e condições em lojas).

## 7. Acessibilidade

Objetivo: WCAG 2.2 nível AA (exigido a muitos negócios na UE pela Lei Europeia da Acessibilidade, desde junho de 2025).

- [ ] Contraste de texto ≥ 4,5:1 (texto grande ≥ 3:1); ícones e bordas de campos ≥ 3:1.
- [ ] Tudo funciona só com teclado (Tab, Enter, Espaço, Esc), por ordem lógica, sem armadilhas.
- [ ] Foco sempre visível (nunca `outline: none` sem alternativa).
- [ ] Link "Saltar para o conteúdo" no topo.
- [ ] `<html lang="...">` correto.
- [ ] Um `<h1>` por página; cabeçalhos por ordem (h2, h3...) sem saltos usados só pelo tamanho.
- [ ] Campos de formulário com `<label>` associado; erros anunciados e explicados em texto (não só a vermelho).
- [ ] Botões são `<button>`, links são `<a href>` — não `<div onclick>`.
- [ ] Ícones-botão têm nome acessível (`aria-label`).
- [ ] Imagens com `alt` adequado (ver secção 3).
- [ ] Alvos de toque ≥ 24×24 px (ideal 44×44).
- [ ] Zoom até 200% e texto ampliado não partem o layout; não bloquear o zoom (`user-scalable=no` é erro).
- [ ] Informação não transmitida só por cor.
- [ ] Animações respeitam `prefers-reduced-motion`; nada pisca mais de 3 vezes por segundo.
- [ ] Vídeos com legendas; áudio com transcrição.
- [ ] Modais prendem o foco enquanto abertos e devolvem-no ao fechar; fecham com Esc.
- [ ] Conteúdo dinâmico importante anunciado (`aria-live`) — ex.: "adicionado ao carrinho".
- [ ] Declaração de acessibilidade publicada (obrigatória para entidades públicas; boa prática para todos).

## 8. SEO e partilha

- [ ] `<title>` único por página (≈ 50–60 caracteres) e `<meta name="description">` (≈ 120–160).
- [ ] Um `<h1>` claro por página com o tema principal.
- [ ] URLs legíveis e estáveis (`/servicos/limpeza`, não `/p?id=382`).
- [ ] `<link rel="canonical">` correto, sem duplicados (http/https, www, barra final, parâmetros).
- [ ] `robots.txt` existe e não bloqueia o site por engano (`Disallow: /` esquecido de desenvolvimento!); nenhuma página importante com `noindex`.
- [ ] `sitemap.xml` existe, está atualizado e referido no `robots.txt`.
- [ ] Dados estruturados (JSON-LD) adequados: `Organization`/`LocalBusiness`, `Product`, `Article`, `FAQ`, `Breadcrumb` — válidos.
- [ ] Open Graph e Twitter Cards (`og:title`, `og:description`, `og:image`, `og:url`) para boas pré-visualizações no WhatsApp, Facebook, LinkedIn.
- [ ] Sites multilíngua com `hreflang` e `lang` corretos.
- [ ] Conteúdo importante presente no HTML (não só gerado no browser) ou renderizado no servidor.
- [ ] Links internos entre páginas relacionadas; texto dos links descritivo (não "clique aqui").
- [ ] Negócio local: perfil do Google Business coerente com nome, morada e telefone do site.
- [ ] Site registado no Google Search Console (e Bing Webmaster) — verificar erros de indexação lá.

## 9. Conteúdo

- [ ] Sem gralhas e erros ortográficos nos títulos e botões principais.
- [ ] Sem texto de exemplo esquecido (*Lorem ipsum*, "Título aqui", "Produto 1", imagens de stock com marca de água).
- [ ] Ano do copyright, preços, horários, contactos e morada atualizados.
- [ ] Contactos funcionam (`tel:`, `mailto:`, WhatsApp, mapas).
- [ ] Proposta de valor clara no topo da página inicial: o que é, para quem, o que fazer a seguir (botão principal visível).
- [ ] Tom consistente; traduções completas (sem mistura de línguas).
- [ ] Links para redes sociais certos e ativos.

## 10. Compatibilidade

- [ ] Últimas versões de Chrome, Safari (macOS e **iOS** — é onde aparecem mais diferenças), Firefox, Edge, Samsung Internet.
- [ ] Funcionalidades CSS/JS recentes com alternativa ou verificadas em caniuse.com para o público-alvo.
- [ ] iOS: `100vh`, campos com zoom automático (< 16 px), `position: fixed` com teclado, vídeos `playsinline`, datas `new Date("2025-01-01 10:00")` (formato que o Safari rejeita).
- [ ] Ecrãs muito grandes (≥ 2560 px): conteúdo com largura máxima, não esticado.
- [ ] Ligações lentas (3G simulado): o site é utilizável, mostra estados de carregamento.
- [ ] Sem funcionalidades só para rato (hover sem equivalente em toque).

## 11. Domínio, alojamento e email

- [ ] Certificado SSL válido, renovação automática, não expira nos próximos 30 dias.
- [ ] Domínio com renovação automática e dados de contacto do registo atualizados.
- [ ] DNS: registos A/AAAA/CNAME corretos, sem registos antigos a apontar para serviços desativados (risco de *subdomain takeover*).
- [ ] Email do domínio com **SPF**, **DKIM** e **DMARC** configurados (senão os emails do site e do formulário vão para spam e o domínio pode ser falsificado).
- [ ] Emails do formulário de contacto chegam (testar) e não usam um endereço "from" que falhe o SPF.
- [ ] Cópias de segurança automáticas do site e da base de dados, guardadas noutro sítio, e **testadas** (restauro).
- [ ] Monitorização de disponibilidade (ex.: UptimeRobot) e alertas.
- [ ] Ambiente de testes separado da produção; nada de testar diretamente no site público.

## 12. Qualidade do código

- [ ] Build sem erros nem avisos importantes; linter (ESLint, Stylelint) sem erros.
- [ ] Sem `console.log`, `debugger`, código comentado e ficheiros não usados em produção.
- [ ] Dependências atualizadas (pelo menos sem versões abandonadas ou com falhas conhecidas); sem dependências duplicadas ou não usadas.
- [ ] Erros tratados (pedidos de rede com `try/catch`, estados de erro na interface), não engolidos em silêncio.
- [ ] Configuração por variáveis de ambiente, não valores fixos espalhados pelo código.
- [ ] HTML válido (atributos duplicados, tags mal fechadas, IDs repetidos).
- [ ] CSS sem `!important` em excesso nem regras mortas; componentes reutilizados em vez de copiados.
- [ ] Testes para as funcionalidades críticas (checkout, login, formulários), se o projeto tiver testes.
- [ ] README com como correr e publicar o projeto.
