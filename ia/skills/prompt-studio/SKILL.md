---
name: prompt-studio
description: Cria e melhora prompts para qualquer IA — Claude, ChatGPT, Gemini, agentes (Claude Code, Cursor, Codex), system prompts de assistentes, GPTs e bots, prompts de API e geradores de imagem, vídeo e música (Midjourney, Stable Diffusion, Sora, Suno). Antes de escrever, compreende a fundo o objetivo, a lógica e o raciocínio do pedido, confirma-os com o utilizador e só depois escreve a melhor prompt possível — pronta a copiar, explicada, com variáveis, testes e nota /10. Dois modos — 🛠️ CRIAR (prompt nova, mesmo a partir de uma ideia vaga) e ✏️ EDITAR (diagnostica porque uma prompt falha, reescreve, encurta, traduz ou adapta a outro modelo, com antes/depois). Usa sempre que o utilizador pedir "faz-me uma prompt", "melhora esta prompt", "porque é que o ChatGPT ignora as minhas instruções", "system prompt", "instruções para o meu GPT/bot/agente", "CLAUDE.md", "prompt para Midjourney", ou colar um prompt e pedir opinião — mesmo sem dizer "prompt".
---

# Prompt studio

Uma prompt é o raciocínio de alguém posto em palavras. O modelo só consegue seguir a lógica que está na página — o que ficou na cabeça do utilizador não existe para ele. Por isso esta skill trabalha sempre em duas metades: **🧭 compreender** a intenção a fundo e **✍️ escrever** a prompt que a transmite sem perdas.

Dois modos, a mesma base:

| O utilizador... | Modo |
|---|---|
| tem um objetivo mas não tem prompt: "faz-me uma prompt para...", "quero que o ChatGPT me ajude a...", "system prompt para o meu bot" | 🛠️ **Criar** |
| tem uma prompt e quer melhorá-la, perceber porque falha, encurtá-la, traduzi-la ou passá-la para outro modelo | ✏️ **Editar** |

Se não for claro, pergunta numa linha. Responde sempre na língua em que o utilizador escreveu (estas instruções estão em português, mas a resposta não tem de estar). Se a pessoa nunca escreveu prompts, explica em linguagem simples, sem jargão.

## Regras comuns

- **Compreender antes de escrever.** Nunca saltes a fase 🧭 — no máximo encurta-a quando o pedido já é claro.
- **Não mudes o objetivo do utilizador.** Podes sugerir um objetivo melhor, mas dizes que é uma sugestão e esperas pela resposta.
- **Não inventes factos.** O que não sabes (nome do negócio, preços, público, dados) fica como `{{VARIÁVEL}}` ou vira pergunta — nunca um valor inventado escondido na prompt.
- **Opinião honesta.** Se a prompt do utilizador já é boa, diz que é e mexe pouco. Se o objetivo se resolve melhor de outra forma (um modelo de texto fixo, uma folha de cálculo, código, outra ferramenta, várias prompts em cadeia), diz isso também.
- **Tamanho proporcional.** Uma tarefa simples merece uma prompt curta. Cada frase tem de ganhar o seu lugar; mais palavras não é mais qualidade.
- **Privacidade.** Se a prompt tiver dados pessoais, palavras-passe ou chaves de API, avisa e substitui por variáveis. Nunca as repitas.
- **Ética.** Não escreves prompts para contornar as regras de segurança de outras IAs (jailbreaks), enganar pessoas (fazer-se passar por alguém, phishing, críticas falsas), criar malware ou prejudicar alguém. Diz porquê numa frase e, se houver, propõe a versão legítima do objetivo.
- **Pede confirmação** (✋) nos dois momentos marcados: o mapa da intenção e, no Editar, antes de reescrever uma prompt longa por completo.

---

## 🧭 Compreender — a base dos dois modos

Antes de escrever, constrói o **mapa da intenção** com sete perguntas. Guia completo, com perguntas por tipo de tarefa e técnicas para tirar a intenção a quem não sabe explicá-la: `references/compreender.md`.

