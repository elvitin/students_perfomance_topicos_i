# Relatório de Análise de Dados — Performance de Estudantes

## 1. Objetivo da etapa

Esta etapa representa o trabalho do profissional de análise de dados após a consolidação da engenharia de dados em arquitetura medalhão.

O foco aqui não é construir a pipeline, mas interpretar os dados já tratados para responder perguntas de negócio:

- O que aconteceu com o desempenho acadêmico dos alunos?
- Quais fatores parecem mais associados ao GPA e ao risco de reprovação?
- Onde a escola deve concentrar ações pedagógicas e de acompanhamento?

## 2. Fonte de dados utilizada

- Base original: Students Performance Dataset, Kaggle.
- Fonte analítica consumida nesta etapa: tabelas `dim_aluno`, `fato_desempenho` e `gold_*` no arquivo `data/data_lakehouse.db`.
- Volume analisado: 2.392 alunos.

## 3. Resumo executivo

Os resultados mostram um cenário de atenção para a instituição.

- 50,63% dos alunos estão na classe `F (GPA < 2.0)`.
- 67,93% foram classificados como `Reprovado/Em Risco` no critério analítico do projeto.
- O GPA médio geral é 1,91 e a mediana é 1,89.
- Faltas aparecem como o fator mais fortemente associado ao desempenho, com correlação de `-0,9193` com o GPA.
- Horas de estudo, suporte parental e tutoria também se destacam como fatores associados a melhores resultados.
- O perfil dedicado, definido como aluno com `estudo >= 10h` e `faltas <= 10`, apresenta GPA médio de `2,99`, muito acima dos `1,68` observados nos demais perfis.

Em linguagem de negócio: a escola precisa olhar primeiro para frequência, hábitos de estudo e rede de apoio, porque esses fatores aparecem com maior peso analítico do que idade ou gênero.

## 4. Leitura dos gráficos do notebook

## Gráfico 1 — Distribuição do GPA

Objetivo: mostrar como o desempenho acadêmico está espalhado ao longo da escala de GPA.

Como analisar: observar onde existe maior concentração de alunos e se a distribuição está mais próxima das faixas altas ou baixas.

O que o gráfico mostra: a distribuição está concentrada em valores baixos e intermediários, com média `1,91` e mediana `1,89`, o que já indica um desempenho geral abaixo do esperado para uma base saudável.

O que ele responde: responde à pergunta “como está o desempenho acadêmico geral da base?”.

## Gráfico 2 — Distribuição percentual por classe de nota

Objetivo: transformar o GPA em classes interpretáveis para facilitar a leitura gerencial.

Como analisar: comparar o percentual de alunos em cada faixa `A`, `B`, `C`, `D` e `F`.

O que o gráfico mostra:

- `A`: 4,47%
- `B`: 11,25%
- `C`: 16,35%
- `D`: 17,31%
- `F`: 50,63%

O que ele responde: responde à pergunta “qual faixa de nota concentra mais alunos?”.

Leitura para apresentação: a principal mensagem é que metade da base está na classe mais crítica, o que reforça a necessidade de intervenção pedagógica.

## Gráfico 3 — Taxa de aprovação versus risco acadêmico

Objetivo: resumir o problema em um KPI simples para gestão.

Como analisar: comparar a participação dos alunos aprovados contra os alunos classificados como em risco ou reprovados.

O que o gráfico mostra:

- `Aprovado`: 32,07%
- `Reprovado/Em Risco`: 67,93%

O que ele responde: responde diretamente à pergunta “o problema é relevante do ponto de vista institucional?”.

Leitura para apresentação: o gráfico mostra que o grupo em risco é mais que o dobro do grupo aprovado, justificando o uso de acompanhamento preventivo.

## Gráfico 4 — Distribuição do GPA por gênero

Objetivo: verificar se existe diferença relevante de desempenho entre masculino e feminino.

Como analisar: comparar mediana, dispersão e concentração dos boxplots. Se as caixas forem muito parecidas, o fator não parece ser determinante.

O que o gráfico mostra: as médias são próximas, com `1,9187` para masculino e `1,8942` para feminino.

O que ele responde: responde à pergunta “gênero parece explicar a maior parte da variação do desempenho?”.

Leitura para apresentação: a diferença é pequena, então gênero não aparece como fator central quando comparado a frequência, estudo e suporte parental.

## Gráfico 5 — GPA médio por faixa de horas de estudo

Objetivo: avaliar a hipótese de que mais tempo de estudo semanal está associado a melhor desempenho.

Como analisar: verificar se existe crescimento consistente do GPA conforme as faixas de estudo aumentam.

O que o gráfico mostra:

