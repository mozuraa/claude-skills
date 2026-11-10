# Claude Skills — biblioteca de mozuraa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-4-D97757)

**[Português](#português) · [English](#english)**

---

## Português

Todas as [skills](#o-que-é-uma-skill) para o **Claude** que criei, num só sítio. Cada skill vive no seu próprio repositório público, com instruções de instalação, exemplos e licença MIT. Esta página é o catálogo.

### Catálogo

#### 💡 Ideias

| Skill | O que faz | Versão |
|---|---|---|
| [**ideias-apps**](https://github.com/mozuraa/claude-skill-ideias-apps) | Ideias detalhadas de **apps e jogos novos** que uma pessoa sozinha consegue construir e publicar: público, ciclo principal, modelo de negócio, esforço, primeiros passos e riscos. | 1.0.0 |
| [**ideias-funcionalidades**](https://github.com/mozuraa/claude-skill-ideias-funcionalidades) | Ideias de **funcionalidades novas para uma app ou jogo que já existe**, verificadas contra o código e com os ficheiros onde encaixam. | 1.0.0 |
| [**ideias-monetizacao**](https://github.com/mozuraa/claude-skill-ideias-monetizacao) | Estratégias de **monetização** justas para apps e jogos, com preços concretos, momento certo e regras da App Store e do Google Play. | 1.0.0 |
| [**brainstorming**](https://github.com/mozuraa/claude-skill-brainstorming) | **Brainstorming sobre qualquer tema** — presentes, nomes, eventos, negócios — com as 2–3 melhores ideias, distintas e prontas a pôr em prática. | 1.0.0 |

A lista também existe em formato de dados em [`skills.json`](skills.json).

### Instalar

**Uma skill (Claude Code)** — troca `NOME` pelo nome da skill:

```bash
git clone https://github.com/mozuraa/claude-skill-NOME.git ~/.claude/skills/NOME
```

**Todas de uma vez (Claude Code):**

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming; do git clone https://github.com/mozuraa/claude-skill-$s.git ~/.claude/skills/$s; done
```

Abre uma sessão nova do Claude Code para as skills serem carregadas.

**App Claude / claude.ai:** abre o repositório da skill, carrega em **Code → Download ZIP** e carrega o ZIP nas **Definições**, na secção **Skills** (em *Capacidades*).

**Atualizar todas:**

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming; do git -C ~/.claude/skills/$s pull; done
```

### O que é uma skill?

Uma skill é uma pasta com um ficheiro `SKILL.md`: um nome, uma descrição de quando deve ser usada e instruções. O Claude lê só a descrição até ela ser útil; quando o pedido encaixa, carrega as instruções e segue-as. Não instala programas nem corre código — é só texto.

### Princípios destas skills

- **Poucas respostas, bem pensadas** — 2 a 3 ideias desenvolvidas em vez de listas longas.
- **Formato fixo** — cada ideia tem sempre as mesmas secções, fáceis de comparar.
- **Qualquer língua** — as instruções estão em português, mas o Claude responde na língua em que lhe escreves.
- **Livres** — licença MIT: usa, altera e partilha.

### Sugestões

Encontraste um problema ou tens uma ideia para uma skill? Abre uma *issue* no repositório da skill (ou [aqui](https://github.com/mozuraa/claude-skills/issues) para ideias de skills novas).

---

## English

All the [skills](#what-is-a-skill) for **Claude** that I've created, in one place. Each skill lives in its own public repository with installation instructions, examples and an MIT license. This page is the catalog.

### Catalog

#### 💡 Ideas

| Skill | What it does | Version |
|---|---|---|
| [**ideias-apps**](https://github.com/mozuraa/claude-skill-ideias-apps) | Detailed ideas for **new apps and games** a solo developer can build and ship: audience, core loop, business model, effort, first steps and risks. | 1.0.0 |
| [**ideias-funcionalidades**](https://github.com/mozuraa/claude-skill-ideias-funcionalidades) | **New feature ideas for an existing app or game**, checked against the code and pointing to the files they touch. | 1.0.0 |
| [**ideias-monetizacao**](https://github.com/mozuraa/claude-skill-ideias-monetizacao) | Fair **monetization** strategies for apps and games, with concrete prices, the right timing and App Store / Google Play rules. | 1.0.0 |
| [**brainstorming**](https://github.com/mozuraa/claude-skill-brainstorming) | **Brainstorming on any topic** — gifts, names, events, businesses — with the 2–3 best, distinct, ready-to-act ideas. | 1.0.0 |

The list is also available as data in [`skills.json`](skills.json).

### Install

**One skill (Claude Code)** — replace `NAME` with the skill name:

```bash
git clone https://github.com/mozuraa/claude-skill-NAME.git ~/.claude/skills/NAME
```

**All at once (Claude Code):**

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming; do git clone https://github.com/mozuraa/claude-skill-$s.git ~/.claude/skills/$s; done
```

Start a new Claude Code session so the skills are loaded.

**Claude app / claude.ai:** open the skill's repository, click **Code → Download ZIP** and upload it in **Settings**, under **Skills** (in *Capabilities*).

**Update all:**

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming; do git -C ~/.claude/skills/$s pull; done
```

### What is a skill?

A skill is a folder with a `SKILL.md` file: a name, a description of when it should be used, and instructions. Claude only reads the description until it becomes relevant; when a request matches, it loads the instructions and follows them. It installs no programs and runs no code — it's just text.

### Principles

- **Few, well-thought-out answers** — 2–3 developed ideas instead of long lists.
- **Fixed format** — every idea has the same sections, easy to compare.
- **Any language** — instructions are in Portuguese, but Claude replies in the language you write in.
- **Free** — MIT license: use, modify and share.

### Feedback

Found a problem or have an idea for a skill? Open an issue in the skill's repository (or [here](https://github.com/mozuraa/claude-skills/issues) for new skill ideas).

---

## License

[MIT](LICENSE)
