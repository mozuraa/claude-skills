# Exemplo de utilização — website-doctor

> Exemplo ilustrativo, com um site fictício. Os relatórios reais dependem do que for encontrado — cada problema vem com a prova (linha de código, cabeçalho, captura, medição).

---

## 1. Pedido

> revê o meu site da padaria, acho que está tudo bem mas quero ter a certeza. o código está nesta pasta

## 2. Consulta

O Claude vê que é um site em Next.js na pasta e faz só as perguntas que faltam:

> Antes de começar, três perguntas rápidas:
>
> 1. **O site já está publicado?** Se sim, qual é o endereço? Assim vejo o que os clientes veem, e não só o código.
> 2. **O que é mais importante no site?** Encomendas online, pedidos de contacto, ou mostrar a padaria e o horário?
> 3. **Posso corrigir o que encontrar, ou preferes primeiro só o relatório?**

> **Utilizador:** está em padaria-exemplo.pt, o mais importante são as encomendas pelo formulário. primeiro só o relatório

## 3. Relatório

# Relatório de saúde — padaria-exemplo.pt

**Resumo:** O site está bonito e rápido no computador, mas há **um problema grave de privacidade**, **um de segurança** e o formulário de encomendas **falha no iPhone**, que é a coisa mais importante. Nada disto é difícil de resolver.

| Área | Estado | Em resumo |
|---|---|---|
| Funcionamento | 🔴 | O formulário de encomendas falha no Safari do iPhone |
| Layout e alinhamentos | 🟠 | Scroll horizontal em telemóvel por causa da tabela de preços |
| Imagens | 🟠 | 3 fotografias com mais de 2 MB |
| Desempenho | 🟡 | 96 no computador, 61 no telemóvel |
| Segurança | 🔴 | Chave secreta do serviço de email no código público |
| Privacidade e RGPD | 🔴 | Google Analytics e Meta Pixel carregam antes do consentimento |
| Acessibilidade | 🟡 | Contraste baixo no rodapé; campos sem etiqueta |
| SEO | 🟢 | Títulos, descrições e sitemap corretos |
| Domínio e email | 🟠 | Sem DMARC — emails das encomendas podem ir para spam |

## 🔴 Crítico — resolver já

### 1. O formulário de encomendas falha no iPhone
- **O que é:** no Safari do iPhone, ao escolher a data de entrega, aparece "Data inválida" e não é possível enviar.
- **Onde:** `components/OrderForm.tsx:42` — `new Date(\`${dia} ${hora}\`)`. O Safari não aceita datas neste formato.
- **Porque importa:** cerca de metade dos visitantes de um site como este usa iPhone. Estão a perder-se encomendas.
- **Como corrigir:** construir a data com o formato `2025-03-14T10:00` (ISO), que todos os browsers aceitam.
- **Esforço:** Baixo.

### 2. Chave secreta do serviço de email exposta
- **O que é:** a chave que permite enviar emails em nome da padaria está dentro do código que vai para o browser — qualquer pessoa a pode copiar e enviar spam em teu nome.
- **Onde:** `lib/email.ts:3`, numa variável `NEXT_PUBLIC_…` (tudo o que começa assim fica público). *(A chave não é repetida aqui.)*
- **Porque importa:** risco de abuso, de bloqueio da conta de email e de o domínio ir parar a listas de spam.
- **Como corrigir:** **1)** gerar uma chave nova no painel do serviço e apagar a antiga (isto tens de ser tu a fazer); **2)** mover o envio do email para uma rota do servidor (`app/api/order/route.ts`) que usa a chave sem a mostrar.
- **Esforço:** Médio.

### 3. Rastreadores carregam antes do consentimento
- **O que é:** ao abrir o site pela primeira vez, sem aceitar nada, já são feitos pedidos ao Google Analytics e ao Meta Pixel.
- **Onde:** `app/layout.tsx:18–31`; confirmado no separador Rede do browser.
- **Porque importa:** viola o RGPD e a lei dos cookies — o banner existe, mas não está a bloquear nada.
- **Como corrigir:** só carregar estes scripts depois de o visitante carregar em "Aceitar".
- **Esforço:** Baixo.

## 🟠 Importante
*(mais 3 problemas: scroll horizontal na tabela de preços, fotografias pesadas, DMARC em falta — cada um com onde, porquê, como e esforço)*

## 🟡 Melhorias
*(4 melhorias: contraste do rodapé, etiquetas dos campos, fontes servidas localmente, imagem de partilha)*

## 🟢 O que está bem
- HTTPS e redirecionamentos corretos.
- Títulos, descrições, sitemap e dados estruturados de `Bakery` bem feitos.
- Código limpo e organizado, build sem avisos.

## 💬 A minha opinião

Eu começava **pelo formulário no iPhone** — é a razão de ser do site e é uma correção de 10 minutos. A seguir, **a chave exposta** (precisa de ti para gerar a nova) e **os rastreadores** — são os dois com risco legal ou de abuso. As fotografias e o scroll horizontal fazem-se na mesma ida e tornam o site visivelmente mais rápido no telemóvel.

Sinceramente, **não precisas do Meta Pixel** se não fazes anúncios no Instagram/Facebook — tirá-lo resolve metade do problema de privacidade e acelera o site. O resto das melhorias pode esperar.

## ❓ Perguntas para ti
1. **Fazes anúncios no Facebook/Instagram?** Se não, removo o Meta Pixel em vez de o pôr atrás do consentimento.
2. **Queres manter o Google Analytics?** Há alternativas sem cookies que dispensam o banner para isso.
3. **Quem gere o email do domínio?** Para o DMARC preciso de saber onde se configuram os registos DNS.

## 4. Decisão

> **Claude:** Como queres avançar?
> - **Corrijo os 3 críticos e os 3 importantes** (recomendado)
> - Escolhes um a um
> - Fica só o relatório

> **Utilizador:** corrige tudo. não faço anúncios. e se eu tirar o banner de cookies de vez?

> **Claude:** Concordo em tirar o Meta Pixel. Quanto ao banner: **só o podes tirar se deixares de usar cookies não essenciais**. Se trocares o Google Analytics por uma ferramenta sem cookies (como Plausible ou Umami), sim — e acho que é a melhor opção para uma padaria: menos burocracia, site mais rápido, e os números de que precisas estão lá. Se quiseres manter o Google Analytics, o banner tem de ficar. Queres que faça a troca?
