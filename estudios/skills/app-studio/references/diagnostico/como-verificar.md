# Como verificar — ferramentas e comandos

Formas concretas de verificar cada área do `checklist.md`. Usa o que estiver disponível: terminal, simulador/emulador, ferramentas de simulador do Claude, ou só o código. Se uma ferramenta não existir, usa a alternativa ou diz ao utilizador como verificar ele próprio (ex.: num dispositivo real).

Compilar e correr simuladores é pesado — num computador lento, faz um de cada vez e corre comandos longos em segundo plano.

## Índice

- [iOS (Xcode, Swift, SwiftUI)](#ios-xcode-swift-swiftui)
- [Android (Gradle, Kotlin, Compose)](#android-gradle-kotlin-compose)
- [Flutter](#flutter)
- [React Native / Expo](#react-native--expo)
- [Pesquisas no código (todas as plataformas)](#pesquisas-no-código-todas-as-plataformas)
- [Testes manuais que valem ouro](#testes-manuais-que-valem-ouro)

---

## iOS (Xcode, Swift, SwiftUI)

**Compilar e contar avisos**

```bash
xcodebuild -list                                   # esquemas disponíveis
xcodebuild -scheme ESQUEMA -destination 'generic/platform=iOS Simulator' -configuration Release build 2>&1 | grep -E "warning:|error:" | sort | uniq -c | sort -rn | head -30
```

**Testes**

```bash
xcodebuild test -scheme ESQUEMA -destination 'platform=iOS Simulator,name=iPhone 16'
```
(Usa um simulador que exista: `xcrun simctl list devices available`.)

**Definições importantes**

```bash
xcodebuild -scheme ESQUEMA -showBuildSettings 2>/dev/null | grep -E " (MARKETING_VERSION|CURRENT_PROJECT_VERSION|IPHONEOS_DEPLOYMENT_TARGET|PRODUCT_BUNDLE_IDENTIFIER|SWIFT_VERSION|SWIFT_STRICT_CONCURRENCY|TARGETED_DEVICE_FAMILY|INFOPLIST_FILE) ="
```

**Info.plist, permissões e privacidade**

```bash
plutil -p CAMINHO/Info.plist | grep -E "UsageDescription|NSAppTransportSecurity|NSAllowsArbitraryLoads|ITSAppUsesNonExemptEncryption|UIBackgroundModes|CFBundleURLTypes|UISupportedInterfaceOrientations"
find . -name "PrivacyInfo.xcprivacy" -not -path "*/DerivedData/*"
```
Projetos com `GENERATE_INFOPLIST_FILE` têm as chaves nas build settings (`INFOPLIST_KEY_NS...UsageDescription`). Confirma que cada API sensível usada tem texto, e que as APIs de razão obrigatória estão no Privacy Manifest:

```bash
grep -rnE "UserDefaults|\.creationDate|\.modificationDate|systemUptime|mach_absolute_time|volumeAvailableCapacity|activeInputModes" --include=*.swift . | grep -v "/DerivedData/" | head
```

**Simulador: ecrãs, modo escuro, texto grande, capturas**

```bash
xcrun simctl list devices available | grep -E "iPhone SE|Pro Max|iPad"
xcrun simctl boot "iPhone SE (3rd generation)"
xcrun simctl install booted CAMINHO/App.app
xcrun simctl launch booted BUNDLE_ID
xcrun simctl ui booted appearance dark                             # modo escuro (light para voltar)
xcrun simctl ui booted content_size accessibility-extra-extra-extra-large   # maior texto (large para voltar)
xcrun simctl status_bar booted override --time 9:41 --batteryState charged --batteryLevel 100
xcrun simctl io booted screenshot ~/Desktop/captura.png
xcrun simctl openurl booted "esquema://caminho"                   # testar deep links
xcrun simctl privacy booted reset all BUNDLE_ID                    # voltar a ver os pedidos de permissão
xcrun simctl spawn booted log stream --level error --predicate 'process == "NOME_DA_APP"'
```
O `.app` do simulador fica em `DerivedData/.../Build/Products/Debug-iphonesimulator/` (ou usa `-derivedDataPath build` no `xcodebuild`). Se o Claude tiver ferramentas de simulador (capturas, toques), usa-as para percorrer os ecrãs.

**Crashes**

- Registos de crash do simulador e do Mac: `~/Library/Logs/DiagnosticReports/` (ficheiros `.ips`).
- Dispositivos reais e utilizadores: Xcode → Window → Organizer → Crashes; App Store Connect → TestFlight → Crashes.
- Lê o registo até à primeira linha com o nome da app — é aí que está o problema.

**Desempenho e memória**

- Instruments (Xcode → Product → Profile): *Time Profiler* (lentidão), *Leaks* e *Allocations* (memória), *Hangs*, *Energy Log*.
- Em linha de comando: `xcrun xctrace record --template "Leaks" --device "NOME" --launch -- CAMINHO/App.app --time-limit 30s`.
- Tamanho: `du -sh CAMINHO/App.app`; o relatório de tamanho do App Store Connect mostra o tamanho real por dispositivo.

**SwiftLint** (se instalado): `swiftlint lint --quiet | head -50`.

## Android (Gradle, Kotlin, Compose)

```bash
./gradlew lint                  # relatório em app/build/reports/lint-results-*.html
./gradlew test                  # testes unitários
./gradlew assembleRelease       # build de release (avisos e erros do R8)
./gradlew dependencies --configuration releaseRuntimeClasspath | grep -E "\->" | head -30   # conflitos de versões
```

**Manifest e configuração**

```bash
grep -nE "debuggable|allowBackup|usesCleartextTraffic|networkSecurityConfig|exported=\"true\"|uses-permission|targetSdk|minSdk" app/src/main/AndroidManifest.xml
grep -nE "minSdk|targetSdk|compileSdk|versionCode|versionName|minifyEnabled|isMinifyEnabled|shrinkResources" app/build.gradle*
```

**Emulador / dispositivo**

```bash
adb devices
adb install -r app/build/outputs/apk/release/app-release.apk
adb shell cmd uimode night yes                     # modo escuro (no para voltar)
adb shell settings put system font_scale 2.0       # texto grande (1.0 para voltar)
adb shell wm size 720x1280; adb shell wm density 320   # simular ecrã pequeno (wm size reset; wm density reset)
adb exec-out screencap -p > captura.png
adb shell am start -a android.intent.action.VIEW -d "esquema://caminho"   # deep link
adb logcat *:E | grep -i NOME_DO_PACOTE
adb shell dumpsys gfxinfo NOME_DO_PACOTE             # fluidez (frames lentos)
```
Crashes e ANRs de utilizadores: Play Console → Android vitals. Perfis de desempenho: Android Studio Profiler.

## Flutter

```bash
flutter doctor
flutter analyze
flutter test
flutter pub outdated
flutter build ios --release --no-codesign   # ou: flutter build appbundle
```
Testar texto grande e modo escuro pelo simulador/emulador (comandos acima). Procurar `!` (null assertion) em dados externos e `setState` depois de `dispose`.

## React Native / Expo

```bash
npx tsc --noEmit                # erros de tipos (se TypeScript)
npx eslint . --ext .js,.jsx,.ts,.tsx
npm audit --omit=dev
npx expo-doctor                 # projetos Expo: configuração e versões compatíveis
npx expo config --type public   # ver a configuração final (permissões, plugins, ícones)
```
Verificar `app.json`/`app.config.js`: textos de permissões iOS (`ios.infoPlist`), permissões Android, `privacyManifests`. Procurar segredos em variáveis `EXPO_PUBLIC_*` (são públicas).

## Pesquisas no código (todas as plataformas)

**Segredos**

```bash
git grep -nIE '(sk_live_[0-9a-zA-Z]{10,}|rk_live_|AKIA[0-9A-Z]{16}|ghp_[0-9A-Za-z]{36}|github_pat_|xox[baprs]-|-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY|service_role|SUPABASE_SERVICE|client_secret|api[_-]?secret)'
git log -p --all | grep -nE 'sk_live_|AKIA[0-9A-Z]{16}|ghp_|PRIVATE KEY|service_role|client_secret' | head -20
```
Quando encontrares um segredo real, **não o repitas na resposta** — diz onde está e que tem de ser revogado e substituído.

**Armazenamento inseguro de dados sensíveis**

```bash
grep -rnEi "(UserDefaults|SharedPreferences|AsyncStorage|localStorage).{0,80}(token|password|senha|secret|pin|cartao|card)" --include=*.swift --include=*.kt --include=*.java --include=*.dart --include=*.ts --include=*.tsx --include=*.js . | head
```

**Pontos de crash prováveis**

```bash
grep -rnE "try!|as! |fatalError\(|\.first!|\.last!|URL\(string: [^\"]" --include=*.swift . | grep -v Tests | head -40     # iOS
grep -rnE "!!" --include=*.kt . | grep -v test | head -40                                                                 # Android
```
Nem todos são erros (um `URL(string: "https://fixo")!` com texto fixo é seguro) — confirma cada um.

**Logs com dados sensíveis**

```bash
grep -rnEi "(print|NSLog|os_log|Log\.[dviwe]|console\.log|debugPrint)\(.{0,60}(token|password|email|senha)" . --include=*.swift --include=*.kt --include=*.java --include=*.dart --include=*.ts --include=*.js | head
```

**Textos fixos fora das traduções** (SwiftUI): `grep -rnE 'Text\("[A-Za-zÀ-ú]' --include=*.swift . | head` — em SwiftUI, `Text("...")` com texto literal é traduzível pelo String Catalog, mas texto em variáveis `String` não é; confirma caso a caso.

## Testes manuais que valem ouro

Faz (ou pede ao utilizador para fazer num dispositivo real) estes testes, que apanham a maioria dos problemas:

1. **Instalação limpa** → percorrer o onboarding → usar a funcionalidade principal.
2. **Atualização** a partir da versão publicada anterior → os dados continuam lá?
3. **Modo avião** a meio de uma ação.
4. **Recusar todas as permissões** e usar a app.
5. **Maior tamanho de texto + modo escuro + iPhone SE** (ou Android pequeno).
6. **Fechar a app** a meio de uma tarefa (gesto de multitarefa) e reabrir.
7. **Comprar, cancelar, restaurar** (em sandbox).
8. **VoiceOver/TalkBack ligado**: consegues completar a tarefa principal de olhos fechados?
9. **Rodar o ecrã** em todos os ecrãs principais.
10. **Deixar a app em segundo plano 10 minutos** e voltar.
