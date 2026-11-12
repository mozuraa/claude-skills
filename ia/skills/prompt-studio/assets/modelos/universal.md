# Modelo universal — prompt de texto

Copia, apaga os blocos que não precisas e preenche. Os comentários `<!-- -->` são para ti — apaga-os antes de usar.

---

```xml
<!-- 1. OBJETIVO — 1–2 frases: o que queres e para quê. -->
[Quero que ... para que ...]

<!-- 2. PAPEL — opcional, uma linha específica que dá critério. -->
[És ...]

<!-- 3. CONTEXTO — situação, público, porquê; factos que o modelo não sabe. -->
<contexto>
[Quem vai ler/usar o resultado e o que sabe.]
[A situação e porque isto importa.]
[Factos necessários: nomes, números, políticas, datas.]
</contexto>

<!-- 4. MATERIAL — o que o modelo trabalha. Textos longos: põe este bloco no início da prompt. -->
<material>
{{MATERIAL}}
</material>

<!-- 5. PROCESSO — só se a ordem ou o método importam. -->
Como fazer:
1. [passo]
2. [passo — se X, faz Y; se não, faz Z]
3. [passo]

<!-- 6. REGRAS E PRIORIDADES — na positiva, com o porquê. -->
O que importa, por ordem de prioridade:
- [regra], porque [razão].
- [regra], porque [razão].
- Se [regra A] e [regra B] chocarem, [qual ganha].

<!-- 8. EXEMPLOS — 2–5, variados. -->
<exemplos>
<exemplo>
<entrada>[...]</entrada>
<saida>[...]</saida>
</exemplo>
<exemplo>
<entrada>[caso difícil]</entrada>
<saida>[...]</saida>
</exemplo>
</exemplos>
Os exemplos mostram o estilo e o formato; não reutilizes o conteúdo deles.

<!-- 9. CASOS-LIMITE -->
Se faltar [informação], [pergunta / diz o que falta / usa este valor].
Se o pedido estiver fora de [âmbito], [o que responder].
Se não tiveres a certeza, diz isso em vez de adivinhar.

<!-- 7. FORMATO — perto do fim. -->
Formato da resposta: [estrutura], [tamanho], [tom], em [língua].

<!-- 10. VERIFICAÇÃO — só para tarefas onde os erros custam caro. -->
Antes de responderes, confirma que [critério 1] e [critério 2].
```

---

**Versão mínima** (para tarefas simples):

```
[Objetivo + para quê.] [Contexto essencial numa ou duas frases.]
[Formato: estrutura, tamanho, tom.]
```

Exemplo: `Resume esta ata de reunião para a equipa que faltou: quero saber que decisões foram tomadas e quem ficou com que tarefa. Responde com duas listas — "Decisões" e "Tarefas (pessoa — prazo)" — sem mais nada.`
