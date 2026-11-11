# Briefing — perguntas e o que cada tipo de app tem de ter

Depois das 5 perguntas essenciais (ver `SKILL.md`), usa a secção do tipo de app para as perguntas específicas e para saber o que a app **tem de ter**. Pergunta só o que falta — tudo numa mensagem.

## Índice

- [Perguntas práticas (todas as apps)](#perguntas-práticas-todas-as-apps)
- [Jogo casual / arcada](#jogo-casual--arcada)
- [Jogo de níveis / puzzle](#jogo-de-níveis--puzzle)
- [Utilidade / ferramenta](#utilidade--ferramenta)
- [Produtividade, hábitos, registo](#produtividade-hábitos-registo)
- [Saúde e fitness](#saúde-e-fitness)
- [Educação e crianças](#educação-e-crianças)
- [Social, comunidade, conteúdo de utilizadores](#social-comunidade-conteúdo-de-utilizadores)
- [App de um negócio (restaurante, loja, serviços)](#app-de-um-negócio)
- [App de brincadeira / novidade](#app-de-brincadeira--novidade)

---

## Perguntas práticas (todas as apps)

- **Computador**: tem Mac? (Apps iOS nativas precisam de Mac com Xcode; com Expo/EAS é possível compilar iOS na nuvem.)
- **Contas de programador**: Apple Developer Program (~99 €/ano, obrigatório para publicar e para TestFlight); Google Play Console (~25 USD, pagamento único). Individual ou empresa (empresa exige número D-U-N-S)?
- **Nome** e se já verificou que está livre nas lojas (o nome da loja tem de ser único na App Store).
- **Línguas** e **países**.
- **Dispositivos**: só iPhone? iPad? Android telemóvel e tablet? Relógio?
- **Funciona sem internet?** Precisa de contas de utilizador? Os dados têm de passar entre dispositivos ou pessoas?
- **Monetização**: grátis, paga, compra única para desbloquear, subscrição, anúncios, ou um mix.
- **Prazo** e **orçamento** para serviços.
- **Quem mantém** a app depois (o utilizador sozinho, com o Claude?).

## Jogo casual / arcada

**Perguntar:** a mecânica central numa frase; sessões de quanto tempo; estilo visual (minimalista, ilustrado, pixel art); sons e música (originais? licenciados?); progressão (recordes, desbloqueáveis); modos (infinito, diário); ranking (Game Center / Play Games).

**Tem de ter:** controlos que se percebem em 3 segundos; *game feel* (resposta imediata, vibração, partículas, sons); pausa automática ao sair da app; recordes guardados; definições de som/vibração; tutorial dentro do jogo (não um texto); desempenho estável no dispositivo mais fraco suportado; nunca perder o progresso numa atualização.

## Jogo de níveis / puzzle

**Perguntar:** número de níveis na versão 1; mundos/temas; sistema de estrelas ou pontuação; dicas; quem desenha os níveis.

**Tem de ter:** curva de dificuldade gradual com os primeiros níveis a ensinarem; **verificação de que todos os níveis têm solução** (de preferência um verificador automático); repetir/saltar nível; progresso guardado por nível; níveis em ficheiros de dados (fáceis de acrescentar).

## Utilidade / ferramenta

**Perguntar:** a tarefa principal e quantos toques deve levar; dados de entrada e saída; integração com Fotos, Ficheiros, Partilha, Atalhos, widgets.

**Tem de ter:** a tarefa principal em ≤ 3 toques a partir do arranque; resultado partilhável/exportável; funciona sem internet se possível; widgets/atalhos se fizer sentido; sem contas se não forem precisas.

## Produtividade, hábitos, registo

**Perguntar:** o que se regista, com que frequência; lembretes; gráficos/estatísticas; sincronização entre dispositivos; exportação.

**Tem de ter:** registo rápido (1–2 toques); notificações opcionais e configuráveis; histórico e estatísticas claras; **exportar os dados** (CSV/JSON); sincronização (iCloud/CloudKit é simples no iOS); perdão de falhas (um dia falhado não destrói tudo).

## Saúde e fitness

**Perguntar:** que dados de saúde; integração com Saúde (HealthKit) / Health Connect; se dá conselhos médicos.

**Tem de ter:** **dados de saúde são sensíveis** (RGPD art. 9.º) — mínimos, no dispositivo sempre que possível, nunca para publicidade; textos de permissões claros; avisos de que não substitui um profissional; regras específicas das lojas para apps de saúde (não fazer diagnósticos sem certificação). Diz ao utilizador estes riscos com franqueza.

## Educação e crianças

**Perguntar:** idades; com ou sem adultos; conteúdos; progressos.

**Tem de ter:** se o público inclui crianças: categoria Crianças (App Store) / política Famílias (Google Play) — **sem anúncios personalizados nem SDKs de rastreio**, compras e links externos atrás de uma "barreira parental"; nada de recolha de dados sem consentimento parental; interface com alvos grandes, áudio para quem ainda não lê.

## Social, comunidade, conteúdo de utilizadores

**Perguntar:** o que os utilizadores publicam; quem vê; moderação; tamanho esperado.

**Opinião a dar:** é o tipo de app mais difícil para uma pessoa — precisa de servidor, moderação e muitos utilizadores para ter valor. Sugere começar mais pequeno (ex.: partilha privada entre amigos).

**Tem de ter (exigido pelas lojas):** termos de utilização, **denunciar conteúdo**, **bloquear utilizadores**, moderação e resposta a denúncias, apagar conta e conteúdos.

## App de um negócio

*(restaurante, loja, ginásio, clínica, serviços)*

**Perguntar:** o que a app faz que o site não faz (encomendar, marcar, cartão de fidelização, notificações).

**Opinião a dar:** muitas vezes **um bom site (website-studio) resolve melhor e mais barato**; uma app só se justifica se os clientes a abrirem com frequência. Uma app que é só o site embrulhado é rejeitada (regra 4.2).

**Tem de ter:** funcionalidade nativa real (marcações, cartão de pontos, encomendas, notificações úteis); login simples; integração com o sistema que o negócio já usa.

## App de brincadeira / novidade

**Perguntar:** a piada/efeito em uma frase; o que faz quem paga (se for paga).

**Tem de ter:** valor real o suficiente para passar na revisão (regras 4.2/4.3 — apps "de pouca utilidade" podem ser rejeitadas); descrição honesta na loja (não enganar sobre o que faz); se a piada é um preço exagerado, deixar claro na descrição para evitar reembolsos e más avaliações.
