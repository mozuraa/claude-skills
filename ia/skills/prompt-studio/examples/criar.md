# Exemplo — prompt-studio, modo 🛠️ Criar

> Exemplo ilustrativo, com uma loja fictícia. Mostra a fase 🧭 Compreender (onde a skill mais conversa) e a entrega completa.

---

## 1. Pedido

> quero uma prompt para o chatgpt me ajudar a responder às reviews negativas da minha loja online

## 2. 🧭 Compreender

> ## 🧭 O que percebi
>
> 🎯 **Objetivo:** respostas a críticas negativas — para que quem as ler (sobretudo **futuros clientes**) veja uma loja que se importa e resolve. A resposta é lida por muito mais gente do que quem se queixou.
> 🧩 **Lógica:** crítica → perceber a queixa e se tem razão → reconhecer → explicar/resolver → convidar a continuar em privado.
> 💭 **O que pesa mais:** não parecer defensivo nem copiado; nunca prometer o que a loja não pode cumprir.
> 🖥️ **Onde corre:** ChatGPT, várias vezes → modelo reutilizável onde colas cada crítica.
>
> ⚠️ **Suposições:** respostas em português de Portugal; tratar o cliente por "você".
>
> ❓ **Antes de escrever:**
> 1. **O que vendes** e onde aparecem as críticas? (Google, site, Trustpilot...)
> 2. **O que podes oferecer** quando a loja errou? (a) troca/reembolso conforme a política (b) desconto na próxima compra (c) só pedir desculpa e resolver em privado — se não souberes, assumo (a), sem números.
> 3. **Tom:** (a) próximo e caloroso (b) formal — assumo (a).
> 4. **Tens uma resposta antiga de que gostaste?** Ajuda muito a acertar no tom.

> **Utilizador:** vendo velas artesanais, as reviews são no google. posso oferecer troca ou reembolso dentro de 30 dias e portes grátis na próxima. tom próximo. não tenho exemplos. assinamos "Ana, da Luz de Casa"

## 3. 📦 Entrega

## 🎯 O que percebi

Respostas a críticas negativas no Google da **Luz de Casa** (velas artesanais), escritas a pensar nos futuros clientes que as vão ler. Prioridades: reconhecer sem ser defensivo, oferecer só o que a política permite (troca/reembolso em 30 dias, portes grátis na próxima) e passar a conversa para privado.

## ✨ A prompt

```xml
Vou dar-te uma crítica negativa que a minha loja recebeu no Google. Escreve a resposta
pública da loja. O objetivo principal não é só acalmar quem se queixou: quem vai ler a
resposta são sobretudo futuros clientes, a decidir se confiam em nós. Querem ver uma loja
que ouve, assume os erros e resolve.

<contexto>
A Luz de Casa é uma pequena loja online portuguesa de velas artesanais. Somos poucas
pessoas e cada encomenda é preparada à mão — é por isso que os clientes nos escolhem.
O que podemos oferecer quando falhámos:
- troca ou reembolso até 30 dias após a entrega;
- portes grátis na próxima encomenda.
Não ofereças mais nada (descontos, brindes, prazos de entrega garantidos): não os podemos cumprir.
</contexto>

<critica>
{{CRITICA}}
</critica>

Como fazer:
1. Percebe qual é a queixa concreta e se a crítica tem razão, tem razão em parte, ou
   parece um mal-entendido.
2. Começa por agradecer ou reconhecer a experiência da pessoa, com uma frase que mostre
   que leste a crítica dela (refere o problema concreto, não "lamentamos o sucedido").
3. Se falhámos, assume-o sem desculpas nem "mas". Se for um mal-entendido, esclarece com
   factos e sem corrigir o cliente em tom de lição.
4. Diz o que fazemos para resolver, só com as opções do contexto.
5. Convida a pessoa a escrever-nos para geral@luzdecasa.pt (exemplo) para tratarmos em privado.
6. Assina "Ana, da Luz de Casa".

O que importa:
- Tom próximo e caloroso, a tratar por "você" — somos uma loja pequena e queremos soar
  como pessoas, não como um departamento.
- Nada de frases feitas de apoio ao cliente ("pedimos desculpa pelo incómodo causado",
  "a sua satisfação é a nossa prioridade"): soam a copiar e colar, e quem lê nota.
- Nunca discutas nem culpes o cliente, mesmo que a crítica seja injusta — os futuros
  clientes vão julgar-nos pela forma como respondemos, não pela crítica.
- Se a crítica mencionar dados pessoais (morada, número de encomenda), não os repitas.

Se a crítica for ofensiva ou parecer falsa (por exemplo, fala de um produto que não
vendemos), escreve na mesma uma resposta curta e educada a convidar o contacto privado,
e acrescenta uma nota para mim a explicar porque desconfias.

Formato: 60–110 palavras, um ou dois parágrafos, sem emojis nem listas. Dá-me a resposta
dentro de <resposta> e, se tiveres uma nota para mim, dentro de <nota>.
```

## 🧠 Porque está assim

- **Escrita para os futuros clientes** — era o teu objetivo real, e muda o tom de "defender a loja" para "mostrar como tratamos as pessoas".
- **As ofertas estão fechadas na prompt** — sem isso, o modelo tende a prometer descontos ou prazos que não podes cumprir.
- **As frases feitas estão proibidas com a razão e com o que fazer em vez delas** (referir o problema concreto) — é o maior sinal de resposta "de robô".
- **Críticas falsas ou ofensivas têm um caminho próprio** — é o caso-limite que mais corre mal.
- **A resposta e a nota vêm separadas** — copias só a resposta para o Google.

## 🔧 Como usar

1. Num chat novo do ChatGPT, cola a prompt e substitui `{{CRITICA}}` pelo texto da crítica.
2. Troca o email de exemplo pelo verdadeiro.
3. Para ficar sempre disponível, cola a prompt (sem a parte da crítica) nas instruções de um **Projeto** ou de um **GPT** e, em cada conversa, cola só a crítica.

## 🧪 Como testar

| Caso | Crítica de teste | Deve acontecer |
|---|---|---|
| Normal | "A vela chegou partida e ninguém me respondeu ao email." | Assume as duas falhas, oferece troca/reembolso, convida o contacto privado |
| Difícil | "Cheira bem mas dura metade do que dizem. Caro para o que é." | Não discute; agradece a parte boa; esclarece a duração com factos *só se os tiveres*; sem descontos |
| Limite | "Pior loja de sempre, ladrões!!!" (sem detalhes) | Resposta curta e calma + `<nota>` a dizer que não há queixa concreta |

## 📊 Nota

| Dimensão | Nota | |
|---|---|---|
| 🎯 Objetivo | 2 | escrito para os futuros clientes |
| 📚 Contexto | 2 | loja, ofertas e limites |
| 🧩 Lógica e regras | 2 | passos, razões, prioridades |
| 📏 Formato | 2 | tamanho, tom, saída separada |
| 🛡️ Robustez | 1 | sem exemplos reais teus nem testes feitos |
| **Total** | **9/10** | |

**Para chegar a 10:** testa os 3 casos acima e, quando tiveres 2–3 respostas de que gostes muito, junta-as como exemplos.

Queres uma versão mais curta, a mesma para responder a críticas **positivas**, ou testamos juntos com uma crítica real?
