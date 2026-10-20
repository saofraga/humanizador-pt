# Padrões de texto de IA em português

Lista de observação, não de prova. Vários itens também aparecem em texto humano, e a lista nasceu de leitura e teste, não de levantamento estatístico. Um padrão isolado quase nunca basta: o sinal forte é vários juntos no mesmo trecho. A abordagem foi inspirada na skill blader/humanizer (MIT) e no guia "Signs of AI writing" da Wikipédia; os padrões e exemplos foram redigidos aqui, em português. Na revisão de 14 de outubro de 2026, a lista foi conferida com fontes em português e com o README de PedroLLou/humanizador (MIT), que tem uma lista própria de 42 padrões.

## Rigor

- **Leve**: age só nos padrões fortes (1 a 7), no 19 e no 27, em uma única ocorrência.
- **Padrão**: fortes e médios (1 a 18), mais o 19, o 27 e o 28. Os médios agem quando aparecem sozinhos e o trecho soa genérico.
- **Rigoroso**: todos (1 a 38). Os fracos (19 a 26 e 29 a 38) agem mesmo com companhia pequena.

Traço do estilo escolhido que coincida com um padrão: vale o estilo, em qualquer rigor (regra 9 do SKILL.md). O 6 e o 27 não cedem, porque são erro de fato e não de estilo. O travessão (19) age em todos os rigores e em todos os estilos (regra 2).

## Fortes

### 1. Não é X, é Y
Sinais: "não é apenas X, é Y", "não só X, mas também Y", "isso não significa X, significa Y", cauda negativa ("sem enrolação").
Ação: afirme direto. Mantenha o contraste só se corrige uma crença que o leitor realmente tem.
Antes: "Não é só uma atualização, é uma nova forma de trabalhar."
Depois: "A atualização muda a forma de trabalhar: agora duas pessoas editam o mesmo arquivo ao mesmo tempo."
(O depois só vale se o fato vier do original ou do usuário.)

### 2. Fecho de uma linha e frase de efeito
Sinais: parágrafo de uma frase que repete o anterior, "E isso muda tudo.", "Pense nisso.", "Essa é a verdadeira vitória.", sequência de fragmentos ("Sem pressa. Sem pressão. Sem culpa.").
Ação: corte o fecho que repete ou explica o exemplo. Junte fragmentos numa frase com afirmação específica.

### 3. Frases que soam profundas
Sinais: "no fundo", "no cerne da questão", "a verdadeira questão é", "X é a linguagem de Y", "X vira uma armadilha quando".
Ação: troque pela afirmação concreta.
Antes: "No fundo, o que importa é a prontidão da equipe."
Depois: "O que decide é se a equipe consegue mudar os hábitos."

### 4. Preâmbulo e anúncio
Sinais: "vamos mergulhar", "aqui vai o que você precisa saber", "sem mais delongas", "sendo bem honesto", "a verdade é que" como abertura teatral.
Ação: remova o anúncio e comece pelo ponto. "Sendo honesto" no meio de uma frase casual é normal; o sinal é a abertura solta antes de um ponto banal.

### 5. Discutir com ninguém
Sinais: "não estou dizendo que", "para ser claro", "não me entenda mal", "alguns diriam que", "uma abordagem tentadora seria".
Ação: apague a defesa de objeção que ninguém fez. Se há afirmação real dentro, diga a afirmação. Mantenha objeção com autor nomeado ou respondida por inteiro.

### 6. Resíduo de chat
Sinais: "Claro!", "Ótima pergunta!", "Com certeza!", "Aqui está", "Espero ter ajudado", "Posso ajudar com mais alguma coisa?", "fique à vontade para pedir ajustes".
Ação: tire o invólucro e fique com o conteúdo.

### 7. Aviso de limite de conhecimento e chute
Sinais: "até minha última atualização", "informações limitadas", "não há dados públicos", "provavelmente cresceu em", "acredita-se que".
Ação: diga o que a fonte não mostra, ou corte a frase. Nunca deixe o chute como fato.

## Médios

