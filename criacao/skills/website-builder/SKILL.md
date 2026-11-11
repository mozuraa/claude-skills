---
name: website-builder
description: Cria websites completos de raiz, com o utilizador — faz perguntas (objetivo, público, páginas, estilo, conteúdo), propõe estrutura, design e tecnologia com opinião honesta, constrói página a página (mobile-first, acessível, rápido, seguro, com RGPD/cookies e páginas legais), verifica com capturas e testes, e ajuda a publicar (GitHub Pages, Netlify, Vercel, Cloudflare, domínio, email). Inclui um site-base pronto com boas práticas. Usa sempre que o utilizador quiser "criar/fazer um site", "uma página para o meu negócio", "um portfolio", "uma landing page para a minha app", "um site para o restaurante/loja/evento", "refazer o site do zero", ou perguntar como ter um site — mesmo que não diga "website". Para examinar ou corrigir um site que já existe usa website-doctor.
---

# Website builder

Constróis o site **com** o utilizador, não por ele. O trabalho tem sete fases e três momentos em que o utilizador aprova antes de avançares. Em cada fase fazes perguntas, propões, dás a tua opinião franca e explicas as escolhas — a decisão final é sempre dele.

Responde sempre na língua em que o utilizador escreveu (estas instruções estão em português, mas a resposta não tem de estar). Se a pessoa não programa, explica tudo em linguagem simples e diz-lhe exatamente o que tem de fazer quando for preciso (ex.: criar uma conta, comprar um domínio).

```
1. Briefing ─► 2. Plano ─► ✋ aprovação ─► 3. Identidade visual ─► 4. Página inicial ─► ✋ aprovação
   ─► 5. Resto do site ─► 6. Verificação ─► ✋ aprovação ─► 7. Lançamento e entrega
```

Os guias detalhados estão em `references/` — lê o de cada fase quando lá chegares:

| Fase | Guia |
|---|---|
| Briefing | `references/briefing.md` — perguntas e secções obrigatórias por tipo de site |
| Plano (tecnologia) | `references/stack.md` — que tecnologia, alojamento e serviços escolher, e quanto custam |
| Identidade visual e páginas | `references/design.md` — sistema de design, tipografia, cor, espaçamento, componentes |
| Conteúdo das páginas | `references/paginas.md` — o que cada página deve ter, textos e páginas legais |
| Verificação | `references/qualidade.md` — lista de verificação antes de publicar |
| Lançamento | `references/lancamento.md` — publicar, domínio, email, Search Console, manutenção |

O site-base pronto a usar está em `assets/starter/` (ver a secção *Site-base*).

## 1. Briefing — perceber o site antes de o desenhar

Faz as perguntas essenciais **de uma só vez** (no máximo 5, com opções sugeridas; usa a ferramenta de perguntas, se existir). As essenciais:

1. **Para que é o site?** (negócio local, portfolio, landing page de uma app/produto, restaurante, loja, evento, blog, pessoal/CV, associação...)
2. **O que deve o visitante fazer?** A ação principal: ligar, marcar, encomendar, descarregar a app, enviar mensagem, comprar, inscrever-se.
3. **Para quem é?** Público, idade, língua(s), país.
4. **Que conteúdo já tens?** Logótipo, cores, fotografias, textos, preços, horários — ou começamos do zero.
5. **Tens preferências de estilo?** Sites de que gostas (como referência de *sensação*, não para copiar), 3 palavras que descrevem a marca (ex.: "calmo, artesanal, confiável").

Depois, conforme o tipo de site, faz as perguntas específicas do `references/briefing.md` (ex.: restaurante → menu, reservas; loja → número de produtos, pagamentos). Pergunta também, quando relevante: **quem vai atualizar o site** depois (o utilizador sozinho, sem código?), **orçamento** para alojamento/domínio, **prazo**, e se já tem **domínio**.

Não perguntes o que o pedido ou o contexto já respondem. Se o utilizador disser "decide tu", decide e diz o que assumiste.

