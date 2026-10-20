# humanizador-pt

Skill para dar **voz** a textos em português. Ela faz três coisas, juntas ou separadas:

- **Humanizar**: tira as marcas de texto de IA (fórmulas, tríades forçadas, "não é X, é Y", resíduos de chat) sem mudar o que o texto diz.
- **Estilizar**: reescreve o texto numa voz escolhida entre 38 estilos, de registros de uso (conversacional, jornalístico, técnico, profissional) a tons (sarcástico, clássico, romântico moderno, conservador, filosófico), autores brasileiros, filósofos, autores estrangeiros clássicos e modernos, e um registro formal e solene.
- **Escrever**: transforma anotações, tópicos ou fatos soltos em texto, já sem marcas de IA e, se você pedir, num dos estilos. Usa só os fatos que você der, e o que faltar ela pergunta, nunca inventa.

A regra central é a fidelidade: a voz muda a forma, nunca o fato, o número, a data, o grau de certeza nem a relação entre os fatos do original (ou das suas anotações, no ramo escrever).

## Como usar

Depois de instalada, peça em linguagem natural:

```
Humanize este texto: [texto]
Reescreva no estilo machadiano, rigor leve: [texto]
Humanize e deixe jornalístico, mantendo as tríades: [texto]
Escreva um aviso a partir destas anotações, no estilo jornalístico: [anotações]
Só aponte o que parece texto de IA, sem reescrever: [texto]
Aqui está uma amostra minha: [2 ou 3 parágrafos]. Reescreva este texto com a minha voz: [texto]
```

Opções: **rigor** (padrão, leve ou rigoroso), **manter** (padrões que você quer preservar), **amostra** (sua escrita, que vence estilo e padrões, salvo fidelidade e travessão), **apontar** (só lista os trechos que parecem texto de IA, sem reescrever) e **modo** (colado, arquivo ou embutido). No modo arquivo, a skill aceita .txt e .md e grava o resultado ao lado do original, com sufixo (por exemplo, relatorio.humanizado.md), sem sobrescrever. O ramo escrever só funciona nos modos colado e embutido.

## Instalação

- **Claude Code**: copie a pasta `humanizador-pt` para `~/.claude/skills/` (ou para `.claude/skills/` do projeto).
- **Claude.ai e Claude Desktop**: compacte a pasta `humanizador-pt` em um ZIP (com a pasta na raiz do ZIP) e envie como skill nas configurações.

## Estrutura

```
humanizador-pt/
  SKILL.md                      passos, opções e regras
  references/
    padroes.md                  38 padrões de texto de IA em português
    estilos/
      indice.md                 os 38 estilos
      <estilo>.md               um arquivo por estilo
```

Cada arquivo de estilo traz: o que é, traços de forma, quando usar, o que evitar, cuidado de fidelidade e uma amostra sobre o mesmo fato-base, para comparar as vozes.

## Avisos

- Os traços de cada autor e estilo são caracterizações de forma, redigidas aqui a partir de fontes secundárias abertas (enciclopédias, manuais de redação, guias de estilo) e de convenções da skill, e não substituem a leitura das obras. Cada arquivo de estilo traz uma seção "Lastro" que separa o que foi confirmado em fonte lida do que é convenção da skill, sem fonte. Nenhum trecho de autor é reproduzido, e a skill não atribui frases a ninguém.
- Autores vivos (Dan Brown, Stephen King, Harari, Gladwell, Peterson) entram só como forma, sem endosso de ideias nem uso para fingir autoria.
- Sarcasmo pede confirmação, porque ironia pode inverter o sentido.
- Quando precisa de uma decisão sua (título, sarcasmo, estilo ambíguo), a skill pergunta tudo de uma vez, no começo. Sem como perguntar, segue o padrão mais seguro e lista as suposições.
- A skill só altera o título e os subtítulos do texto com a sua autorização: quando houver título, ela pergunta se pode mexer e, se puder, como.
- A skill não usa travessão como pontuação em nenhum estilo, rigor ou modo, nem a pedido. O travessão que marca fala em diálogo é preservado.
- A lista de padrões é de observação, não de prova estatística. Vários itens aparecem em texto humano, e um padrão isolado raramente basta.
- Humanizar edita para leitores humanos. Escapar de detectores de IA não é objetivo.

## Créditos e licença

Inspirada na skill [blader/humanizer](https://github.com/blader/humanizer) (licença MIT) e no guia "Signs of AI writing" da Wikipédia (WikiProject AI Cleanup). Os padrões, os estilos e o texto desta skill foram redigidos em português. Na revisão de 14 de outubro de 2026, a lista de padrões foi conferida com fontes em português e com o README de [PedroLLou/humanizador](https://github.com/PedroLLou/humanizador) (licença MIT), que tem uma lista própria de 42 padrões.

Licença MIT. Veja `LICENSE`.
