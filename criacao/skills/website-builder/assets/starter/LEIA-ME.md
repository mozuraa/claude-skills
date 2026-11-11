# Site-base · Starter site

Site estático pronto a adaptar, da skill [website-builder](https://github.com/mozuraa/claude-skill-website-builder). *A static starter site from the website-builder skill.*

**Personalizar · Customize:** procura `TODO:` e os textos `[entre parênteses retos]` em todos os ficheiros. No fim não pode ficar nenhum. *Search for `TODO:` and `[bracketed text]`; none may remain.*

| Ficheiro | Para quê |
|---|---|
| `index.html` | Página inicial (topo, serviços, como funciona, testemunho, sobre, perguntas, contactos) |
| `css/styles.css` | Estilos com *design tokens* no `:root`: muda as cores e fontes da marca aí |
| `js/main.js` | Menu móvel acessível e ano automático no rodapé (~1 KB) |
| `404.html` | Página de erro |
| `privacidade.html` | Modelo de política de privacidade (rever para o caso concreto) |
| `robots.txt`, `sitemap.xml` | Motores de busca (trocar `exemplo.pt` pelo domínio) |
| `site.webmanifest`, `favicon.svg` | Ícones (acrescentar `apple-touch-icon.png` 180×180, `icon-512.png` e `og.jpg` 1200×630) |
| `_headers` | Cabeçalhos de segurança e cache para Netlify / Cloudflare Pages |
| `vercel.json` | O mesmo para a Vercel |

**Ver localmente · Preview locally:**

```bash
python3 -m http.server 8000
```

Depois abre http://localhost:8000. Os caminhos começam por `/`, por isso abrir o ficheiro diretamente (`file://`) não carrega os estilos. *Paths start with `/`, so use a local server rather than opening the file directly.*

**Formulário · Form:** troca o `action` pelo teu serviço (Formspree, Netlify Forms...). Se o domínio mudar, atualiza `form-action` no `_headers` e no `vercel.json`.
