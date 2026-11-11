# Exemplo de utilização — app-studio, modo Idear

> Exemplo ilustrativo do formato de resposta. As respostas reais variam com o pedido e o contexto.

## Pedido

> Sei programar em SwiftUI e quero fazer um jogo simples para iPhone que consiga acabar num mês. Dá-me ideias.

## Resposta

### 1. Maré Alta — um puzzle de deslizar onde a água sobe a cada jogada

**O que é:** Cada nível é uma grelha pequena com blocos de madeira. Cada jogada faz a água subir uma linha, e tens de levar o barquinho até à saída antes de a grelha ficar submersa. É calmo à primeira vista, mas cada movimento conta.

**Para quem:** Quem joga puzzles curtos no telemóvel (transportes, filas de espera) e gosta de "só mais um nível".

**Como funciona:**
- Desliza blocos para abrir caminho.
- Cada jogada faz subir a água; os blocos submersos deixam de se mexer.
- 3 estrelas consoante o número de jogadas.
- Níveis novos desbloqueiam por mundos (10 níveis cada).

**O que a torna diferente:** Os puzzles de deslizar clássicos não têm pressão de tempo nem estado que muda; aqui a água transforma o tabuleiro a cada jogada.

**Como ganha dinheiro:** Grátis com os 2 primeiros mundos; compra única de 2,99 € para desbloquear o resto. Sem anúncios.

**Esforço:** Baixo — tudo em SwiftUI com uma grelha; sem física nem servidor.

**Primeiros passos:**
1. Modelar a grelha e as regras numa `struct` testável.
2. Fazer 5 níveis em JSON e um ecrã de jogo simples.
3. Escrever um verificador que confirme que cada nível tem solução.
4. Testar com amigos via TestFlight.

**Riscos:** Desenhar níveis bons dá mais trabalho do que o código; o género é concorrido.

### 2. Eco — um jogo de ritmo em que tocas o padrão que acabaste de ouvir

**O que é:** O jogo toca uma sequência curta de sons e luzes; tens de a repetir. Cada ronda acrescenta uma nota e muda ligeiramente o tempo.

**Para quem:** Jogadores casuais e quem gosta de música; funciona bem para jogar a dois, passando o telemóvel.

**Como funciona:**
- Ouvir → repetir → a sequência cresce.
- Modos: clássico, contra-relógio e "duelo" (cada jogador acrescenta uma nota).
- Ranking diário com a mesma sequência para todos.

**O que a torna diferente:** O modo duelo para dois e as sequências diárias partilhadas.

**Como ganha dinheiro:** Grátis com anúncio opcional para continuar; 1,99 € para remover anúncios e desbloquear pacotes de sons.

**Esforço:** Médio — o áudio precisa de latência baixa (AVAudioEngine) e o ranking usa Game Center.

**Primeiros passos:**
1. Protótipo com 4 botões e sons gerados.
2. Medir a latência do toque em dispositivo real.
3. Acrescentar o modo duelo.
4. Ligar o Game Center para o ranking diário.

**Riscos:** Latência de áudio em alguns dispositivos; pouca variedade se não houver modos novos.

**Recomendação:** Começa pela **Maré Alta** — cabe em um mês, não depende de áudio nem de rede, e o verificador de níveis protege-te de puzzles impossíveis. Queres que detalhe os primeiros 5 níveis ou que gere outra ronda com outro tema?
