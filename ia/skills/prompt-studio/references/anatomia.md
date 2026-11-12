# 📐 Anatomia de uma prompt

Os blocos com que se constrói qualquer prompt de texto. Nem todas precisam de todos: uma prompt simples pode ter só o 1, o 3 e o 7. Usa os que a tarefa pede.

## Índice

1. Os 10 blocos
2. Ordem recomendada
3. Escolher a arquitetura
4. Modelo universal
5. Cadeias de prompts
6. Variáveis e modelos reutilizáveis

---

## 1. Os 10 blocos

| # | Bloco | O que leva | Quando é preciso |
|---|---|---|---|
| 1 | **Objetivo** | O que se quer e para quê, em 1–2 frases | Sempre |
| 2 | **Papel / perspetiva** | Uma linha específica que dá critério ("És revisor técnico de documentação para principiantes") | Quando muda o tom, o nível ou o critério |
| 3 | **Contexto** | Situação, público, porquê, factos que o modelo não sabe | Quase sempre |
| 4 | **Dados / entradas** | O texto, documento ou pergunta a trabalhar, entre tags | Quando há material |
| 5 | **Processo** | Os passos por ordem, as decisões e os critérios | Quando a ordem ou o método importam |
| 6 | **Regras e prioridades** | O que fazer (com razões) e o que ganha quando as regras chocam | Quando há exigências não óbvias |
| 7 | **Formato da resposta** | Estrutura, tamanho, tom, língua, markdown ou não | Sempre que a forma importa (quase sempre) |
| 8 | **Exemplos** | 2–5 exemplos variados de entrada → saída | Quando o estilo ou o formato são difíceis de descrever |
| 9 | **Casos-limite** | O que fazer se faltar informação, se for ambíguo, se estiver fora do tema | Prompts reutilizáveis, system prompts, extração |
| 10 | **Verificação final** | O que confirmar antes de responder | Tarefas onde os erros custam caro |

---

## 2. Ordem recomendada

```
1 Objetivo  →  2 Papel  →  3 Contexto  →  4 Dados (se forem curtos)
→  5 Processo  →  6 Regras  →  8 Exemplos  →  9 Casos-limite
→  7 Formato  →  10 Verificação
```

**Exceção importante — textos longos:** quando os dados são grandes (documentos, transcrições, código), põe-nos **no início**, entre tags, e as instruções e a pergunta **no fim**. Os modelos respondem melhor quando a pergunta vem depois do material.

**O formato perto do fim** funciona bem porque é a última coisa que o modelo lê antes de escrever.

---

## 3. Escolher a arquitetura

```
É para usar uma vez?
├── Sim → a tarefa é curta? ── Sim → PROMPT SIMPLES
│                           └─ Não → PROMPT ESTRUTURADA
└── Não (reutilizável)
    ├── É a "personalidade" de um assistente/bot/GPT? → SYSTEM PROMPT
    ├── Muda só o material de cada vez? → MODELO COM VARIÁVEIS
    └── O modelo vai agir sozinho com ferramentas? → PROMPT DE AGENTE

A tarefa tem fases muito diferentes (pesquisar, decidir, escrever, rever)?
└── Sim → CADEIA DE PROMPTS (uma por fase)

O resultado é imagem, vídeo, música ou voz?
└── Sim → PROMPT DESCRITIVA (ver destinos.md)
```

---

## 4. Modelo universal

O modelo completo, pronto a preencher, está em `assets/modelos/universal.md`. Esqueleto:

```xml
[OBJETIVO — 1–2 frases: o que queres e para quê.]

[PAPEL — opcional, 1 linha.]

<contexto>
[Situação, público, porquê. Os factos que o modelo não pode adivinhar.]
</contexto>

<material>
{{TEXTO_OU_DADOS}}
</material>

Como fazer:
1. [passo]
2. [passo — com o critério de decisão, se houver]
3. [passo]

O que importa (por ordem de prioridade):
- [regra + porquê]
- [regra + porquê]
- Se [regra A] e [regra B] chocarem, [qual ganha].

<exemplos>
<exemplo>
Entrada: ...
Saída: ...
</exemplo>
</exemplos>
(Os exemplos mostram o estilo; não copies o conteúdo.)

Se faltar informação para [X], [pergunta / diz o que falta / usa Y]. Se não souberes, diz que não sabes.

Formato da resposta: [estrutura, tamanho, tom, língua].
```

**Tags XML** — os nomes são livres; o que importa é que sejam claros e consistentes (`<contrato>`, `<email_do_cliente>`, `<regras_da_marca>`). Refere-te a elas no texto ("Usando o contrato em `<contrato>`..."). Ajudam todos os modelos principais, não só o Claude. Alternativa equivalente: títulos em markdown (`## Contexto`).

---

## 5. Cadeias de prompts

Quando uma tarefa tem fases com objetivos diferentes, uma prompt por fase dá resultados melhores e mais fáceis de corrigir.

**Exemplo — artigo para um blog:**

```
Prompt 1 (pesquisa)  → lista de factos com fonte
Prompt 2 (estrutura) → recebe os factos, devolve o esquema do artigo
      ✋ o utilizador aprova o esquema
Prompt 3 (escrita)   → recebe esquema + factos, escreve o artigo
Prompt 4 (revisão)   → recebe o artigo + critérios, devolve correções
```

**Regras das cadeias:**
- Cada prompt tem **uma** tarefa e um formato de saída que serve de entrada à seguinte (tags com nomes claros).
- Põe um ponto de aprovação humana onde um erro sairia caro.
- Uma prompt de revisão separada encontra mais erros do que pedir "e revê no fim" na mesma prompt.
- Quando entregares uma cadeia, mostra o diagrama, as prompts numeradas e como passar a saída de uma para a outra.

---

## 6. Variáveis e modelos reutilizáveis

- Usa `{{NOME_EM_MAIÚSCULAS}}` para o que muda de cada vez. Um nome claro diz o que lá vai: `{{EMAIL_DO_CLIENTE}}`, não `{{X}}`.
- Lista as variáveis no "Como usar", com um exemplo de valor para cada.
- Põe as variáveis **dentro de tags**, para o modelo não as confundir com instruções (sobretudo se vierem de terceiros: emails, formulários, páginas web).
- Partes que não mudam primeiro, variáveis no fim — em APIs com cache de prompts, isto também poupa custos.
- Se a variável puder vir vazia, diz o que fazer nesse caso.