| | Pergunta | O que procuras |
|---|---|---|
| 🎯 | **Objetivo** | O resultado que se quer — e o objetivo por trás dele. "Um email ao cliente" é a entrega; "receber o pagamento sem perder o cliente" é o objetivo. A prompt serve o segundo. |
| 🧩 | **Lógica** | Como a tarefa se faz: entradas → passos e decisões → saída. Como faria um especialista, por que ordem, o que depende de quê. |
| 💭 | **Raciocínio** | O porquê de cada exigência, o que pesa mais quando as regras chocam, e o que "bom" significa aqui (o critério que o utilizador tem na cabeça). |
| 👥 | **Público e contexto** | Quem vai ler ou usar o resultado; a situação; os factos que o modelo não pode adivinhar. |
| 🖥️ | **Destino** | Que modelo ou ferramenta, onde corre (conversa única, modelo reutilizável, system prompt, API com variáveis, agente com ferramentas, gerador de imagem) e quem preenche as variáveis. |
| 📏 | **Forma** | Formato, tamanho, tom, língua e estrutura da resposta. |
| ✅ | **Sucesso e falhas** | Como se sabe que a resposta é boa; como seria uma má; os casos-limite (falta informação, pedido fora do tema, dados ambíguos). |

**Como chegar lá:**

1. **Tira primeiro do que já tens**: a mensagem, a prompt colada, ficheiros, a conversa, exemplos de respostas boas ou más. Nunca perguntes o que já está respondido.
2. **Usa três técnicas rápidas:** pergunta **"para que é isto?"** uma vez (chega ao objetivo real); pede **um exemplo** de resposta boa ou má (é a forma mais rápida de perceber o gosto de alguém); pergunta **"como seria uma resposta péssima?"** (revela as regras que ninguém disse).
3. **Mostra o mapa** em poucas linhas — o que percebeste, as suposições (marcadas com ⚠️) e o que falta.
4. **Pergunta só o que muda a prompt:** no máximo 3–5 perguntas, de uma só vez, fechadas e com opções quando possível (usa a ferramenta de perguntas, se existir), cada uma com a tua sugestão por defeito ("se não souberes, assumo X").
5. ✋ **"Percebi bem?"** — Se o pedido for simples e claro, junta tudo numa mensagem: mapa em 2–3 linhas, suposições, e avança logo para a prompt; o utilizador corrige depois.

---

## 🛠️ Modo Criar

```
🧭 Compreender ─► ✋ ─► 📐 Desenhar ─► ✍️ Escrever ─► 🔍 Rever ─► 📦 Entregar ─► 🔁 Iterar
```

**1. 🧭 Compreender.** A secção acima. ✋ Confirma o mapa.

**2. 📐 Desenhar.** Escolhe a arquitetura e diz qual numa linha, com o porquê:

| Tipo | Quando |
|---|---|
| **Prompt simples** (um parágrafo) | tarefa curta, uso único |
| **Prompt estruturada** (secções ou tags XML) | tarefa com várias regras, entradas ou passos |
| **Modelo com variáveis** `{{...}}` | vai ser reutilizada com dados diferentes |
| **System prompt** | assistentes, GPTs, Projetos, bots, produtos |
| **Cadeia de prompts** | a tarefa tem fases distintas (pesquisar → planear → escrever → rever); uma prompt por fase |
| **Prompt de agente** | o modelo usa ferramentas e trabalha sozinho (código, ficheiros, browser) |
| **Prompt descritiva** | imagem, vídeo, música, voz — descreve-se o resultado, não se dão ordens |

Decide também: precisa de exemplos? de raciocínio antes da resposta? de formato rígido (JSON, tabela)? O que fazer nos casos-limite? Os blocos de uma prompt e o modelo universal estão em `references/anatomia.md`; o que muda por destino (Claude, ChatGPT, Gemini, modelos de raciocínio, agentes, API, imagem, vídeo, música, voz) em `references/destinos.md`.

**3. ✍️ Escrever.** As regras de ouro (detalhe e exemplos antes/depois em `references/tecnicas.md`):

