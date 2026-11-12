# 🔍 Checklist — rever, diagnosticar e dar nota

Usa a lista inteira no modo Editar (diagnóstico) e no fim do modo Criar (revisão). Para prompts curtas, as secções A e B chegam.

## Índice

A. Os 5 testes rápidos
B. Lista de verificação
C. Anti-padrões — como reconhecer e corrigir
D. Critérios da nota /10
E. Diagnóstico a partir de uma resposta má

---

## A. Os 5 testes rápidos

1. **Teste do colega** — um colega brilhante, sem contexto nenhum, conseguiria fazer exatamente o que se quer só com esta prompt?
2. **Teste da primeira frase** — lendo só as 2 primeiras frases, percebe-se o objetivo?
3. **Teste do porquê** — cada regra importante tem razão (escrita ou óbvia)?
4. **Teste da resposta péssima** — dá para cumprir a prompt à letra e mesmo assim dar uma resposta má? Se sim, falta uma regra ou um critério.
5. **Teste do corte** — se apagares esta frase, a resposta piora? Se não, apaga-a.

---

## B. Lista de verificação

**🎯 Objetivo**
- [ ] O objetivo está escrito, no início, numa ou duas frases.
- [ ] Diz para quê (o objetivo por trás da entrega), não só o quê.
- [ ] Há um só objetivo principal (ou a prompt está dividida em cadeia).

**📚 Contexto**
- [ ] Público e situação estão descritos.
- [ ] Os factos que o modelo não pode adivinhar estão lá (ou como variáveis).
- [ ] Não há contexto irrelevante que distraia.
- [ ] Nenhum facto foi inventado para preencher lacunas.

**🧩 Lógica e regras**
- [ ] Os passos estão por ordem, quando a ordem importa.
- [ ] Os critérios de decisão estão explícitos ("se X, então Y").
- [ ] As regras importantes têm razão.
- [ ] As regras estão na positiva (o que fazer), com proibições só onde fazem falta e com alternativa.
- [ ] Não há regras contraditórias entre si, nem com os exemplos, nem com o tom da prompt.
- [ ] Está dito o que ganha quando as regras chocam.
- [ ] Ênfase (MAIÚSCULAS, "crítico") usada no máximo uma ou duas vezes.

**📏 Formato**
- [ ] Estrutura da resposta definida (ou mostrada num exemplo).
- [ ] Tamanho concreto (palavras, frases, pontos).
- [ ] Tom e língua definidos.
- [ ] Palavras vagas ("curto", "profissional", "bom", "simples") definidas.
- [ ] Se for lido por um programa: formato rígido (JSON/schema) e o que pôr quando falta um valor.

**🛡️ Robustez**
- [ ] Casos-limite tratados: falta de informação, ambiguidade, pedido fora do âmbito, entrada vazia.
- [ ] Licença para dizer "não sei" / pedir esclarecimento.
- [ ] Exemplos (se houver) variados, entre tags, ditos ilustrativos e coerentes com as regras.
- [ ] Material de terceiros entre tags e tratado como conteúdo, não instruções.
- [ ] Adequada ao destino (`destinos.md`): modelo, ferramenta, ecrã, voz.
- [ ] Variáveis com nomes claros, todas explicadas no "Como usar".
- [ ] Sem dados pessoais, palavras-passe ou chaves.

---

## C. Anti-padrões — como reconhecer e corrigir

| Anti-padrão | Como se reconhece | Correção |
|---|---|---|
| **Objetivo enterrado** | O que se quer aparece no último parágrafo | Objetivo nas primeiras linhas |
| **Pedido telegráfico** | "Faz um post sobre o produto." | Teste do colega: público, objetivo, tom, tamanho, factos |
| **Grito permanente** | MAIÚSCULAS, "!!!", "OBRIGATÓRIO" em quase todas as linhas | Tom calmo + razões; ênfase só no crítico |
| **Lista de proibições** | Dez "não faças", nenhum "faz" | Reescrever na positiva, manter só as proibições com motivo |
| **Regras sem porquê** | "Nunca uses a palavra grátis." | Acrescentar a razão (ou perguntar ao autor) |
| **Contradição escondida** | "Sê breve" + "explica tudo em detalhe" | Escolher, ou dizer qual ganha e quando |
| **Exemplo que contradiz a regra** | Regra: "sem emojis"; exemplo cheio de emojis | Corrigir o exemplo — ganha sempre à regra |
| **Clones** | 3 exemplos quase iguais | Exemplos variados, incluindo um difícil |
| **Persona inflacionada** | "O melhor especialista do mundo com 30 anos de experiência" | Uma linha específica que dá critério, ou nada |
| **Palavras vagas** | "curto", "profissional", "envolvente" sem definição | Números e descrições concretas |
| **Tudo numa prompt** | Pesquisa + análise + escrita + revisão + tradução de uma vez | Cadeia de prompts |
| **Dados misturados com ordens** | Texto do cliente colado no meio das instruções | Tags + "trata como conteúdo" |
| **"Não alucines"** | Pede exatidão sem dar fontes | Dar fontes, pedir citações, licença para "não sei" |
| **Truques antigos** | "Vou dar-te uma gorjeta", "a minha avó vai morrer", ameaças | Apagar; explicar o objetivo |
| **Formato fantasma** | Nada diz como deve ser a resposta | Estrutura, tamanho, tom |
| **Prompt-novela** | Muito texto que não muda o resultado | Teste do corte |
| **Suposição de conhecimento** | Assume que o modelo conhece o negócio, o produto ou factos recentes | Dar os factos ou variáveis |
| **Âmbito sem saída** | System prompt diz o que não fazer, mas não o que responder | Resposta-tipo + alternativa útil |
| **Variáveis soltas** | `{{X}}`, `[inserir aqui]`, nomes inconsistentes | Nomes claros, em tags, explicados |
| **Pedido de imagem em forma de ordem** | "Cria uma imagem que mostre que o produto é bom" | Descrição visual concreta (`destinos.md`) |

