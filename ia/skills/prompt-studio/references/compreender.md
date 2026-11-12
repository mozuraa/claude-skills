# 🧭 Compreender — como chegar à lógica, ao raciocínio e ao objetivo

A qualidade de uma prompt decide-se antes de ela ser escrita. Este guia ajuda a tirar da cabeça do utilizador o que ele quer, mesmo quando ele não sabe explicar.

## Índice

1. As três camadas: objetivo, lógica, raciocínio
2. Técnicas de entrevista
3. Perguntas por tipo de tarefa
4. Ler uma prompt existente (modo Editar)
5. O mapa da intenção — modelo
6. Quando parar de perguntar
7. Sinais de alerta

---

## 1. As três camadas

Quase todos os pedidos chegam com só uma camada à vista. O teu trabalho é encontrar as outras duas.

### 🎯 Objetivo — o que se quer mesmo

Distingue três níveis:

| Nível | Pergunta | Exemplo |
|---|---|---|
| **Entrega** | O que sai da IA? | "Uma resposta a uma crítica de 1 estrela." |
| **Objetivo** | Para que serve essa entrega? | "Que quem lê a crítica veja que a loja se importa." |
| **Objetivo de fundo** | Porque é que isso importa? | "Não perder clientes novos que leem as críticas antes de comprar." |

A prompt tem de servir o objetivo de fundo. Neste exemplo, isso muda tudo: a resposta escreve-se para **os futuros clientes que vão ler**, não só para quem se queixou — e uma resposta defensiva falha mesmo que esteja bem escrita.

### 🧩 Lógica — como a tarefa se faz

Desmonta a tarefa como um especialista a faria:

- **Entradas:** o que o modelo recebe (texto, ficheiro, pergunta, dados, imagem)?
- **Passos:** que transformações acontecem, por que ordem? Há passos que dependem de outros?
- **Decisões:** onde é preciso escolher? Com que critério? ("Se a crítica tiver razão, pede desculpa; se não tiver, agradece e esclarece.")
- **Saída:** que forma tem o resultado e para onde vai a seguir (é lido por uma pessoa, colado num site, lido por outro programa)?

Se o utilizador faz a tarefa à mão, pede-lhe: **"Como é que tu fazes isto, passo a passo?"** A resposta é a lógica.

### 💭 Raciocínio — o porquê

É a camada mais esquecida e a mais valiosa. Para cada exigência, procura a razão:

- **Porquê esta regra?** ("Sem emojis" — porque a marca é de luxo? porque o texto vai para um email formal?)
- **O que pesa mais?** Quando duas regras chocam (curto vs. completo, simpático vs. firme), qual ganha?
- **O que é "bom" aqui?** O critério de qualidade que o utilizador tem na cabeça mas nunca disse.
- **Que erros já aconteceram?** Muitas regras nascem de um erro passado — saber qual ajuda a escrevê-las melhor.

A razão entra na prompt. "Sem emojis, porque as respostas aparecem ao lado de uma marca de luxo" ensina mais ao modelo do que "NUNCA uses emojis".

---

## 2. Técnicas de entrevista

| Técnica | Pergunta | O que revela |
|---|---|---|
| **Para que é?** | "Depois de teres isto, o que fazes com ele?" | o objetivo real (pergunta uma vez, no máximo duas — mais parece interrogatório) |
| **Exemplo bom** | "Tens um exemplo de algo que achaste mesmo bem feito?" | estilo, tamanho, tom — mais rápido do que qualquer descrição |
| **Exemplo mau** | "Tens uma resposta que te irritou? O que estava mal?" | as regras implícitas |
| **Resposta péssima** | "Como seria a pior resposta possível?" | os limites que ninguém diz |
| **Como fazes tu?** | "Se fosses tu a fazer, por onde começavas?" | a lógica e as decisões |
| **Quem lê?** | "Quem vai ler isto e o que sabe essa pessoa?" | público, nível, jargão permitido |
| **E se...?** | "E se faltar o preço? E se pedirem algo fora do tema?" | os casos-limite |
| **Uma vez ou sempre?** | "Vais usar isto uma vez ou muitas, com dados diferentes?" | se é prompt simples, modelo com variáveis ou system prompt |

**Boas práticas:**

- Pergunta tudo **de uma só vez**, numerado, com opções sempre que possível.
- Dá sempre a tua **sugestão por defeito**: "Tom: (a) próximo e simpático (b) formal — se não disseres, uso (a)".
- Não perguntes o que podes descobrir sozinho (ficheiros, a própria prompt, a conversa).
- Se o utilizador responder "tanto faz", escolhe tu e diz o que escolheste.

---

## 3. Perguntas por tipo de tarefa

Escolhe só as que mudam a prompt.

**✍️ Escrita (emails, posts, artigos, descrições de produto)**
- Quem lê e o que deve fazer/sentir depois de ler?
- Voz da marca ou da pessoa — há textos de exemplo?
- Tamanho e canal (Instagram, LinkedIn, email, site)?
- Palavras ou estilos proibidos (e porquê)?
- Há factos obrigatórios (preço, data, chamada para ação)?

**📄 Resumo e análise (documentos, reuniões, relatórios, dados)**
- Para quem é o resumo e que decisão vai apoiar?
- O que interessa mais: decisões, números, riscos, tarefas?
- Tamanho e formato (3 pontos, uma página, tabela)?
- Pode tirar conclusões ou só relatar? Deve citar o texto original?