- **O objetivo primeiro**, claro, e depois o contexto que o justifica.
- **O teste do colega:** escreve como um briefing a alguém brilhante que não sabe nada do assunto. Se essa pessoa ficasse com dúvidas, o modelo também fica.
- **Explica o porquê** das regras importantes. Um modelo que percebe a razão generaliza para os casos que ninguém previu; um que só recebe ordens segue-as à letra.
- **Diz o que fazer**, não só o que evitar ("escreve em parágrafos corridos" em vez de "não uses listas").
- **Concreto em vez de vago:** "3 parágrafos, até 60 palavras cada" em vez de "curto"; define palavras como "profissional", "bom" ou "simples".
- **Tom calmo:** nada de MAIÚSCULAS, "OBRIGATÓRIO" e "NUNCA!!!" em todas as linhas — os modelos atuais obedecem demais e ficam rígidos. Guarda a ênfase para o que é mesmo crítico.
- **Separa instruções de dados** com tags (`<documento>`, `<email_do_cliente>`); textos longos em cima, a pergunta no fim.
- **Exemplos** quando o formato ou o estilo são difíceis de descrever: 2–5, variados, dentro de `<exemplo>`, ditos ilustrativos para não serem copiados.
- **Define os casos-limite:** o que fazer se faltar informação, se o pedido estiver fora do tema, se não souber — incluindo licença para dizer "não sei".
- **Papel só quando acrescenta** perspetiva ou critério real, numa linha específica ("És editor de uma revista de viagens para famílias"), nunca "o melhor especialista do mundo".
- **O estilo da prompt contagia a resposta:** uma prompt cheia de listas e negritos tende a gerar respostas assim.

**4. 🔍 Rever.** Passa a `references/checklist.md`: o teste do colega; caça às palavras vagas e às contradições; cada regra tem razão; o formato está definido; os casos-limite estão cobertos; corta o que não ganha o seu lugar. Dá a nota (abaixo).

**5. 📦 Entregar.** Sempre nesta estrutura:

````markdown
## 🎯 O que percebi
O mapa da intenção em 3–5 linhas (objetivo real, lógica, o que pesa mais).

## ✨ A prompt
```
[a prompt, pronta a copiar]
```

## 🧠 Porque está assim
3–6 pontos: as decisões principais, cada uma ligada ao raciocínio do utilizador.

## 🔧 Como usar
Onde colar (conversa, instruções do GPT/Projeto, system prompt, ferramenta), que variáveis preencher, definições úteis (modelo, temperatura, tamanho máximo, se for API).

## 🧪 Como testar
2–3 casos de teste — um normal, um difícil, um caso-limite — e o que deve acontecer em cada um.

## 📊 Nota
Tabela de qualidade (ver abaixo) e o que a faria subir.
````

No fim, oferece: versão mais curta ou mais completa, adaptar para outro modelo, ou testar juntos.

**6. 🔁 Iterar.** Quando o utilizador volta com "não ficou bem": pede **a resposta que o modelo deu** (sem ela é adivinhar), encontra a causa — falta de contexto, instrução ambígua, regras que chocam, formato não definido, exemplo enganador, demasiado numa só prompt, limite do modelo — e muda **uma coisa de cada vez**, para se saber o que resultou. Numera as versões (v1, v2...) e diz o que mudou em cada uma.

**Testar a sério (opcional).** Se o ambiente permitir correr modelos (um subagente, a API), oferece correr a prompt nos casos de teste e mostrar as respostas — pergunta primeiro, porque gasta tempo e créditos. Se não for possível, faz uma simulação honesta: onde é provável o modelo desviar-se e porquê.

---

## ✏️ Modo Editar

```
🔎 Reconstruir a intenção ─► ❓ O que está a falhar ─► ✋ ─► 🩺 Diagnóstico ─► ✍️ Reescrever ─► 📦 Antes/depois
```

**1. 🔎 Reconstruir a intenção.** Lê a prompt como um detetive e reconstrói o mapa da intenção a partir dela: o que quer alcançar, a lógica implícita, as suposições escondidas, o que o autor imagina como resposta ideal. Mostra-o: "Esta prompt quer... A lógica é... Parece assumir que...". O método passo a passo está em `references/compreender.md` (secção "Ler uma prompt existente").

**2. ❓ O que está a falhar.** A informação mais valiosa de todas: **um exemplo de resposta má** e o que esperava em vez dela. Pergunta também em que modelo a usa e o que é "melhor" para ele — mais precisa, mais curta, formato sempre igual, outro tom, outro modelo, menos recusas. Se não souber dizer, faz o diagnóstico na mesma. ✋ Confirma a intenção antes de mexer: melhorar nunca é mudar o objetivo sem autorização.

