# Qualidade — verificação antes de publicar

Percorre esta lista na fase 6. Para cada ponto, **verifica de verdade** (captura, medição, teste) — não marques de memória. Mostra ao utilizador um resumo: o que passou, o que corrigiste, o que fica pendente e porquê. Para um exame mais profundo, usa o modo **Diagnosticar** desta skill: `references/diagnostico/checklist.md` (150+ verificações) e `references/diagnostico/como-verificar.md` (os comandos para cada uma).

## Orçamento de desempenho (objetivos)

| Métrica (telemóvel) | Objetivo |
|---|---|
| Lighthouse — Desempenho, Acessibilidade, Boas práticas, SEO | ≥ 90 cada |
| LCP (maior elemento visível) | < 2,5 s |
| CLS (saltos de layout) | < 0,1 |
| INP (resposta a toques) | < 200 ms |
| Peso da página inicial | < 1 MB (ideal < 500 KB) |
| JavaScript | < 100 KB num site de apresentação |
| Pedidos a outros domínios | 0 por defeito |

## Lista

**Layout e aspeto**
- [ ] Capturas de todas as páginas em 375, 768 e 1440 px (e 320 px na página inicial).
- [ ] Sem scroll horizontal em nenhuma largura; nada sobreposto ou cortado.
- [ ] Alinhamentos e espaçamentos consistentes; títulos sem palavras soltas na última linha.
- [ ] Modo escuro (se existir) verificado em todas as páginas.
- [ ] Favicon visível no separador; ícone ao adicionar ao ecrã inicial do telemóvel.

**Funcionamento**
- [ ] Consola sem erros em todas as páginas.
- [ ] Todos os links internos e externos funcionam; `tel:`, `mailto:` e WhatsApp abrem corretamente.
- [ ] Formulário: enviado de verdade, mensagem recebida, confirmação visível, erros compreensíveis, spam bloqueado (honeypot).
- [ ] Menu móvel abre, fecha (incluindo com Esc) e funciona com teclado.
- [ ] Página 404 aparece num endereço inexistente (no alojamento, com código 404).

**Conteúdo**
- [ ] Nenhum *Lorem ipsum*, `TODO`, `[NOME]`, texto de exemplo ou imagem provisória.
- [ ] Todos os rascunhos escritos pelo Claude foram confirmados pelo utilizador.
- [ ] Contactos, horários, preços e morada confirmados pelo utilizador.
- [ ] Ortografia revista; língua consistente.
- [ ] Ano do © atualizado (de preferência automático).

**Imagens**
- [ ] Todas em WebP/AVIF (ou SVG), redimensionadas, com `width`/`height` e `alt` adequado.
- [ ] Imagem do topo sem *lazy loading* e com `fetchpriority="high"`; as restantes com `loading="lazy"`.
- [ ] Nenhuma imagem acima de ~300 KB sem razão; sem metadados GPS.
- [ ] Imagem de partilha (1200×630) testada (ex.: colar o link numa conversa).

**Acessibilidade**
- [ ] Contraste ≥ 4,5:1 em todo o texto (incluindo botões, rodapé, texto sobre imagens).
- [ ] Navegação completa só com teclado; foco sempre visível; link "Saltar para o conteúdo".
- [ ] Um `h1` por página; cabeçalhos por ordem; `lang` correto.
- [ ] Campos com etiqueta; botões e ícones com nome acessível.
- [ ] Zoom a 200% sem perder conteúdo; `prefers-reduced-motion` respeitado.

**SEO e partilha**
- [ ] Título e descrição únicos em todas as páginas; canonical correto.
- [ ] `sitemap.xml` com todas as páginas públicas e o domínio final; `robots.txt` aponta para o sitemap e **não bloqueia** o site.
- [ ] Dados estruturados válidos (Rich Results Test).
- [ ] Open Graph em todas as páginas.
- [ ] Páginas privadas (ex.: obrigado, casamento) com `noindex` se for o caso.

**Segurança**
- [ ] Cabeçalhos de segurança configurados no alojamento (o site-base traz `_headers` e `vercel.json`): CSP, HSTS, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`, `frame-ancestors`.
- [ ] Nenhuma chave secreta no código público nem no repositório; `.env` no `.gitignore`.
- [ ] Links externos com `rel="noopener"` quando abrem noutra janela.
- [ ] Formulários validados também no servidor/serviço.

**Privacidade**
- [ ] Ao abrir o site sem aceitar nada, **zero** pedidos a rastreadores (ver a rede no browser).
- [ ] Fontes alojadas no próprio site; vídeos e mapas só carregam ao clicar.
- [ ] Política de privacidade completa e coerente com os serviços realmente usados; link no rodapé e junto aos formulários.
- [ ] Banner de cookies só se houver cookies não essenciais — e então a funcionar de verdade.
- [ ] Páginas legais obrigatórias para o tipo de negócio (ver `paginas.md`).

**Depois de publicar (repetir no endereço final)**
- [ ] HTTPS ativo; `http://` e `www` redirecionam para o endereço final.
- [ ] Cabeçalhos de segurança presentes (`curl -sI https://dominio`).
- [ ] Lighthouse/PageSpeed no endereço final.
- [ ] Formulário testado no site publicado.
- [ ] Sitemap submetido no Google Search Console.