## 2. Plano — propor antes de construir

Apresenta um plano curto com:

- **Mapa do site**: as páginas e, para a página inicial, as secções por ordem (ex.: Topo com ação principal → Serviços → Testemunhos → Sobre → Contactos).
- **Tecnologia e alojamento**, escolhidos com o `references/stack.md`, com o porquê numa frase e o custo mensal/anual.
- **Direção visual** em palavras: sensação, 2–3 cores, tipo de letra, tipo de imagens.
- **Funcionalidades**: formulário, mapa, reservas, línguas, blog, newsletter — e como cada uma funciona (serviço, custo).
- **Privacidade**: que serviços externos vai ter (o objetivo por defeito é **nenhum rastreador** → sem banner de cookies).
- **O que falta do utilizador** (fotografias, textos, logótipo, acessos).

Termina com **💬 A minha opinião** (o que recomendas e o que não vale a pena — ex.: "não precisas de WordPress para 4 páginas que mudam duas vezes por ano") e pede aprovação: ✋ **"Avanço com este plano?"**

## 3. Identidade visual — o sistema antes das páginas

Com o `references/design.md`, define os *design tokens*: paleta (com contraste verificado ≥ 4,5:1 para texto), tipografia (1–2 famílias, escala de tamanhos), espaçamento (escala de 4/8 px), cantos, sombras, largura máxima do conteúdo. Põe-nos em variáveis CSS (`:root`) — o site-base já tem a estrutura.

O design deve **nascer da marca e do público**, não de um modelo genérico: o site de uma padaria artesanal não deve parecer o de uma startup de software. Nunca copies o design, os textos ou as imagens de um site existente, e nunca uses o nome ou a marca de outra empresa.

## 4. Página inicial — o primeiro protótipo a sério

Constrói **só a página inicial**, completa e com conteúdo real (ou rascunho realista — ver *Conteúdo*), em versão telemóvel e desktop. Se tiveres browser, abre-a em 375 px e 1440 px e mostra as capturas ao utilizador.

✋ Pede opinião e aprovação: "Gostas da direção? Muda alguma coisa antes de eu fazer o resto?" Ajustar aqui é barato; depois de 6 páginas é caro.

## 5. Resto do site

Constrói as outras páginas reutilizando os mesmos componentes e tokens, seguindo o `references/paginas.md` para o conteúdo de cada uma. Inclui sempre:

- **Página 404** útil.
- **Páginas legais** necessárias (privacidade; cookies só se houver cookies não essenciais; termos se vender; em Portugal, livro de reclamações eletrónico para negócios com atendimento ao público). Usa os modelos do `references/paginas.md`, adaptados, e diz ao utilizador que **devem ser revistos** para o caso dele — não és advogado.
- **SEO de base** em todas as páginas: título, descrição, canonical, Open Graph, dados estruturados adequados, `sitemap.xml`, `robots.txt`.
- **Favicon, ícones e imagem de partilha.**

Mostra o progresso ao utilizador à medida que avanças (capturas de cada página nova).

## 6. Verificação — não entregues sem testar

Percorre o `references/qualidade.md` inteiro. No mínimo:

- Capturas em **375, 768 e 1440 px**, em todas as páginas; sem scroll horizontal; nada sobreposto.
- **Consola sem erros**, todos os links a funcionar, formulário testado de ponta a ponta (a mensagem chega?).
- **Lighthouse** (ou PageSpeed Insights) em telemóvel: objetivo **≥ 90** em desempenho, acessibilidade, boas práticas e SEO.
- Imagens otimizadas (WebP/AVIF, tamanho certo, `alt`), navegação por teclado, contraste.
- **Nenhum texto de exemplo esquecido** (*Lorem ipsum*, "[NOME]", "TODO").
- Nenhum rastreador antes de consentimento; segredos fora do código público.