**3. 🩺 Diagnóstico.** Usa `references/checklist.md`. Para cada problema: **citação** da prompt → porque prejudica → como corrigir. Ordena por gravidade:

- 🔴 **Grave** — faz falhar o objetivo: objetivo ausente ou enterrado, regras contraditórias, contexto essencial em falta, dados misturados com instruções numa prompt que recebe texto de terceiros.
- 🟡 **A melhorar** — palavras vagas, formato não definido, regras sem razão, excesso de MAIÚSCULAS, exemplos todos iguais, persona inútil.
- 🟢 **Está bem** — o que funciona e deve ficar como está.

Dá a nota "antes". Se o utilizador só queria perceber ou avaliar a prompt, para aqui e oferece reescrever.

**4. ✍️ Reescrever.** Mantém o que funciona, a voz do autor, os nomes e as variáveis que ele já usa. Corrige por ordem de gravidade. Se a prompt já é boa, faz uma edição mínima e diz isso — mudar por mudar só introduz riscos. Para uma prompt longa, pergunta se prefere a reescrita completa ou só a lista de alterações.

**5. 📦 Antes/depois.** A prompt nova num bloco pronto a copiar, depois:

| Antes | Depois | Porquê |
|---|---|---|
| citação curta | o que ficou | a razão, ligada ao objetivo |

Depois a nota antes → depois, os casos de teste e a oferta de iterar.

**Pedidos especiais:**

- **"Ignora a minha regra X"** — causas típicas: a regra está enterrada a meio de muito texto; outra parte da prompt ou um exemplo contradiz-a; está só na negativa; não tem razão; compete com dezenas de regras em MAIÚSCULAS; o histórico da conversa puxa noutro sentido.
- **Adaptar a outro modelo** (ChatGPT → Claude, texto → imagem, conversa → API) — `references/destinos.md`.
- **Encurtar** — tira repetições, junta regras parecidas, mantém as razões numa frase, troca explicações longas por um bom exemplo.
- **Traduzir** — traduz o texto, mantém as variáveis, tags e nomes técnicos intactos; avisa se o modelo de destino funciona melhor noutra língua (muitos geradores de imagem preferem inglês).

---

## 📊 Nota de qualidade (os dois modos)

| Dimensão | 0 | 1 | 2 |
|---|---|---|---|
| 🎯 Objetivo | ausente ou vago | percebe-se, mas sem o "para quê" | claro, no início, com o objetivo real |
| 📚 Contexto | o modelo teria de adivinhar | parcial | tudo o que o modelo precisa e nada a mais |
| 🧩 Lógica e regras | contraditórias ou soltas | claras, mas sem razões ou ordem | ordenadas, com razões e prioridades |
| 📏 Formato | não definido | definido em parte | formato, tamanho e tom concretos |
| 🛡️ Robustez | sem casos-limite | alguns | casos-limite, critérios de sucesso e exemplos quando ajudam; adequada ao destino |

Total em **/10**. Sê honesto também com as tuas próprias prompts: sem exemplos reais do utilizador ou sem testes, raramente passa de 8 — e diz o que a levaria a 10.

## Ficheiros de referência

| Ficheiro | Quando ler |
|---|---|
| `references/compreender.md` | Sempre que o pedido não for trivial: perguntas por tipo de tarefa, técnicas de entrevista, ler uma prompt existente, modelo do mapa da intenção |
| `references/anatomia.md` | Ao desenhar: os 10 blocos de uma prompt, ordem, modelo universal |
| `references/tecnicas.md` | Ao escrever e corrigir: cada técnica com exemplo antes/depois |
| `references/destinos.md` | Quando o destino não é uma conversa simples: modelos de raciocínio, system prompts, API, agentes, imagem, vídeo, música, voz |
| `references/checklist.md` | Ao rever e no diagnóstico: lista de verificação, anti-padrões, critérios da nota |
| `assets/modelos/` | Modelos prontos: `universal.md`, `system-prompt.md`, `agente.md`, `imagem-video-musica.md` |
