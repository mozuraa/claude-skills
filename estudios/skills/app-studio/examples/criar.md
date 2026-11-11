# Exemplo de utilização — app-studio, modo Criar

> Exemplo ilustrativo, com uma app fictícia. Mostra o briefing e o plano, que é onde o modo Criar mais conversa com o utilizador.

---

## 1. Pedido

> quero fazer uma app para registar as minhas plantas e quando as rego. só para iphone

## 2. Briefing

> Boa ideia — e simples de fazer bem. Algumas perguntas para eu propor um plano:
>
> 1. **O que deve a app lembrar-te?** Só a rega, ou também adubo, mudar de vaso, luz?
> 2. **Para quem é?** Só para ti, ou queres publicá-la na App Store?
> 3. **Tens Mac e conta de programador da Apple?** (Para testar no teu iPhone e publicar, a conta custa ~99 €/ano.)
> 4. **Os dados devem passar entre o teu iPhone e o iPad?**
> 5. **Como imaginas ganhar dinheiro**, se for publicada? (Grátis, paga, ou grátis com uma versão completa.)

> **Utilizador:** rega e adubo. quero publicar. tenho mac e conta. só iphone. grátis com uma versão completa

## 3. Plano

**MVP (versão 1.0):**
- Adicionar planta: nome, fotografia, local (sala, varanda...), de quantos em quantos dias rega e aduba.
- Ecrã "Hoje": as plantas que precisam de água/adubo hoje, com um toque para marcar como feito.
- Lembretes (notificações locais) à hora que o utilizador escolher.
- Histórico por planta.
- **Versão completa** (compra única): plantas ilimitadas (grátis: 5), widget no ecrã inicial, temas de cor.

**Depois (1.1+):** identificar a planta pela fotografia, dicas por espécie, partilhar com a família.

**Ecrãs:** Hoje · Plantas (lista + detalhe) · Adicionar/editar · Definições (lembretes, versão completa, restaurar compras, privacidade).

**Tecnologia:** **Swift + SwiftUI**, **SwiftData** para os dados (versionado desde o início), notificações locais (sem servidor), **StoreKit 2** para a versão completa, **WidgetKit** para o widget. Sem contas, sem servidor, sem rastreadores — os dados ficam no iPhone (e no backup do iCloud).

**Privacidade:** a app não recolhe dados → etiqueta "Dados não recolhidos" na App Store; Privacy Manifest com o uso de `UserDefaults`; permissões: notificações (pedidas ao criar o primeiro lembrete) e fotografias via seletor do sistema (sem pedir acesso à biblioteca).

**Custos:** conta Apple que já tens; 0 € de serviços. Precisas de um site simples com política de privacidade e suporte (o website-studio faz isto).

**💬 A minha opinião:** o essencial é o ecrã **Hoje** ser instantâneo e satisfatório de usar (um toque, uma pequena animação, a planta "agradece"). É isso que faz as pessoas voltarem. Deixava a identificação por fotografia para depois: é a funcionalidade mais vistosa, mas também a mais difícil e a que menos ajuda a regar a tempo. O limite grátis de 5 plantas parece-me justo: dá para experimentar a sério.

✋ **Avanço com este plano?**

> **Utilizador:** sim, mas queria login com google para guardar as plantas na nuvem

> **Claude:** Percebo — não perder as plantas é importante. Mas com login com Google, a Apple obriga a oferecer também o Iniciar sessão com a Apple, a app passa a ter de permitir apagar a conta, e passas a recolher dados pessoais (etiquetas de privacidade, RGPD). A minha sugestão: **sincronizar com o iCloud** (CloudKit). Fica guardado na nuvem, passa para um iPhone novo automaticamente, não precisa de login nenhum e é grátis. Se um dia quiseres versão Android, aí sim pensamos em contas. Faço com iCloud?