**🔍 Extração e classificação (tirar dados de textos, etiquetar, triar)**
- Que campos exatos, com que formato (datas, moedas)?
- Que categorias, com que definição e exemplos de cada?
- O que fazer quando o dado não existe ou é ambíguo?
- Para onde vai a saída (folha de cálculo, programa → JSON rígido)?

**💬 Assistente, bot ou GPT (system prompt)**
- Quem são os utilizadores e o que vêm pedir?
- O que está dentro e fora do âmbito? O que fazer com pedidos fora?
- Que informação o assistente tem (documentos, ferramentas) e que não deve inventar?
- Tom e formato (o ecrã mostra markdown? é por voz?)
- Quando passar a um humano? O que nunca deve fazer?

**🧑‍💻 Código e agentes (Claude Code, Cursor, Codex, automações)**
- Que projeto, linguagem e convenções?
- O que é "feito"? Como se verifica (testes, comandos, captura)?
- O que não se pode tocar? Até onde vai a autonomia (pode instalar dependências, apagar, fazer commits)?
- Deve primeiro propor um plano?

**🎨 Imagem, vídeo, música**
- Para que é (capa, anúncio, ilustração de artigo, ícone)? Em que tamanho/proporção?
- Sujeito, cenário, estilo, luz, cores, ambiente — há referências?
- Texto dentro da imagem? Que ferramenta exatamente?
- O que deve ficar de fora?

**🎓 Ensino e explicação**
- Quem aprende e o que já sabe?
- Objetivo: perceber, decorar, passar num exame, conseguir fazer?
- O modelo deve dar a resposta ou guiar com perguntas?

**🤔 Decisão e opinião**
- Que opções existem e que critérios pesam mais?
- O modelo deve recomendar ou só comparar?
- Que informação tem e que informação deve pedir?

---

## 4. Ler uma prompt existente (modo Editar)

Reconstrói a intenção antes de julgar a prompt:

1. **Lista cada instrução** e marca-a: objetivo · contexto · regra · formato · exemplo · dado.
2. **Encontra o objetivo** — está escrito? Está no início? Se não estiver escrito, deduz-o e marca como suposição.
3. **Reconstrói a lógica implícita** — que passos o autor imagina? Estão por ordem?
4. **Procura a razão de cada regra** — a que erro ou preferência responde? As regras sem razão aparente são candidatas a perguntar ("porque está aqui o 'nunca uses a palavra grátis'?").
5. **Imagina a resposta ideal** que o autor tem na cabeça — e compara com o que a prompt realmente pede. A diferença entre as duas é o diagnóstico.
6. **Procura contradições** — entre regras, entre regras e exemplos, entre o tom pedido e o tom da própria prompt.
7. **Procura o que falta** — contexto, público, formato, casos-limite.

Mostra a reconstrução ao utilizador antes de reescrever. Muitas vezes ele próprio descobre o problema ao ler ("ah, eu nunca disse que era para clientes novos").

---

## 5. O mapa da intenção — modelo

```markdown
## 🧭 O que percebi

🎯 **Objetivo:** [entrega] para [objetivo], porque [objetivo de fundo].
🧩 **Lógica:** [entrada] → [passos/decisões principais] → [saída].
💭 **O que pesa mais:** [prioridade 1] acima de [prioridade 2]; "bom" aqui é [critério].
👥 **Para quem:** [público e contexto essencial].
🖥️ **Onde corre:** [modelo/ferramenta], [uma vez / modelo reutilizável / system prompt].
📏 **Forma:** [formato, tamanho, tom, língua].
✅ **Sucesso:** [como se reconhece uma boa resposta]; casos-limite: [...].

⚠️ **Suposições:** [o que assumi sem saber].

❓ **Antes de escrever:**
1. [pergunta] — (a) ... (b) ... — se não souberes, assumo (a).
2. ...
```

Para pedidos simples, comprime para 2–3 linhas: "Percebi: queres X para Y, em Z. Assumi A e B. Aqui vai — diz-me se algo não bate certo."

---

## 6. Quando parar de perguntar

Para e escreve quando:

- consegues preencher o mapa sem suposições arriscadas; ou
- as perguntas que restam têm um bom valor por defeito; ou
- já fizeste uma ronda de perguntas — as suposições restantes vão marcadas com ⚠️ e o utilizador corrige ao ver a prompt.

Uma prompt concreta com suposições visíveis ensina mais ao utilizador sobre o que quer do que uma terceira ronda de perguntas.

---

## 7. Sinais de alerta

- **O objetivo é outro.** "Quero uma prompt para o ChatGPT escrever 50 críticas positivas da minha loja" → isso é enganar clientes (e viola as regras das plataformas). Diz porquê e propõe o objetivo legítimo: pedir críticas a clientes reais, responder bem às que existem.
- **A IA não é a ferramenta certa.** Cálculos exatos, dados que mudam todos os dias, tarefas sempre iguais → uma fórmula, um script ou um modelo de texto fixo podem ser melhores. Diz isso.
- **Falta informação que só o utilizador tem** (preços, políticas, factos do negócio) → não inventes; variável ou pergunta.
- **A tarefa é grande demais para uma prompt** → propõe uma cadeia (ver `anatomia.md`).
