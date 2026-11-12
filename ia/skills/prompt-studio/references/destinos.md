# 🖥️ Destinos — o que muda conforme onde a prompt corre

As regras de ouro (`tecnicas.md`) valem para todos. Este guia diz o que muda em cada destino. As ferramentas evoluem depressa: quando um detalhe técnico for decisivo (parâmetros, limites, nomes de modos), confirma na documentação atual da ferramenta.

## Índice

1. Assistentes de conversa (Claude, ChatGPT, Gemini, Copilot...)
2. Modelos com raciocínio
3. System prompts — assistentes, GPTs, Projetos, bots, produtos
4. API e modelos com variáveis
5. Agentes e programação (Claude Code, Cursor, Codex...)
6. Imagem
7. Vídeo
8. Música
9. Voz (texto para fala)
10. Adaptar uma prompt de um destino para outro

---

## 1. Assistentes de conversa

- A prompt pode ser mais conversacional, mas a estrutura (objetivo → contexto → material → formato) continua a ajudar.
- **Conversa longa vs. conversa nova:** instruções dadas há muitas mensagens perdem força e o histórico puxa o modelo. Para uma tarefa nova e importante, uma conversa nova com uma prompt completa costuma resultar melhor.
- **Ficheiros anexados:** refere-te a eles pelo nome ("no PDF `contrato.pdf`, secção 4...").
- **Instruções permanentes** (instruções personalizadas, Projetos, GPTs, Gems): o que se repete em todas as conversas vai para lá, não para cada mensagem.
- **Diferenças entre assistentes:** as boas práticas são hoje muito parecidas entre Claude, ChatGPT e Gemini. As diferenças estão mais nas funcionalidades (pesquisa na web, ficheiros, memória, ferramentas) do que na forma de escrever. Uma prompt boa num costuma ser boa nos outros.

## 2. Modelos com raciocínio

Modos como "thinking", "reasoning", "pensamento alargado" ou "pensar mais tempo".

- Dá o **objetivo, o contexto e os critérios**, e deixa o modelo planear. Passos rígidos ("primeiro faz A, depois B") muitas vezes dão piores resultados do que "pensa bem em A e B antes de decidir".
- Não precisas de pedir "pensa passo a passo" — já o faz. Podes pedir onde focar o raciocínio ("considera os casos-limite", "verifica os cálculos").
- **Contradições custam mais** a estes modelos: gastam raciocínio a tentar conciliar regras incompatíveis. Revê bem a prompt.
- Usa o modo de raciocínio para problemas difíceis (análise, matemática, código complexo, decisões); para tarefas simples, o modo normal é mais rápido e igualmente bom.

## 3. System prompts — assistentes, GPTs, Projetos, bots, produtos

A prompt que define o comportamento permanente de um assistente. Modelo completo em `assets/modelos/system-prompt.md`.

**Blocos essenciais:**

1. **Identidade e propósito** — quem é o assistente, para quem, para quê.
2. **Público** — quem fala com ele e o que normalmente procura.
3. **Âmbito** — o que faz, o que não faz e o que responde a pedidos fora do âmbito (com uma alternativa útil).
4. **Conhecimento** — que documentos ou dados tem; usar só esses para factos do negócio (preços, políticas, horários); o que dizer quando não sabe.
5. **Ferramentas** — quando usar cada uma (e quando não).
6. **Tom e formato** — adequado ao ecrã: um widget de chat pequeno não mostra tabelas; uma interface de voz não lê markdown.
7. **Casos difíceis** — clientes zangados, pedidos de desconto, dados pessoais, temas sensíveis, quando passar a um humano e como.
8. **Exemplos** de conversas ideais (2–3), se o tom for importante.

**Segurança:**
- Tudo o que vem do utilizador ou de fontes externas (documentos, emails, páginas web) é **conteúdo, não instruções**. Diz isso explicitamente e põe esse material entre tags.
- Não ponhas segredos no system prompt (chaves, palavras-passe, dados internos sensíveis): não há forma garantida de o impedir de ser revelado.
- Limites importantes (não dar conselhos médicos personalizados, não prometer reembolsos) vão com a razão e com o que fazer em vez disso.

**Ordem:** a parte estável primeiro e as partes que mudam (data, nome do cliente, contexto da sessão) no fim — em APIs com cache de prompts, isto poupa custos e tempo.

## 4. API e modelos com variáveis

