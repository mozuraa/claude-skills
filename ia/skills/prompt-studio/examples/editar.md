# Exemplo — prompt-studio, modo ✏️ Editar

> Exemplo ilustrativo, com uma marca fictícia. Mostra a reconstrução da intenção, o diagnóstico e o antes/depois.

---

## 1. Pedido

> melhora esta prompt, os posts saem sempre genéricos:
>
> "És um expert em marketing com 20 anos de experiência. Escreve um post para o instagram sobre o meu produto. TEM QUE SER BOM E VIRAL!!! NÃO uses muitas hashtags. Não sejas chato. Usa emojis. O produto é um sérum de vitamina C."

## 2. 🔎 Reconstruir a intenção

> **Esta prompt quer** um post de Instagram que faça pessoas interessarem-se pelo sérum de vitamina C — provavelmente para vender ou ganhar seguidores.
> **A lógica implícita é** "um especialista escreve um post que se espalha".
> **Parece assumir** que o modelo sabe quem é a marca, para quem vende, o que torna este sérum diferente e o que é "bom" para ti. Não sabe — por isso escreve o post médio de todos os séruns de vitamina C. É daí que vem o "genérico".

## 3. ❓ O que está a falhar

> Para eu acertar:
> 1. **Tens um exemplo** de um post que saiu e não gostaste? (Ou de um post de que gostaste, teu ou de outra marca.)
> 2. **O que torna o teu sérum diferente?** (concentração, ingredientes, preço, origem, textura...)
> 3. **Para quem é?** (idade, preocupação de pele, o que já experimentaram)
> 4. **O que deve a pessoa fazer** depois de ler? (a) ir ao link na bio comprar (b) guardar/partilhar (c) comentar — assumo (a).
> 5. **O tom da marca:** (a) próximo e divertido (b) científico e sóbrio (c) luxuoso.

> **Utilizador:** é da minha marca, Orvalho. 15% vitamina C estabilizada com ácido ferúlico, sem perfume, feito em portugal, 24€. para mulheres 28-45 com manchas que já tentaram de tudo. querem ir ao link comprar. tom próximo mas honesto, nada de promessas milagrosas. um post que saiu dizia "✨ Descobre o segredo para uma pele radiante! ✨" e odiei

## 4. 🩺 Diagnóstico

🔴 **Grave**
1. **Falta todo o contexto do produto e do público** — "o meu produto" + "sérum de vitamina C". → O modelo não tem nada específico para dizer, por isso escreve clichés. **Correção:** dar os factos (15%, ácido ferúlico, sem perfume, feito em Portugal, 24 €) e o público (28–45, manchas, já tentaram de tudo).
2. **O objetivo está vago** — "TEM QUE SER BOM E VIRAL!!!". → "Viral" não é uma instrução que o modelo possa cumprir e empurra para o exagero ("o segredo para uma pele radiante!"). **Correção:** o objetivo real — levar quem já desconfia de promessas a clicar no link para comprar.

🟡 **A melhorar**
3. **Persona inflacionada** — "expert com 20 anos de experiência" não dá critério nenhum. → Trocar por uma perspetiva que diga como escrever.
4. **Instruções vagas e só na negativa** — "não sejas chato", "não uses muitas hashtags". → Quanto é "muitas"? O que é "chato"? Dizer o que fazer.
5. **Gritos** — MAIÚSCULAS e "!!!" puxam o tom do post para o exagero que odiaste.
6. **Formato não definido** — tamanho, estrutura, chamada para ação.

🟢 **Está bem**
- "Usa emojis" — fica, mas com medida.
- Escolher o Instagram como canal define bem o formato base.

**Nota antes: 2/10**

## 5. ✨ A prompt nova