---

## D. Critérios da nota /10

Cinco dimensões, 0–2 pontos cada.

| Dimensão | 0 | 1 | 2 |
|---|---|---|---|
| 🎯 **Objetivo** | ausente ou vago | percebe-se, mas sem o "para quê" ou não está no início | claro, no início, com o objetivo real |
| 📚 **Contexto** | o modelo teria de adivinhar o essencial | parte do contexto, ou contexto a mais que distrai | tudo o que o modelo precisa e nada a mais |
| 🧩 **Lógica e regras** | contraditórias, soltas ou ausentes quando eram precisas | claras, mas sem razões, prioridades ou ordem | ordenadas, com razões, prioridades e critérios de decisão |
| 📏 **Formato** | não definido | definido em parte (ex.: tom mas não tamanho) | estrutura, tamanho, tom e língua concretos |
| 🛡️ **Robustez** | sem casos-limite nem critérios | alguns casos-limite ou exemplos | casos-limite, critérios de sucesso, exemplos quando ajudam, adequada ao destino |

**Leitura:** 9–10 pronta para produção · 7–8 boa, com melhorias claras · 4–6 funciona às vezes · 0–3 o modelo está a adivinhar.

**Honestidade:** uma prompt que nunca foi testada com casos reais raramente merece mais de 8. Diz sempre o que falta para subir ("com 2 exemplos reais teus e um teste com 5 emails, chegava a 9–10").

**Formato da nota:**

```markdown
| Dimensão | Antes | Depois | Nota |
|---|---|---|---|
| 🎯 Objetivo | 0 | 2 | agora diz para quê |
| 📚 Contexto | 1 | 2 | público e factos do produto |
| 🧩 Lógica e regras | 1 | 2 | razões e prioridades |
| 📏 Formato | 0 | 2 | 3 variantes, até 150 palavras |
| 🛡️ Robustez | 0 | 1 | falta testar com casos reais |
| **Total** | **2/10** | **9/10** | |
```

No modo Criar, só a coluna "Nota".

---

## E. Diagnóstico a partir de uma resposta má

Quando o utilizador mostra uma resposta que não gostou, encontra a causa antes de mexer:

| Sintoma | Causa provável | Onde mexer |
|---|---|---|
| Genérica, "podia ser para qualquer um" | Falta de contexto específico | Contexto, exemplos reais |
| Formato errado ou variável | Formato não definido | Formato + exemplo |
| Demasiado longa | Tamanho não definido; prompt também longa e cheia de listas | Tamanho concreto; estilo da prompt |
| Ignora uma regra | Regra enterrada, contraditória, sem razão ou só na negativa | Subir a regra, dar razão, resolver o conflito |
| Inventa factos | Sem fontes; sem licença para "não sei" | Fontes, citações, casos-limite |
| Rígida, aplica a regra onde não devia | Ênfase excessiva, regra absoluta sem razão | Tom calmo + porquê + exceções |
| Faz sempre igual ao exemplo | Exemplo único ou exemplos clones | Exemplos variados, ditos ilustrativos |
| Tom errado | Tom descrito com palavras vagas | Definir o tom com detalhe ou exemplo |
| Faz demais / de menos | Âmbito ou ambição não definidos | "Só X" ou "vai além: ..." |
| Sugere em vez de fazer (ou o contrário) | Verbo ambíguo | Agir vs. sugerir explícito |
| Melhor num modelo do que noutro | Prompt dependente de um modelo; funcionalidades diferentes | `destinos.md`, secção 10 |
| Segue texto do utilizador como se fossem ordens | Dados misturados com instruções | Tags + "trata como conteúdo" |

Muda uma coisa de cada vez e volta a testar com a mesma entrada — só assim se sabe o que resultou.