- `0-5h`: 1,69
- `5-10h`: 1,85
- `10-15h`: 2,00
- `15-20h`: 2,11

O que ele responde: responde à hipótese de que maior dedicação aos estudos está associada a melhores notas.

Leitura para apresentação: há uma progressão clara e monotônica, o que fortalece a interpretação de que o hábito de estudo é um fator relevante.

## Gráfico 6 — GPA médio por faixa de faltas

Objetivo: medir o efeito da frequência escolar no desempenho.

Como analisar: observar se o GPA cai à medida que a faixa de faltas sobe.

O que o gráfico mostra:

- `0-10 faltas`: 2,86
- `11-20 faltas`: 1,81
- `21-30 faltas`: 0,88

O que ele responde: responde à pergunta “baixa frequência está associada a pior resultado acadêmico?”.

Leitura para apresentação: este é um dos gráficos mais fortes do notebook. A queda do GPA é acentuada e indica que frequência deve ser tratada como indicador prioritário de risco.

## Gráfico 7 — Relação entre horas de estudo e GPA

Objetivo: complementar a análise anterior usando a variável contínua em vez de faixas.

Como analisar: observar a inclinação da linha de tendência e a dispersão dos pontos.

O que o gráfico mostra: a linha de tendência é positiva, indicando que mais horas de estudo se associam a maior GPA, embora exista dispersão entre os alunos.

O que ele responde: responde à pergunta “a relação entre estudo e desempenho é consistente também no nível individual?”.

Leitura para apresentação: o padrão é positivo, mas não absoluto; estudar mais ajuda, porém não explica tudo sozinho.

## Gráfico 8 — Relação entre faltas e GPA

Objetivo: verificar o comportamento individual da relação entre frequência e desempenho.

Como analisar: observar a inclinação da linha de tendência e a força visual da queda.

O que o gráfico mostra: a linha de tendência é fortemente negativa, confirmando que o aumento de faltas acompanha uma queda relevante do GPA.

O que ele responde: responde à pergunta “faltas são apenas um detalhe ou um forte sinal de risco?”.

Leitura para apresentação: faltas não aparecem como detalhe; elas são o principal sinal operacional de risco dentro desta base.

## Gráfico 9 — GPA médio por suporte parental

Objetivo: medir como a rede de apoio familiar aparece na performance dos alunos.

Como analisar: verificar se o GPA cresce à medida que o suporte parental aumenta.

O que o gráfico mostra:

- `Nenhum`: 1,54
- `Baixo`: 1,76
- `Moderado`: 1,88
- `Alto`: 2,04
- `Muito Alto`: 2,19

O que ele responde: responde à hipótese de que maior suporte dos pais está associado a melhores resultados.

Leitura para apresentação: a progressão é clara e consistente, o que faz do suporte parental um dos fatores positivos mais importantes da análise.

## Gráfico 10 — GPA médio com e sem tutoria

Objetivo: avaliar se aulas particulares ou reforço estão associados a melhor desempenho.

Como analisar: comparar diretamente as médias dos dois grupos.

O que o gráfico mostra:

- `Sem tutoria`: 1,82
- `Com tutoria`: 2,11

O que ele responde: responde à hipótese de que tutoria está associada a maior rendimento acadêmico.

Leitura para apresentação: a diferença é relevante e reforça a ideia de que apoio acadêmico direcionado pode ser uma alavanca prática para a escola.

## Gráfico 11 — GPA médio com e sem extracurricular

Objetivo: verificar se participação em atividades extracurriculares se relaciona com melhor desempenho.

Como analisar: comparar as médias entre quem participa e quem não participa.

O que o gráfico mostra:

- `Não`: 1,84
- `Sim`: 2,02

O que ele responde: responde à hipótese de que maior engajamento escolar pode caminhar junto com melhor desempenho.

Leitura para apresentação: extracurricular não é o fator mais forte da base, mas aparece associado a um resultado melhor e pode refletir maior vínculo com a escola.

## Gráfico 12 — GPA médio por escolaridade dos pais

Objetivo: investigar se o nível educacional dos pais aparece como fator explicativo importante.

Como analisar: verificar se existe uma progressão clara entre os níveis de escolaridade.

O que o gráfico mostra: as médias variam pouco, entre `1,81` e `1,94`, e não formam uma sequência monotônica.

O que ele responde: responde à pergunta “escolaridade dos pais, isoladamente, explica o desempenho de forma forte?”.

Leitura para apresentação: o efeito existe, mas é bem mais fraco e menos estável que o de suporte parental, frequência ou tutoria. Isso exige cautela na interpretação.

## Gráfico 13 — GPA médio por perfil dedicado

