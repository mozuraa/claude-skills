# Exemplo — clean-studio, modo 💻 Computador (Mac)

> Exemplo ilustrativo. Mostra o relatório e plano — o momento em que o utilizador decide.

## Pedido

> o disco está quase cheio, liberta espaço

## Perguntas

> Antes de procurar:
> 1. **Objetivo:** (a) libertar espaço — recomendado (b) arrumar pastas (c) as duas
> 2. **Onde estão os teus projetos?** Encontrei `~/Developer` e `~/Documents/Projetos` — (a) as duas (b) só uma
> 3. **Posso incluir caches de programação** (npm, Xcode, simuladores)? Voltam a ser criadas quando precisas. (a) sim — recomendado (b) não

> **Utilizador:** a, a, a

## 📋 Relatório e plano

**Resumo:** Tens 14 GB livres de 245 GB (6%) — o Mac começa a ficar lento abaixo de ~10%. Consigo libertar **~41 GB sem risco** (tudo regenerável ou para o Lixo).

| | Encontrado | Espaço |
|---|---|---|
| Simuladores iOS antigos e indisponíveis | 9 | 18,4 GB |
| Xcode DerivedData + iOS DeviceSupport antigos | — | 9,1 GB |
| `node_modules` de projetos parados há > 3 meses | 7 | 6,2 GB |
| Caches npm, pip, Homebrew | — | 4,3 GB |
| Instaladores `.dmg` em Downloads com > 30 dias | 11 | 3,0 GB |

### 🟢 Reversível / regenerável — aprovação em grupo
| # | Ação | Liberta | Como desfazer |
|---|---|---|---|
| 1 | `xcrun simctl delete unavailable` + simuladores de iOS < 17 | 18,4 GB | o Xcode volta a descarregá-los |
| 2 | DerivedData e DeviceSupport antigos → Lixo | 9,1 GB | recriados no próximo build |
| 3 | `node_modules` dos 7 projetos parados → Lixo | 6,2 GB | `npm install` |
| 4 | `npm cache clean`, `pip cache purge`, `brew cleanup` | 4,3 GB | recriadas sozinhas |
| 5 | 11 instaladores `.dmg` → Lixo | 3,0 GB | "Pôr de volta" no Lixo |

### 🟡 Difícil de desfazer
| 6 | Esvaziar o Lixo no fim | (só então o espaço aparece) | sem volta |

### 🟢 O que não vou tocar
- `~/Developer/loja-online` tem 3 ficheiros por fazer commit — fica como está.
- `~/Pictures` (34 GB) é a fototeca — fora do âmbito.

### 💬 A minha opinião
Os simuladores são a vitória fácil: 18 GB e não perdes nada. Faria 1–5 já e esvaziava o Lixo daqui a uns dias, quando tiveres a certeza.

### ✋ Como queres avançar?
(a) 1–5 agora, o 6 depois — recomendado (b) escolher por número (c) só o relatório
