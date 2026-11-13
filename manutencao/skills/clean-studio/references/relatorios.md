# 📋 Modelos de relatório

## Relatório e plano (antes de fazer qualquer coisa)

```markdown
# 🔎 Relatório — [GitHub: conta X / Computador: Mac de Y]

**Resumo:** 2–3 frases. Ex.: "Tens 38 repos: 6 parados há mais de 12 meses, 13 forks sem alterações e 1 segredo exposto num repo público. No disco tens 18 GB livres de 245 GB; consigo libertar ~31 GB sem risco."

| | Encontrado | Quantos | Espaço |
|---|---|---|---|
| ... | ... | ... | ... |

## ⚠️ Alertas (resolver primeiro)
- Segredos: repo · ficheiro · linha/commit · tipo — nunca o valor.

## 📋 Plano proposto

### 🟢 Reversível — pode ser aprovado em grupo
| # | Ação | Itens | Liberta | Como desfazer |
|---|---|---|---|---|

### 🟡 Difícil de desfazer — aprovação por grupo
| # | Ação | Itens | Liberta | Porque é seguro |

### 🔴 Sem volta — aprovação item a item
| # | Ação | Item | Porquê | Cópia de segurança proposta |

## 🟢 O que está bem / o que não vou tocar
## 💬 A minha opinião
O que eu faria primeiro e o que não vale a pena.

## ✋ Como queres avançar?
(a) todo o 🟢 agora, 🟡 e 🔴 um a um — recomendado  (b) escolher por número  (c) só o relatório
```

## Relatório final (depois de executar)

```markdown
# ✅ Feito

**Espaço livre:** 18,2 GB → 49,6 GB (+31,4 GB)  ·  **Repos:** 6 arquivados, 9 descrições completadas, 14 branches apagados

| Ação | Resultado | Como desfazer |
|---|---|---|

**No Lixo/Reciclagem:** X GB — fica lá até o esvaziares (podes recuperar com "Pôr de volta").
**Registo das mudanças:** caminho do ficheiro de registo.
**Não fiz:** o que ficou por aprovar ou falhou, e porquê.
**O que tens de fazer tu:** ex.: revogar o token no serviço X.
**Próxima arrumação:** sugestão de quando repetir.
```