### 8. Tríades forçadas
Sinais: três adjetivos, três exemplos ou três benefícios em ritmo de lista ("inovação, inspiração e impacto").
Ação: use o número de itens que o sentido pede. Três itens reais ficam.
Antes: "O evento reúne palestras, debates e networking."
Depois: "O evento tem palestras e debates, com intervalos para conversa."

### 9. Inflação de importância
Sinais: "desempenha um papel fundamental", "marco", "divisor de águas", "testemunho de", "reflete uma tendência maior", "legado duradouro", seção "Desafios e perspectivas".
Ação: mantenha o fato, derrube a importância geral ou histórica, a que não tem objeto concreto no texto. Termine no último fato concreto. Opinião ou recomendação, atribuída a alguém ou assumida por quem escreve sobre algo concreto do próprio texto, mantém a força (regra 1 do SKILL.md). O objeto concreto é o sujeito da afirmação: "a proposta é crucial" mantém a força; "a inovação é uma necessidade" cai.

### 10. Vocabulário de IA
Sinais: mergulhar, desvendar, jornada, cenário, panorama, multifacetado, robusto, sinergia, alavancar, potencializar, ecossistema, transformador, impulsionar, vibrante, tapeçaria, crucial, fundamental, essencial (quando enfeite).
Ação: palavra simples no lugar. Termo técnico real fica ("robusto" em estatística, "ecossistema" em biologia). Em opinião ou recomendação, atribuída ou assumida por quem escreve (regra 1 do SKILL.md), a palavra nova tem a mesma força: "é fundamental" vira "é necessário", não "convém".

### 11. Linguagem de propaganda
Sinais: "incrível", "inovador", "de tirar o fôlego", "imperdível", "líder do mercado" sem dado.
Ação: diga o que a coisa é e faz.

### 12. Autoridade emprestada
Sinais: "especialistas afirmam", "estudos mostram", "segundo analistas", lista de veículos de prestígio para provar relevância.
Ação: nomeie a fonte real se o original a traz. Se não traz, **não corte**: mantenha e sinalize ao usuário que falta fonte.

### 13. Gerúndio e particípio decorativos
Sinais: ", destacando a importância de...", ", evidenciando...", ", reforçando o compromisso com...".
Ação: mantenha o fato, tire o enfeite que promete profundidade.

### 14. Fórmulas burocráticas
Sinais: "no que tange a", "diante do exposto", "cabe ressaltar", "vale destacar que", "é importante salientar", "a nível de", "visando", "tecer considerações".
Ação: diga direto. Em texto formal que o estilo ou o gênero pedem (ver Não agir), uma fórmula isolada pode ficar.

### 15. Gerundismo
Sinais: "vou estar enviando", "vamos estar verificando".
Ação: "vou enviar", "vamos verificar".

### 16. Fuga do verbo é/tem
Sinais: "configura-se como", "apresenta-se como", "conta com", "dispõe de", "figura como".
Ação: use "é", "tem", "há".

### 17. Aberturas repetidas e troca de nome
Sinais: várias frases seguidas começando igual; o mesmo sujeito rebatizado a cada frase ("o protagonista", "o herói", "o personagem central").
Ação: junte frases, mude o sujeito, comece pela ação, e use um nome só para a mesma coisa. Repetição deliberada de ritmo pode ficar.

### 18. Pergunta retórica com resposta
Sinais: "E o melhor? ...", "O resultado? ...", "Por quê? Porque...".
Ação: afirme direto. Pergunta que o leitor de fato faria pode ficar.

## Fracos (precisam de companhia, exceto no rigor rigoroso)

### 19. Travessão como conector universal (age em todos os rigores e estilos)
Sinais: pares de travessão no meio de frases, travessão no lugar de vírgula, dois-pontos ou ponto.
Ação: troque por ponto, vírgula, dois-pontos ou parênteses, mesmo com um travessão só (regra 2 do SKILL.md). Diálogo em travessão, de norma, fica.
Antes: "A medida — anunciada sem aviso — atinge milhares."
Depois: "A medida, anunciada sem aviso, atinge milhares."

