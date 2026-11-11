# Exemplo de utilização — website-builder

> Exemplo ilustrativo, com um negócio fictício. Mostra as primeiras fases (briefing e plano), que é onde a skill mais conversa com o utilizador.

---

## 1. Pedido

> quero um site para o meu estúdio de pilates, ainda não tenho nada

## 2. Briefing

> Vamos fazer isso. Cinco perguntas rápidas para eu propor um plano:
>
> 1. **O que deve uma pessoa fazer no site?** Marcar uma aula experimental, ver o horário, comprar um pacote, ou contactar-te?
> 2. **Para quem é?** Ex.: pessoas da zona entre 30 e 60 anos, grávidas, recuperação de lesões...
> 3. **Que conteúdo já tens?** Logótipo, fotografias do estúdio, preços, horário, descrição das aulas.
> 4. **Que sensação queres que o site passe?** Diz-me 3 palavras (ex.: "calmo, profissional, próximo") e, se quiseres, um site de que gostes.
> 5. **Já tens domínio** (ex.: `estudiox.pt`)? E vais ser tu a mudar o horário quando for preciso?

> **Utilizador:** marcar aula experimental. mulheres 35-60 na zona de Alvalade. tenho logo e fotos do estúdio, preços em papel. calmo, luminoso, próximo. não tenho domínio. o horário muda todos os meses e quero ser eu a mudar

Pergunta de seguimento específica (do `briefing.md`, secção *Saúde, bem-estar*):

> Mais duas: as marcações são por telefone/WhatsApp ou queres que as pessoas marquem sozinhas num calendário online? E tens alguma certificação ou formação que queiras mostrar?

> **Utilizador:** whatsapp. sou certificada pela [escola de formação]

## 3. Plano

**Mapa do site** (uma só página longa + páginas legais — chega para o objetivo e é mais fácil no telemóvel):

1. Topo — "Pilates em grupos pequenos em Alvalade" + botão **Marcar aula experimental (WhatsApp)**
2. Para quem é — 3 cartões (costas e postura, depois da gravidez, manter-se ativa)
3. As aulas — tipos de aula, duração, máximo de pessoas
4. Horário — tabela simples **editável num ficheiro** (ver abaixo)
5. Preços — 3 pacotes, com o recomendado destacado
6. Sobre mim — fotografia, certificação, a minha história
7. Testemunhos — *precisamos de 2–3 reais, com autorização*
8. Perguntas — "Nunca fiz pilates, posso ir?", "O que levo?", "Há estacionamento?"
9. Contactos — WhatsApp, telefone, morada, mapa (imagem com link), horário de atendimento
+ Política de privacidade, Livro de Reclamações, página 404

**Tecnologia:** HTML + CSS (site-base da skill), alojado na **Netlify** (grátis). O horário fica num ficheiro `horario.json` que te ensino a editar no próprio GitHub, pelo browser — mudas uma linha, guardas, e o site atualiza em 1 minuto.

**Direção visual:** *calmo, luminoso, próximo* → fundo creme muito claro, verde-salva suave como cor principal, títulos numa serifa suave, muito espaço, fotografias do teu estúdio com luz natural, cantos arredondados.

**Privacidade:** sem rastreadores e sem banner de cookies. O mapa é uma imagem com link (o mapa do Google incorporado trazia cookies). Se quiseres saber quantas visitas tens, posso pôr estatísticas sem cookies.

**Custos:**

| Item | Valor |
|---|---|
| Domínio `.pt` | ~15 € por ano (compras tu — eu digo-te onde e como) |
| Alojamento (Netlify) | 0 € |
| Email `ola@…pt` (opcional) | 0–5 €/mês |

**Preciso de ti:** logótipo (o ficheiro original, se tiveres), 6–10 fotografias do estúdio, os preços, o horário atual, 2–3 testemunhos de alunas (com autorização), o teu número de WhatsApp.

**💬 A minha opinião:** uma página única com um botão de WhatsApp sempre à mão é o que mais vai converter para o teu objetivo — as pessoas querem ver o espaço, o preço e marcar, sem navegar. **Não recomendo** WordPress nem um sistema de marcações online por agora: dão trabalho e custos e, com WhatsApp, já marcas facilmente. Se um dia tiveres mais de 2–3 instrutoras, aí sim faz sentido um calendário online (posso integrar o Cal.com).

✋ **Avanço com este plano?**

> **Utilizador:** sim! mas queria uma música calma a tocar quando se abre o site

> **Claude:** Percebo a ideia — passar a sensação do estúdio. Mas a minha opinião honesta é que **não vale a pena**: os browsers bloqueiam som automático (não tocaria na maioria das visitas), quem abre o site no trabalho ou nos transportes fecha-o logo, e é um problema de acessibilidade. Para passar a mesma calma, proponho **um vídeo curto e silencioso do estúdio** no topo (5–8 segundos, em loop, leve) ou uma fotografia grande com luz da manhã. Se mesmo assim quiseres música, ponho um botão "▶ Ouvir a playlist do estúdio" que só toca se a pessoa carregar. Qual preferes?
