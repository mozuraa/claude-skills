# Modelo — tarefa para um agente (Claude Code, Cursor, Codex, Copilot...)

Os comentários `<!-- -->` são para ti — apaga-os antes de usar.

---

```markdown
<!-- OBJETIVO E PORQUÊ -->
[O que fazer], para [razão / quem beneficia].

<!-- CONTEXTO -->
## Contexto
- Projeto: [o que é, linguagem, framework].
- Ficheiros relevantes: `[caminho]` ([o que tem]), `[caminho]`.
- Convenções a seguir: [ex.: componentes em `src/components`, testes ao lado do ficheiro].
- Decisões já tomadas: [ex.: usar a biblioteca X que já está no projeto].

<!-- LIMITES -->
## Limites
- Não alteres [ficheiros/áreas], porque [razão].
- Não adiciones dependências novas sem perguntar.
- [Pode / não pode] fazer commits. [Pode / não pode] apagar ficheiros.
- Se encontrares algo fora do âmbito que devia ser corrigido, anota no relatório em vez de corrigir.

<!-- PLANO PRIMEIRO (tarefas grandes) -->
Antes de escrever código, mostra-me um plano curto (ficheiros a mudar e porquê) e espera pela minha aprovação.

<!-- DEFINIÇÃO DE FEITO -->
## Está feito quando
- [ ] [critério verificável]
- [ ] [critério verificável]
- [ ] Os testes existentes continuam a passar.

<!-- COMO VERIFICAR -->
## Como verificar
- `[comando de testes]`
- `[comando de build/lint]`
- [verificação manual: abrir X, fazer Y, ver Z]

Resolve a causa dos problemas; não alteres testes só para passarem nem cries casos especiais para os testes.

<!-- RELATÓRIO -->
## No fim, diz-me
- O que mudou (ficheiros e porquê).
- O que testaste e o resultado.
- O que ficou por fazer ou o que te deixou dúvidas.
```

---

**Ficheiro de instruções permanentes** (`CLAUDE.md`, `AGENTS.md`, regras do Cursor) — esqueleto curto:

```markdown
# [Projeto]

[O que é, numa frase.]

## Comandos
- Correr: `...`
- Testes: `...`
- Lint/formatação: `...`

## Convenções
- [regra] — [porquê]

## Armadilhas conhecidas
- [o que costuma correr mal e como evitar]
```
