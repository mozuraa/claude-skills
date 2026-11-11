# Tecnologia, dados, compras, serviços e custos

A regra: **a tecnologia que dá a melhor app para este utilizador e que ele consegue manter.** Explica a escolha numa frase e diz quanto custa. Preços e regras mudam — confirma no site do serviço antes de os prometer.

## Índice

- [Decisão rápida](#decisão-rápida)
- [Opções em detalhe](#opções-em-detalhe)
- [Jogos](#jogos)
- [Onde guardar os dados](#onde-guardar-os-dados)
- [Contas de utilizador](#contas-de-utilizador)
- [Compras e subscrições](#compras-e-subscrições)
- [Anúncios](#anúncios)
- [Estatísticas e registo de crashes](#estatísticas-e-registo-de-crashes)
- [Notificações](#notificações)
- [Custos típicos](#custos-típicos)

---

## Decisão rápida

| Situação | Recomendação |
|---|---|
| Só iPhone/iPad, tem Mac, quer a melhor experiência | **Swift + SwiftUI** (UIKit onde for preciso) |
| Só Android | **Kotlin + Jetpack Compose** |
| iPhone **e** Android com uma só base de código | **Flutter** ou **React Native com Expo** |
| Sabe JavaScript/React; quer compilar iOS sem Mac | **Expo** (EAS Build compila iOS na nuvem) |
| Jogo 2D só para Apple | **SpriteKit** |
| Jogo 2D/3D para iOS e Android | **Godot** (grátis, código aberto) ou **Unity** (verificar licença) |
| É basicamente conteúdo/informação, sem funções do telemóvel | Talvez **um site** (website-studio) e não uma app — diz isto |

## Opções em detalhe

**Swift + SwiftUI (iOS nativo)**
- ✅ A melhor integração com o sistema (widgets, Live Activities, Atalhos, iCloud, Game Center, acessibilidade), desempenho e aspeto nativos, ferramentas oficiais.
- ❌ Só plataformas Apple; precisa de Mac e Xcode.
- Criar: Xcode → New Project → App (SwiftUI). Testes: XCTest / Swift Testing.

**Kotlin + Jetpack Compose (Android nativo)**
- ✅ Melhor integração com Android e Material 3.
- ❌ Só Android. Android Studio (funciona em Mac, Windows, Linux).

**Flutter (Dart)**
- ✅ Uma base de código para iOS e Android (e web/desktop), interface consistente, bom desempenho, hot reload.
- ❌ A interface não é a nativa por defeito (desenha os próprios componentes); funcionalidades novas do sistema chegam mais tarde ou exigem código nativo. iOS continua a precisar de Mac para compilar localmente.
- Criar: `flutter create nome`.

**React Native + Expo (JavaScript/TypeScript)**
- ✅ Usa componentes nativos; muito bom para quem sabe React; Expo simplifica builds, atualizações e envio para as lojas (EAS Build/Submit), incluindo compilar iOS sem Mac.
- ❌ Algumas funcionalidades exigem módulos nativos; dependências para manter atualizadas.
- Criar: `npx create-expo-app@latest`.

**PWA (app web instalável)**
- ✅ Sem lojas, sem contas de programador, um só código.
- ❌ Fora das lojas (menos descoberta), limitações no iOS, sem compras na app. Boa para ferramentas internas ou testes de ideia.

## Jogos

- **SpriteKit**: 2D nativo Apple, física incluída, ótimo para jogos casuais; integra Game Center, SwiftUI e haptics facilmente.
- **Godot**: grátis e aberto, 2D excelente, exporta para iOS/Android/desktop; GDScript é fácil de aprender.
- **Unity**: o mais usado, 2D/3D, muitos recursos; confirmar o modelo de licença atual.
- Em qualquer motor: física simples e determinística quando possível (facilita verificar níveis), texturas em atlas, áudio com latência baixa, 60 fps estáveis no dispositivo mais fraco.

## Onde guardar os dados

| Necessidade | iOS | Android | Multiplataforma |
|---|---|---|---|
| Definições pequenas | `UserDefaults` / `@AppStorage` | DataStore | `shared_preferences` / MMKV |
| Dados da app (listas, registos, progresso) | **SwiftData** ou Core Data; ou ficheiros JSON `Codable` | **Room** | SQLite (`drift`, `sqflite`, `expo-sqlite`) |
| Segredos e tokens | **Keychain** | **Android Keystore** + armazenamento cifrado | `flutter_secure_storage` / `expo-secure-store` |
| Sincronizar entre dispositivos do mesmo utilizador | **CloudKit / iCloud** (grátis, sem servidor) | Backup / conta própria | Firebase, Supabase |
| Dados partilhados entre utilizadores | CloudKit (partilha) ou servidor | Servidor | **Firebase** (Firestore) ou **Supabase** (Postgres com RLS) |

Regras: **local primeiro** (funciona sem internet, privado, grátis); servidor só quando for mesmo preciso. Modelos de dados **versionados** desde o primeiro dia, para que atualizações nunca apaguem progresso. Com servidor: regras de acesso restritivas (Firestore rules, Supabase RLS) desde o início.

## Contas de utilizador

- Pergunta primeiro: **é mesmo preciso login?** Muitas apps funcionam melhor sem (e evitam as obrigações de apagar conta e de login com a Apple).
- Se for preciso: **Iniciar sessão com a Apple** (obrigatório oferecer uma opção equivalente se houver login com Google/Facebook), email com link mágico, ou Firebase/Supabase Auth.
- Obrigatório: **apagar conta dentro da app** (e por link web no Google Play).

## Compras e subscrições

- **iOS: StoreKit 2** (verificação de transações incluída, `Product`, `Transaction.updates`, restaurar com `AppStore.sync()`).
- **Android: Google Play Billing Library.**
- **Multiplataforma: RevenueCat** (gere iOS e Android, subscrições e análise; grátis até um valor de receita mensal) ou os plugins oficiais do Flutter/Expo.
- Conteúdo digital **tem de** ser vendido por compras na app. Comissão das lojas: normalmente 15% para pequenos programadores (programas para pequenas empresas) e 30% acima do limite — confirmar.
- Testar em sandbox (App Store) / testes de licença (Google Play), incluindo cancelamento, reembolso e renovação.

## Anúncios

- **AdMob** (Google) é o mais comum. No Espaço Económico Europeu exige consentimento (Google UMP). Anúncios personalizados no iOS exigem pedido App Tracking Transparency.
- Preferir anúncios com recompensa (o jogador escolhe ver) a anúncios intersticiais frequentes.
- Opinião a dar: anúncios rendem pouco com poucos utilizadores e pioram a experiência e a privacidade; muitas vezes uma compra única para remover anúncios ou desbloquear tudo é melhor.

## Estatísticas e registo de crashes

- **Crashes**: Xcode Organizer + MetricKit (iOS, grátis), Play Console → Android vitals (grátis), **Sentry** ou **Firebase Crashlytics** (multiplataforma).
- **Estatísticas de uso**: preferir soluções focadas em privacidade (TelemetryDeck, Aptabase) a SDKs de publicidade. Tudo o que recolher entra nas etiquetas de privacidade e no Privacy Manifest.

## Notificações

- APNs (iOS) e FCM (Android); Firebase Cloud Messaging ou OneSignal para os dois. Notificações locais (lembretes) não precisam de servidor.
- Pedir permissão só quando o utilizador percebe o benefício (ex.: ao criar o primeiro lembrete).

## Custos típicos

| Item | Valor indicativo |
|---|---|
| Apple Developer Program | ~99 €/ano (obrigatório para publicar na App Store e usar TestFlight) |
| Google Play Console | ~25 USD, uma vez |
| Mac (se não tiver) | qualquer Mac recente com a versão de Xcode exigida pela Apple |
| CloudKit | grátis dentro de limites generosos |
| Firebase / Supabase | grátis para começar; pago a partir de certo uso |
| RevenueCat | grátis até um limite de receita mensal |
| Expo EAS | plano gratuito com builds limitados; pago para mais |
| Domínio + site de suporte/privacidade | ~10–25 €/ano (as lojas exigem URL de suporte e de política de privacidade) |

Apresenta sempre ao utilizador uma tabela com **o que vai pagar, quanto e quando renova**.
