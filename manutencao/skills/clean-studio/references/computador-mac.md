# 💻 Mac — análise e limpeza

## Nunca tocar (a não ser que o utilizador peça especificamente)

`/System`, `/Library`, `/usr`, `/bin`, `/sbin`, `/private`, `/Applications` (apps só se o utilizador pedir para desinstalar), `~/Library` exceto as caches listadas abaixo, `~/Pictures` (Fotos), `~/Music`, `~/Movies`, `~/Library/Mobile Documents` (iCloud Drive), `~/Library/Mail`, `~/Library/Messages`, bases de dados de apps, e qualquer repositório git com alterações por fazer commit ou push.

O macOS pode bloquear a leitura de algumas pastas (Documentos, Ambiente de Trabalho, Downloads) sem "Acesso total ao disco" — se der "Operation not permitted", diz ao utilizador e salta essa pasta. Não tentes contornar.

## 1. Espaço (só leitura)

```bash
df -h /System/Volumes/Data                                 # total e livre (no macOS, "/" é só o volume do sistema)
du -xhd1 ~ 2>/dev/null | sort -hr | head -20               # pastas maiores na pasta pessoal
du -xhd1 ~/Library 2>/dev/null | sort -hr | head -10
find ~ -xdev -type f -size +500M 2>/dev/null -exec du -h {} + | sort -hr | head -20   # ficheiros > 500 MB
```

Corre o `du` sobre a pasta pessoal em segundo plano e com `nice` se demorar; começa pelas pastas prováveis.

## 2. Lixo seguro — caches e pastas regeneráveis

| O quê | Onde | Como medir | Como limpar (depois de aprovado) |
|---|---|---|---|
| Xcode DerivedData | `~/Library/Developer/Xcode/DerivedData` | `du -sh` | mover para o Lixo; o Xcode recria |
| Arquivos do Xcode | `~/Library/Developer/Xcode/Archives` | `du -sh` | ⚠️ contêm builds enviados para a App Store (dSYM) — só os antigos e com aprovação item a item |
| Suporte de dispositivos iOS | `~/Library/Developer/Xcode/iOS DeviceSupport` | `du -sh` | as versões antigas; o Xcode recria quando liga o iPhone |
| Simuladores indisponíveis | — | `xcrun simctl list devices unavailable` | `xcrun simctl delete unavailable` |
| Caches do CoreSimulator | `~/Library/Developer/CoreSimulator/Caches` | `du -sh` | Lixo |
| npm | `~/.npm/_cacache` | `du -sh` | `npm cache clean --force` |
| pnpm | `~/Library/pnpm/store` | `du -sh` | `pnpm store prune` |
| yarn | `~/Library/Caches/Yarn` | `du -sh` | `yarn cache clean` |
| pip | `~/Library/Caches/pip` | `du -sh` | `pip cache purge` (ou `python3 -m pip cache purge`) |
| Homebrew | `$(brew --cache)` | `du -sh` | `brew cleanup -s` |
| Gradle | `~/.gradle/caches` | `du -sh` | Lixo (só com o Android Studio fechado) |
| CocoaPods | `~/Library/Caches/CocoaPods` | `du -sh` | `pod cache clean --all` |
| Caches de apps | `~/Library/Caches/*` | `du -sh ~/Library/Caches/* \| sort -hr \| head` | só as de ferramentas de programação e browsers fechados; diz quais |
| Lixo | `~/.Trash` | `du -sh ~/.Trash` | esvaziar = 🟡 sem volta, só com aprovação |

**Pastas de projetos:**

```bash
find PASTA_DE_PROJETOS -type d \( -name node_modules -o -name .next -o -name dist -o -name build -o -name target -o -name .gradle -o -name Pods -o -name .venv -o -name venv -o -name __pycache__ \) -prune -print 2>/dev/null
```

Para cada uma, o tamanho e a data da última alteração do projeto. Propõe só as de projetos parados há mais de 3 meses (ou todas, se o utilizador quiser). Lembra que `npm install` / `pod install` as recriam. Não mexas em `build/` de projetos que não sejam de código (ex.: uma pasta chamada "build" com documentos).

## 3. Clones antigos que já estão no GitHub

Para cada pasta com `.git`:

```bash
git -C PASTA remote get-url origin                   # tem remoto no GitHub?
git -C PASTA status --porcelain                      # vazio = sem alterações por fazer commit
git -C PASTA fetch --quiet && git -C PASTA status -sb | head -1   # sem "ahead" = nada por fazer push
git -C PASTA stash list                              # vazio = sem stashes
git -C PASTA log --branches --not --remotes --oneline   # vazio = todos os branches locais estão no remoto
```

Só é candidato se passar **tudo**. Mesmo assim: ficheiros ignorados pelo git (ex.: `.env`, bases de dados locais, chaves) não estão no GitHub — lista-os com `git -C PASTA status --ignored --porcelain | grep '^!!'` e avisa antes de propor.

## 4. Duplicados

```bash
find PASTA -type f -size +1M -not -path '*/node_modules/*' -not -path '*/.git/*' 2>/dev/null \
  | while read -r f; do stat -f '%z %N' "$f"; done | sort -n | awk '...mesmo tamanho...'
shasum -a 256 FICHEIROS_COM_O_MESMO_TAMANHO
```

Primeiro agrupa por tamanho (rápido), depois confirma com hash só os grupos com mais de um. Ignora ficheiros < 1 MB por defeito. Fotografias e documentos: aprovação item a item.

## 5. Downloads e Ambiente de Trabalho

```bash
find ~/Downloads -maxdepth 1 -type f -mtime +90 | wc -l          # com mais de 90 dias
find ~/Downloads -maxdepth 1 -type f \( -name '*.dmg' -o -name '*.pkg' -o -name '*.zip' \) -exec du -h {} + | sort -hr
```

Proposta típica: instaladores (`.dmg`, `.pkg`) com mais de 30 dias → Lixo; ZIPs cuja pasta extraída existe ao lado → Lixo; o resto em subpastas por tipo e ano (`references/estrutura-pastas.md`). Nunca apagues capturas de ecrã ou documentos sem item a item.

## 6. Mover para o Lixo (em vez de rm)

```bash
osascript -e 'tell application "Finder" to delete POSIX file "/caminho/absoluto"'
```

Ou, se existir, o comando `trash` (macOS 15+ tem `/usr/bin/trash`). Vai para o Lixo e pode ser recuperado ("Pôr de volta"). Usa sempre caminhos absolutos e verifica que existem antes. `rm -rf` só para caches regeneráveis e só depois de aprovado — nunca com variáveis que possam ficar vazias.
