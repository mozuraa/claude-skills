# Exemplo de utilização — website-studio, modo Idear

> Exemplo ilustrativo, com um negócio fictício.

---

## Pedido

> tenho um site da minha oficina de bicicletas mas quase ninguém me contacta por lá. ideias?

## Resposta

*(Antes de responder, o Claude abre o site: 4 páginas, telefone só no rodapé, sem preços, formulário de contacto genérico, nenhuma página por serviço.)*

### 1. Orçamento em 3 passos — o cliente diz o que precisa sem ter de ligar

**O que é:** um botão "Pedir orçamento" no topo e no telemóvel sempre visível. Abre 3 ecrãs curtos: tipo de bicicleta → o que se passa (com ícones: travões, mudanças, furo, revisão) → nome, contacto e uma fotografia opcional.
**Objetivo:** mais pedidos de quem não quer telefonar (a maioria dos mais novos) e pedidos já com a informação certa.
**Como fica no site:** uma secção nova na página inicial e uma página `/orcamento`. O pedido chega por email, já organizado.
**Tecnologia e custo:** formulário em passos com um serviço de formulários (0 € até ao limite mensal).
**Esforço:** Baixo — meio dia.
**Primeiros passos:** definir as 6–8 avarias mais comuns; escrever os textos; montar e testar no telemóvel.
**Riscos / atenção a:** responder depressa (prometer "respondemos no mesmo dia" só se for verdade); política de privacidade junto ao formulário.
**Como medir:** pedidos por semana antes e depois.

### 2. Preços de referência — tirar o medo do "quanto vai custar?"

**O que é:** uma tabela simples com os serviços mais pedidos e um preço "a partir de" (revisão básica, troca de câmara de ar, afinação de mudanças).
**Objetivo:** as pessoas contactam mais quando têm uma ideia do preço; também atrai pesquisas no Google ("preço revisão bicicleta Lisboa").
**Como fica no site:** secção "Serviços e preços" com dados estruturados `Service`.
**Tecnologia e custo:** HTML; 0 €.
**Esforço:** Baixo.
**Primeiros passos:** escolher 8–10 serviços; o dono confirma os preços (o Claude não os inventa).
**Riscos:** preços desatualizados — fica num ficheiro fácil de editar.
**Como medir:** cliques em "Pedir orçamento" a partir da tabela.

### 3. Páginas "Reparação de bicicletas em [bairro]" — aparecer no Google na zona certa

**O que é:** 3–4 páginas para os bairros vizinhos, cada uma com fotografias reais de trabalhos lá feitos, como chegar, e o botão de orçamento.
**Objetivo:** visitas do Google de quem procura perto de casa.
**Esforço:** Médio — precisa de texto e fotografias diferentes em cada página (páginas copiadas não funcionam).
**Riscos:** só vale a pena com conteúdo verdadeiro de cada zona.

**A minha recomendação:** começar pelo **orçamento em 3 passos** com a **tabela de preços** — juntas, atacam diretamente o "quase ninguém contacta" e fazem-se num dia. As páginas por bairro ficam para depois de ver os resultados. Queres que passe ao modo **Criar** e as construa no teu site?
