# Exemplos de utilização — code-for-noobs

> Exemplos ilustrativos do formato de resposta. As respostas reais variam com o pedido e o nível da pessoa.

---

## Exemplo 1 — "O que é o git?"

### Pedido

> toda a gente me diz para usar git mas eu nao faço ideia do que é

### Resposta

**Em uma frase:** o git guarda o histórico de todas as versões do teu projeto, para poderes voltar atrás sempre que quiseres.

**Imagina que...** estás a escrever um livro e, sempre que acabas um capítulo, tiras uma fotografia a todas as páginas e escreves uma nota atrás: "acabei o capítulo 3". Se amanhã estragares tudo, pegas na fotografia de ontem e continuas dali. O git faz isso ao teu código.

**Passo a passo:**
1. Trabalhas no teu projeto como sempre.
2. Quando uma parte fica pronta, fazes um *commit* — a tal fotografia, com uma nota a dizer o que mudou.
3. O git guarda todos os commits por ordem, como um álbum.
4. Se algo correr mal, podes ver o que mudou entre duas fotografias ou voltar a uma antiga.
5. Se quiseres, envias o álbum para a internet (por exemplo, o GitHub), para teres uma cópia de segurança ou trabalhares com outras pessoas.

**Experimenta:** no Terminal, dentro da pasta de um projeto que já use git, escreve:

```bash
git log --oneline
```

Isto mostra a lista de fotografias (commits) do projeto, da mais recente para a mais antiga, uma por linha. Não muda nada — só mostra.

**Palavras novas:**
- *Commit* — uma fotografia do projeto com uma nota a explicar o que mudou.
- *GitHub* — um site onde guardas os teus projetos git na internet.

Queres mais simples ou mais detalhe?

---

## Exemplo 2 — Um erro

### Pedido

> apareceu isto e a app nao abre: `Fatal error: Unexpectedly found nil while unwrapping an Optional value`

### Resposta

**O que quer dizer:** a app foi buscar uma informação que devia estar lá, mas a "caixa" estava vazia — e em vez de continuar sem ela, parou de vez.

**Porque aconteceu:** no código há um sítio que diz "tenho a certeza de que aqui há um valor" (em Swift, isso escreve-se com um `!`). Desta vez não havia, e a app fechou. Acontece muito quando uma imagem, um ficheiro ou um dado guardado não existe.

**Como resolver:**
1. No Xcode, quando a app parar, aparece uma linha destacada a vermelho. Essa é a linha do problema.
2. Procura nessa linha um `!` (por exemplo `imagem!` ou `UIImage(named: "fundo")!`).
3. Vê o que essa linha está a ir buscar — muitas vezes é um nome de imagem ou ficheiro com uma letra trocada.
4. Corrige o nome, ou cola-me aqui essa linha e eu digo-te exatamente o que mudar.

**Como evitar da próxima vez:** em vez de `!` ("tenho a certeza"), o código pode dizer "se houver valor, usa-o; se não, faz outra coisa". Posso mostrar-te como, se quiseres.

Não te preocupes — este é um dos erros mais comuns em apps de iPhone, e quase sempre é uma coisa pequena.
