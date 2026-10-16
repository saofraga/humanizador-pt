# humanizador-pt

Skill para dar **voz** a textos em português. Ela faz duas coisas, juntas ou separadas:

- **Humanizar**: tira as marcas de texto de IA (fórmulas, tríades forçadas, "não é X, é Y", resíduos de chat) sem mudar o que o texto diz.
- **Estilizar**: reescreve o texto numa voz escolhida entre 38 estilos, de registros de uso (conversacional, jornalístico, técnico, profissional) a tons (sarcástico, clássico, romântico moderno, conservador, filosófico), autores brasileiros, filósofos, autores estrangeiros clássicos e modernos, e a sua própria voz a partir de amostras.

A regra central é a fidelidade: a voz muda a forma, nunca o fato, o número, a data nem o grau de certeza do original.

## Como usar

Depois de instalada, peça em linguagem natural:

```
Humanize este texto: [texto]
Reescreva no estilo machadiano, rigor leve: [texto]
Humanize e deixe jornalístico, mantendo os travessões: [texto]
Aqui está uma amostra minha: [2 ou 3 parágrafos]. Reescreva este texto com a minha voz: [texto]
```

Opções: **rigor** (padrão, leve ou rigoroso), **manter** (padrões que você quer preservar), **amostra** (sua escrita, que vence qualquer regra) e **modo** (colado, arquivo ou embutido).

## Instalação

- **Claude Code**: copie a pasta `humanizador-pt` para `~/.claude/skills/` (ou para `.claude/skills/` do projeto).
- **Claude.ai e Claude Desktop**: compacte a pasta `humanizador-pt` em um ZIP (com a pasta na raiz do ZIP) e envie como skill nas configurações.

## Estrutura

```
humanizador-pt/
  SKILL.md                      passos, opções e regras
  references/
    padroes.md                  29 padrões de texto de IA em português
    perfil-pessoal.md           roteiro do estilo pessoal
    estilos/
      indice.md                 os 38 estilos
      <estilo>.md               um arquivo por estilo
```

Cada arquivo de estilo traz: o que é, traços de forma, quando usar, o que evitar, cuidado de fidelidade e uma amostra sobre o mesmo fato-base, para comparar as vozes.

## Avisos

- Os traços de cada autor e estilo são caracterizações de forma, redigidas aqui a partir de fontes secundárias abertas (enciclopédias, manuais de redação, guias de estilo) e de convenções da skill, e não substituem a leitura das obras. Cada arquivo de estilo traz uma seção "Lastro" que separa o que foi confirmado em fonte lida do que é convenção da skill, sem fonte. Nenhum trecho de autor é reproduzido, e a skill não atribui frases a ninguém.
- Autores vivos (Dan Brown, Stephen King, Harari, Gladwell, Peterson) entram só como forma, sem endosso de ideias nem uso para fingir autoria.
- Sarcasmo pede confirmação, porque ironia pode inverter o sentido.
- A lista de padrões é de observação, não de prova estatística. Vários itens aparecem em texto humano, e um padrão isolado raramente basta.
- Humanizar edita para leitores humanos. Escapar de detectores de IA não é objetivo.

## Créditos e licença

Inspirada na skill [blader/humanizer](https://github.com/blader/humanizer) (licença MIT) e no guia "Signs of AI writing" da Wikipédia (WikiProject AI Cleanup). Os padrões, os estilos e o texto desta skill foram redigidos em português. Na revisão de 14 de outubro de 2026, a lista de padrões foi conferida com fontes em português e com o README de [PedroLLou/humanizador](https://github.com/PedroLLou/humanizador) (licença MIT), que tem uma lista própria de 42 padrões.

Licença MIT. Veja `LICENSE`.
