# Exemplo — 🔄 Novidades

Projeto fictício: **Migalha** (app web e iOS que divide contas). Última etiqueta: `v1.2.0`.

---

**Utilizador:** o que há de novo desde a 1.2? quero anunciar a 1.3.

**Claude:** *(corre `git log v1.2.0..HEAD --no-merges`, abre os diffs dos candidatos)*

```
a91c3e2 feat: export history to CSV
77f0b1d perf: lazy-load history list
5d2e9a0 fix: crash when rotating in split view
c13b8f4 feat: support Dynamic Type in result screen
9e0d771 refactor: extract currency formatter
41aa2c9 test: add rounding tests
0b7f5e3 chore(deps): bump dependencies
e2c4d18 fix: tip rounding off by one cent with 7 people
```

**Triagem**

| Grupo | Mudança | Para o utilizador | Destaque? |
|---|---|---|---|
| Novo | exportar CSV | Exporta o histórico para uma folha de cálculo. | ⭐ 1 |
| Melhor | histórico mais rápido | O histórico abre num instante, mesmo com centenas de contas. | ⭐ 2 |
| Corrigido | crash ao rodar | Já não fecha ao rodar o telemóvel no ecrã de divisão. | ⭐ 3 (era a queixa mais comum) |
| Melhor | tamanho de letra do sistema | O resultado acompanha o tamanho de letra do teu telemóvel. | notas |
| Corrigido | gorjeta com 7 pessoas | A gorjeta já não falha 1 cêntimo em grupos de 7. | notas |
| Interno | refactor, testes, dependências | — | fora |

Confirmei no diff que o crash corrigido era mesmo o da rotação. Concordas com estes três destaques?

**Utilizador:** sim.

---

**Claude:** *(escreve `launch-output/novidades.md`)*

**App Store — Novidades nesta versão (PT)** (384/4000)
> Exporta as tuas contas! Agora podes enviar o histórico para uma folha de cálculo, para fechar as contas da viagem ou da casa.
>
> Também nesta versão:
> • O histórico abre num instante, mesmo com centenas de contas.
> • A app já não fecha ao rodar o telemóvel no ecrã de divisão.
> • O resultado acompanha o tamanho de letra do teu telemóvel.
> • A gorjeta já não falha 1 cêntimo em grupos de 7.

**Google Play — Novidades (PT)** (177/500)
> • Exporta o histórico para uma folha de cálculo
> • Histórico mais rápido
> • Já não fecha ao rodar o telemóvel
> • Texto maior se o usares no telemóvel
> • Gorjeta certa em grupos de 7

**App Store — What's New (EN)** (317/4000)
> Export your bills! Send your history to a spreadsheet to settle a trip or a shared flat.
>
> Also in this version:
> • History opens instantly, even with hundreds of bills.
> • No more crash when rotating your phone on the split screen.
> • Results follow your phone's text size.
> • Tips no longer go 1 cent off in groups of 7.

**GitHub Release `v1.3.0`** e uma entrada para o `CHANGELOG.md` no formato que o projeto já usa — posso acrescentá-la ao ficheiro?

**Vídeo** (`video/novidades-1.3-9x16.mp4`, 12 s, 120 BPM, tom do lançamento):

| Tempo | Cena | Texto |
|---|---|---|
| 0,0–2,0 s | "Novo no Migalha 1.3" sobre a cor da marca | |
| 2,0–6,0 s | gravação: tocar em "Exportar" → a folha de cálculo abre | "Exporta para uma folha de cálculo" |
| 6,0–8,0 s | gravação: lista de 300 contas a abrir e a deslizar | "O histórico abre num instante" |
| 8,0–10,0 s | gravação: rodar o simulador no ecrã de divisão, sem fechar | "Já não fecha ao rodar" |
| 10,0–12,0 s | nome + "Atualiza já" | |

**Post (X)**
> O Migalha 1.3 já está cá fora:
> • exporta as contas para uma folha de cálculo
> • o histórico abre num instante
> • já não fecha ao rodar o telemóvel (obrigado a quem reportou!)

**A minha opinião:** a exportação merece o vídeo; o resto chega nas notas. Não pus o "refactor" nem as dependências — não interessam a quem usa a app. Não verifiquei o vídeo no telemóvel real.
