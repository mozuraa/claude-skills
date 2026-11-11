# Checklist completo — aplicações

Tudo o que examinar numa app. Cada item diz **o que verificar** e, quando útil, **o valor certo**. Os comandos estão em `como-verificar.md`. Itens marcados **[iOS]** ou **[Android]** aplicam-se só a essa plataforma; o resto aplica-se a todas (incluindo Flutter e React Native, que geram apps iOS e Android). Salta o que não faz sentido (uma app sem compras não tem a secção 11) e diz que saltaste.

## Índice

1. [Estabilidade](#1-estabilidade)
2. [Funcionamento, textos e idiomas](#2-funcionamento-textos-e-idiomas)
3. [Layout e alinhamentos](#3-layout-e-alinhamentos)
4. [Ícones, imagens e assets](#4-ícones-imagens-e-assets)
5. [Desempenho e bateria](#5-desempenho-e-bateria)
6. [Segurança](#6-segurança)
7. [Privacidade](#7-privacidade)
8. [Acessibilidade](#8-acessibilidade)
9. [Regras das lojas](#9-regras-das-lojas)
10. [Rede, offline e dados](#10-rede-offline-e-dados)
11. [Compras e monetização](#11-compras-e-monetização)
12. [Build, configuração e código](#12-build-configuração-e-código)

---

## 1. Estabilidade

- [ ] Sem crashes conhecidos (Xcode Organizer, App Store Connect, Play Console → Android vitals, Crashlytics/Sentry).
- [ ] **[iOS]** Sem desembrulhos forçados em dados que podem faltar: `!` em opcionais vindos de rede, ficheiros, `UserDefaults`, `URL(string:)!` com texto variável, `try!`, `as!`, `.first!`, `fatalError` em caminhos alcançáveis.
- [ ] **[Android]** Sem `!!` em valores que podem ser nulos; `lateinit` inicializado antes de usar.
- [ ] Sem acessos a listas fora dos limites (`array[i]` sem verificar), divisões por zero, conversões de texto para número sem tratar falha.
- [ ] Interface atualizada só na thread principal; trabalho pesado fora dela.
- [ ] Concorrência sem condições de corrida (Swift 6 / *strict concurrency* sem avisos; coroutines com o dispatcher certo).
- [ ] Erros tratados com mensagem ao utilizador — não engolidos em silêncio, não a rebentar a app.
- [ ] **[Android]** Sem ANRs (app parada > 5 s); a app sobrevive à rotação e à destruição da Activity pelo sistema sem perder estado.
- [ ] **React Native/Flutter**: sem promessas rejeitadas não tratadas; *error boundary* / `FlutterError.onError` configurados.
- [ ] A app recupera quando é fechada pelo sistema a meio de uma tarefa e quando volta do segundo plano.
- [ ] Ferramenta de registo de crashes ativa em produção, com símbolos (dSYM / mapping do R8) enviados.

## 2. Funcionamento, textos e idiomas

- [ ] Todos os fluxos principais funcionam de ponta a ponta (registo, login, criar/editar/apagar, comprar, partilhar, definições).
- [ ] Primeiro arranque (onboarding) e atualização a partir da versão anterior funcionam — dados antigos mantêm-se.
- [ ] Definições e progresso guardam-se e sobrevivem a fechar e reabrir a app.
- [ ] Terminar sessão limpa os dados privados da conta anterior.
- [ ] Deep links / Universal Links / App Links abrem o ecrã certo, também com a app fechada.
- [ ] Notificações chegam, abrem o ecrã certo, e a app funciona bem se forem recusadas.
- [ ] Widgets, extensões, atalhos, partilha (*share sheet*) — se existirem — funcionam.
- [ ] **[Android]** Botão/gesto "voltar" faz sempre o esperado (incluindo *predictive back*).
- [ ] Botões sem efeito, ecrãs sem saída, links para páginas que não existem: nenhum.
- [ ] Nenhum texto fixo no código fora do sistema de traduções; todas as línguas completas, sem mistura.
- [ ] Plurais corretos ("1 moeda" / "2 moedas"); datas, horas, números e moedas no formato do país (`DateFormatter`/`NumberFormatter`, `Intl`), vírgula decimal em português.
- [ ] Textos de permissões e do `Info.plist` também traduzidos (**[iOS]** `InfoPlist.strings` / String Catalog).
- [ ] Sem texto de exemplo esquecido ("Lorem ipsum", "TODO", "Test", dados falsos).
- [ ] Mudança de fuso horário, de dia (meia-noite) e de idioma do sistema não partem nada.

## 3. Layout e alinhamentos

- [ ] Testado no **ecrã mais pequeno suportado** (ex.: iPhone SE 375×667 pt; Android 360×640 dp) e no **maior** (Pro Max; tablets se suportados).
- [ ] **[iOS]** iPad, se a app o suporta: Split View, Slide Over, Stage Manager, rotação. Se não suporta iPad, confirmar que corre bem em modo de compatibilidade.
- [ ] **[Android]** Ecrãs dobráveis e tablets, janelas redimensionáveis (Android 16 obriga apps a adaptar-se a ecrãs grandes).
- [ ] Áreas seguras respeitadas: notch/Dynamic Island, indicador de início, barras de sistema; nada cortado nem tapado. Fundos podem ir até às bordas, conteúdo não.
- [ ] **[Android]** *Edge-to-edge* (obrigatório a partir do Android 15) tratado com *insets*.
- [ ] Rotação: suportada e correta, ou bloqueada de propósito.
- [ ] Teclado não tapa o campo onde se escreve nem o botão de enviar; fecha ao tocar fora/ao enviar.
- [ ] **Texto grande**: no maior tamanho (incluindo os tamanhos de acessibilidade) o texto não é cortado nem sobreposto — quebra de linha ou scroll.
- [ ] **Modo escuro**: todas as cores adaptam-se; sem texto preto em fundo escuro; imagens e logos visíveis; se a app só tem um modo, isso é intencional.
- [ ] Traduções longas (alemão +30%) não partem botões nem títulos; RTL (árabe, hebraico) correto, se a app tiver essas línguas.
- [ ] Alinhamentos numa grelha consistente; margens iguais; espaçamentos de uma escala (4/8/16/24...).
- [ ] Conteúdo que pode crescer está dentro de scroll.
- [ ] Estados vazios, de carregamento e de erro desenhados (não ecrãs em branco).
- [ ] Ecrã de arranque igual ao primeiro ecrã da app (sem "salto").
- [ ] Sem tamanhos fixos que só funcionam num modelo de telefone.

## 4. Ícones, imagens e assets

- [ ] **[iOS]** Ícone 1024×1024 sem transparência nem cantos arredondados; variantes escura e tingida (iOS 18+) se quiser um aspeto cuidado.
- [ ] **[Android]** Ícone adaptativo (primeiro plano + fundo) e ícone monocromático para ícones temáticos (Android 13+); ícone da Play Store 512×512.
- [ ] Ícones da interface em vetor (SF Symbols, PDF/SVG vetorial, Material Symbols) ou em todas as densidades (@2x/@3x; mdpi→xxxhdpi).
- [ ] Imagens comprimidas e no tamanho certo; fotografias grandes **reduzidas antes de mostrar** (uma imagem 4000×3000 descomprimida ocupa ~48 MB de memória).
- [ ] Sem assets não usados a aumentar o tamanho da app.
- [ ] Imagens nítidas (nada esticado ou pixelizado) e sem deformações (proporção mantida).
- [ ] Capturas de ecrã da loja nos tamanhos exigidos, atuais e fiéis à app (App Store: iPhone 6,9" obrigatório; iPad 13" se suporta iPad).
- [ ] Imagens e sons com licença para uso comercial.

## 5. Desempenho e bateria

- [ ] Arranque rápido: primeiro ecrã útil em ≲ 1 s em dispositivo recente; nada pesado no arranque (rede, bases de dados grandes, SDKs desnecessários) antes do primeiro ecrã.
- [ ] Sem bloqueios da interface (*hangs*): nenhuma operação > 100–250 ms na thread principal (ficheiros, JSON grande, imagens, base de dados).
- [ ] Scroll e animações fluidos (60/120 fps); listas longas com reutilização de células (`List`/`LazyVStack`, `RecyclerView`/`LazyColumn`, `FlatList`).
- [ ] **SwiftUI**: corpos de vista leves, sem trabalho caro no `body`; **Compose**: sem recomposições excessivas.
- [ ] Sem fugas de memória (ciclos de referência em closures — `[weak self]`; observadores e timers removidos); memória estável ao entrar e sair dos ecrãs repetidamente.
- [ ] Rede eficiente: sem pedidos repetidos, com cache; imagens descarregadas no tamanho certo.
- [ ] Bateria: localização com a precisão mínima necessária e parada quando não é precisa; sem timers/sensores ativos em segundo plano; trabalho em segundo plano com as APIs do sistema (BGTaskScheduler, WorkManager).
- [ ] Jogos (SpriteKit, etc.): número de nós e texturas controlado; texturas em atlas; física só onde é precisa; FPS estável no dispositivo mais fraco suportado.
- [ ] Tamanho da app razoável (iOS avisa acima de 200 MB em dados móveis); recursos grandes descarregados à parte se possível.

## 6. Segurança

- [ ] **Nenhum segredo dentro da app** (chaves secretas de APIs, chaves de servidor, `service_role`, palavras-passe): qualquer pessoa pode extrair o pacote da app. Chaves secretas vivem num servidor. (Chaves "públicas" de cliente — ex.: chave anónima do Supabase com RLS, chave do Firebase com regras — são aceitáveis.)
- [ ] Tokens e dados sensíveis guardados no **Keychain** **[iOS]** / **Android Keystore** com armazenamento cifrado **[Android]** — nunca em `UserDefaults`, `SharedPreferences`, `AsyncStorage` ou ficheiros simples.
- [ ] Toda a comunicação por HTTPS. **[iOS]** sem `NSAllowsArbitraryLoads` no App Transport Security; **[Android]** `usesCleartextTraffic="false"` / network security config sem texto claro.
- [ ] Registos (logs) de produção sem tokens, palavras-passe ou dados pessoais.
- [ ] Deep links e notificações validam os parâmetros; nenhuma ação sensível (pagar, apagar) executada só por abrir um link, sem confirmação.
- [ ] WebViews: só carregam domínios próprios/confiáveis; pontes JavaScript↔nativo não expostas a conteúdo externo.
- [ ] Compras verificadas: **[iOS]** StoreKit 2 `VerificationResult` verificado (ou validação no servidor para conteúdo valioso); **[Android]** compras verificadas e *acknowledged* — nunca confiar só numa variável local "comprado = true".
- [ ] Regras do backend (Firestore rules, Supabase RLS, permissões da API) impedem um utilizador de ler ou alterar dados de outro.
- [ ] **[Android]** `android:debuggable` falso em release; componentes `exported="true"` só quando necessário e protegidos; `allowBackup` desligado ou com regras para dados sensíveis; R8/ProGuard ativo; `FileProvider` para partilhar ficheiros.
- [ ] Ecrãs sensíveis (dados bancários, saúde) escondidos na pré-visualização do multitarefa, se relevante.
- [ ] A app não lê a área de transferência sem razão (o iOS mostra um aviso ao utilizador).
- [ ] Dependências sem vulnerabilidades conhecidas e atualizadas (Swift Packages, CocoaPods, Gradle, npm, pub).
- [ ] Autenticação: sessão expira e renova; terminar sessão invalida o token também no servidor.

## 7. Privacidade

- [ ] **Inventário** de tudo o que recolhe dados: analytics, crashes, anúncios, login social, mapas, SDKs de terceiros — e o que cada um recolhe.
- [ ] Permissões pedidas **só quando necessárias e no momento em que fazem sentido** (não todas no arranque), com explicação antes do pedido do sistema.
- [ ] **[iOS]** Cada permissão usada tem o texto de explicação no `Info.plist` (`NSCameraUsageDescription`, `NSPhotoLibraryUsageDescription`, `NSLocationWhenInUseUsageDescription`...), claro e verdadeiro — texto vago é motivo de rejeição.
- [ ] Usa as alternativas que não pedem permissão quando chegam: seletor de fotos do sistema (PHPicker / Android Photo Picker), localização aproximada.
- [ ] A app funciona (o melhor possível) quando uma permissão é recusada, e explica como a ativar nas Definições.
- [ ] **[iOS]** **Privacy Manifest** (`PrivacyInfo.xcprivacy`) presente, com as **APIs de razão obrigatória** usadas declaradas (ex.: `UserDefaults` → `CA92.1`; datas de ficheiros; tempo desde o arranque; espaço em disco) e os tipos de dados recolhidos; SDKs de terceiros com o seu próprio manifest.
- [ ] **[iOS]** Etiquetas de privacidade ("Privacidade da app") no App Store Connect coincidem com o que a app e os SDKs realmente recolhem.
- [ ] **[iOS]** Se há rastreio entre apps/sites (anúncios personalizados, IDFA, partilha com corretores de dados): pedido **App Tracking Transparency** antes de rastrear, e nada de rastreio se recusado.
- [ ] **[Android]** Secção **Data safety** da Play Console preenchida e verdadeira; permissões sensíveis (localização em segundo plano, SMS, todos os ficheiros) justificadas ou removidas.
- [ ] **[Android 13+]** Pedido de permissão de notificações (`POST_NOTIFICATIONS`).
- [ ] Política de privacidade com link na loja **e** dentro da app, coerente com a realidade.
- [ ] **Apagar conta dentro da app**, se a app permite criar conta (obrigatório na App Store e no Google Play — no Google Play também por link web).
- [ ] UE/RGPD: consentimento antes de anúncios personalizados/analytics não essenciais (ex.: Google UMP para AdMob no Espaço Económico Europeu); dados mínimos; direito de acesso e apagamento.
- [ ] Crianças: se o público inclui menores, regras da categoria Crianças (App Store) / política Famílias (Google Play) — sem anúncios personalizados nem SDKs de rastreio.

## 8. Acessibilidade

- [ ] **VoiceOver / TalkBack**: todos os botões e ícones têm nome que faz sentido ("Fechar", não "botão" ou "x.circle"); ordem de leitura lógica; imagens decorativas ignoradas.
- [ ] Elementos agrupados quando faz sentido (ex.: cartão lido de uma vez); controlos personalizados com o tipo certo (botão, ajustável...).
- [ ] **Texto dinâmico / tamanho de letra do sistema** suportado até aos tamanhos de acessibilidade (ver secção 3).
- [ ] Contraste de texto ≥ 4,5:1 (grande ≥ 3:1), também no modo escuro.
- [ ] Alvos de toque ≥ **44×44 pt** **[iOS]** / **48×48 dp** **[Android]**.
- [ ] Informação não transmitida só por cor; sons e vibração não são o único aviso.
- [ ] **Reduzir movimento** respeitado (sem animações grandes, parallax ou tremores).
- [ ] Vídeos com legendas.
- [ ] Teclado físico / acesso por comutador funcionam no iPad e em Android, se relevante.
- [ ] Apps de comércio, bancos, transportes e comunicações na UE: obrigatório pela Lei Europeia da Acessibilidade (desde junho de 2025).

## 9. Regras das lojas

**App Store (motivos de rejeição mais comuns)**
- [ ] 2.1 — App completa: sem crashes, sem conteúdo de exemplo, sem links partidos; **conta de demonstração** nas notas para a revisão se houver login.
- [ ] 2.3 — Metadados fiéis: nome, descrição, capturas e palavras-chave correspondem à app; sem referências a outras plataformas ("também no Android").
- [ ] 3.1.1 — Conteúdo digital (moedas, níveis, subscrições, remover anúncios) vendido **só por compras na app**; botão **Restaurar compras** para não consumíveis e subscrições.
- [ ] 3.1.2 — Subscrições: preço, duração e o que inclui claros antes de comprar; links para Termos (EULA) e Política de Privacidade na app e nos metadados.
- [ ] 4.2 — Funcionalidade mínima: não pode ser só um site embrulhado ou uma app vazia.
- [ ] 4.3 — Não ser uma cópia de outra app (incluindo das próprias).
- [ ] 4.8 — Login com Google/Facebook exige também uma opção equivalente que proteja a privacidade (ex.: Iniciar sessão com a Apple).
- [ ] 5.1.1 — Textos de permissões, política de privacidade, apagar conta (ver secção 7).
- [ ] 5.1.2 — Rastreio só com App Tracking Transparency.
- [ ] Classificação etária atualizada (questionário com as categorias 13+, 16+, 18+).
- [ ] `ITSAppUsesNonExemptEncryption` definido no `Info.plist` (evita a pergunta de exportação em cada build).
- [ ] UE: estado de **comerciante** (Digital Services Act) declarado no App Store Connect para distribuir na UE.
- [ ] Nome na loja disponível e diferente de marcas de terceiros.

**Google Play**
- [ ] *Target API level* igual ou acima do mínimo exigido nesse ano (sobe todos os anos em agosto).
- [ ] Data safety, política de privacidade, classificação de conteúdo e público-alvo preenchidos.
- [ ] Conteúdo digital vendido com **Google Play Billing**.
- [ ] Apagar conta na app **e** por link web.
- [ ] Contas pessoais novas: teste fechado com o número mínimo de testadores durante o período exigido antes de publicar em produção.
- [ ] Declarações para permissões sensíveis (localização em segundo plano, acessibilidade, SMS, alarmes exatos).
- [ ] Anúncios cumprem a política (sem anúncios que enganem ou tapem a interface).

## 10. Rede, offline e dados

- [ ] Sem internet / modo avião: a app abre, mostra o que tem guardado e explica que está sem ligação — sem ecrãs em branco nem rodas infinitas.
- [ ] Pedidos com tempo limite, nova tentativa razoável e mensagens de erro compreensíveis.
- [ ] Erros do servidor (500, 401, 429) tratados; sessão expirada renova ou pede login.
- [ ] Dados guardados no sítio certo: **[iOS]** documentos do utilizador em Documents, dados da app em Application Support, cache em Caches (que o sistema pode apagar); caches grandes excluídas do backup do iCloud.
- [ ] **Migrações**: mudanças ao modelo de dados (Core Data, SwiftData, Room, Codable/JSON) leem os dados antigos — atualizar a app nunca apaga o progresso.
- [ ] Descodificação tolerante: campos novos ou em falta não fazem perder tudo.
- [ ] Gravação segura (escrita atómica); dados não corrompem se a app fechar a meio.
- [ ] Sincronização (iCloud, conta) resolve conflitos sem perder dados.
- [ ] Datas guardadas em formato independente do fuso horário.

## 11. Compras e monetização

- [ ] Produtos carregam da loja; se falharem, a loja da app mostra erro e permite tentar de novo (não fica vazia ou partida).
- [ ] Preços mostrados **vindos da loja** (já no formato e moeda do país), nunca escritos à mão.
- [ ] Todos os estados de compra tratados: sucesso, cancelada, falhada, **pendente** (Ask to Buy / pagamento diferido), já comprada.
- [ ] **Restaurar compras** funciona noutro dispositivo e depois de reinstalar.
- [ ] Subscrições: estado atualizado ao abrir a app (renovação, expiração, período de graça, reembolso/revogação); benefícios retirados quando expira.
- [ ] Transações terminadas (`finish()` / acknowledge) para não ficarem pendentes.
- [ ] Testado em sandbox / TestFlight / teste interno com contas de teste (incluindo cancelamento e renovação acelerada).
- [ ] Paywall honesto: preço e condições claros, botão de fechar visível, sem truques (contagens decrescentes falsas, botões enganadores).
- [ ] Anúncios: frequência razoável, nunca durante ações importantes, nunca a tapar botões; anúncios com recompensa entregam mesmo a recompensa.
- [ ] Economia do jogo coerente (moedas ganhas vs preços), sem forma de obter itens pagos de graça por erro.

## 12. Build, configuração e código

- [ ] Build de release sem erros e com o mínimo de avisos; sem APIs obsoletas importantes.
- [ ] Versão (`CFBundleShortVersionString` / `versionName`) e número de build (`CFBundleVersion` / `versionCode`) aumentados a cada envio.
- [ ] Versão mínima do sistema sensata (cobre a maioria dos utilizadores, sem obrigar a código antigo desnecessário).
- [ ] Configuração de release: sem servidores de teste, sem menus de debug, sem logs verbosos, sem flags de desenvolvimento.
- [ ] Assinatura, capacidades (*entitlements*) e identificadores coerentes (Game Center, push, iCloud, compras ativados no portal e no projeto).
- [ ] Símbolos de crash enviados (dSYM; ficheiro de mapping do R8).
- [ ] Linter / análise estática sem erros (SwiftLint, Android Lint, `flutter analyze`, ESLint/TypeScript).
- [ ] Testes para a lógica crítica (compras, cálculos, migrações de dados) a passar.
- [ ] Sem código morto, ficheiros não usados, `print`/`console.log` de depuração em produção.
- [ ] Dependências fixadas em versões e atualizadas.
- [ ] README com como compilar, testar e publicar.