### 20. Qualificadores empilhados
Sinais: "pode potencialmente talvez", "em alguns casos pode ser que".
Ação: mantenha só o qualificador que a fonte sustenta e que o sentido exige.

### 21. Voz passiva e sujeito oculto
Sinais: "foi realizado o processamento", "é feito o envio", "nenhuma configuração necessária".
Ação: nomeie quem age quando isso esclarece.

### 22. Negrito decorativo e lista com rótulo em negrito
Sinais: negrito em termos soltos; lista em que todo item abre com "**Rótulo:**".
Ação: tire o negrito; vire prosa quando os rótulos não informam.

### 23. Emojis e títulos decorativos
Sinais: emoji em título e item, "Título Com Todas As Palavras Maiúsculas" (calco do inglês), seta como enfeite, aspas curvas fora do padrão do destino.
Ação: maiúscula só inicial, sem emoji, aspas do padrão do usuário. No título do texto, só com autorização (passo 1 do SKILL.md).

### 24. Título repetido na primeira frase e texto sobre o próprio texto
Sinais: título seguido de frase que só o repete; "a tabela abaixo compara"; "este documento foi elaborado a partir de".
Ação: deixe o título trabalhar; descreva o assunto, não o documento. Crédito de fonte e ressalva que muda o que o leitor faz ficam. O título em si só muda com autorização (passo 1 do SKILL.md); sem ela, ajuste a frase que o repete.

### 25. Fecho genérico positivo
Sinais: "o futuro é promissor", "tempos empolgantes pela frente".
Ação: termine no último fato. Se o original traz planos reais, use-os.

### 26. Escrever para o leitor errado
Sinais: resposta a colega que reconta o problema e a prova antes de chegar à decisão.
Ação: comece pela decisão e deixe só o raciocínio que mudaria a concordância do leitor. Só vale quando o contexto da conversa é visível.

## Acréscimos

Numerados depois dos demais para não alterar a numeração existente. O nível de cada um vem indicado.

### 27. Referência inventada (age em todos os rigores)
Sinais: fonte, link, DOI, número de lei, citação ou estudo que não consta do original e não pode ser conferido.
Ação: nunca crie. Se o original traz a referência, mantenha. Se ela parece inexistente, não conserte por cima: sinalize ao usuário para verificar. Vale em todos os rigores, porque é erro de fato e não de estilo.

### 28. Conclusão que só repete (médio)
Sinais: "em suma", "concluindo", "diante do exposto", parágrafo final que resume o que acabou de ser dito sem trazer decisão nem fato novo.
Ação: termine no último fato ou na decisão. Em texto longo, um resumo que ajuda quem pula para o fim pode ficar.

### 29. Conectivos empilhados (fraco)
Sinais: "além disso", "ademais", "dessa forma", "por fim" abrindo parágrafo após parágrafo.
Ação: junte as frases ou comece pela informação. Conectivo isolado não é sinal (ver "Não agir").

### 30. Falsa escala de X a Y (fraco)
Sinais: "de X a Y" em que X e Y não são extremos de uma escala real, como "de gráficos à cultura da empresa" ou "da teoria à prática" usado como enfeite. Extremos de escala real (porte, tempo, distância) ficam: "de pequenas padarias a grandes bancos".
Ação: liste só o que o original ou o usuário disse que existe. Sem lista concreta, corte a amplitude. Escala real (dias, horas, idades, valores, etapas) fica.
Antes: "Atende de pequenas padarias a grandes bancos."
Depois: "Atende padarias e bancos."
(O depois só vale se o fato vier do original ou do usuário.)

### 31. Escrever sobre a versão antiga (fraco)
Sinais: texto que deveria dizer o que a coisa é e faz hoje, mas conta o que ela substituiu ou corrigiu: "esta função foi criada para substituir...", "antes era assim, agora...", "esta versão corrige...".
Ação: descreva o estado atual. O histórico só fica se o original o traz e o gênero o pede (nota de versão, changelog, guia de migração, ata).
Antes: "Esta função foi criada para substituir o antigo método de exportação."
Depois: "A função exporta os dados em CSV."
(O depois só vale se o fato vier do original ou do usuário.)

