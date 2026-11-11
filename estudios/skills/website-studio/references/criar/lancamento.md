# Lançamento, domínio, email e manutenção

Explica cada passo em linguagem simples. Quando um passo exige uma conta, um pagamento ou uma confirmação do utilizador, **para e diz-lhe exatamente o que fazer** — nunca cries contas, faças compras ou introduzas palavras-passe por ele.

## Índice

- [1. Pôr o código num repositório](#1-pôr-o-código-num-repositório)
- [2. Publicar](#2-publicar)
- [3. Ligar o domínio](#3-ligar-o-domínio)
- [4. Email no domínio](#4-email-no-domínio)
- [5. Google e outros motores](#5-google-e-outros-motores)
- [6. Verificação final no endereço real](#6-verificação-final-no-endereço-real)
- [7. Entrega: guia de manutenção](#7-entrega-guia-de-manutenção)

---

## 1. Pôr o código num repositório

- Um repositório Git (GitHub, GitLab) guarda o histórico e permite publicar automaticamente a cada alteração.
- `.gitignore` com `node_modules/`, `.env*`, `dist/`, `.DS_Store`.
- Repositório **privado** se o código tiver algo que não deva ser público; o site publicado é sempre público.

## 2. Publicar

**GitHub Pages** (sites estáticos simples, grátis)
1. Repositório no GitHub com os ficheiros do site na raiz (ou numa pasta `docs/`).
2. Settings → Pages → *Deploy from a branch* → `main` / raiz → Save.
3. O site fica em `https://UTILIZADOR.github.io/REPOSITORIO/` em 1–2 minutos.
4. Limitação: não permite cabeçalhos HTTP personalizados (CSP/HSTS próprios) nem formulários — usa um serviço de formulários externo.

**Netlify** (estáticos com formulários e cabeçalhos)
1. Criar conta (o utilizador) → *Add new site* → *Import from Git* → escolher o repositório.
2. Build: vazio para HTML puro (pasta de publicação `.`), ou `npm run build` / `dist` para Astro.
3. O `_headers` do site-base é aplicado automaticamente. Netlify Forms: atributo `data-netlify="true"` no `<form>`.

**Cloudflare Pages**
1. *Workers & Pages* → *Create* → *Pages* → ligar o repositório.
2. Mesmas opções de build; o `_headers` também é lido.

**Vercel**
1. *Add New Project* → importar o repositório; deteta Astro/Next automaticamente.
2. Cabeçalhos no `vercel.json` (o site-base traz um).
3. Confirmar com o utilizador se o plano gratuito serve para uso comercial (os termos mudam — verificar).

Depois de ligar o repositório, **cada `git push` publica o site automaticamente**. Explica isto ao utilizador.

## 3. Ligar o domínio

1. Se não tem domínio: sugerir comprar num registador conhecido (o utilizador compra — tu não). Ativar renovação automática e privacidade WHOIS.
2. No alojamento: *Add custom domain* → `dominio.pt` e `www.dominio.pt`.
3. No painel DNS do registador, criar os registos que o alojamento indicar (normalmente `A`/`ALIAS` para o domínio raiz e `CNAME` para `www`). Mostra ao utilizador uma tabela exata: tipo, nome, valor.
4. Esperar a propagação (minutos a algumas horas); o HTTPS é emitido automaticamente.
5. Escolher o endereço final (com ou sem `www`) e confirmar que o outro redireciona (301) para ele.
6. Atualizar `canonical`, `og:url`, `sitemap.xml` e `robots.txt` com o domínio final.

## 4. Email no domínio

- Se o utilizador quer `ola@dominio.pt`: serviço de email (Google Workspace, Microsoft 365, Zoho Mail, Proton, ou o do registador) → criar os registos **MX** indicados.
- **SPF** (`TXT` no domínio): `v=spf1 include:<serviço> ~all` — um só registo SPF, juntando todos os serviços que enviam email (incluindo o serviço de formulários, se enviar em nome do domínio).
- **DKIM**: ativar no serviço de email e criar o registo `TXT`/`CNAME` indicado.
- **DMARC** (`TXT` em `_dmarc.dominio.pt`): começar com `v=DMARC1; p=none; rua=mailto:ola@dominio.pt` e passar a `p=quarantine` quando tudo estiver a passar.
- Testar: enviar um email para uma conta Gmail e ver "Mostrar original" → SPF, DKIM e DMARC = PASS.
- Se não há email no domínio, configurar à mesma um SPF que impede falsificação: `v=spf1 -all` e DMARC `p=reject`.

## 5. Google e outros motores

1. **Google Search Console**: o utilizador adiciona a propriedade (verificação por DNS é a melhor) → submeter `https://dominio.pt/sitemap.xml` → pedir indexação da página inicial.
2. **Bing Webmaster Tools**: pode importar do Search Console.
3. **Negócio local**: criar/atualizar o **Perfil da Empresa no Google** e o **Apple Business Connect** com o mesmo nome, morada, telefone e o link do site.
4. Atualizar os links nas redes sociais e na assinatura de email.

## 6. Verificação final no endereço real

Repetir no site publicado a secção "Depois de publicar" do `qualidade.md`:

```bash
curl -sI https://dominio.pt | grep -iE "strict-transport|content-security|x-content-type|referrer-policy|permissions-policy"
curl -sIL http://www.dominio.pt -o /dev/null -w '%{url_effective} %{http_code}\n'
curl -s -o /dev/null -w '%{http_code}\n' https://dominio.pt/nao-existe-123     # deve ser 404
```

E: PageSpeed Insights em telemóvel, formulário enviado a partir do site real, capturas em telemóvel real se possível.

## 7. Entrega: guia de manutenção

Cria `COMO-EDITAR.md` na raiz do projeto (em linguagem simples), com:

1. **Onde está tudo**: repositório, alojamento, domínio, email, formulários, estatísticas — com o link de cada painel (sem palavras-passe).
2. **Mudar um texto, preço ou horário**: o ficheiro exato e a linha, ou como pedir ao Claude ("abre o projeto e diz: muda o horário de sábado para 9h–13h").
3. **Trocar uma imagem**: tamanho recomendado, onde a pôr, como otimizar.
4. **Publicar uma alteração**: `git add`, `git commit`, `git push` (ou o botão do serviço) — e quanto tempo demora a aparecer.
5. **Custos e renovações**: tabela com serviço, valor, data de renovação.
6. **Verificação trimestral** (10 minutos): o site abre? O formulário chega? O domínio e o SSL renovam? Há avisos no Search Console? Os horários/preços estão certos?
7. **Se algo correr mal**: como voltar à versão anterior (o alojamento guarda as publicações anteriores; *rollback* com um clique).