Se a skill `website-doctor` estiver disponível, podes usá-la para um exame completo. Mostra os resultados ao utilizador e corrige o que falhar. ✋ **"Está tudo verificado — publicamos?"**

## 7. Lançamento e entrega

Segue o `references/lancamento.md`:

- **Publicar** no alojamento escolhido (passo a passo, com o que o utilizador tem de clicar se for ele a fazê-lo).
- **Domínio** ligado, HTTPS ativo, `www` e sem `www` a redirecionar para o mesmo endereço.
- **Email do domínio** (se houver) com SPF, DKIM e DMARC; formulário a entregar mensagens.
- **Google Search Console** (e Bing) com o sitemap submetido; perfil do Google Business coerente, se for negócio local.
- **Testar o site publicado** (não só o local): capturas, formulário, HTTPS, cabeçalhos de segurança.

Entrega um **guia de manutenção** (ficheiro `COMO-EDITAR.md` ou secção no README do projeto) com: como mudar textos, imagens e preços; como publicar uma alteração; contas e serviços usados (sem palavras-passe); custos e datas de renovação; e o que verificar de 3 em 3 meses.

## Conteúdo

- **Conteúdo real é melhor do que design bonito.** Pede ao utilizador os textos, fotografias e dados verdadeiros.
- Se faltar texto, **escreve um rascunho realista** com base no briefing (não *Lorem ipsum*) e marca-o claramente para revisão (ex.: lista no fim da fase 5 "Textos que escrevi e precisas de confirmar"). Nunca inventes factos verificáveis: preços, moradas, prémios, testemunhos, números de clientes, certificações. Para isso, deixa um marcador visível e pede o dado.
- **Imagens**: as do utilizador primeiro. Senão, sugere bancos com licença livre (ex.: Unsplash, Pexels), ilustrações ou formas gráficas — nunca imagens tiradas da internet sem licença. Otimiza sempre (ver `design.md`).
- Escreve para o visitante: o que ganha, em frases curtas, com uma ação clara por secção.

## Site-base

`assets/starter/` tem um site estático pronto, com as boas práticas já feitas: HTML semântico e acessível (link "Saltar para o conteúdo", navegação por teclado, menu móvel acessível), CSS com tokens e reset moderno, modo escuro, metatags de SEO e partilha, dados estruturados, página 404, página de privacidade, `robots.txt`, `sitemap.xml`, manifest, e cabeçalhos de segurança para Netlify (`_headers`), Vercel (`vercel.json`) e Cloudflare Pages.

- Para sites simples (até ~10 páginas, sem área de cliente), **copia o site-base** para a pasta do projeto e adapta — é rápido e dá ótimas pontuações.
- Para Astro, Next.js ou outro framework, usa o site-base como **referência** (tokens, cabeçalhos, estrutura de metatags, padrões de acessibilidade) e cria o projeto com a ferramenta oficial.
- Procura `TODO:` nos ficheiros do site-base: são os sítios a personalizar. No fim, não pode ficar nenhum.

## Princípios

- **Telemóvel primeiro**: a maioria dos visitantes chega pelo telemóvel; desenha para 375 px e depois alarga.
- **Rápido por defeito**: sem bibliotecas desnecessárias; imagens otimizadas; fontes alojadas no próprio site.
- **Privado por defeito**: sem rastreadores a menos que o utilizador os peça (e então com consentimento); estatísticas sem cookies se ele quiser números.
- **Acessível por defeito**: WCAG 2.2 AA desde o início, não no fim.
- **Seguro por defeito**: HTTPS, cabeçalhos de segurança, nenhum segredo no código público, formulários com proteção anti-spam.
- **Simples de manter**: a tecnologia mais simples que resolve; o utilizador tem de conseguir atualizar o site ou saber a quem pedir.
- **Honesto**: se o utilizador pedir algo que prejudica o site (um carrossel automático no topo, música automática, 10 fontes), diz porquê com respeito, propõe a alternativa, e respeita a decisão dele.
