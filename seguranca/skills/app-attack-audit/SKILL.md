---
name: app-attack-audit
description: Auditoria defensiva da tua própria app contra 20 classes de ataque reais e públicas (nível pen-test) — HTTP/2 Rapid Reset, bypass de login com username de 52 caracteres (Okta/bcrypt), SAML bypass (GitLab), nOAuth email spoof, GraphQL aliases, replay de códigos 2FA, ReDoS, JWT alg confusion, request smuggling, cache poisoning, IP spoofing via cabeçalhos, views que contornam RLS, tokens com Math.random, timing attacks, padding oracle, prototype pollution, template injection, XXE, WebSocket hijacking e Unicode account takeover (Spotify). Para cada uma explica o que é, como saber se te afeta, a correção e o que procurar no código. Usa sempre que o utilizador pedir para rever a segurança da sua app, "a minha app é segura?", "audita o meu código", "fiz isto com vibe coding, pode ser hackeado?", antes de lançar em produção, ou ao implementar login, OAuth, SSO/SAML, JWT, 2FA, GraphQL, uploads de XML, WebSockets, caching, rate limiting ou Supabase/Postgres RLS.
---

# App Attack Audit

Skill extraída do reel **"20 (pen-test level) ways a stranger hacks your vibecoded app"** de [@murphmaxxing](https://www.instagram.com/reel/DfsWbkrB6vN/) (nov. 2026). O autor sublinha que os 20 casos são **públicos e já foram corrigidos** nas empresas afetadas (Google Cloud, Okta, GitLab, Spotify…). O guia completo que ele envia por DM não faz parte do post.

> A lista dos 20 ataques é a do reel. As explicações, verificações e correções foram escritas a partir de fontes públicas (CVEs, relatórios das empresas, OWASP).

**Âmbito: só código e sistemas do próprio utilizador.** Esta skill serve para encontrar e corrigir falhas na app de quem pede — não para atacar sistemas de terceiros. Não escrevas exploits funcionais contra alvos reais; descreve o padrão vulnerável e a correção.

Responde na língua do utilizador.

## Como fazer a auditoria

1. **Mapeia a stack:** framework, servidor/proxy/CDN, autenticação (sessões, JWT, OAuth/SSO, SAML), base de dados (RLS?), GraphQL, WebSockets, parsing de XML, templates.
2. **Marca cada um dos 20 como:** ✅ não aplicável · 🔎 aplicável, verificado e seguro · ⚠️ vulnerável · ❓ não dá para confirmar só com o código.
3. Para cada ⚠️: ficheiro:linha, porque é explorável, correção concreta (diff), severidade (crítica/alta/média/baixa).
4. Termina com as **3 correções mais urgentes** e o que precisa de teste manual/infra.

## Os 20 ataques

### 1. HTTP/2 Rapid Reset (CVE-2023-44487)
- **Caso público:** em out. 2023 a Google Cloud travou um DDoS de **398 milhões de pedidos/s** que abria e cancelava streams HTTP/2 em ciclo.
- **Afeta-te se:** gere o teu próprio servidor/proxy HTTP/2 (nginx, Envoy, Node `http2`, Go `net/http`, HAProxy) sem patches.
- **Correção:** atualiza servidor/proxy; limita streams concorrentes e resets por ligação; põe um CDN/WAF (Cloudflare, Cloud Armor) à frente.

### 2. Username de 52 caracteres (Okta, 2024)
- **Caso público:** a chave de cache de login era um hash **bcrypt de userId + username + password**; o bcrypt ignora tudo depois de 72 bytes, por isso com username ≥52 caracteres a password deixava de contar e um login em cache passava sem a password certa.
- **Afeta-te se:** usas bcrypt sobre strings concatenadas, ou fazes hash de inputs que podem passar 72 bytes.
- **Correção:** bcrypt só para a password (e limita o tamanho); para chaves de cache usa HMAC-SHA256 ou Argon2id; nunca concatenes campos controlados pelo utilizador antes de truncar.

### 3. SAML bypass (GitLab / ruby-saml, CVE-2024-45409 e CVE-2025-25291/25292)
- **Caso público:** falhas na verificação da assinatura XML permitiam forjar uma resposta SAML e entrar como qualquer utilizador.
- **Afeta-te se:** implementas SSO SAML ou usas bibliotecas SAML desatualizadas.
- **Correção:** atualiza a biblioteca; valida a assinatura da asserção **e** que o elemento assinado é o que usas; rejeita respostas não assinadas; testa com respostas adulteradas.

### 4. nOAuth — email spoof em OAuth (Microsoft Entra, 2023)
- **Caso público:** apps que identificavam o utilizador pelo claim `email` do Entra ID — um campo editável e não verificado — permitiam account takeover.
- **Afeta-te se:** fazes "Sign in with X" e ligas contas pelo email.
- **Correção:** identifica pelo par `iss` + `sub` (ou `oid`), nunca pelo email; só confias no email se `email_verified` for true e o fornecedor o garantir.

### 5. GraphQL aliases (batching brute force)
- **Padrão:** num único pedido HTTP, centenas de aliases (`a1: login(...)`, `a2: login(...)`) contornam o rate limit por pedido — força bruta de passwords ou códigos OTP.
- **Correção:** rate limit por operação/resolver (não por pedido), limite de aliases e de custo/complexidade da query, desativa batching onde não é preciso, e a introspeção em produção.

### 6. Replay de código 2FA
- **Padrão:** o código TOTP/SMS continua válido depois de usado ou durante a janela inteira; pode ser reutilizado ou tentado sem limite.
- **Correção:** marca o código como usado (guarda o último *time-step* aceite), expira rápido, limita tentativas (ex.: 5) e bloqueia temporariamente, liga o código à sessão/utilizador.

### 7. ReDoS (Regular expression DoS)
- **Caso público:** a indisponibilidade global da Cloudflare em jul. 2019 foi causada por uma regex com backtracking catastrófico.
- **Afeta-te se:** tens regex com quantificadores aninhados (`(a+)+`, `(.*)*`, `(\w+\s?)*$`) aplicadas a input do utilizador.
- **Correção:** simplifica as regex, limita o tamanho do input, usa motores lineares (RE2, `re2` no Node, Rust `regex`), ou define timeouts; deteta com `safe-regex`/`recheck`.

### 8. JWT alg confusion
- **Padrão:** o servidor aceita `alg: none`, ou aceita HS256 usando a **chave pública** RSA como segredo HMAC.
- **Correção:** fixa o algoritmo esperado na verificação (`algorithms: ['RS256']`), rejeita `none`, usa bibliotecas atuais, valida `exp`, `iss`, `aud`.

### 9. HTTP request smuggling
- **Padrão:** proxy e servidor discordam onde acaba um pedido (`Content-Length` vs `Transfer-Encoding`), permitindo injetar pedidos escondidos.
- **Correção:** atualiza proxy/servidor; rejeita pedidos com CL e TE em simultâneo ou ambíguos; usa HTTP/2 de ponta a ponta onde possível; normaliza no edge.

### 10. Web cache poisoning
- **Padrão:** a resposta depende de um cabeçalho **não incluído na chave de cache** (ex.: `X-Forwarded-Host`), e um atacante envenena a cache para todos os utilizadores; ou *cache deception* guarda páginas privadas como estáticas.
- **Correção:** não uses cabeçalhos não-keyed para gerar URLs/conteúdo; `Cache-Control: private, no-store` em páginas autenticadas; regras de cache só para caminhos estáticos explícitos.

### 11. Spoofed IP header
- **Padrão:** rate limiting, allowlists ou logs confiam em `X-Forwarded-For`/`X-Real-IP` enviados pelo cliente.
- **Correção:** só confias no cabeçalho definido pelo teu proxy conhecido (configura `trust proxy` com o número certo de saltos), ou usa o IP do socket; em Cloudflare usa `CF-Connecting-IP` só se o tráfego vier forçosamente pela Cloudflare.

### 12. Views que contornam RLS (Postgres / Supabase)
- **Padrão:** uma `VIEW` corre com as permissões do **dono** (normalmente `postgres`), por isso ignora as políticas RLS das tabelas e expõe dados de todos pela API.
- **Correção:** `CREATE VIEW ... WITH (security_invoker = true)` (Postgres 15+), ou revoga acesso de `anon`/`authenticated` à view; corre o Security Advisor do Supabase; o mesmo cuidado com funções `SECURITY DEFINER`.

### 13. Tokens com `Math.random()`
- **Padrão:** tokens de reset de password, convites, IDs de sessão ou códigos gerados com `Math.random()` (ou `random` do Python) são previsíveis.
- **Correção:** `crypto.randomUUID()` / `crypto.getRandomValues()` / `crypto.randomBytes(32)` no Node, `secrets` no Python, `SecRandomCopyBytes` no iOS.

### 14. Timing attack
- **Padrão:** comparar segredos (tokens, assinaturas HMAC, API keys) com `===` deixa medir quantos caracteres batem certo pelo tempo de resposta.
- **Correção:** comparação em tempo constante — `crypto.timingSafeEqual`, `hmac.compare_digest`; e respostas iguais para "utilizador não existe" e "password errada".

### 15. Padding oracle
- **Padrão:** dados cifrados em AES-CBC sem autenticação, e o servidor responde de forma diferente a padding inválido → o atacante decifra os dados byte a byte (caso clássico: ASP.NET, 2010).
- **Correção:** usa cifra autenticada (AES-GCM, ChaCha20-Poly1305) ou bibliotecas de alto nível (libsodium, `Fernet`); nunca reveles erros de padding.

### 16. Prototype pollution (JavaScript)
- **Padrão:** merge/clone recursivo de JSON do utilizador aceita `__proto__`/`constructor.prototype` e altera todos os objetos da app (bypass de verificações, até RCE).
- **Correção:** bloqueia essas chaves, usa `Object.create(null)` ou `Map`, valida input com schema (Zod), atualiza `lodash` e afins; `node --disable-proto=throw`.

### 17. Server-side template injection (SSTI)
- **Padrão:** input do utilizador é passado como **template** (Jinja2, Handlebars, EJS, Twig) em vez de como dado → execução de código no servidor.
- **Correção:** nunca compiles templates a partir de input; passa input só como variáveis; usa sandbox/logic-less templates; o mesmo vale para prompts que geram templates.

### 18. XXE — XML External Entity
- **Padrão:** o parser XML resolve entidades externas e lê ficheiros do servidor (`file:///etc/passwd`) ou faz pedidos internos (SSRF). Afeta uploads de SVG, DOCX/XLSX, SAML, feeds.
- **Correção:** desativa DTDs e entidades externas no parser; usa `defusedxml` (Python); prefere JSON.

### 19. Cross-Site WebSocket Hijacking (CSWSH)
- **Padrão:** o handshake WebSocket autentica só com cookies e não verifica o `Origin` → um site malicioso abre a ligação com a sessão da vítima.
- **Correção:** valida o cabeçalho `Origin` contra uma allowlist; autentica com token no handshake; `SameSite=Lax/Strict` nos cookies.

### 20. Unicode account takeover (Spotify, 2013)
- **Caso público:** usernames com caracteres Unicode "parecidos" (ex.: `ᴮᴵᴳᴮᴵᴿᴰ`) eram normalizados de forma inconsistente no registo e no reset de password, permitindo tomar contas alheias.
- **Correção:** normaliza **uma vez e sempre igual** (NFKC + case folding) no registo, login e reset; guarda a forma canónica e impõe unicidade sobre ela; considera restringir usernames a um conjunto de caracteres seguro.

## Prompt de auditoria (para Claude Code, no repositório do próprio utilizador)

```
Audita este repositório (que é meu) contra estas 20 classes de vulnerabilidade:
HTTP/2 Rapid Reset, bcrypt com input >72 bytes, SAML signature bypass, OAuth a ligar contas por email (nOAuth),
GraphQL alias batching, replay/brute force de 2FA, ReDoS, JWT alg confusion, request smuggling, cache poisoning,
confiança em X-Forwarded-For, views/SECURITY DEFINER a contornar RLS, Math.random em tokens, comparação de segredos
sem tempo constante, CBC sem autenticação, prototype pollution, template injection, XXE, WebSocket sem verificação de
Origin, normalização Unicode inconsistente de usernames.
Para cada uma: não aplicável / seguro / vulnerável / precisa de teste manual, com ficheiro:linha e evidência.
Para cada vulnerável: severidade, porque é explorável e o diff da correção. Não alteres código sem eu aprovar.
Termina com as 3 correções mais urgentes.
```

Para uma auditoria mais profunda e geral, ver a skill `security-audit` da Cloudflare em `claude-skills-catalog`.
