# Exemplo de utilização — ideias-funcionalidades

> Exemplo ilustrativo do formato de resposta, com uma app fictícia. As respostas reais variam com o pedido e o código da app.

## Pedido

> Tenho uma app de hábitos em React Native (está nesta pasta). Os utilizadores instalam, usam uma semana e desaparecem. Que funcionalidades devia acrescentar?

## Resposta

*(Antes de responder, a skill lê rapidamente os ecrãs e o modelo de dados da app — por exemplo `src/screens/` e `src/store/habits.ts` — para não propor o que já existe.)*

### 1. Dias de descanso — falhar um dia já não apaga a sequência

**O que é:** Cada utilizador ganha 1 "dia de descanso" por semana. Se falhar um hábito, a app usa-o automaticamente e a sequência continua, com um ícone de almofada nesse dia.

**Porque vale a pena:** A maioria das pessoas desiste no dia em que perde uma sequência longa. Isto ataca diretamente a saída ao fim de uma semana.

**Como encaixa na app:** Acrescenta um campo `restDaysLeft` em `src/store/habits.ts`; o cálculo da sequência em `streak.ts` passa a contar dias de descanso; o calendário em `src/screens/HabitDetail.tsx` mostra o ícone.

**Detalhes de design:** 1 dia por semana, não acumula mais de 2; nunca dois dias de descanso seguidos; mostrar uma notificação suave ("Usámos o teu dia de descanso — amanhã continuas").

**Esforço:** Baixo — lógica local, sem servidor.

**Como testar se resultou:** Percentagem de utilizadores ainda ativos ao dia 14 e ao dia 30.

### 2. Resumo de domingo — a semana numa imagem

**O que é:** Ao domingo à noite, uma notificação abre um ecrã com a semana: hábitos cumpridos, melhor sequência e uma frase de incentivo, com botão para partilhar a imagem.

**Porque vale a pena:** Dá uma razão para abrir a app mesmo a quem já se esqueceu dela, e a partilha traz utilizadores novos.

**Como encaixa na app:** Novo ecrã `src/screens/WeeklySummary.tsx`; usa os dados já guardados; notificação local agendada com a biblioteca de notificações que a app já usa.

**Detalhes de design:** Só aparece se o utilizador teve pelo menos 1 hábito na semana; a imagem tem o nome da app discreto num canto.

**Esforço:** Médio — o ecrã é simples, mas gerar e partilhar a imagem exige alguns testes por plataforma.

**Como testar se resultou:** Taxa de abertura da notificação de domingo e número de partilhas por semana.

**Recomendação:** Começa pelos **Dias de descanso** — é a de melhor valor/esforço e atinge exatamente o problema da primeira semana. Queres que a implemente?
