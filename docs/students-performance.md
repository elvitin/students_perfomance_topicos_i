|                               |                                                                |
| ----------------------------- | -------------------------------------------------------------- |
| ![](data:image/png;base64...) | **Universidade do Oeste Paulista**  **Sistemas de Informação** |

**Alunos:**

**Diego Vinicius Brito Matricardi- RA: 262124858**

**Felipe Huss Mendes Pereira- RA: 262216051**

**Victor Taveira Rodrigues- RA: 261911759**

**Definição de Problema-Projeto**

Tópicos Especiais Em Sistemas De Informação 1

**Presidente Prudente – SP**

**2026**

**Base escolhida para realizar o projeto:**

https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset

1. Contexto

A dor do negócio está relacionada à dificuldade das instituições de ensino em **identificar antecipadamente alunos com baixo desempenho acadêmico**. Muitas vezes, quando o problema é percebido, já é tarde para realizar intervenções eficazes, o que pode resultar em **reprovação ou queda no rendimento escolar**.

O dataset utilizado contém informações sobre estudantes, incluindo dados demográficos, hábitos de estudo, participação em atividades extracurriculares, nível educacional dos pais e outros fatores que podem influenciar o desempenho acadêmico.

Os principais **stakeholders** envolvidos nesse cenário são:

* **Gestores e diretores escolares**, que precisam acompanhar indicadores educacionais
* **Professores e coordenadores pedagógicos**, que podem realizar intervenções educacionais
* **Secretarias de educação**, interessadas em melhorar o desempenho geral dos alunos

2. Objetivo

O objetivo deste projeto é **desenvolver um modelo preditivo capaz de estimar o desempenho acadêmico dos alunos**, classificando-os em categorias de notas com base nas características presentes no dataset.

Com isso, pretendemos **identificar alunos com maior risco de baixo desempenho** de forma antecipada. Dessa forma, a instituição pode tomar medidas como reforço escolar, acompanhamento pedagógico ou outras intervenções para melhorar o desempenho desses estudantes.

3. KPIs

Para avaliar os resultados do projeto, serão utilizados **KPIs técnicos do modelo** e **KPIs de negócio**.

KPIs do modelo (Machine Learning)

* **Acurácia Global** – porcentagem de previsões corretas do modelo (Tudo o que acertou e errou)
* **Acurácia por Classe** - Olhares o que acertou e errou para classe específica.
* **Precision** – precisão na identificação de alunos com baixo desempenho
* **Recall** – capacidade do modelo de identificar corretamente alunos em risco
* **F1-score** – equilíbrio entre precision e recall
* **Matriz de confusão** – análise dos erros e acertos por categoria de nota

KPIs de negócio

* **Taxa de reprovação dos alunos**
* **Taxa de aprovação**
* **Média geral das notas**
* **Quantidade de alunos identificados precocemente com risco de baixo desempenho**
* **Melhoria no desempenho após intervenções pedagógicas**

4. Restrições

Durante o desenvolvimento do projeto, algumas restrições precisam ser consideradas.

LGPD e dados sensíveis

Algumas variáveis do dataset representam **informações pessoais dos alunos**, como gênero, nível educacional dos pais e etnia. Por isso, é importante garantir que o uso desses dados respeite princípios de privacidade e boas práticas de análise de dados.

Fairness (justiça algorítmica)

Durante a análise exploratória, identificamos que a variável **etnia (Ethnicity)** apresenta um **grande desbalanceamento entre suas categorias**, ou seja, algumas etnias possuem muito mais registros do que outras.

Esse desbalanceamento pode gerar problemas como:

* viés no modelo
* menor capacidade de generalização para grupos minoritários
* risco de decisões injustas ou discriminatórias

Além disso, **etnia é considerada um dado sensível**, o que exige maior cuidado em sua utilização.

Por esse motivo, optamos por **remover a variável "Ethnicity" do treinamento do modelo**, com o objetivo de reduzir possíveis vieses e garantir maior equidade nas previsões.

5.**Hipóteses**

Com base nas variáveis presentes no dataset, levantamos algumas hipóteses sobre os fatores que podem influenciar o desempenho acadêmico dos estudantes.

**Hipótese 1**
 Alunos que possuem **mais horas de estudo semanais (StudyTimeWeekly)** tendem a apresentar **melhor desempenho acadêmico**.

**Hipótese 2**
 Alunos com **maior frequência escolar (Attendance)** tendem a obter **notas mais altas**, pois participam mais das aulas e atividades.

**Hipótese 3**
 Alunos que participam de **atividades extracurriculares (Extracurricular)** podem apresentar melhor desempenho devido ao maior engajamento com a escola.

**Hipótese 4**
 Alunos que possuem **maior suporte dos pais (ParentalSupport)** tendem a ter melhores resultados acadêmicos.

**Hipótese 5**
 O **nível de educação dos pais (ParentalEducation)** pode influenciar o desempenho dos alunos, já que pais com maior nível educacional podem oferecer maior apoio no processo de aprendizagem.

**Hipótese 6**
 Alunos que possuem **histórico de faltas ou baixa frequência** podem apresentar **maior probabilidade de baixo desempenho acadêmico**.

**Hipótese 7**
 A **idade do aluno (Age)** pode influenciar o desempenho acadêmico, já que alunos mais velhos ou mais novos dentro da mesma série podem apresentar diferenças no rendimento.

**Hipótese 8**
 Alunos que dedicam **mais tempo aos estudos e possuem maior frequência escolar** têm maior probabilidade de alcançar **notas mais altas nas avaliações**.

**Hipótese 9**
 A combinação entre **hábitos de estudo, frequência escolar e suporte familiar** pode ser um dos principais fatores que explicam o desempenho acadêmico.

**Hipótese 10**

Alunos que tem aulas particulares, tem maior rendimento.