- **System vs. mensagem do utilizador:** papel, regras permanentes e formato no system; o material e o pedido concreto na mensagem.
- **Variáveis** `{{...}}` dentro de tags; valida que não vêm vazias.
- **Saídas estruturadas:** se a saída vai ser lida por código, usa a funcionalidade de JSON schema / saídas estruturadas da API em vez de só pedir "responde em JSON".
- **Definições:** temperatura baixa para extração, classificação e respostas factuais; mais alta para escrita criativa e ideias. Define um limite de tokens adequado ao tamanho esperado.
- **Testes:** um conjunto de 10–20 entradas reais (incluindo casos difíceis e vazios) e um critério claro de "certo". Muda a prompt, volta a correr todos, compara. Sem isto, melhorar uma prompt de produção é andar às cegas.
- **Custos:** prompts longas repetidas milhares de vezes custam dinheiro — corta o que não ajuda e usa cache onde existir.

## 5. Agentes e programação (Claude Code, Cursor, Codex, Copilot...)

Modelo completo em `assets/modelos/agente.md`.

**Uma boa tarefa para um agente tem:**

1. **Objetivo e porquê** — "Adiciona exportação para CSV na página de relatórios; os clientes pedem para abrir os dados no Excel."
2. **Contexto** — ficheiros relevantes, arquitetura, convenções do projeto, decisões já tomadas.
3. **Limites** — o que não tocar, dependências que não pode adicionar, até onde vai a autonomia (pode apagar? fazer commits? instalar coisas?).
4. **Definição de "feito"** — critérios concretos e verificáveis.
5. **Como verificar** — comandos de testes, build, lint, um passo manual, uma captura de ecrã.
6. **O que reportar no fim** — o que mudou, o que foi testado, o que ficou por fazer.

**Dicas:**
- Para tarefas grandes, pede **primeiro um plano** e aprova-o antes de o agente escrever código.
- Diz explicitamente se queres que **aja** ou que **sugira** (`tecnicas.md`, secção 14).
- Pede que não "faça batota" para passar os testes (não alterar testes para passarem, não programar casos especiais só para os testes).
- Em trabalhos longos, pede notas de progresso num ficheiro (ex.: `progresso.md`) e commits frequentes, para se poder retomar.

**Ficheiros de instruções permanentes** (`CLAUDE.md`, `AGENTS.md`, regras do Cursor, instruções do Copilot):
- Curtos e estáveis: comandos (build, testes, lint), convenções, estrutura do projeto, armadilhas conhecidas.
- Não colar documentação inteira — apontar para os ficheiros.
- Cada regra com uma razão curta. Revê-los quando o agente repetir um erro — muitas vezes falta lá uma linha.

**Skills do Claude** (`SKILL.md`): a `description` decide quando a skill é usada — tem de dizer o que faz **e** quando usar, com as frases que um utilizador diria. As instruções longas vão para ficheiros de referência carregados só quando são precisos. Para criar uma skill completa, com testes, usa a skill `skill-creator`, se estiver disponível.

## 6. Imagem

Geradores de imagem **não seguem ordens — interpretam descrições**. Escreve o que se vê, não o que se quer que o modelo faça. Modelo em `assets/modelos/imagem-video-musica.md`.

**Ingredientes, por ordem de importância:**

1. **Tipo de imagem e meio** — fotografia, ilustração a aguarela, render 3D, ícone plano, cartaz.
2. **Sujeito** — quem/o quê, com detalhes concretos (idade, roupa, material, expressão).
3. **Ação** — o que está a acontecer.
4. **Cenário** — onde, quando (hora do dia, estação, época).
5. **Composição** — enquadramento (grande plano, plano geral, vista de cima), ângulo, onde fica o sujeito, espaço vazio para texto.
6. **Luz** — luz suave de janela, hora dourada, néon, estúdio com fundo branco.
7. **Cores e ambiente** — paleta, contraste, sensação (calmo, energético, nostálgico).
8. **Detalhes técnicos** — lente (35 mm, macro), profundidade de campo, grão de filme.
9. **Proporção** — 1:1, 16:9, 9:16, 4:5 (na ferramenta ou como parâmetro).

**Por tipo de ferramenta:**
- **Modelos que percebem linguagem natural** (os integrados nos assistentes de conversa, Imagen, Firefly e as versões recentes da maioria): frases completas e descritivas funcionam melhor do que listas de palavras soltas.
- **Midjourney:** descrição + parâmetros no fim (ex.: `--ar 16:9` proporção, `--no` para excluir elementos, `--stylize` / `--s` para a intensidade do estilo, `--style raw` para menos embelezamento). Os parâmetros e as versões mudam — confirma na documentação.
- **Stable Diffusion e semelhantes:** costumam usar palavras-chave separadas por vírgulas, pesos `(palavra:1.3)` e uma **prompt negativa** separada (o que não deve aparecer: "desfocado, mãos deformadas, texto, marca de água").