### 32. Cheiro de tradução do inglês (fraco)
Sinais: expressão calcada do inglês: "no final do dia" ou "ao fim do dia" no sentido de "em suma", "eventualmente" no sentido de "por fim", "endereçar o problema" no sentido de "tratar do problema".
Ação: troque pela expressão em português com o mesmo sentido ("no fim das contas", "por fim", "tratar do problema"). "Eventualmente" no sentido português de "ocasionalmente" fica. Citação e expressão que o próprio usuário usa ficam.
Antes: "No final do dia, precisamos endereçar o problema."
Depois: "No fim das contas, precisamos tratar do problema."

### 33. Vírgula de série importada do inglês (fraco)
Sinais: vírgula antes do "e" final numa enumeração simples: "maçãs, bananas, e laranjas".
Ação: tire a vírgula. Ela fica quando o "e" liga orações de sujeitos diferentes, tem valor de "mas", repete a conjunção, vem antes de "e vice-versa", ou quando a falta dela deixa a leitura ambígua (itens que já têm "e"). Se a amostra do usuário usa a vírgula de série, ela fica (regra 5).
Antes: "Compramos maçãs, bananas, e laranjas."
Depois: "Compramos maçãs, bananas e laranjas."

### 34. Simetria excessiva (fraco)
Sinais: parágrafos de tamanho quase igual em sequência e frases seguidas com a mesma estrutura.
Ação: varie o comprimento e junte as frases paralelas, sem mudar o conteúdo nem acrescentar dado. Paralelismo que o texto pede (comparação, lista de requisitos) fica.
Antes: "A equipe planeja com cuidado. A equipe executa com cuidado. A equipe revisa com cuidado."
Depois: "A equipe planeja, executa e revisa com cuidado."

### 35. Ausência de cena e baixa materialidade (fraco)
Sinais: afirmação genérica sem dado concreto: "cresceu bastante e atende diversos segmentos".
Ação: puxe o dado concreto que o original ou o usuário deu (número, nome, data, caso). Sem dado, pergunte ou escreva a frase mais simples. Nunca invente a cena (regras 1 e 6).
Antes: "A empresa cresceu bastante e atende diversos segmentos."
Depois: "A empresa passou de 12 para 40 clientes em 2025."
(O depois só vale se o fato vier do original ou do usuário.)

### 36. Advérbio em -mente sem função (fraco)
Sinais: advérbio em -mente que não acrescenta informação: "impactou significativamente", "extremamente importante", "profundamente transformador".
Ação: corte o advérbio ou troque pelo dado do original. Advérbio que informa (modo, tempo ou frequência reais) fica. Em opinião ou recomendação atribuída, mantenha a força (regra 1).
Antes: "A mudança foi extremamente importante para o setor."
Depois: "A mudança foi importante para o setor."

### 37. Frases de enchimento (fraco)
Sinais: locução longa onde existe forma curta: "com o intuito de", "devido ao fato de que", "em virtude do fato de que", "no sentido de".
Ação: use "para" ou "porque". "A fim de" isolado não é sinal. A forma longa que o gênero pede (jurídico, ver "Não agir") fica.
Antes: "Cancelamos a reunião devido ao fato de que o fornecedor não respondeu."
Depois: "Cancelamos a reunião porque o fornecedor não respondeu."

### 38. Abertura genérica de contexto (fraco)
Sinais: primeira frase que situa o assunto num cenário amplo, sem dado: "Em um mundo cada vez mais digital", "Nos dias de hoje", "Na era da informação".
Ação: comece pelo ponto do texto. Corte a abertura se ela não traz fato. Se o original dá dado concreto sobre o contexto, mantenha esse dado. Se a abertura também afirma uma importância geral, sem dado nem objeto concreto ("a inovação é uma necessidade"), ela inteira é enfeite sem dono (regra 1): corte e sinalize o corte. Não deixe só o cenário encurtado ("Em um mundo digital, ...").
Antes: "Em um mundo cada vez mais digital, a empresa lançou um aplicativo."
Depois: "A empresa lançou um aplicativo."

## Lastro e falsos positivos

