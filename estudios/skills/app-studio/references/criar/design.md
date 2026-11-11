# Design de apps — convenções, sistema e ecrãs

Uma boa app **parece pertencer ao telemóvel**: usa os padrões que o utilizador já conhece (Human Interface Guidelines da Apple, Material 3 da Google) e tem personalidade própria nos detalhes — cor, ícone, ilustrações, animações, tom dos textos.

## Índice

- [1. Convenções da plataforma](#1-convenções-da-plataforma)
- [2. Sistema de design](#2-sistema-de-design)
- [3. Navegação](#3-navegação)
- [4. Ecrãs essenciais](#4-ecrãs-essenciais)
- [5. Texto, acessibilidade e idiomas](#5-texto-acessibilidade-e-idiomas)
- [6. Movimento, vibração e som](#6-movimento-vibração-e-som)
- [7. Ícone da app e ecrã de arranque](#7-ícone-da-app-e-ecrã-de-arranque)
- [8. Jogos](#8-jogos)
- [9. Erros comuns a evitar](#9-erros-comuns-a-evitar)

---

## 1. Convenções da plataforma

- **Componentes nativos primeiro** (`NavigationStack`, `List`, `Form`, `TabView`, `sheet`, `Toggle`, `Picker` em SwiftUI; equivalentes Material em Compose). São acessíveis, rápidos e familiares de graça.
- **iOS**: barra de separadores em baixo (3–5 secções), títulos grandes, gestos de voltar, folhas (sheets) para tarefas curtas, botões de ação na barra de navegação, SF Symbols, materiais translúcidos do sistema.
- **Android**: barra de navegação inferior ou gaveta, botão de ação flutuante para a ação principal (se fizer sentido), gesto/botão de voltar sempre funcional, Material Symbols, cores dinâmicas (Material You) opcionais.
- Numa app multiplataforma, respeita as diferenças nos pontos que o utilizador sente (voltar, alertas, seletores de data, tipografia).

## 2. Sistema de design

Define tudo uma vez e usa sempre os mesmos nomes:

- **Cores**: cores **semânticas** (fundo, superfície, texto principal, texto secundário, acento, sucesso, erro) com variante **clara e escura** (Asset Catalog no iOS; tema Material no Android). Usa as cores do sistema para texto e fundos sempre que possível; a cor da marca como acento. Contraste ≥ 4,5:1 em texto, nos dois modos.
- **Tipografia**: estilos do sistema (`.largeTitle`, `.title`, `.headline`, `.body`, `.caption` / escala Material) para respeitar o **tamanho de letra do utilizador**. Fontes personalizadas só nos títulos, e com escala dinâmica (`.custom(_:size:relativeTo:)`).
- **Espaçamento**: escala de 4/8 pt (4, 8, 12, 16, 24, 32); margens laterais de 16–20 pt.
- **Forma**: raio dos cantos consistente; cartões com fundo de superfície em vez de sombras fortes.
- **Ícones**: SF Symbols / Material Symbols com o mesmo peso em toda a app; ícones personalizados em vetor.

## 3. Navegação

- O utilizador deve saber sempre **onde está, como voltar e o que fazer a seguir**.
- 1 ação principal por ecrã, bem visível; ações destrutivas a vermelho e com confirmação.
- Profundidade baixa: a tarefa principal a ≤ 3 toques do arranque.
- Modais/sheets para tarefas curtas e independentes, com "Cancelar" e "Guardar/Concluído" claros.
- Deep links para os ecrãs importantes (notificações, widgets, partilha).

## 4. Ecrãs essenciais

- **Onboarding**: no máximo 3 ecrãs, saltável, a mostrar o benefício (não instruções); melhor ainda: ensinar durante o uso. Permissões pedidas no momento em que fazem sentido, não aqui.
- **Estado vazio**: explica o que vai aparecer e oferece a primeira ação ("Ainda não tens registos — adiciona o primeiro").
- **Carregamento**: esqueleto ou indicador; nunca ecrã em branco.
- **Erro**: o que aconteceu, em linguagem humana, e o que fazer ("Sem ligação. Tentar de novo").
- **Definições**: só o necessário; inclui sobre/versão, contacto/suporte, política de privacidade, restaurar compras, apagar conta (se houver contas).
- **Paywall** (se existir): o que se ganha, preço vindo da loja, condições claras, fechar visível, restaurar compras, links para termos e privacidade.

## 5. Texto, acessibilidade e idiomas

- Textos curtos, com verbos nos botões ("Guardar", "Começar treino").
- **VoiceOver/TalkBack**: nome em todos os botões de ícone; agrupar elementos relacionados; ordem lógica.
- **Texto grande**: os ecrãs têm de funcionar no maior tamanho (deixar o texto quebrar linha; usar scroll; trocar layouts horizontais por verticais quando o texto cresce).
- Alvos de toque ≥ 44×44 pt / 48×48 dp. Informação nunca só por cor.
- Todos os textos no sistema de traduções (String Catalog / `strings.xml` / `intl`); datas, números e moedas formatados pelo sistema; prever +30% de comprimento noutras línguas.

## 6. Movimento, vibração e som

- Animações curtas (150–300 ms) que explicam o que mudou; usar as transições do sistema.
- Respeitar **Reduzir movimento**.
- Vibração (haptics) leve para confirmar ações importantes, não para tudo; opção para desligar.
- Sons opcionais e respeitando o modo silencioso.

## 7. Ícone da app e ecrã de arranque

- **Ícone**: uma ideia simples e reconhecível em pequeno (testar a 60 px), sem texto, sem fotografias, sem transparência (iOS). Cores fortes que se destacam no ecrã inicial.
- **iOS**: 1024×1024 no Asset Catalog (o Xcode gera os tamanhos); variantes escura e tingida; nas versões recentes do iOS, ícones em camadas criados com o Icon Composer.
- **Android**: ícone adaptativo (primeiro plano + fundo, 108 dp com zona segura de 66 dp) e camada monocromática para ícones temáticos; 512×512 para a Play Store.
- **Ecrã de arranque**: igual ao primeiro ecrã sem conteúdo (fundo + barra), não um anúncio nem um logótipo grande; transição sem "salto".

## 8. Jogos

- Controlos que se percebem em 3 segundos; uma mão, polegar; zonas de toque generosas.
- Legível em ecrãs pequenos; elementos importantes longe das bordas e da Dynamic Island.
- *Juice*: resposta imediata a cada toque (som, vibração, partículas, pequenas animações).
- Pausa automática ao sair; continuar exatamente onde estava.
- Interface (HUD) mínima; menus grandes e simples; definições de som, música e vibração.
- Paleta coerente e estilo visual único; nada de recursos de jogos conhecidos.

## 9. Erros comuns a evitar

- Recriar componentes do sistema (perde-se acessibilidade e familiaridade).
- Tamanhos fixos de letra e de layout que partem com texto grande ou no iPhone SE.
- Pedir todas as permissões no primeiro arranque.
- Login obrigatório antes de mostrar qualquer valor.
- Pop-ups de avaliação cedo demais (usar o pedido do sistema, depois de um momento positivo).
- Esquecer o modo escuro (texto preto em fundo escuro).
- Gestos escondidos como única forma de fazer algo importante.
