# Lojas e entrega — TestFlight, App Store, Google Play e depois

Prepara tudo o que puderes e diz ao utilizador **exatamente** o que ele tem de fazer: criar contas, aceitar acordos, pagar e carregar nos botões finais de envio são ações dele. Nunca escrevas palavras-passe nem aceites termos por ele.

## Índice

- [1. Contas e identificadores](#1-contas-e-identificadores)
- [2. Versão, build e assinatura](#2-versão-build-e-assinatura)
- [3. Testes com pessoas reais](#3-testes-com-pessoas-reais)
- [4. Página da loja](#4-página-da-loja)
- [5. Privacidade, classificação e requisitos](#5-privacidade-classificação-e-requisitos)
- [6. Enviar para revisão](#6-enviar-para-revisão)
- [7. Se for rejeitada](#7-se-for-rejeitada)
- [8. Depois do lançamento](#8-depois-do-lançamento)
- [9. Entrega: COMO-ATUALIZAR.md](#9-entrega-como-atualizarmd)

---

## 1. Contas e identificadores

- **Apple Developer Program** (individual ou organização com D-U-N-S) e **App Store Connect**; aceitar os acordos (incluindo o de apps pagas, se houver compras) e preencher dados bancários e fiscais (pelo utilizador).
- **Google Play Console** (conta pessoal exige verificação de identidade; organização exige D-U-N-S).
- **Identificador da app** (bundle ID / applicationId) em formato de domínio invertido (ex.: `com.marca.app`). Definitivo depois de publicado — escolhe bem e confirma com o utilizador (há quem não queira o nome pessoal no identificador).
- **Nome da app**: único na App Store; pode ser diferente do nome no ecrã inicial.
- **URLs obrigatórias**: política de privacidade e suporte (um site simples serve — o website-studio faz isso).

## 2. Versão, build e assinatura

- **Versão** (ex.: 1.0.0) visível para o utilizador; **build** (1, 2, 3...) aumenta a cada envio.
- **iOS**: assinatura automática do Xcode com a equipa certa; *capabilities* (Game Center, iCloud, compras, notificações) ativadas no projeto e no portal. Arquivar: Product → Archive → Distribute App → App Store Connect. Em linha de comando: `xcodebuild archive` + `xcodebuild -exportArchive` com um `ExportOptions.plist` (método `app-store-connect`, destino `upload`).
- **Android**: Android App Bundle (`.aab`) assinado; **Play App Signing** (a Google guarda a chave de distribuição; o utilizador guarda a chave de upload em lugar seguro).
- **Expo**: `eas build --platform all` e `eas submit`.
- Configuração de **release**: sem servidores de teste, sem logs verbosos, símbolos de crash enviados (dSYM / mapping).

## 3. Testes com pessoas reais

- **TestFlight**: testadores internos (equipa, até 100, sem revisão) e externos (até 10 000, primeira build passa por uma revisão beta rápida). Escrever "O que testar".
- **Google Play**: teste interno (rápido, até 100) → teste fechado → produção. **Contas pessoais novas** têm de fazer um teste fechado com um número mínimo de testadores durante um período mínimo (regra introduzida em 2023 e ajustada desde então) antes de poderem publicar em produção — confirmar os valores atuais na Play Console.
- Pedir aos testadores: instalar de raiz, usar a tarefa principal, testar compras em sandbox, reportar com capturas.

## 4. Página da loja

**App Store (App Store Connect)**
- Nome (30 caracteres), subtítulo (30), palavras-chave (100, separadas por vírgulas, sem repetir palavras do nome), texto promocional (170, muda sem nova versão), descrição (4000).
- **Capturas**: obrigatórias para iPhone de 6,9" (ex.: 1320×2868) e para iPad de 13" se a app suportar iPad; até 10 por tamanho; as primeiras 3 são as que se veem — mostram o benefício com legendas curtas.
- Vídeo de pré-visualização opcional (até 30 s, gravado da app).
- Categoria principal e secundária; URL de suporte e de marketing.

**Google Play**
- Título (30), descrição curta (80), descrição completa (4000).
- Ícone 512×512, **imagem de destaque 1024×500**, pelo menos 2 capturas de telemóvel (e de tablet, se suportar).
- Categoria, contactos, política de privacidade.

**Dicas (ASO):** a palavra mais importante no nome/título; capturas que contam uma história; descrição que começa pelo benefício; traduzir a página para os países principais; responder a avaliações.

## 5. Privacidade, classificação e requisitos

- **App Store**: etiquetas "Privacidade da app" (o que a app e os SDKs recolhem, para quê, se está ligado à identidade, se rastreia) — têm de coincidir com o Privacy Manifest e com a realidade.
- **Google Play**: formulário **Data safety**; declaração de anúncios; público-alvo e conteúdo; acesso à app (credenciais de demonstração se houver login); classificação de conteúdo (questionário IARC).
- **Classificação etária** (questionário da Apple).
- **Exportação de criptografia**: `ITSAppUsesNonExemptEncryption = NO` no `Info.plist` se só usar HTTPS/criptografia do sistema.
- **UE**: estado de comerciante (Digital Services Act) declarado no App Store Connect para distribuir na UE (se for comerciante, os contactos ficam públicos — explicar ao utilizador).
- **Preço e disponibilidade**: países, preço (escalões da loja), data de lançamento.

## 6. Enviar para revisão

- **Notas para a revisão**: o que a app faz, como testar a funcionalidade principal, conta de demonstração (se houver login), explicação de funcionalidades menos óbvias (ex.: compras, permissões).
- **Opções de lançamento**: manual (o utilizador carrega em "Lançar" depois de aprovada), automático, ou **lançamento faseado** de 7 dias (App Store) / **lançamento gradual** por percentagem (Google Play) — recomendado para atualizações.
- Tempo típico de revisão: horas a 2 dias (Apple); horas a vários dias (Google, sobretudo contas novas).

## 7. Se for rejeitada

1. Lê a mensagem com o utilizador e identifica a regra citada (ex.: 2.1, 4.3, 5.1.1).
2. Usa o modo **🩺 Diagnosticar** (área 9 do checklist) para encontrar e corrigir a causa.
3. Responde no Centro de Resolução (Apple) / Play Console de forma educada e concreta: o que foi alterado, ou porque a app cumpre (com passos para o revisor ver).
4. Envia uma nova build se houve alterações.

## 8. Depois do lançamento

- **Crashes**: ver diariamente na primeira semana (Organizer, Android vitals, Sentry/Crashlytics); corrigir depressa.
- **Avaliações**: responder às negativas com soluções; pedir avaliação com o pedido do sistema depois de momentos positivos.
- **Atualizações**: pequenas e frequentes; notas de versão claras; aumentar sempre versão/build; manter a compatibilidade dos dados guardados.
- **Requisitos anuais**: novo SDK mínimo da Apple (versão do Xcode exigida) e novo *target API level* do Google Play — avisar o utilizador com antecedência.
- **Métricas**: transferências, conversão da página da loja, retenção dia 1/7/30, receita.

## 9. Entrega: COMO-ATUALIZAR.md

Cria na raiz do projeto, em linguagem simples:

1. **Onde está tudo**: projeto, App Store Connect, Play Console, serviços (Firebase, RevenueCat...) — links, sem palavras-passe.
2. **Fazer uma alteração e testar**: abrir o projeto, correr no simulador, onde estão os textos/níveis/preços.
3. **Publicar uma versão nova**: aumentar versão/build, arquivar/enviar (ou o comando do Expo), TestFlight, enviar para revisão, notas de versão.
4. **Custos e renovações**: conta Apple (anual), serviços, domínio.
5. **Antes de cada versão**: lista curta do modo Diagnosticar (crashes, ecrã pequeno/grande, modo escuro, texto grande, compras em sandbox, dados antigos continuam lá).
6. **Se algo correr mal**: como voltar atrás (remover da venda, lançar correção urgente, pausar lançamento gradual).