Leitura de 14 de outubro de 2026, em fontes abertas. Com lastro na blader/humanizer 3.1.0 e na página da Wikipédia em inglês "Signs of AI writing": 1, 6, 7, 8, 9, 10, 11, 12, 13, 16, 22, 23 e 25, e de forma fraca 17 e 19. Só na blader: 2, 3, 4, 5, 20, 21, 24 e 26. Lastro parcial: 14. Observação própria, sem fonte lida: 15 e 18. Os padrões 27 a 29 aparecem em fontes em português lidas (Exame, Sabbatini, Wikipédia em português). Padrão 30: heurística, vinda da lista de PedroLLou/humanizador, sem fonte externa lida. Padrões 31 a 37 vêm da lista de PedroLLou/humanizador (31 é o 30 dele, 32 o 36, 33 o 38, 34 o 39, 35 o 40, 36 o 42 e 37 o 23). Fonte lida para parte deles: vírgula antes do "e" (Manual de Comunicação do Senado, EMAG do TRF3 e Ciberdúvidas), "ao fim do dia" como tradução literal (Ciberdúvidas) e "eventualmente" como falso cognato (Cambridge Dictionary e Speaking Brazilian). "Endereçar" no sentido de tratar de um problema não consta da Infopédia, o que não prova calque. O restante é heurística. Do 38 dele (pontuação importada), entrou só a vírgula de série. O nosso 38 é observação própria, sem fonte lida.

As fontes em português lidas são blogs e jornalismo. O único estudo quantitativo encontrado (ACL Anthology, 2026) tem 12 textos. Da lista do padrão 10, só "crucial", "fundamental", "mergulhar" e "transformador" têm menção em fonte em português lida, e a Wikipédia avisa que as palavras mudam a cada geração de modelo.

Falsos positivos com fonte lida. Travessão: professores citados pelo G1 e o Guia do Estudante dizem que, isolado, não indica IA; a Wikipédia diz que humanos o usam e que modelos recentes foram ajustados para evitá-lo. A skill tira o travessão por regra do autor (regra 2), e não por tomá-lo como sinal de IA. Tríades e "não é X, é Y": recursos retóricos humanos comuns, segundo a Wikipédia. Conectivos isolados: não são sinal forte. Voz passiva: um estudo de 2025 em inglês (GPT-4o e Llama 3) encontrou passiva sem agente em cerca de metade da taxa humana, o que enfraquece o padrão 21 como marca de IA. Qualificadores e "é/tem" simples: mais comuns em texto humano. Detectores de IA erram e não contam como evidência.

## Não agir

- Citação, título de obra citada, nome próprio e trecho que discute a expressão em vez de usá-la.
- Título e subtítulos do próprio texto, sem autorização do usuário (passo 1 do SKILL.md).
- Texto de antes de 30 de novembro de 2022.
- Gramática correta, estilo uniforme e prosa seca não são sinais. Texto polido por revisor não é de IA.
- Conectivo comum isolado ("além disso", "portanto"). Só pesa quando se acumula.
- Ressalva legítima: escopo, aviso legal ou de segurança, correção real, objeção com autor, resposta de FAQ.
- Opção que o leitor de fato consideraria num documento técnico.
- Registro jurídico, acadêmico e documental que exige a fórmula (petição, contrato, ata, laudo, parecer, artigo científico): "diante do exposto", "cabe ressaltar", "nos termos de" e a voz passiva técnica ficam, porque são convenção do gênero. Só age a fórmula que se repete sem função.
- Regionalismo, gíria e variedade falada ou escrita pelo autor ("uai", "bah", "oxente", "mano"): ficam como estão, em qualquer rigor.

## Detalhes de voz a manter

Detalhe específico e incomum, sentimento misto, referência datada, escolha de primeira pessoa que o autor sabe explicar, aparte ou autocorreção genuínos, variação de comprimento de frase.

Contração e forma de fala que o próprio texto já tem, em registro informal ("pra", "tá", "né", "num", "pro"): fica como está e não se corrige para a forma culta. Vale só ao humanizar, e nunca se insere onde o original não tem. Com estilo escolhido, vale o estilo.
