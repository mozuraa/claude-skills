# Checklist e calendário de lançamento

Um lançamento corre bem quando o produto está pronto, os links funcionam e o criador está presente para responder. Este guia ajuda a montar `kit/checklist.md` (modelo em `assets/kit/checklist-template.md`) com datas reais.

## Índice

1. Está pronto para lançar?
2. Escolher as plataformas
3. Montar o calendário
4. Fusos horários
5. Ficheiro `.ics` (opcional)
6. Depois do lançamento
7. Expectativas honestas

---

## 1. Está pronto para lançar?

Antes de preparar o kit, verifica (e diz com franqueza se a resposta for "ainda não"):

- O **fluxo principal** funciona do princípio ao fim, também no telemóvel e numa ligação lenta.
- O **link** abre a coisa certa: a loja, o site, o repositório — não uma página em construção.
- Quem chega pelo vídeo **consegue experimentar** em menos de um minuto (ou percebe porque não, ex.: "lista de espera").
- Há **forma de contacto** e, se recolhe dados, **política de privacidade**.
- Na App Store / Google Play: a página está **aprovada e publicada** (ou em pré-encomenda) antes do dia L.

Se algo falhar, propõe adiar ou lançar em "beta" com honestidade. Um lançamento só acontece uma vez em cada plataforma (o Product Hunt e o Show HN não gostam de repetições).

## 2. Escolher as plataformas

| Tipo de projeto | Onde costuma resultar | Onde costuma resultar pouco |
|---|---|---|
| Ferramenta web / extensão | Product Hunt, X, Show HN, Reddit (comunidades do tema), LinkedIn | — |
| App iOS / Android | TikTok, Reels, Shorts (o vídeo vertical brilha), X, Reddit do tema | Show HN (se não houver versão grátis para experimentar) |
| Jogo | TikTok, Reels, Shorts, Reddit (r/IndieDev, comunidades do género), X, Discord | LinkedIn, Product Hunt |
| Projeto open source / CLI | Show HN, Reddit (comunidades técnicas), X, Bluesky, Mastodon | Instagram, TikTok |
| Produto para empresas / B2B | LinkedIn, Product Hunt, X, email | TikTok |
| Projeto divertido / absurdo | X, TikTok, Reels, Reddit | LinkedIn (a não ser que o humor encaixe) |

Recomenda **3–4 plataformas bem feitas** em vez de 9 mal feitas, e diz porquê.

## 3. Montar o calendário

- **L−14 a L−7:** produto pronto, contas e perfis (o utilizador), regras das comunidades lidas, página "em breve".
- **L−6 a L−2:** vídeo, imagens, textos; lista de pessoas a avisar; agendar o Product Hunt (o utilizador).
- **L−1:** testar todos os links no telemóvel; ver o vídeo com e sem som; descansar.
- **Dia L:** escalonar as publicações (não tudo no mesmo minuto) para conseguir responder a cada uma; começar pelo sítio com hora fixa (Product Hunt), depois as pessoas próximas, depois as redes.
- **L+1 a L+7:** agradecer, juntar feedback, corrigir o urgente, publicar "o que aprendi", planear as **🔄 Novidades** da versão seguinte.

Usa **datas reais** a partir da data L que o utilizador escolher (ex.: "terça, 17 de novembro"). Se ele não souber, sugere uma terça a quinta para produtos de trabalho, ou um fim de semana para jogos e apps de lazer — e diz que é uma heurística, não uma regra.

## 4. Fusos horários

- Escreve todas as horas no **fuso do utilizador** e diz qual é.
- **Product Hunt:** o dia começa às 00:01 hora do Pacífico (America/Los_Angeles). Em Lisboa (Europe/Lisbon) isso é quase sempre às 08:01; nas poucas semanas em que um país já mudou a hora e o outro ainda não, é às 07:01 ou 09:01 — confirma para a data certa:
  ```bash
  python3 -c "from datetime import datetime; from zoneinfo import ZoneInfo as Z; print(datetime(2026,11,17,0,1,tzinfo=Z('America/Los_Angeles')).astimezone(Z('Europe/Lisbon')))"
  ```
- **Hacker News e Reddit em inglês:** o público é muito norte-americano; manhãs nos EUA (tarde na Europa) têm mais gente — e mais concorrência.
- Para o público português, as horas locais habituais (manhã, hora de almoço, noite) chegam.

## 5. Ficheiro `.ics` (opcional)

Para o utilizador importar no calendário dele (tu não crias eventos na conta dele). Um evento por momento importante; horas em UTC (sufixo `Z`) para evitar erros de fuso:

```
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//launch-studio//PT
BEGIN:VEVENT
UID:lancamento-ph-20261117@launch-studio
DTSTAMP:20261111T120000Z
DTSTART:20261117T080100Z
DTEND:20261117T083000Z
SUMMARY:Product Hunt fica ativo — publicar primeiro comentário
DESCRIPTION:Texto em kit/copy.md (secção Product Hunt).
END:VEVENT
END:VCALENDAR
```

Linhas com `CRLF` e no máximo 75 caracteres (dobra as mais compridas com uma linha que começa por um espaço). Guarda em `kit/calendario.ics`.

## 6. Depois do lançamento

- Responder a **todos** os comentários nas primeiras 24 h, com calma, mesmo aos duros.
- Juntar o feedback em `kit/feedback.md`: bugs (com passos), pedidos, elogios, dúvidas frequentes (viram FAQ).
- Agradecer publicamente a quem ajudou (com autorização para os nomear).
- Um post "o que aprendi" uma semana depois funciona bem — com números reais só se o utilizador os quiser partilhar.
- Guardar o que resultou para o próximo lançamento.

## 7. Expectativas honestas

Diz ao utilizador, sem dramatismo, que a maioria dos lançamentos tem um pico pequeno e curto, e que o que conta é o que se aprende e as primeiras pessoas que ficam. Nunca prometas números, posições no Product Hunt nem "viralidade". Não sugiras comprar votos, seguidores, comentários ou avaliações — é contra as regras de todas as plataformas e pode acabar com a conta.
