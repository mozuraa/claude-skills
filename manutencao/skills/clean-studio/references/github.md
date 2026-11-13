# 🐙 GitHub — comandos, critérios e segurança

Tudo com o `gh` (GitHub CLI). Se não estiver no PATH, procura-o (`~/.local/bin/gh`, `/opt/homebrew/bin/gh`, `C:\Program Files\GitHub CLI\gh.exe`). Se não existir, explica como instalar e pede autorização antes.

## 1. Inventário (só leitura)

```bash
gh auth status
gh repo list DONO --limit 1000 --json name,visibility,isFork,parent,isArchived,isEmpty,diskUsage,pushedAt,updatedAt,description,repositoryTopics,licenseInfo,defaultBranchRef,primaryLanguage
```

- **Último commit:** `pushedAt` (data do último push). Para a data exata do último commit do branch principal: `gh api repos/DONO/REPO/commits?per_page=1 --jq '.[0].commit.committer.date'`.
- **README:** `gh api repos/DONO/REPO/readme --silent` (erro 404 = não tem).
- **Tamanho:** `diskUsage` em KB.
- **Branches:** `gh api repos/DONO/REPO/branches --paginate --jq '.[].name'`.

Em contas com muitos repos, faz as chamadas por repo em sequência (não em paralelo) para não bater no limite da API; usa `gh api rate_limit` se falhar.

## 2. Critérios

| Achado | Como se deteta | Proposta | Risco |
|---|---|---|---|
| **Parado** | `pushedAt` mais antigo que o limite (12 meses por defeito) | arquivar | 🟢 |
| **Sem descrição / tópicos** | campos vazios | sugerir texto a partir do README e da linguagem | 🟢 |
| **Sem README** | 404 no `/readme` | sugerir um README curto | 🟢 |
| **Sem licença** (públicos) | `licenseInfo` nulo | perguntar qual (MIT sugerido para projetos pessoais abertos) | 🟢 |
| **Branch fundido** | ver §3 | apagar o branch | 🟡 |
| **Fork sem alterações** | §4 | apagar ou manter (é só uma cópia) | 🔴 se apagar |
| **Duplicado** | nomes parecidos (`app`, `app-v2`, `app-old`), mesma descrição, mesmo primeiro commit | manter um, arquivar o outro | 🟢 arquivar / 🔴 apagar |
| **Vazio** | `isEmpty` ou sem ficheiros | apagar ou dar-lhe uso | 🔴 se apagar |
| **Segredo exposto** | §5 | revogar + tirar do código + (opcional) limpar histórico | 🔴 para o histórico |

Não sugiras arquivar repos que são **página de downloads, site publicado ou dependência** de outro projeto só por estarem parados — diz que estão parados mas parecem ter função.

## 3. Branches já fundidos

```bash
gh api repos/DONO/REPO/compare/PRINCIPAL...BRANCH --jq '{ahead: .ahead_by, behind: .behind_by}'
```

`ahead_by == 0` → o branch não tem nada que o principal não tenha → está fundido. Também conta um branch cujo PR foi fundido (`gh pr list -R DONO/REPO --state merged --json headRefName`), mesmo com squash. Nunca proponhas apagar o branch principal, branches protegidos (`gh api repos/DONO/REPO/branches/BRANCH --jq .protected`) ou branches de deploy (`gh-pages`, `production`, `release*`) sem perguntar.

Apagar (🟡, depois de aprovado):
```bash
gh api -X DELETE repos/DONO/REPO/git/refs/heads/BRANCH
```
Guarda antes o SHA (`gh api repos/DONO/REPO/branches/BRANCH --jq .commit.sha`) no relatório — serve para o restaurar: `gh api -X POST repos/DONO/REPO/git/refs -f ref=refs/heads/BRANCH -f sha=SHA`.

## 4. Forks sem alterações

```bash
gh api repos/ORIGINAL_DONO/ORIGINAL/compare/BRANCH_ORIGINAL...DONO:BRANCH_FORK --jq '{ahead: .ahead_by}'
```