Objetivo: sintetizar duas variáveis centrais do projeto em um perfil comportamental simples.

Como analisar: comparar o GPA médio do grupo dedicado contra os demais alunos.

O que o gráfico mostra:

- `Dedicado (estudo>=10h e faltas<=10)`: 2,99
- `Demais alunos`: 1,68

O que ele responde: responde à pergunta “quando bons hábitos se combinam, a diferença de desempenho fica mais evidente?”.

Leitura para apresentação: sim. Este é um dos gráficos mais didáticos do notebook, porque transforma duas variáveis técnicas em um perfil fácil de explicar ao professor.

## Gráfico 14 — Correlação das variáveis com o GPA

Objetivo: ranquear os fatores que mais se associam ao GPA.

Como analisar: observar o sinal e a magnitude da correlação. Valores positivos indicam associação com melhora do GPA; valores negativos indicam associação com piora.

O que o gráfico mostra:

- `Absences`: `-0,9193`
- `ParentalSupport`: `0,1908`
- `StudyTimeWeekly`: `0,1793`
- `Tutoring`: `0,1451`
- `Extracurricular`: `0,0941`
- `Age`: `0,0003`

O que ele responde: responde à pergunta “quais variáveis parecem mais importantes na priorização analítica?”.

Leitura para apresentação: faltas se destacam muito acima das demais como fator negativo, enquanto suporte parental, estudo e tutoria aparecem como os fatores positivos mais relevantes.

## Gráfico 15 — GPA médio por idade

Objetivo: avaliar se a idade diferencia substancialmente o desempenho.

Como analisar: verificar se existe uma variação ampla entre as idades.

O que o gráfico mostra: as médias ficam praticamente estáveis entre `1,89` e `1,93` nas idades de 15 a 18 anos.

O que ele responde: responde à pergunta “idade é um fator central nesta base?”.

Leitura para apresentação: não. O efeito é pequeno e perde relevância quando comparado a frequência, estudo e suporte.

## Gráfico 16 — GPA médio por suporte parental e tutoria

Objetivo: combinar rede de apoio familiar com apoio acadêmico direto.

Como analisar: observar se a tutoria melhora o GPA dentro de cada nível de suporte parental e identificar a combinação mais favorável e a mais crítica.

O que o gráfico mostra:

- Sem suporte e sem tutoria: `1,49`
- Sem suporte e com tutoria: `1,66`
- Suporte moderado e com tutoria: `2,12`
- Suporte alto e com tutoria: `2,25`
- Suporte muito alto e com tutoria: `2,39`

O que ele responde: responde à pergunta “a tutoria ajuda mesmo quando o contexto familiar é menos favorável?”.

Leitura para apresentação: sim. A tutoria melhora o GPA em todos os níveis de suporte parental, o que sustenta sua utilização como ferramenta de intervenção pedagógica.

## 5. Principais conclusões para apresentar ao professor

1. O problema de negócio é real e grande: metade da base está em `F` e quase 68% dos alunos estão no grupo de risco.
2. Faltas são o indicador analítico mais crítico do projeto e devem ser monitoradas de forma contínua.
3. Mais horas de estudo se associam a melhor GPA, mas o ganho fica muito mais forte quando a frequência também é boa.
4. Suporte parental e tutoria aparecem como alavancas positivas relevantes para o desempenho.
5. Escolaridade dos pais e idade têm efeito bem menor do que hábitos e apoio direto.
6. O perfil dedicado resume bem a lógica do projeto e pode ser usado como mensagem central na apresentação.

## 6. Recomendações práticas

### Para gestão escolar

- Criar alerta precoce para alunos com aumento de faltas.
- Priorizar acompanhamento dos alunos fora do perfil dedicado.
- Usar taxa de risco acadêmico como KPI periódico.

### Para coordenação pedagógica

- Direcionar tutoria para alunos com faltas altas e baixo suporte parental.
- Acompanhar rotinas de estudo como indicador de prevenção.
- Cruzar frequência com intervenções pedagógicas antes da reprovação consolidada.

### Para professores

- Identificar rapidamente quedas de frequência como sinal de piora acadêmica futura.
- Estimular hábitos de estudo fora da sala de aula.
- Usar atividades de reforço e vínculo escolar para grupos mais vulneráveis.

## 7. Fechamento

Esta etapa de análise de dados mostra que a base não deve ser interpretada apenas como um problema de nota, mas como um problema combinado de frequência, rotina de estudo e rede de apoio.

O principal valor analítico do trabalho está em transformar esses padrões em leitura acionável para a escola: quem precisa de intervenção, por que precisa e quais ações têm maior probabilidade de gerar impacto.