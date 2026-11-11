# Claude Skills — biblioteca de mozuraa

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-8-D97757)
![Categorias](https://img.shields.io/badge/categorias-4-2EAD6B)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-8A63D2)

**[Português](#português) · [English](#english)**

---

## Português

Todas as [skills](#o-que-é-uma-skill) para o **Claude** que criei, organizadas por categoria. Cada skill está completa aqui dentro e também tem o seu próprio repositório público, com instruções, exemplos e licença MIT.

### Categorias

| | Categoria | Skills |
|---|---|---|
| 💡 | **[Ideias](ideias/)** | `ideias-apps` · `ideias-funcionalidades` · `ideias-monetizacao` · `brainstorming` |
| 🛠️ | **[Criação](criacao/)** | `website-builder` |
| 🧑‍💻 | **[Programação](programacao/)** | `code-for-noobs` |
| 🩺 | **[Diagnóstico](diagnostico/)** | `website-doctor` · `app-doctor` |

### Que skill uso?

| Quero... | Skill |
|---|---|
| uma ideia para uma app ou jogo **novo** | [`ideias-apps`](ideias/skills/ideias-apps/SKILL.md) |
| melhorar uma app que **já tenho** | [`ideias-funcionalidades`](ideias/skills/ideias-funcionalidades/SKILL.md) |
| ganhar dinheiro com a minha app | [`ideias-monetizacao`](ideias/skills/ideias-monetizacao/SKILL.md) |
| ideias sobre **outra coisa qualquer** | [`brainstorming`](ideias/skills/brainstorming/SKILL.md) |
| **criar um site** de raiz | [`website-builder`](criacao/skills/website-builder/SKILL.md) |
| perceber código, um erro ou um termo técnico | [`code-for-noobs`](programacao/skills/code-for-noobs/SKILL.md) |
| saber o que está mal no meu **site** e corrigir | [`website-doctor`](diagnostico/skills/website-doctor/SKILL.md) |
| saber o que está mal na minha **app** e se está pronta para a loja | [`app-doctor`](diagnostico/skills/app-doctor/SKILL.md) |

Não precisas de escolher: com as skills instaladas, o Claude usa a certa sozinho quando o pedido encaixa.

### Catálogo

#### 💡 Ideias

| | Skill | O que faz | Versão |
|---|---|---|---|
| | [**ideias-apps**](https://github.com/mozuraa/claude-skill-ideias-apps) | Ideias detalhadas de **apps e jogos novos** que uma pessoa sozinha consegue construir e publicar: público, ciclo principal, modelo de negócio, esforço, primeiros passos e riscos. | 1.0.0 |
| | [**ideias-funcionalidades**](https://github.com/mozuraa/claude-skill-ideias-funcionalidades) | Ideias de **funcionalidades novas para uma app ou jogo que já existe**, verificadas contra o código e com os ficheiros onde encaixam. | 1.0.0 |
| | [**ideias-monetizacao**](https://github.com/mozuraa/claude-skill-ideias-monetizacao) | Estratégias de **monetização** justas, com preços concretos, momento certo e regras da App Store e do Google Play. | 1.0.0 |
| | [**brainstorming**](https://github.com/mozuraa/claude-skill-brainstorming) | **Brainstorming sobre qualquer tema** — presentes, nomes, eventos, negócios — com as 2–3 melhores ideias, prontas a pôr em prática. | 1.0.0 |

#### 🛠️ Criação

| | Skill | O que faz | Versão |
|---|---|---|---|
| <img src="criacao/skills/website-builder/icon.svg" width="32" alt=""> | [**website-builder**](https://github.com/mozuraa/claude-skill-website-builder) | **Cria websites completos de raiz, contigo**: briefing, plano com a sua opinião (tecnologia, alojamento e custos), identidade visual, página inicial para aprovares, resto do site, verificação (Lighthouse ≥ 90, acessibilidade, privacidade) e lançamento com domínio e email. Inclui 6 guias e um site-base pronto. | 1.0.0 |

#### 🧑‍💻 Programação

| | Skill | O que faz | Versão |
|---|---|---|---|
| <img src="programacao/skills/code-for-noobs/icon.svg" width="32" alt=""> | [**code-for-noobs**](https://github.com/mozuraa/claude-skill-code-for-noobs) | Explica **código, erros e programação a quem nunca programou**, em linguagem simples, com analogias e um glossário de 40+ termos. | 1.0.0 |

#### 🩺 Diagnóstico

| | Skill | O que faz | Versão |
|---|---|---|---|
| <img src="diagnostico/skills/website-doctor/icon.svg" width="32" alt=""> | [**website-doctor**](https://github.com/mozuraa/claude-skill-website-doctor) | **Médico de websites**: faz perguntas, examina 12 áreas (150+ verificações) — funcionamento, layout e alinhamentos, imagens, desempenho, segurança, privacidade/RGPD, acessibilidade, SEO e mais —, mostra um relatório de saúde com a sua opinião e corrige o que autorizares. | 1.0.1 |
| <img src="diagnostico/skills/app-doctor/icon.svg" width="32" alt=""> | [**app-doctor**](https://github.com/mozuraa/claude-skill-app-doctor) | **Médico de apps** (iOS, Android, Flutter, React Native): crashes, layout em todos os ecrãs, segurança, privacidade, acessibilidade, compras e regras da App Store e do Google Play (140+ verificações) — com relatório, opinião e correções. | 1.0.0 |

A lista também existe em formato de dados em [`skills.json`](skills.json).

### Instalar

**1. Claude Code — como plugin (recomendado).** No Claude Code, escreve:

```
/plugin marketplace add mozuraa/claude-skills
```

E depois instala as categorias que quiseres:

```
/plugin install ideias@mozuraa-skills
/plugin install criacao@mozuraa-skills
/plugin install programacao@mozuraa-skills
/plugin install diagnostico@mozuraa-skills
```

As atualizações chegam com `/plugin marketplace update mozuraa-skills`. Instaladas assim, as skills aparecem com o nome da categoria à frente (ex.: `/diagnostico:website-doctor`).

**2. Claude Code — skills soltas.** Uma skill (troca `NOME`):

```bash
git clone https://github.com/mozuraa/claude-skill-NOME.git ~/.claude/skills/NOME
```

Todas de uma vez:

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming website-builder code-for-noobs website-doctor app-doctor; do git clone https://github.com/mozuraa/claude-skill-$s.git ~/.claude/skills/$s; done
```

Atualizar todas:

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming website-builder code-for-noobs website-doctor app-doctor; do git -C ~/.claude/skills/$s pull; done
```

**3. App Claude / claude.ai.** Abre o repositório da skill, carrega em **Code → Download ZIP** e carrega o ZIP nas **Definições**, na secção **Skills** (em *Capacidades*).

Abre uma sessão nova depois de instalar.

### Como está organizado

```
claude-skills/
├── .claude-plugin/marketplace.json   # catálogo de plugins para o Claude Code
├── ideias/                           # 💡 plugin "ideias"
│   ├── .claude-plugin/plugin.json
│   └── skills/
│       ├── ideias-apps/
│       ├── ideias-funcionalidades/
│       ├── ideias-monetizacao/
│       └── brainstorming/
├── criacao/                          # 🛠️ plugin "criacao"
│   └── skills/website-builder/
├── programacao/                      # 🧑‍💻 plugin "programacao"
│   └── skills/code-for-noobs/
├── diagnostico/                      # 🩺 plugin "diagnostico"
│   └── skills/
│       ├── website-doctor/
│       └── app-doctor/
├── skills.json                       # a lista em formato de dados
└── scripts/sincronizar.sh            # copia as skills dos repositórios individuais para aqui
```

Cada skill tem o seu `SKILL.md` e, quando precisa, `references/` (listas e guias), `assets/` (ficheiros prontos a usar, como o site-base), `examples/` e `icon.svg`. Os repositórios individuais são a fonte; esta biblioteca guarda cópias organizadas, atualizadas com `scripts/sincronizar.sh`.

### O que é uma skill?

Uma skill é uma pasta com um ficheiro `SKILL.md`: um nome, uma descrição de quando deve ser usada e instruções. O Claude lê só a descrição até ela ser útil; quando o pedido encaixa, carrega as instruções e segue-as. Não instala programas — é texto com instruções.

### Princípios destas skills

- **Qualidade acima de quantidade:** poucas respostas, bem pensadas e com provas.
- **Formato fixo:** as mesmas secções sempre, fáceis de comparar.
- **Opinião honesta:** as skills dizem o que fariam e porquê, mas tu decides.
- **Seguras:** os médicos só examinam projetos teus e nunca atacam nada.
- **Qualquer língua:** as instruções estão em português, mas o Claude responde na língua em que lhe escreves.
- **Livres:** licença MIT.

### Sugestões

Encontraste um problema ou tens uma ideia para uma skill? Abre uma *issue* no repositório da skill, ou [aqui](https://github.com/mozuraa/claude-skills/issues) para ideias de skills novas.

---

## English

All the [skills](#what-is-a-skill) for **Claude** that I've created, organized by category. Every skill is included here in full and also has its own public repository with instructions, examples and an MIT license.

### Categories

| | Category | Skills |
|---|---|---|
| 💡 | **[Ideas](ideias/)** (`ideias`) | `ideias-apps` · `ideias-funcionalidades` · `ideias-monetizacao` · `brainstorming` |
| 🛠️ | **[Creation](criacao/)** (`criacao`) | `website-builder` |
| 🧑‍💻 | **[Programming](programacao/)** (`programacao`) | `code-for-noobs` |
| 🩺 | **[Diagnostics](diagnostico/)** (`diagnostico`) | `website-doctor` · `app-doctor` |

### Which skill do I need?

| I want... | Skill |
|---|---|
| an idea for a **new** app or game | `ideias-apps` |
| to improve an app I **already have** | `ideias-funcionalidades` |
| to make money from my app | `ideias-monetizacao` |
| ideas about **anything else** | `brainstorming` |
| to **build a website** from scratch | `website-builder` |
| to understand code, an error or a technical term | `code-for-noobs` |
| to find and fix what's wrong with my **website** | `website-doctor` |
| to find and fix what's wrong with my **app**, and know if it's store-ready | `app-doctor` |

You don't have to choose: once installed, Claude picks the right one on its own when a request matches.

### Catalog

| Category | Skill | What it does |
|---|---|---|
| 💡 | [**ideias-apps**](https://github.com/mozuraa/claude-skill-ideias-apps) | Detailed ideas for **new apps and games** a solo developer can build and ship. |
| 💡 | [**ideias-funcionalidades**](https://github.com/mozuraa/claude-skill-ideias-funcionalidades) | **New feature ideas for an existing app or game**, checked against the code. |
| 💡 | [**ideias-monetizacao**](https://github.com/mozuraa/claude-skill-ideias-monetizacao) | Fair **monetization** strategies with concrete prices and store rules. |
| 💡 | [**brainstorming**](https://github.com/mozuraa/claude-skill-brainstorming) | **Brainstorming on any topic**, with the 2–3 best ready-to-act ideas. |
| 🛠️ | [**website-builder**](https://github.com/mozuraa/claude-skill-website-builder) | **Builds complete websites from scratch with you**: briefing, opinionated plan, visual identity, home page for your approval, the rest of the site, checks and launch. Includes 6 guides and a starter site. |
| 🧑‍💻 | [**code-for-noobs**](https://github.com/mozuraa/claude-skill-code-for-noobs) | Explains **code, errors and programming to people who have never coded**. |
| 🩺 | [**website-doctor**](https://github.com/mozuraa/claude-skill-website-doctor) | **Website doctor**: 12 areas, 150+ checks (functionality, layout, images, performance, security, privacy/GDPR, accessibility, SEO...), health report with its opinion, and approved fixes. |
| 🩺 | [**app-doctor**](https://github.com/mozuraa/claude-skill-app-doctor) | **App doctor** (iOS, Android, Flutter, React Native): crashes, layout, security, privacy, accessibility, purchases and App Store / Google Play rules (140+ checks). |

The list is also available as data in [`skills.json`](skills.json).

### Install

**1. Claude Code, as a plugin (recommended):**

```
/plugin marketplace add mozuraa/claude-skills
/plugin install ideias@mozuraa-skills
/plugin install criacao@mozuraa-skills
/plugin install programacao@mozuraa-skills
/plugin install diagnostico@mozuraa-skills
```

Update with `/plugin marketplace update mozuraa-skills`. Installed this way, skills are prefixed with their category (e.g. `/diagnostico:website-doctor`).

**2. Claude Code, standalone skills:**

```bash
for s in ideias-apps ideias-funcionalidades ideias-monetizacao brainstorming website-builder code-for-noobs website-doctor app-doctor; do git clone https://github.com/mozuraa/claude-skill-$s.git ~/.claude/skills/$s; done
```

**3. Claude app / claude.ai:** open the skill's repository, click **Code → Download ZIP** and upload it in **Settings**, under **Skills** (in *Capabilities*).

Start a new session after installing.

### What is a skill?

A skill is a folder with a `SKILL.md` file: a name, a description of when it should be used, and instructions. Claude only reads the description until it becomes relevant; when a request matches, it loads the instructions and follows them.

### Principles

- **Quality over quantity:** few, well-thought-out answers backed by evidence.
- **Fixed format:** the same sections every time, easy to compare.
- **Honest opinions:** skills say what they'd do and why, but you decide.
- **Safe:** the doctors only examine your own projects and never attack anything.
- **Any language:** instructions are in Portuguese, but Claude replies in the language you write in.
- **Free:** MIT license.

### Feedback

Found a problem or have an idea for a skill? Open an issue in the skill's repository, or [here](https://github.com/mozuraa/claude-skills/issues) for new skill ideas.

---

## License

[MIT](LICENSE)
