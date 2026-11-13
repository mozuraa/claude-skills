# 💻 Windows — análise e limpeza (PowerShell)

## Nunca tocar (a não ser que o utilizador peça especificamente)

`C:\Windows`, `C:\Program Files`, `C:\Program Files (x86)`, `C:\ProgramData`, `C:\$Recycle.Bin` (só através da Reciclagem), `%USERPROFILE%\AppData` exceto as caches listadas abaixo, `Imagens`, `Música`, `Vídeos`, `OneDrive` (só se pedirem — apagar lá apaga na nuvem), ficheiros de paginação/hibernação, e qualquer repositório git com alterações por fazer commit ou push. Nada que exija privilégios de administrador sem o utilizador saber.

## 1. Espaço (só leitura)

```powershell
Get-PSDrive -PSProvider FileSystem | Select Name, @{n='Usado(GB)';e={[math]::Round($_.Used/1GB,1)}}, @{n='Livre(GB)';e={[math]::Round($_.Free/1GB,1)}}

# Pastas maiores na pasta pessoal
Get-ChildItem $env:USERPROFILE -Directory -Force -ErrorAction SilentlyContinue | ForEach-Object {
  $s = (Get-ChildItem $_.FullName -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum
  [pscustomobject]@{Pasta=$_.Name; GB=[math]::Round($s/1GB,2)} } | Sort GB -Descending | Select -First 20

# Ficheiros > 500 MB
Get-ChildItem $env:USERPROFILE -Recurse -File -Force -ErrorAction SilentlyContinue |
  Where Length -gt 500MB | Sort Length -Descending | Select -First 20 FullName, @{n='GB';e={[math]::Round($_.Length/1GB,2)}}
```

Estes varrimentos são pesados: começa pelas pastas prováveis e diz que pode demorar.

## 2. Lixo seguro

| O quê | Onde | Como limpar (depois de aprovado) |
|---|---|---|
| Temporários do utilizador | `$env:TEMP` | Reciclagem (ignora os ficheiros em uso) |
| npm | `%LOCALAPPDATA%\npm-cache` | `npm cache clean --force` |
| pnpm | `%LOCALAPPDATA%\pnpm\store` | `pnpm store prune` |
| yarn | `%LOCALAPPDATA%\Yarn\Cache` | `yarn cache clean` |
| pip | `%LOCALAPPDATA%\pip\Cache` | `pip cache purge` |
| Gradle | `%USERPROFILE%\.gradle\caches` | Reciclagem (Android Studio fechado) |
| NuGet | `%USERPROFILE%\.nuget\packages` | `dotnet nuget locals all --clear` |
| Visual Studio | `.vs`, `bin`, `obj` dentro dos projetos | Reciclagem |
| Reciclagem | — | `Clear-RecycleBin` = 🟡 sem volta, só com aprovação |
| Limpeza do sistema | — | sugere a ferramenta do Windows (Definições → Sistema → Armazenamento → Ficheiros temporários) em vez de apagar à mão |

**Pastas de projetos:**

```powershell
Get-ChildItem PASTA_DE_PROJETOS -Recurse -Directory -Force -ErrorAction SilentlyContinue |
  Where { $_.Name -in 'node_modules','.next','dist','build','target','.gradle','.venv','venv','__pycache__','bin','obj' } |
  Where { $_.FullName -notmatch '\\node_modules\\.+\\node_modules' }
```

## 3. Clones antigos que já estão no GitHub

Os mesmos testes do Mac (`git status --porcelain`, ahead, stashes, `git log --branches --not --remotes`, ficheiros ignorados). Só candidatos que passem tudo.

## 4. Duplicados

```powershell
Get-ChildItem PASTA -Recurse -File -ErrorAction SilentlyContinue | Where Length -gt 1MB |
  Group-Object Length | Where Count -gt 1 | ForEach-Object { $_.Group | Get-FileHash -Algorithm SHA256 } |
  Group-Object Hash | Where Count -gt 1
```

## 5. Downloads e Ambiente de Trabalho

`$env:USERPROFILE\Downloads` e `[Environment]::GetFolderPath('Desktop')` (pode estar dentro do OneDrive — avisa). Instaladores antigos (`.exe`, `.msi`), ZIPs já extraídos, e o resto por tipo/ano (`references/estrutura-pastas.md`).

## 6. Enviar para a Reciclagem (em vez de Remove-Item)

```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile('C:\caminho\ficheiro', 'OnlyErrorDialogs', 'SendToRecycleBin')
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory('C:\caminho\pasta', 'OnlyErrorDialogs', 'SendToRecycleBin')
```

`Remove-Item -Recurse` só para caches regeneráveis e depois de aprovado, sempre com caminhos completos verificados com `Test-Path`.