`ahead_by == 0` → o fork não tem commits teus. Diz isso e pergunta se o utilizador o quer manter (marcador, cópia de segurança) ou apagar. Os forks não ocupam espaço no computador — o único ganho de apagar é arrumação.

## 5. Segredos

**Onde procurar:** primeiro nos repos **públicos** (são os que importam mais); nos privados se o utilizador pedir. No estado atual e no histórico.

**Ferramentas, se existirem** (não instales sem perguntar): `gitleaks detect --source . --redact` ou `trufflehog git file://. --only-verified`. Usa sempre as opções que **escondem** o valor (`--redact`).

**Sem ferramentas:** clona em modo espelho para uma pasta temporária (`git clone --mirror`) e procura:

| Tipo | Padrão (ERE) |
|---|---|
| Ficheiros sensíveis | nomes `.env`, `.env.*` (exceto `.example`/`.sample`), `*.pem`, `*.p12`, `*.key`, `id_rsa`, `credentials.json`, `service-account*.json`, `*.keystore` |
| Chave privada | `-----BEGIN [A-Z ]*PRIVATE KEY-----` |
| AWS | `AKIA[0-9A-Z]{16}` |
| GitHub | `gh[pousr]_[A-Za-z0-9]{36,}` · `github_pat_[A-Za-z0-9_]{80,}` |
| Google API | `AIza[0-9A-Za-z_-]{35}` |
| Stripe | `sk_live_[0-9a-zA-Z]{24,}` · `rk_live_` |
| Slack | `xox[baprs]-[0-9A-Za-z-]{10,}` |
| Discord (bot) | `[A-Za-z0-9_-]{24,}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27,}` |
| OpenAI / Anthropic | `sk-[A-Za-z0-9]{20,}` · `sk-ant-[A-Za-z0-9_-]{20,}` |
| Genérico | `(api[_-]?key|secret|token|password)\s*[:=]\s*["'][^"']{12,}["']` (muitos falsos positivos — confirma) |

Estado atual: `git grep -nE -e 'PADRÃO'`. Histórico: `git log --all -p -G'PADRÃO' --format='%h %ad' --date=short` (com `grep`, passa sempre o padrão com `-e` — o da chave privada começa por `-----` e seria lido como opção) — **filtra a saída para mostrar só commit, ficheiro e linha, nunca o valor** (ex.: substitui o valor por `<oculto>` com `sed` antes de imprimir, ou usa só `grep -l` / `-c`).

**Relatório de um segredo:** repo · ficheiro · linha ou commit · tipo provável · público ou privado · desde quando. Nunca o valor, nem parcial.

**O que propor, por ordem:**
1. **Revogar/gerar novo no serviço** — é a única correção que funciona de verdade; quem fez um clone já tem o segredo. Só o utilizador o pode fazer: diz onde (ex.: Discord Developer Portal → Bot → Reset Token).
2. Tirar do código atual e pôr num ficheiro ignorado ou variável de ambiente 🟢 (commit normal).
3. Limpar do histórico 🔴 (`git filter-repo` ou recriar o histórico + force-push) — só com confirmação explícita para esse repo; avisa que o GitHub ainda serve os commits antigos pelo SHA até à limpeza dele e que forks e clones mantêm a cópia.

## 6. Executar (depois de aprovado)

```bash
gh repo archive DONO/REPO --yes                     # 🟢  desfazer: gh repo unarchive DONO/REPO --yes
gh repo edit DONO/REPO --description "..."          # 🟢
gh repo edit DONO/REPO --add-topic t1,t2            # 🟢
gh repo delete DONO/REPO --yes                      # 🔴  precisa do âmbito delete_repo; sem volta
```

Antes de apagar um repo (🔴), oferece uma cópia de segurança: `git clone --mirror` para uma pasta que o utilizador escolha. Se faltar o âmbito `delete_repo`, o utilizador corre `gh auth refresh -h github.com -s delete_repo` e aprova no browser; no fim, oferece retirá-lo (`gh auth refresh -h github.com --remove-scopes delete_repo`).