```xml
Escreve a legenda de um post de Instagram da Orvalho, uma pequena marca portuguesa de
cosmética. O objetivo é levar quem lê a clicar no link da bio para comprar o nosso sérum
de vitamina C — mas o nosso público já desconfia de promessas milagrosas, por isso o
post só convence se soar honesto e concreto.

<produto>
Sérum de vitamina C Orvalho:
- 15% de vitamina C estabilizada com ácido ferúlico (ajuda a vitamina C a manter-se ativa);
- sem perfume;
- feito em Portugal;
- 24 €.
</produto>

<publico>
Mulheres de 28 a 45 anos com manchas na pele que já experimentaram vários produtos e se
desiludiram. Estão cansadas de linguagem de anúncio e respeitam marcas que falam claro.
</publico>

Como escrever:
- Começa com uma primeira linha que a nossa leitora reconheça como dela (a frustração de
  já ter tentado tudo, por exemplo) — é a única linha visível antes do "mais".
- Fala dos factos do produto e do que significam para ela, em linguagem simples.
- Tom próximo e honesto, como uma amiga que percebe de pele: sem promessas de resultados
  garantidos nem prazos ("em 7 dias"), porque além de afastarem este público, não as
  podemos provar.
- Evita frases de anúncio como "o segredo para uma pele radiante" ou "descobre a tua
  melhor versão" — são exatamente o que a nossa leitora já não suporta.
- Até 3 emojis, só onde ajudam a ler.

Formato: 80–130 palavras, frases curtas e parágrafos de 1–2 linhas (lê-se no telemóvel),
terminar com uma chamada clara para o link na bio, e depois 3–5 hashtags específicas
(nada de #beauty ou #skincare sozinhas).

Escreve 3 versões com primeiras linhas diferentes, para eu escolher.
```

## 6. 📦 Antes/depois

| Antes | Depois | Porquê |
|---|---|---|
| "És um expert em marketing com 20 anos..." | Perspetiva: "como uma amiga que percebe de pele" | Dá critério de tom; a experiência inventada não dava |
| "sobre o meu produto" + "sérum de vitamina C" | Bloco `<produto>` com os factos reais | Sem factos, o modelo só tinha clichés para usar |
| (sem público) | Bloco `<publico>` | O post é escrito para alguém concreto e desconfiado |
| "TEM QUE SER BOM E VIRAL!!!" | Objetivo: clicar no link para comprar, sendo honesto | Objetivo que o modelo consegue cumprir; tom calmo |
| "Não sejas chato." | Primeira linha que a leitora reconheça; frases curtas | Diz o que fazer em vez do que evitar |
| (o post que odiaste) | Exemplos de frases a evitar, com o porquê | Usa o exemplo mau que deste — é a informação mais valiosa |
| "NÃO uses muitas hashtags" | 3–5 hashtags específicas | "Muitas" era vago |
| (sem formato) | 80–130 palavras, parágrafos curtos, chamada para ação | Formato pensado para o telemóvel |
| 1 versão | 3 versões com primeiras linhas diferentes | Escolher é mais rápido do que pedir nova tentativa |

| Dimensão | Antes | Depois |
|---|---|---|
| 🎯 Objetivo | 0 | 2 |
| 📚 Contexto | 0 | 2 |
| 🧩 Lógica e regras | 1 | 2 |
| 📏 Formato | 0 | 2 |
| 🛡️ Robustez | 1 | 1 |
| **Total** | **2/10** | **9/10** |

**Para chegar a 10:** junta 1–2 legendas da Orvalho de que gostes como exemplo de voz. Testa com o ChatGPT e, se alguma versão sair com cara de anúncio, mostra-ma — afino a regra que falhou.

---

## Mini-exemplo — "porque é que ignora a minha regra?"

> **Utilizador:** no meu GPT digo "NUNCA dês preços" mas ele dá sempre.

> **Diagnóstico:** a regra está no meio de 40 linhas, só na negativa e sem razão — e mais abaixo há "responde a todas as perguntas dos clientes com detalhe", que a contradiz. Além disso, a tabela de preços está nos documentos do GPT, por isso o modelo tem a resposta à mão.
>
> **Correção:** subir a regra para o bloco de âmbito, com razão e alternativa — "Os preços mudam todas as semanas e só a página da loja está sempre certa. Quando perguntarem preços, não indiques valores: envia o link [loja.exemplo/precos]." — e tirar a tabela de preços dos documentos do GPT.
