# Páginas — o que cada uma deve ter, textos e páginas legais

## Índice

- [Escrever para a web](#escrever-para-a-web)
- [Página inicial](#página-inicial)
- [Sobre](#sobre)
- [Serviços / Produtos](#serviços--produtos)
- [Contactos](#contactos)
- [Portfolio / Projeto](#portfolio--projeto)
- [Blog: listagem e artigo](#blog-listagem-e-artigo)
- [FAQ](#faq)
- [Página 404](#página-404)
- [Páginas legais](#páginas-legais)
- [Metadados de cada página](#metadados-de-cada-página)

---

## Escrever para a web

- **O visitante não lê, procura.** Títulos que dizem o essencial, parágrafos de 2–4 linhas, listas, negrito nas palavras-chave.
- **Benefício primeiro**: o que o visitante ganha, não o que a empresa é. "Fique com o carro pronto no mesmo dia" > "Somos uma oficina com 20 anos de experiência".
- **Concreto e verificável**: números, lugares, nomes, prazos. Evitar "qualidade", "excelência", "soluções inovadoras".
- **Uma ação por secção**, com verbo: "Marcar", "Pedir orçamento", "Ver menu", "Descarregar".
- **Tom** coerente com a marca (tu/você decidido no início e mantido).
- **Nunca inventar** factos: testemunhos, prémios, números de clientes, certificações, preços. Se faltarem, deixar marcador e pedir ao utilizador.

## Página inicial

Ordem típica (adaptar ao tipo de site — ver `briefing.md`):

1. **Topo**: título com o benefício principal; subtítulo com para quem/onde; botão principal; imagem forte.
2. **Prova rápida**: logótipos de clientes, avaliação média real, "desde 1998", imprensa — só se for verdade.
3. **O que oferece**: 3–6 serviços/produtos/funcionalidades com título curto e uma frase.
4. **Como funciona**: 3 passos (para serviços/apps) — reduz a incerteza.
5. **Prova social**: 2–3 testemunhos reais com nome e contexto.
6. **Sobre (resumo)**: quem está por trás, com fotografia; link para a página Sobre.
7. **FAQ** curta (3–5 perguntas que travam a decisão).
8. **Chamada final**: repetir a ação principal.
9. **Rodapé**.

## Sobre

- A história em poucas linhas (porquê existe), as pessoas (fotografias reais, nomes, papéis), valores **demonstrados** com factos, e uma ação no fim (contactar, ver trabalhos).

## Serviços / Produtos

- Uma secção (ou página) por serviço: o que é, para quem, o que inclui, preço ou "a partir de", prazo, ação.
- Se os preços variam, explicar de que depende e oferecer orçamento.
- Dados estruturados `Service`/`Product` quando fizer sentido.

## Contactos

- Formas de contacto por ordem de preferência do negócio (ex.: WhatsApp > telefone > email > formulário).
- Telefone com `tel:+351...`, email com `mailto:`, WhatsApp com `https://wa.me/351...`.
- Morada, mapa (imagem estática com link para "Abrir no Google Maps / Apple Maps" — evita cookies), horário (com feriados/fecho anual), estacionamento/acessos.
- Formulário curto (nome, email/telefone, mensagem) com proteção anti-spam e link para privacidade.
- Tempo de resposta esperado ("Respondemos em 24 h úteis").

## Portfolio / Projeto

- Listagem: grelha de imagens com título e categoria; filtros só se houver muitos projetos.
- Página de projeto: contexto/cliente → desafio → abordagem → resultado (com números se houver) → imagens grandes → próximo projeto.

## Blog: listagem e artigo

- Listagem: título, data, resumo, imagem; paginação ou "ver mais"; categorias.
- Artigo: título, data (e atualização), autor, tempo de leitura, conteúdo bem formatado (18 px+, linhas curtas, subtítulos, imagens com legenda), partilha, artigos relacionados, ação no fim.
- RSS e dados estruturados `BlogPosting`.

## FAQ

- Perguntas reais que os clientes fazem (pedir ao utilizador as 5 mais frequentes).
- `<details><summary>` — acessível e sem JavaScript. Dados estruturados `FAQPage` opcionais.

## Página 404

- Mensagem humana ("Esta página não existe ou mudou de sítio"), link para a página inicial, links para as páginas principais, contacto. Manter o cabeçalho e o rodapé. O servidor tem de devolver o código **404** (os alojamentos estáticos fazem-no com `404.html`).

## Páginas legais

> ⚠️ Os modelos abaixo são **pontos de partida**. Diz sempre ao utilizador que devem ser revistos para o caso concreto (e por um profissional, se o negócio trata dados sensíveis, vende online ou tem dúvidas). Não és advogado.

**Quando é preciso cada uma (UE/Portugal):**

| Página | Quando |
|---|---|
| Política de privacidade | **Sempre** que o site recolhe dados pessoais (formulário, email, newsletter, estatísticas, encomendas) — na prática, quase sempre |
| Política de cookies + banner | Só se houver cookies/rastreadores **não essenciais** (analytics com cookies, pixels, vídeos/mapas incorporados sem fachada). Sem eles, basta uma frase na privacidade |
| Termos e condições | Lojas, serviços contratados online, subscrições, área de cliente |
| Política de devoluções / envios | Lojas online (direito de livre resolução de 14 dias na UE) |
| Livro de Reclamações Eletrónico | Portugal: negócios com fornecimento de bens/serviços a consumidores — link visível para `https://www.livroreclamacoes.pt` |
| Resolução Alternativa de Litígios (RAL) | Portugal: negócios com consumidores devem indicar a(s) entidade(s) RAL a que aderem ou são obrigados (lista no Portal do Consumidor) |
| Identificação da empresa | Lojas e serviços online: nome legal, NIF, morada, contacto (Diretiva do Comércio Eletrónico) |
| Declaração de acessibilidade | Obrigatória para entidades públicas; recomendada (e em muitos casos exigida pela Lei Europeia da Acessibilidade) para comércio online |

Nota: a plataforma europeia de Resolução de Litígios em Linha (RLL/ODR) foi encerrada em 2025 — se um site antigo tiver esse link, remove-o.

**Modelo — Política de privacidade (estrutura)**

```
Política de privacidade
Última atualização: [DATA]

1. Quem somos
   [NOME LEGAL], NIF [NIF], [MORADA], [EMAIL DE CONTACTO]. É o responsável pelo tratamento dos seus dados.

2. Que dados recolhemos e porquê
   - Formulário de contacto: nome, email, telefone, mensagem — para responder ao seu pedido (base legal: diligências pré-contratuais / interesse legítimo).
   - [Newsletter: email — com o seu consentimento, que pode retirar a qualquer momento.]
   - [Encomendas: dados de faturação e envio — para executar o contrato e cumprir obrigações fiscais.]
   - [Estatísticas: usamos [SERVIÇO], que não usa cookies nem recolhe dados pessoais.]

3. Durante quanto tempo
   [Ex.: mensagens de contacto: até 12 meses; dados de faturação: o prazo legal (10 anos em Portugal).]

4. Com quem partilhamos
   Prestadores que nos ajudam a funcionar: [alojamento: SERVIÇO, país], [formulário: SERVIÇO, país], [email: SERVIÇO]. [Indicar transferências para fora da UE e as garantias.] Não vendemos dados.

5. Os seus direitos
   Acesso, retificação, apagamento, limitação, portabilidade, oposição e retirar o consentimento — basta escrever para [EMAIL]. Pode também apresentar queixa à CNPD (www.cnpd.pt).

6. Cookies
   [Este site não usa cookies de rastreio. / Ver a Política de cookies.]

7. Alterações
   Atualizaremos esta página se algo mudar.
```

**Banner de cookies (só se necessário)**: "Aceitar" e "Rejeitar" com o mesmo destaque; nada pré-marcado; nenhum script não essencial carregado antes de aceitar; link permanente no rodapé para mudar a escolha. Preferir uma solução simples e leve; ou, melhor ainda, evitar cookies não essenciais e dispensar o banner.

## Metadados de cada página

Cada página tem:

```html
<title>Título da página — Marca</title>                     <!-- ~50–60 caracteres, único -->
<meta name="description" content="...">                      <!-- ~120–160 caracteres, único -->
<link rel="canonical" href="https://dominio.pt/pagina/">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://dominio.pt/og/pagina.jpg">   <!-- 1200×630 -->
<meta property="og:url" content="https://dominio.pt/pagina/">
<meta property="og:type" content="website">                 <!-- article nos artigos -->
<meta name="twitter:card" content="summary_large_image">
```

E, quando faz sentido, um bloco JSON-LD (`Organization`/`LocalBusiness` na página inicial, `BreadcrumbList`, `Article`, `Product`, `Event`, `FAQPage`). Valida-os no Rich Results Test do Google antes de publicar.
