#!/usr/bin/env bash
# Copia cada skill do seu repositório individual para a pasta da categoria na biblioteca.
# Os repositórios individuais (claude-skill-<nome>) são a fonte; esta biblioteca guarda cópias organizadas.
#
# Uso (a partir da pasta da biblioteca, com os repositórios individuais na pasta ao lado):
#   ./scripts/sincronizar.sh
#
# Para acrescentar uma skill: junta uma linha "categoria nome" à lista abaixo.

set -euo pipefail

BIBLIOTECA="$(cd "$(dirname "$0")/.." && pwd)"
ORIGEM="${ORIGEM:-$(dirname "$BIBLIOTECA")}"

SKILLS="
ideias ideias-apps
ideias ideias-funcionalidades
ideias ideias-monetizacao
ideias brainstorming
criacao website-builder
programacao code-for-noobs
diagnostico website-doctor
diagnostico app-doctor
"

echo "$SKILLS" | while read -r categoria nome; do
  [ -z "${categoria:-}" ] && continue
  de="$ORIGEM/claude-skill-$nome"
  para="$BIBLIOTECA/$categoria/skills/$nome"
  if [ ! -f "$de/SKILL.md" ]; then
    echo "AVISO: não encontrei $de/SKILL.md — saltei $nome" >&2
    continue
  fi
  mkdir -p "$para"
  rsync -a --delete \
    --exclude '.git' --exclude 'README.md' --exclude 'LICENSE' --exclude 'CHANGELOG.md' --exclude '.DS_Store' \
    "$de/" "$para/"
  echo "ok  $categoria/skills/$nome"
done
