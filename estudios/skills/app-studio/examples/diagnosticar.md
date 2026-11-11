# Exemplo de utilização — app-studio, modo Diagnosticar

> Exemplo ilustrativo, com uma app fictícia. Os relatórios reais dependem do que for encontrado — cada problema vem com a prova (linha de código, registo de crash, captura, medição).

---

## 1. Pedido

> vou enviar a minha app de receitas para a app store esta semana, podes ver se está tudo bem?

## 2. Consulta

O Claude vê na pasta um projeto SwiftUI só para iPhone e pergunta o que falta:

> Vou fazer um exame completo, com prioridade às regras da App Store e aos crashes. Duas perguntas antes:
>
> 1. **A app tem contas de utilizador ou compras?** Vejo código de login e de StoreKit — estão ativos nesta versão?
> 2. **Posso corrigir o que encontrar, ou preferes primeiro só o relatório?**

> **Utilizador:** sim tem login com google e uma subscrição premium. podes corrigir mas pergunta antes de coisas grandes

## 3. Exame (resumo do que foi feito)

- Build de release: 0 erros, 23 avisos.
- App corrida no simulador em **iPhone SE** e **iPhone 16 Pro Max**, em modo claro e escuro, com o **maior tamanho de texto**.
- Fluxos testados: primeiro arranque, login, criar receita, procurar, subscrição (sandbox), modo avião.
- Código, `Info.plist`, Privacy Manifest e compras revistos.

## 4. Relatório

# Relatório de saúde — Receitas da Avó (iOS, versão 1.0)

**Resumo:** A app está bem construída, mas **ainda não está pronta para enviar — faltam 4 coisas que levariam a uma rejeição quase certa**, e há um crash no iPhone SE. Tudo se resolve num dia.

| Área | Estado | Em resumo |
|---|---|---|
| Estabilidade | 🔴 | Crash ao abrir uma receita sem fotografia |
| Funcionamento | 🟢 | Fluxos principais funcionam |
| Layout | 🟠 | Botão "Guardar" tapado pelo teclado no iPhone SE; texto cortado com letra grande |
| Ícones e imagens | 🟡 | Sem variante escura do ícone |
| Desempenho | 🟡 | Fotografias mostradas em tamanho original (picos de 300 MB de memória) |
| Segurança | 🟠 | Token de sessão guardado em `UserDefaults` |
| Privacidade | 🔴 | Falta `PrivacyInfo.xcprivacy`; texto da câmara vago |
| Acessibilidade | 🟡 | Botões de ícone sem nome para o VoiceOver |
| Regras da App Store | 🔴 | Sem apagar conta, sem Iniciar sessão com a Apple, sem Restaurar compras |
| Compras | 🟠 | Estado "pendente" não tratado |

## 🔴 Crítico — resolver já

### 1. Crash ao abrir uma receita sem fotografia
- **O que é:** a app fecha sozinha quando se abre uma receita criada sem foto.
- **Onde:** `RecipeDetailView.swift:27` — `UIImage(data: recipe.photo!)`.
- **Porque importa:** crash garantido para quem não põe fotos; a Apple testa isto e rejeita (regra 2.1).
- **Como corrigir:** mostrar uma imagem de substituição quando não há foto, em vez de forçar com `!`.
- **Esforço:** Baixo.

### 2. Não é possível apagar a conta dentro da app
- **O que é:** a app deixa criar conta, mas não a apagar.
- **Onde:** `SettingsView.swift` — não existe a opção.
- **Porque importa:** obrigatório pela regra 5.1.1(v) — rejeição certa.
- **Como corrigir:** botão "Apagar conta" nas Definições, com confirmação, que apaga os dados também no servidor.
- **Esforço:** Médio.

### 3. Login com Google sem alternativa da Apple
- **Porque importa:** a regra 4.8 exige uma opção equivalente que proteja a privacidade, como Iniciar sessão com a Apple.
- **Esforço:** Médio.

### 4. Falta o Privacy Manifest
- **O que é:** a app usa `UserDefaults` (uma API de "razão obrigatória") mas não declara porquê.
- **Como corrigir:** criar `PrivacyInfo.xcprivacy` com a razão `CA92.1` e os dados recolhidos (email, para a conta).
- **Esforço:** Baixo.

### 5. Sem botão "Restaurar compras"
- **Porque importa:** obrigatório para subscrições (regra 3.1.1); quem muda de iPhone perde o Premium.
- **Esforço:** Baixo.

## 🟠 Importante
*(4 problemas: teclado a tapar o botão no iPhone SE, token em `UserDefaults` → Keychain, compra pendente não tratada, texto da permissão da câmara vago)*

## 🟡 Melhorias
*(5 melhorias: reduzir fotos antes de mostrar, nomes para o VoiceOver, variante escura do ícone, texto cortado com letra grande, 23 avisos do build)*

## 🟢 O que está bem
- Arquitetura limpa e fácil de seguir.
- Modo escuro impecável.
- Funciona bem em modo avião: as receitas guardadas continuam acessíveis.
- Subscrição verificada com StoreKit 2 (`VerificationResult`).

## 💬 A minha opinião

**Não enviaria esta semana sem corrigir os 5 críticos** — com eles, a rejeição é praticamente certa e perdes uma ou duas semanas em idas e voltas com a Apple. A boa notícia: 3 deles são correções de minutos, e os outros 2 (apagar conta e Iniciar sessão com a Apple) cabem num dia.

Os importantes eu fazia já também, sobretudo o **token no Keychain** e a **compra pendente**: são pequenos e evitam problemas difíceis de diagnosticar depois do lançamento. As melhorias podem ir na versão 1.0.1.

## ❓ Perguntas para ti
1. **Precisas mesmo do login com Google?** Se as receitas só ficam no telemóvel, podes tirar o login e resolver 2 críticos de uma vez (apagar conta e Apple). Se queres sincronizar entre dispositivos, mantemos e acrescento o Iniciar sessão com a Apple.
2. **Os dados das contas estão em que servidor?** Para o "Apagar conta" preciso de saber como apagar lá.

## 5. Decisão

> **Utilizador:** e se eu tirar só o google e deixar o login com email?

> **Claude:** Funciona para a regra 4.8 — com login só por email, a Apple não exige o Iniciar sessão com a Apple. Mas continua a ser preciso o **Apagar conta**. A minha opinião: o Iniciar sessão com a Apple dá-te mais registos (é um toque, sem palavra-passe) e não custa muito mais do que manter o Google. Se o objetivo é lançar esta semana, tirar o Google é o caminho mais rápido. Faço assim, e deixo o da Apple para a versão seguinte?