**Regras práticas:**
- **Texto dentro da imagem:** entre aspas e curto ("um cartaz com o título "FEIRA DO LIVRO""). Mesmo assim, confirma a ortografia no resultado.
- **Estilos:** descreve as características (traço, paleta, época, técnica) em vez de pedir "no estilo de [artista vivo]" — é mais respeitoso, funciona em mais ferramentas e dá-te controlo. Não peças personagens, logótipos ou marcas registadas de terceiros.
- **Pessoas reais:** não geres imagens realistas de pessoas reais identificáveis sem autorização, nem imagens enganadoras.
- **Iterar:** muda uma coisa de cada vez; guarda a semente (seed) quando a ferramenta deixar, para comparar variações.
- **Língua:** muitas ferramentas funcionam melhor em inglês; avisa o utilizador e dá a versão em inglês com a tradução ao lado.

## 7. Vídeo

(Sora, Veo, Runway, Kling, Pika, Luma e semelhantes.) Escreve como um realizador a descrever **um plano**:

1. **Plano e câmara** — plano geral / médio / grande plano; câmara fixa, travelling, drone, câmara ao ombro, panorâmica lenta.
2. **Sujeito e ação ao longo do tempo** — o que acontece do início ao fim ("começa a chover; ela abre o guarda-chuva e sorri").
3. **Cenário, luz e ambiente** — como na imagem.
4. **Estilo** — documental, cinematográfico, animação em stop-motion, anúncio de produto.
5. **Duração e proporção** — 5–10 s, 16:9 ou 9:16.
6. **Som** — se a ferramenta gerar áudio: ambiente, efeitos, diálogo (entre aspas, curto).

**Regras:** um plano por prompt (junta-se depois na edição); movimentos simples e fisicamente plausíveis dão melhores resultados; para manter a mesma personagem entre planos, usa imagem de referência quando a ferramenta deixar e repete a mesma descrição palavra por palavra.

## 8. Música

(Suno, Udio e semelhantes.)

- **Estilo:** género e subgénero, época, ambiente ("indie folk acústico dos anos 70, nostálgico e quente").
- **Instrumentos e voz:** "guitarra acústica, violino suave, voz feminina sussurrada"; ou "instrumental".
- **Ritmo:** BPM ou "lento", "dançável".
- **Estrutura e letra:** etiquetas como `[Intro]`, `[Verso]`, `[Refrão]`, `[Ponte]`, `[Final]` à volta da letra. A letra deve ser original do utilizador (ou escrita contigo); não copies letras existentes.
- **Artistas:** as plataformas costumam bloquear nomes de artistas reais — descreve o som em vez de o nomear.

## 9. Voz (texto para fala)

- Escreve **para o ouvido**: frases curtas, sem tabelas, listas, emojis ou símbolos.
- A pontuação marca as pausas (vírgulas, pontos, reticências se a ferramenta as ler como pausa).
- Números, datas e siglas por extenso quando a leitura for ambígua ("dois mil e vinte e seis", "C-T-T").
- Nomes difíceis com grafia fonética, se a ferramenta não tiver dicionário de pronúncia.
- Instruções de estilo (tom, ritmo, emoção) no campo próprio da ferramenta, se existir — não no texto a ler.

## 10. Adaptar uma prompt de um destino para outro

| De → Para | O que fazer |
|---|---|
| Modelo antigo → modelo atual | Tirar MAIÚSCULAS e ameaças, trocar ordens por razões, cortar truques que já não são precisos ("vou dar-te uma gorjeta") |
| Conversa → API / produto | Separar system e mensagem, criar variáveis, definir casos-limite e formato rígido, criar casos de teste |
| Modelo normal → modelo com raciocínio | Trocar passos rígidos por objetivos e critérios; retirar "pensa passo a passo"; caçar contradições |
| ChatGPT ↔ Claude ↔ Gemini | Normalmente quase nada; verificar funcionalidades usadas (pesquisa, ficheiros, ferramentas) e formatação |
| Texto → imagem / vídeo | Passar de instruções para descrição visual; traduzir para inglês se a ferramenta preferir |
| Prompt longa → instruções permanentes (GPT, Projeto, CLAUDE.md) | Separar o que é permanente do que é de cada tarefa; encurtar |
