# Briefing — perguntas e secções por tipo de site

Depois das 5 perguntas essenciais (ver `SKILL.md`), usa a secção do tipo de site para as perguntas específicas e para saber **o que o site tem de ter**. Pergunta só o que falta — junta as perguntas numa única mensagem.

## Índice

- [Perguntas comuns a todos](#perguntas-comuns-a-todos)
- [Negócio local / serviços](#negócio-local--serviços)
- [Restaurante, café, padaria](#restaurante-café-padaria)
- [Landing page de app ou produto](#landing-page-de-app-ou-produto)
- [Portfolio (criativos, fotógrafos, designers, programadores)](#portfolio)
- [Loja online](#loja-online)
- [Evento, casamento, conferência](#evento-casamento-conferência)
- [Blog / conteúdo](#blog--conteúdo)
- [Pessoal / CV](#pessoal--cv)
- [Associação, clube, ONG](#associação-clube-ong)
- [Alojamento local, turismo](#alojamento-local-turismo)
- [Saúde, bem-estar, profissionais liberais](#saúde-bem-estar-profissionais-liberais)

---

## Perguntas comuns a todos

- **Nome** exato da marca/pessoa e **slogan**, se houver.
- **Domínio**: já tem? Qual? Onde foi comprado? Se não tem, que nomes gosta (verificar disponibilidade).
- **Línguas** do site (cada língua multiplica o conteúdo — pergunta se são mesmo precisas).
- **Quem atualiza** o site e com que frequência (define se precisa de um editor de conteúdo/CMS).
- **Identidade**: logótipo (em vetor/SVG ou PNG grande), cores e tipos de letra da marca, se existirem.
- **Fotografias** próprias (de qualidade?) ou é preciso arranjar.
- **Concorrentes ou referências**: 1–3 sites de que gosta e **o quê** gosta em cada um.
- **Contactos** a mostrar: telefone, email, WhatsApp, morada, redes sociais, horário.
- **Orçamento** para custos recorrentes (domínio, alojamento, email, serviços) e **prazo**.
- **Estatísticas**: quer saber quantas visitas tem? (Se sim, propor uma solução sem cookies.)

## Negócio local / serviços

*(canalizador, cabeleireiro, oficina, contabilista, limpezas, explicações...)*

**Perguntar:** lista de serviços (e preços, se os mostra); zona que serve; marcação online ou só contacto; testemunhos/avaliações reais (Google?); certificações ou anos de experiência; fotografias do trabalho/espaço.

**Tem de ter:** ação principal visível no topo ("Ligar", "Pedir orçamento", "Marcar"); serviços; zona de atuação; prova social real; contactos com `tel:` e mapa; horário; dados estruturados `LocalBusiness`; perfil Google Business coerente; livro de reclamações (Portugal).

## Restaurante, café, padaria

**Perguntar:** menu (muda com que frequência? em PDF ou no site — no site é melhor para telemóvel e Google); reservas (telefone, serviço como TheFork, formulário próprio); encomendas/take-away/entregas (plataformas?); horário e dias de fecho; alergénios; fotografias dos pratos e do espaço; eventos/grupos.

**Tem de ter:** menu em HTML legível no telemóvel (com preços e alergénios); horário claro e atualizado; morada com mapa e "Como chegar"; botão de reserva/ligar sempre à mão; fotografias apetitosas e leves; dados estruturados `Restaurant` com `servesCuisine`, `openingHours`, `menu`.

## Landing page de app ou produto

**Perguntar:** o que a app faz numa frase; para quem; 3 benefícios principais; plataformas (App Store, Google Play, web) e links; capturas de ecrã/vídeo; preço (grátis, compras na app, subscrição); imprensa/prémios/avaliações reais; lista de espera ou já publicada; política de privacidade da app (as lojas exigem uma URL — o site pode alojá-la); página de suporte (a App Store exige URL de suporte).

**Tem de ter:** título com o benefício + botões oficiais das lojas (usar os *badges* oficiais da Apple e da Google, segundo as regras delas); capturas num telemóvel; 3–6 funcionalidades com ícones; FAQ; **política de privacidade da app**; **página de suporte/contacto**; termos, se houver subscrições; Smart App Banner (`apple-itunes-app`) opcional; Open Graph com uma imagem forte; dados estruturados `SoftwareApplication`/`MobileApplication`.

## Portfolio

**Perguntar:** área (fotografia, design, ilustração, arquitetura, desenvolvimento...); 6–12 melhores trabalhos (qualidade > quantidade); para cada projeto: título, cliente, papel, resultado; quer ser contratado para quê; currículo/CV em PDF; disponibilidade.

**Tem de ter:** trabalhos logo no topo; páginas de projeto com contexto (problema → processo → resultado); imagens grandes mas otimizadas (`srcset`, AVIF/WebP, *lazy loading*); sobre com fotografia; contacto simples; para programadores, links para GitHub/projetos ao vivo.

## Loja online

**Perguntar:** número de produtos e variantes (tamanhos, cores); produtos físicos ou digitais; envios (países, custos); pagamentos (MB Way, Multibanco, cartão, PayPal); stock; quem gere encomendas; faturação (em Portugal: software certificado); devoluções.

**Opinião a dar:** para mais de ~10 produtos ou gestão de stock, **uma plataforma de loja** (Shopify, WooCommerce) costuma ser melhor do que programar uma loja — pagamentos, impostos, faturas e segurança já resolvidos. Para 1–5 produtos, links de pagamento (ex.: Stripe Payment Links) num site simples chegam. Diz isto com franqueza.

**Tem de ter:** termos e condições, política de devoluções (14 dias na UE), envios, privacidade, livro de reclamações, resolução alternativa de litígios (Portugal/UE), identificação completa da empresa (NIF, morada), preços com IVA, dados estruturados `Product`/`Offer`.

## Evento, casamento, conferência

**Perguntar:** data, local, programa; inscrição/RSVP (formulário, bilheteira); alojamento e transporte; oradores/participantes; data em que o site deixa de ser preciso; privacidade dos convidados (casamento: site não indexado? palavra-passe?).

**Tem de ter:** data e local no topo; contagem decrescente opcional; programa; mapa e como chegar; RSVP/inscrição testada; FAQ (estacionamento, roupa, crianças); dados estruturados `Event`; `noindex` se for privado.

## Blog / conteúdo

**Perguntar:** temas; frequência de publicação; quem escreve; precisa de newsletter; comentários (normalmente não — dão trabalho e spam); categorias; migrar artigos de outro sítio.

**Opinião a dar:** para escrever com frequência sem programar, um CMS (WordPress, Ghost, ou Astro + editor Decap/Sanity). Para um programador, Markdown num gerador estático (Astro) é ótimo.

**Tem de ter:** listagem de artigos; página de artigo legível (60–75 caracteres por linha, 18 px+); datas; autor; categorias; RSS; partilha; dados estruturados `Article`/`BlogPosting`; imagens de partilha por artigo.

## Pessoal / CV

**Perguntar:** objetivo (emprego, freelance, marca pessoal); experiência, formação, competências; projetos; línguas; o que **não** quer público (morada, telefone).

**Tem de ter:** quem é e o que procura em 2 frases; experiência e projetos com resultados; CV em PDF; contacto (email, LinkedIn); cuidado com dados pessoais (não publicar morada nem data de nascimento).

## Associação, clube, ONG

**Perguntar:** missão; atividades e calendário; como ajudar (sócios, voluntários, donativos); transparência (relatórios, órgãos sociais); quem atualiza (vários voluntários? → CMS simples).

**Tem de ter:** missão clara; como participar/ajudar com botão visível; calendário/notícias; donativos (com o serviço adequado e recibos, se aplicável); contactos; estatutos/relatórios se forem públicos.

## Alojamento local, turismo

**Perguntar:** número de alojamentos; reservas diretas (motor de reservas, Airbnb/Booking com links); número de registo de AL (obrigatório mostrar em Portugal); fotografias profissionais; comodidades; regras da casa; línguas (normalmente PT + EN + outras).

**Tem de ter:** galeria forte e leve; comodidades; localização e o que há perto; preços ou "ver disponibilidade"; número de registo; avaliações reais; várias línguas; dados estruturados `LodgingBusiness`/`VacationRental`.

## Saúde, bem-estar, profissionais liberais

*(clínicas, psicólogos, nutricionistas, advogados, explicadores...)*

**Perguntar:** especialidades; marcação online (serviço?); número de cédula/inscrição na ordem profissional (muitas vezes obrigatório mostrar); acordos/seguros; teleconsulta; regras de publicidade da ordem profissional.

**Tem de ter:** especialidades e para quem; profissionais com fotografia e credenciais; marcação clara; morada, horário, acessibilidade física; **cuidado extra com dados de saúde** (formulários não devem pedir informação clínica; se pedirem, é dado sensível no RGPD — avisar o utilizador); respeitar regras deontológicas sobre publicidade e testemunhos.
