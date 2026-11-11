# Como verificar — ferramentas e comandos

Formas concretas de verificar cada área do `checklist.md`. Usa o que estiver disponível no ambiente: browser (ferramentas de browser do Claude), terminal, ou só o código. Se uma ferramenta não existir, usa a alternativa ou diz ao utilizador como verificar ele próprio.

Troca `SITE` pelo domínio (ex.: `exemplo.pt`) e `URL` pelo endereço completo (ex.: `https://exemplo.pt`). **Só em sites do utilizador.** Todos os comandos abaixo são leituras passivas.

## Índice

- [Com um browser](#com-um-browser)
- [Cabeçalhos, HTTPS e redirecionamentos](#cabeçalhos-https-e-redirecionamentos)
- [Ficheiros expostos](#ficheiros-expostos)
- [Velocidade, acessibilidade e SEO (Lighthouse)](#velocidade-acessibilidade-e-seo-lighthouse)
- [Links partidos](#links-partidos)
- [HTML válido e dados estruturados](#html-válido-e-dados-estruturados)
- [Segredos no código](#segredos-no-código)
- [Dependências](#dependências)
- [Imagens no projeto](#imagens-no-projeto)
- [DNS e email](#dns-e-email)
- [Privacidade e cookies](#privacidade-e-cookies)
- [Plataformas específicas](#plataformas-específicas)

---

## Com um browser

Se tiveres ferramentas de browser (navegar, capturas, consola, rede, executar JavaScript):

1. Abre o site em **375×812** (telemóvel) e **1440×900** (desktop); se possível também em modo escuro. Tira capturas da página inicial e das páginas principais.
2. Lê a **consola** (erros) e os **pedidos de rede** (falhas 4xx/5xx, ficheiros pesados, domínios de terceiros).
3. Corre estes testes rápidos na consola da página:

```js
// Elementos que causam scroll horizontal
[...document.querySelectorAll('*')]
  .filter(e => e.getBoundingClientRect().right > document.documentElement.clientWidth + 1)
  .map(e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : ''))
  .slice(0, 20)
```

```js
// Imagens sem alt, e imagens muito maiores do que o espaço onde aparecem
({
  semAlt: [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.currentSrc).slice(0, 20),
  grandesDemais: [...document.images]
    .filter(i => i.clientWidth > 0 && i.naturalWidth > i.clientWidth * 2.5)
    .map(i => ({ src: i.currentSrc, real: i.naturalWidth, mostrada: i.clientWidth }))
    .slice(0, 20)
})
```

```js
// Estrutura de cabeçalhos, título, descrição, idioma, canonical
({
  lang: document.documentElement.lang,
  title: document.title,
  description: document.querySelector('meta[name=description]')?.content,
  canonical: document.querySelector('link[rel=canonical]')?.href,
  h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim()),
  cabecalhos: [...document.querySelectorAll('h1,h2,h3,h4')].map(h => h.tagName + ' ' + h.textContent.trim().slice(0, 50)).slice(0, 30)
})
```

```js
// Cookies e armazenamento logo na primeira visita (antes de aceitar cookies)
({ cookies: document.cookie, localStorage: Object.keys(localStorage) })
```

4. Testa com o teclado: carrega em Tab várias vezes e confirma que o foco é visível e segue uma ordem lógica.

## Cabeçalhos, HTTPS e redirecionamentos

```bash
curl -sI URL
```
Mostra os cabeçalhos da página. Procura: `strict-transport-security`, `content-security-policy`, `x-content-type-options`, `referrer-policy`, `permissions-policy`, `x-frame-options`, `cache-control`, `content-encoding` (com `-H 'Accept-Encoding: br, gzip'`), e se `server`/`x-powered-by` revelam versões.

```bash
curl -sIL http://SITE -o /dev/null -w '%{url_effective} %{http_code} (%{num_redirects} redirecionamentos)\n'
```
Segue os redirecionamentos a partir de http e sem https: deve acabar no endereço final com 1 salto (2 no máximo).

```bash
echo | openssl s_client -servername SITE -connect SITE:443 2>/dev/null | openssl x509 -noout -issuer -dates
```
Mostra quem emitiu o certificado e quando expira (`notAfter`).

```bash
curl -s -o /dev/null -w '%{http_code}\n' URL/pagina-que-nao-existe-123
```
Deve devolver `404` (se devolver `200`, a página de erro está mal configurada).

## Ficheiros expostos

```bash
for p in .env .git/HEAD .git/config backup.zip backup.sql db.sql .DS_Store phpinfo.php wp-config.php.bak server-status .well-known/security.txt robots.txt sitemap.xml; do
  printf '%-28s %s\n' "$p" "$(curl -s -o /dev/null -w '%{http_code}' URL/$p)"
done
```
`robots.txt`, `sitemap.xml` e `security.txt` devem dar `200`. Todos os outros devem dar `403` ou `404` — um `200` em `.env`, `.git` ou backups é **crítico** (confirma o conteúdo antes de reportar: alguns sites devolvem 200 com a página inicial para qualquer endereço).

## Velocidade, acessibilidade e SEO (Lighthouse)

Se houver Chrome e Node no computador:

```bash
npx lighthouse URL --form-factor=mobile --screenEmulation.mobile --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=./lighthouse.json --chrome-flags="--headless"
```

Sem Chrome local, usa a API pública do PageSpeed Insights (dados de laboratório e, quando há tráfego suficiente, dados reais de utilizadores):

```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&strategy=mobile&category=performance&category=accessibility&category=best-practices&category=seo" -o psi.json
```

No JSON: `lighthouseResult.categories.*.score` (0–1), `lighthouseResult.audits` (cada problema, com `score` < 1 a indicar falha) e `loadingExperience.metrics` (LCP, INP, CLS reais).

Acessibilidade mais detalhada (se disponível): `npx pa11y URL`.

## Links partidos

```bash
npx linkinator URL --recurse --skip "^(?!URL)" --verbosity error
```
Percorre o site e lista links que falham (o `--skip` evita seguir links externos; remove-o para verificar também esses).

## HTML válido e dados estruturados

```bash
curl -s "https://validator.w3.org/nu/?doc=URL&out=json" | python3 -c "import json,sys; [print(m['type'], m.get('lastLine'), m['message']) for m in json.load(sys.stdin)['messages'][:30]]"
```
Validador oficial do W3C. Para dados estruturados, o utilizador pode usar o *Rich Results Test* do Google ou validator.schema.org com o URL.

## Segredos no código

No repositório do projeto:

```bash
git grep -nIE '(sk_live_[0-9a-zA-Z]{10,}|rk_live_|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|ghp_[0-9A-Za-z]{36}|github_pat_|xox[baprs]-|-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY|service_role|SUPABASE_SERVICE|password\s*[:=]\s*["'\''][^"'\'']{4,})'
```

No histórico (um segredo apagado continua no histórico):

```bash
git log -p --all | grep -nE 'sk_live_|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|ghp_|PRIVATE KEY|service_role' | head -20
```

Confirma também se `.env*` está no `.gitignore` e se não foi enviado antes: `git log --all --oneline -- .env`. Se existir `gitleaks` ou `trufflehog`, usa-os. No site publicado, procura chaves nos ficheiros JS (separador Rede do browser, ou `curl` dos bundles).

Quando encontrares um segredo real: **não o repitas na resposta** — diz onde está e que deve ser revogado e substituído.

## Dependências

```bash
npm audit --omit=dev       # ou: pnpm audit / yarn npm audit
npm outdated
```
Python: `pip-audit`. PHP: `composer audit`. Ruby: `bundle audit`. Reporta só vulnerabilidades altas/críticas como 🔴/🟠; as restantes como 🟡.

## Imagens no projeto

```bash
find . -path ./node_modules -prune -o -type f \( -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.png' -o -iname '*.gif' -o -iname '*.webp' \) -size +300k -exec ls -lh {} \; | awk '{print $5, $NF}' | sort -hr | head -20
```
Lista as imagens com mais de 300 KB. Dimensões no macOS: `sips -g pixelWidth -g pixelHeight FICHEIRO`. Conversão para WebP (se instalado): `cwebp -q 80 entrada.jpg -o saida.webp`.

Metadados de localização em fotos (se `exiftool` existir): `exiftool -gps:all -r pasta/`.

## DNS e email

```bash
dig +short A SITE; dig +short AAAA SITE; dig +short CNAME www.SITE
dig +short MX SITE
dig +short TXT SITE | grep -i spf          # SPF
dig +short TXT _dmarc.SITE                 # DMARC (deve existir, com p=quarantine ou p=reject como objetivo)
dig +short TXT google._domainkey.SITE      # DKIM — o nome antes de ._domainkey depende do serviço de email (google, selector1, k1, default...)
```

## Privacidade e cookies

1. Abre o site numa sessão limpa (sem cookies) e **não aceites nada**.
2. No separador Rede, procura pedidos a: `google-analytics.com`, `googletagmanager.com`, `doubleclick.net`, `facebook.net`/`connect.facebook`, `tiktok.com`, `hotjar.com`, `clarity.ms`, `fonts.googleapis.com`, `youtube.com` (não `youtube-nocookie.com`), `maps.googleapis.com`.
3. Corre o teste de cookies da secção do browser.

Qualquer rastreador carregado antes do consentimento é 🔴 (RGPD/ePrivacy). No código, procura onde estes scripts são incluídos e se dependem do consentimento.

## Plataformas específicas

- **Next.js / Vite / React**: `npm run build` — ver avisos e tamanho dos bundles; `next build` mostra o peso de cada página. Procurar `dangerouslySetInnerHTML` e variáveis `NEXT_PUBLIC_*`/`VITE_*` com segredos (são públicas!).
- **WordPress**: com WP-CLI, `wp core version`, `wp plugin list --update=available`, `wp theme list --update=available`; verificar `/wp-json/wp/v2/users` (não deve listar utilizadores) e `xmlrpc.php` (desativar se não usado).
- **Sites estáticos / GitHub Pages / Netlify / Vercel**: cabeçalhos de segurança configuram-se em `_headers`, `netlify.toml`, `vercel.json` ou no CDN.
- **Firebase / Supabase**: rever as regras de segurança (`firestore.rules`, políticas RLS) — uma base de dados aberta é 🔴.
- **Shopify / Wix / Squarespace**: o código do servidor não é acessível; foca em conteúdo, imagens, apps/scripts instalados, SEO, acessibilidade, velocidade e cookies.
