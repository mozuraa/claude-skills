# 🗂️ Estrutura de pastas — propostas

Propõe, não imponhas. Mostra a árvore proposta, diz o que muda de sítio e quantos ficheiros, e pergunta. Adapta ao que o utilizador já tem — se ele já usa `~/Documents/Projetos`, não inventes outra.

## Projetos de código

```
~/Developer/                 (Mac — o Finder mostra-a com ícone próprio)   ·   C:\Users\<nome>\dev\  (Windows)
├── pessoal/                 projetos teus
│   ├── nome-do-projeto/
│   └── ...
├── clientes/                (se houver trabalho para outros)
├── estudos/                 tutoriais, cursos, experiências
├── forks/                   clones de projetos de outros
└── arquivo/                 parados, mas que queres manter localmente
```

**Porquê:** uma só raiz para todo o código facilita backups, pesquisas e limpezas; fora de pastas sincronizadas (iCloud Drive, OneDrive, Dropbox), porque sincronizar `node_modules` e `.git` é lento e dá conflitos.

**Avisos:**
- Mover um projeto pode partir caminhos absolutos (configurações do editor, atalhos, scripts, ambientes virtuais Python). Avisa e oferece mover um de cada vez.
- Projetos do Xcode e do Android Studio guardam caminhos recentes — reabrem a partir da nova pasta sem problema, mas a lista de recentes fica desatualizada.
- Nomes de pastas sem espaços nem acentos evitam problemas em ferramentas de linha de comandos (propõe, não renomeies sem pedir).

## Downloads

```
Downloads/
├── _ordenar/          o que chegou nos últimos 30 dias (fica como está)
├── Documentos/AAAA/   pdf, docx, xlsx, pptx, txt
├── Imagens/AAAA/      jpg, png, heic, gif, svg, webp
├── Vídeos/AAAA/       mp4, mov, mkv
├── Áudio/AAAA/        mp3, wav, m4a
├── Arquivos/AAAA/     zip, rar, 7z, tar.gz
└── Instaladores/      dmg, pkg, exe, msi  → propor Lixo os com mais de 30 dias
```

O ano é o da data de modificação. Ficheiros recentes ficam soltos — o utilizador ainda os está a usar.

## Ambiente de Trabalho

Proposta: deixar só o que está em uso esta semana; o resto vai para `Documentos/Do Ambiente de Trabalho/AAAA-MM/` (uma pasta por mês de arrumação), para nada se perder nem parecer que desapareceu. Capturas de ecrã → `Imagens/Capturas de ecrã/AAAA/` — e, no Mac, sugere mudar o destino das capturas (⌘⇧5 → Opções → Guardar em).

## Registo

Cada arrumação escreve um registo `clean-studio-registo-AAAA-MM-DD.txt` (na pasta arrumada) com `origem → destino` de cada ficheiro movido, para se poder desfazer.
