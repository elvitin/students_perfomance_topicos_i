# Projeto de Engenharia de Dados — Arquitetura Medalhão
## Análise de Desempenho Acadêmico de Estudantes

---

**Universidade do Oeste Paulista**  
**Sistemas de Informação**  
**Tópicos Especiais Em Sistemas De Informação 1**

---

**Alunos:**

- **Diego Vinicius Brito Matricardi — RA: 262124858**
- **Felipe Huss Mendes Pereira — RA: 262216051**
- **Victor Taveira Rodrigues — RA: 261911759**

---

**Presidente Prudente – SP, 2026**

---

## Sumário

1. [Contexto e Objetivo](#1-contexto-e-objetivo)
2. [Dataset Utilizado](#2-dataset-utilizado)
3. [Instalação do Projeto](#3-instalação-do-projeto)
4. [Arquitetura Medalhão](#4-arquitetura-medalhão)
5. [Camada Bronze](#5-camada-bronze)
6. [Camada Silver](#6-camada-silver)
7. [Camada Gold](#7-camada-gold)
8. [Resultados e KPIs](#8-resultados-e-kpis)
9. [Validação das Hipóteses](#9-validação-das-hipóteses)
10. [Conclusão](#10-conclusão)

---

## 1. Contexto e Objetivo

A dificuldade das instituições de ensino em **identificar antecipadamente alunos com baixo desempenho acadêmico** é um problema real e recorrente. Quando o problema é percebido, muitas vezes já é tarde para intervenções eficazes, resultando em reprovação ou queda no rendimento escolar.

Este projeto aplica a **Arquitetura Medalhão** de Engenharia de Dados sobre um dataset de desempenho de estudantes do ensino médio, com o objetivo de:

- Organizar e qualificar os dados seguindo boas práticas de engenharia de dados
- Calcular KPIs de negócio que permitam identificar padrões de desempenho
- Validar hipóteses sobre os fatores que influenciam o rendimento acadêmico
- Subsidiar intervenções pedagógicas baseadas em dados

**Stakeholders principais:**

| Stakeholder                             | Interesse                              |
| --------------------------------------- | -------------------------------------- |
| Gestores e diretores escolares          | Acompanhar indicadores educacionais    |
| Professores e coordenadores pedagógicos | Realizar intervenções educacionais     |
| Secretarias de educação                 | Melhorar o desempenho geral dos alunos |

---

## 2. Dataset Utilizado

**Nome:** Students Performance Dataset  
**Fonte:** [Kaggle — Rabie El Kharoua](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)  
**Licença:** CC BY 4.0  
**Tipo:** Dataset sintético educacional  
**Registros:** 2.392 alunos  
**Arquivo:** `data/student_performance_dataset.csv`

### Descrição das colunas

| Coluna              | Tipo  | Descrição                                      |
| ------------------- | ----- | ---------------------------------------------- |
| `StudentID`         | int   | Identificador único do aluno (1001–3392)       |
| `Age`               | int   | Idade do aluno (15–18 anos)                    |
| `Gender`            | int   | Gênero: 0 = Masculino, 1 = Feminino            |
| `Ethnicity`         | int   | Etnia (removida na Silver — ver seção 6)       |
| `ParentalEducation` | int   | Nível educacional dos pais (0–4)               |
| `StudyTimeWeekly`   | float | Horas de estudo por semana (0–20h)             |
| `Absences`          | int   | Número de faltas no ano (0–30)                 |
| `Tutoring`          | int   | Aulas particulares: 0 = Não, 1 = Sim           |
| `ParentalSupport`   | int   | Nível de suporte parental (0–4)                |
| `Extracurricular`   | int   | Atividades extracurriculares: 0 = Não, 1 = Sim |
| `Sports`            | int   | Prática de esportes: 0 = Não, 1 = Sim          |
| `Music`             | int   | Atividades musicais: 0 = Não, 1 = Sim          |
| `Volunteering`      | int   | Voluntariado: 0 = Não, 1 = Sim                 |
| `GPA`               | float | Média acadêmica (0.0–4.0)                      |
| `GradeClass`        | int   | Classe de nota-alvo (0=A, 1=B, 2=C, 3=D, 4=F)  |

---

## 3. Instalação do Projeto

### Pré-requisitos

- Python 3.10 ou superior
- pip

### Passos

```bash
# 1. Clone ou acesse o diretório do projeto
cd /caminho/para/eng_dados

# 2. Crie e ative o ambiente virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# 3. Instale as dependências via requirements.txt
pip install -r requirements.txt

# 4. Registre o kernel Jupyter
python -m ipykernel install --user --name python3

# 5. Execute os notebooks em sequência
jupyter nbconvert --to notebook --execute --inplace src/students_performance/bronze.ipynb
jupyter nbconvert --to notebook --execute --inplace src/students_performance/silver.ipynb
jupyter nbconvert --to notebook --execute --inplace src/students_performance/gold.ipynb
```

### Estrutura de arquivos

```
eng_dados/
├── requirements.txt                       ← Dependências do projeto
├── data/
│   ├── student_performance_dataset.csv    ← Dataset original
│   └── data_lakehouse.db                  ← SQLite (gerado automaticamente)
├── src/
│   └── students_performance/
│       ├── bronze.ipynb                   ← Camada Bronze
│       ├── silver.ipynb                   ← Camada Silver
│       └── gold.ipynb                     ← Camada Gold
└── docs/
    ├── gerar_pdf.py                        ← Script de geração do PDF
    ├── relatorio_students_performance.md  ← Este relatório
    └── relatorio_students_performance.pdf ← PDF gerado pelo script
```

### Dependências (`requirements.txt`)

| Pacote       | Versão mínima | Finalidade                         |
| ------------ | ------------- | ---------------------------------- |
| `pandas`     | 2.0.0         | Manipulação e análise de dados     |
| `numpy`      | 1.24.0        | Operações numéricas                |
| `jupyter`    | 1.0.0         | Ambiente de notebooks              |
| `nbconvert`  | 7.0.0         | Execução e conversão dos notebooks |
| `ipykernel`  | 6.0.0         | Kernel Python para Jupyter         |
| `markdown`   | 3.5.0         | Conversão de Markdown para HTML    |
| `weasyprint` | 60.0          | Geração de PDF a partir de HTML    |

> `sqlite3` já está incluso na biblioteca padrão do Python — não requer instalação separada.

### Gerar o PDF

Com o ambiente virtual ativado, execute a partir da raiz do projeto:

```bash
python docs/gerar_pdf.py
```

O script (`docs/gerar_pdf.py`) lê o arquivo Markdown deste relatório, converte para HTML via `markdown` e gera o PDF via `weasyprint`. O PDF é salvo em `docs/relatorio_students_performance.pdf`.

---

## 4. Arquitetura Medalhão

A **Arquitetura Medalhão** (Medallion Architecture) é um padrão de design para organização de dados em um lakehouse. Proposta e popularizada pela Databricks, ela organiza os dados em camadas progressivas de qualidade, nomeadas por analogia a medalhas olímpicas:

```
CSV (Fonte)
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  BRONZE  │  Dados brutos — fidelidade total à origem    │
│  (Raw)   │  Sem transformações, preservação histórica   │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  SILVER  │  Dados limpos e enriquecidos                 │
│ (Cleaned)│  Tipos corretos, duplicatas removidas,       │
│          │  colunas categóricas decodificadas           │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  GOLD    │  Dados prontos para negócio                  │
│(Business)│  Dimensões, tabela fato, KPIs, agregações    │
└─────────────────────────────────────────────────────────┘
    │
    ▼
Dashboards / Modelos Preditivos / Relatórios
```

### Princípios da arquitetura

| Princípio                          | Descrição                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------- |
| **Imutabilidade da Bronze**        | Os dados brutos nunca são modificados; qualquer erro é corrigido na Silver |
| **Progressão de qualidade**        | Cada camada adiciona valor sem destruir a anterior                         |
| **Rastreabilidade**                | É possível rastrear qualquer registro da Gold até sua origem na Bronze     |
| **Separação de responsabilidades** | Cada camada tem uma única função bem definida                              |
| **Governança**                     | Regras de qualidade e compliance (LGPD) são aplicadas na Silver            |

### Implementação neste projeto

Neste projeto, o lakehouse é simulado com um banco **SQLite** (`data_lakehouse.db`), seguindo o mesmo padrão adotado no projeto de vendas (`clients_products_sells`). Em produção, esse banco seria substituído por Delta Lake, Apache Iceberg ou um serviço de nuvem como Azure Data Lake / Databricks.

---

## 5. Camada Bronze

**Arquivo:** `src/students_performance/bronze.ipynb`

### Responsabilidade

Ingestão fiel e sem transformações do dataset original. A camada Bronze representa a "zona de pouso" dos dados, garantindo que a versão bruta seja sempre preservada para auditoria, reprocessamento e rastreabilidade.

### O que o notebook faz

1. **Importa** as bibliotecas `pandas` e `sqlite3`
2. **Estabelece conexão** com o banco SQLite `data/data_lakehouse.db`
3. **Lê** o arquivo `data/student_performance_dataset.csv` com `pandas.read_csv()`
4. **Inspeciona** os dados: shape, tipos de colunas, valores nulos e duplicatas
5. **Grava** o DataFrame na tabela `bronze_students` via `to_sql()` com `if_exists="replace"`
6. **Valida** a gravação consultando a contagem de registros

### Tabela gerada

| Tabela            | Registros | Colunas | Tratamento            |
| ----------------- | --------- | ------- | --------------------- |
| `bronze_students` | 2.392     | 15      | Nenhum — dados brutos |

### Diagnóstico da Bronze

A inspeção inicial revelou:

- **2.392 registros** e **15 colunas**
- **0 valores nulos** em nenhuma coluna
- **0 linhas duplicadas** completas
- **0 StudentIDs duplicados**
- Todos os tipos são numéricos (int/float), adequados para processamento

> **Observação:** A ausência de nulos e duplicatas é esperada em datasets sintéticos como este. Em dados reais, problemas de qualidade seriam mais frequentes e seriam todos tratados na camada Silver.

---

## 6. Camada Silver

**Arquivo:** `src/students_performance/silver.ipynb`

### Responsabilidade

Limpeza, validação, padronização e enriquecimento dos dados da Bronze. A Silver é a camada confiável para análises — os dados já foram tratados e estão prontos para modelagem dimensional.

### O que o notebook faz

#### 1. Remoção da coluna `Ethnicity`

A coluna `Ethnicity` é **removida nesta camada** por dois motivos complementares:

**a) LGPD (Lei Geral de Proteção de Dados — Lei 13.709/2018):**  
Etnia é classificada como **dado sensível** pela LGPD, exigindo consentimento explícito e cuidado especial no tratamento. Em conformidade com a lei, optamos por não persistir esse dado nas camadas analíticas.

**b) Fairness / Equidade Algorítmica:**  
A análise da distribuição revelou forte desbalanceamento:

| Etnia (código)     | Registros   |
| ------------------ | ----------- |
| 0 — Caucasiano     | majoritário |
| 1 — Afro-americano | minoria     |
| 2 — Asiático       | minoria     |
| 3 — Outro          | minoria     |

Esse desbalanceamento poderia induzir viés no modelo preditivo, gerando previsões injustas para grupos minoritários e decisões discriminatórias.

> **Princípio aplicado:** A coluna é removida **na Silver** (e não na Bronze), pois a Bronze deve preservar o dado original. Qualquer decisão de exclusão é feita nas camadas de transformação.

#### 2. Validação e correção de tipos

| Coluna                             | Tipo esperado | Ação                                        |
| ---------------------------------- | ------------- | ------------------------------------------- |
| `StudentID`, `Age`, `Gender`, etc. | `int`         | Conversão via `pd.to_numeric`               |
| `StudyTimeWeekly`, `GPA`           | `float`       | Conversão via `pd.to_numeric`               |
| `GradeClass`                       | `int`         | Conversão de `float` (ex: `2.0`) para `int` |

#### 3. Tratamento de nulos e duplicatas

- Linhas com `StudentID`, `GPA` ou `GradeClass` nulos são removidas
- Duplicatas por `StudentID` são removidas (mantendo a primeira ocorrência)

#### 4. Validação de intervalos

Todos os campos foram validados contra os intervalos documentados no dataset:

| Campo             | Intervalo | Status |
| ----------------- | --------- | ------ |
| Age               | 15–18     | ✅ OK   |
| Gender            | 0–1       | ✅ OK   |
| ParentalEducation | 0–4       | ✅ OK   |
| StudyTimeWeekly   | 0–20      | ✅ OK   |
| Absences          | 0–30      | ✅ OK   |
| GPA               | 0.0–4.0   | ✅ OK   |
| GradeClass        | 0–4       | ✅ OK   |

#### 5. Decodificação de colunas categóricas

Colunas `_label` foram adicionadas para legibilidade humana, sem remover os valores numéricos originais:

| Coluna              | Coluna Label              | Mapeamento                        |
| ------------------- | ------------------------- | --------------------------------- |
| `Gender`            | `Gender_label`            | 0 → Masculino, 1 → Feminino       |
| `ParentalEducation` | `ParentalEducation_label` | 0 → Nenhum … 4 → Pós-Graduação    |
| `ParentalSupport`   | `ParentalSupport_label`   | 0 → Nenhum … 4 → Muito Alto       |
| `Tutoring`          | `Tutoring_label`          | 0 → Não, 1 → Sim                  |
| `Extracurricular`   | `Extracurricular_label`   | 0 → Não, 1 → Sim                  |
| `Sports`            | `Sports_label`            | 0 → Não, 1 → Sim                  |
| `Music`             | `Music_label`             | 0 → Não, 1 → Sim                  |
| `Volunteering`      | `Volunteering_label`      | 0 → Não, 1 → Sim                  |
| `GradeClass`        | `GradeClass_label`        | 0 → A, 1 → B, 2 → C, 3 → D, 4 → F |

### Tabela gerada

| Tabela            | Registros | Colunas                                  |
| ----------------- | --------- | ---------------------------------------- |
| `silver_students` | 2.392     | 22 (14 originais − Ethnicity + 8 labels) |

---

## 7. Camada Gold

**Arquivo:** `src/students_performance/gold.ipynb`

### Responsabilidade

Modelagem dimensional e geração de KPIs prontos para consumo analítico. A camada Gold organiza os dados em tabelas otimizadas para consulta, seguindo o modelo estrela (star schema) com dimensões e tabela fato.

### O que o notebook faz

#### Modelagem dimensional

**`dim_aluno`** — Dimensão com dados descritivos do aluno:

```
dim_aluno
├── StudentID (PK)
├── Age
├── Gender / Gender_label
├── ParentalEducation / ParentalEducation_label
└── ParentalSupport / ParentalSupport_label
```

**`fato_desempenho`** — Tabela fato com indicadores mensuráveis:

```
fato_desempenho
├── StudentID (FK → dim_aluno)
├── StudyTimeWeekly
├── Absences
├── Tutoring / Tutoring_label
├── Extracurricular / Extracurricular_label
├── Sports / Sports_label
├── Music / Music_label
├── Volunteering / Volunteering_label
├── GPA
└── GradeClass / GradeClass_label
```

#### Tabelas KPI geradas

| Tabela Gold                     | Descrição                                      | Hipóteses relacionadas |
| ------------------------------- | ---------------------------------------------- | ---------------------- |
| `gold_distribuicao_gradeclass`  | Contagem e % por classe de nota                | KPI de negócio         |
| `gold_taxa_aprovacao`           | Aprovados vs Reprovados/Em Risco               | KPI de negócio         |
| `gold_gpa_por_suporte_parental` | GPA médio por nível de suporte familiar        | H4                     |
| `gold_gpa_por_educacao_pais`    | GPA médio por nível educacional dos pais       | H5                     |
| `gold_gpa_por_tutoria`          | GPA médio com/sem aulas particulares           | H10                    |
| `gold_gpa_por_extracurricular`  | GPA médio com/sem atividades extracurriculares | H3                     |
| `gold_gpa_faixas_estudo`        | GPA médio por faixa de horas de estudo         | H1, H8                 |
| `gold_gpa_faixas_faltas`        | GPA médio por faixa de faltas                  | H2, H6                 |
| `gold_gpa_por_idade`            | GPA médio por idade                            | H7                     |
| `gold_gpa_perfil_dedicado`      | GPA para alunos dedicados vs demais            | H8, H9                 |
| `gold_correlacao_com_gpa`       | Correlação de Pearson de cada variável com GPA | H1–H10                 |
| `gold_hipoteses_mapeadas`       | Mapeamento das hipóteses para tabelas Gold     | Todas                  |

---

## 8. Resultados e KPIs

### 8.1 Estatísticas gerais

| Métrica              | Valor      |
| -------------------- | ---------- |
| Total de alunos      | 2.392      |
| GPA Médio            | **1,9062** |
| GPA Mediana          | 1,8934     |
| Desvio Padrão do GPA | 0,9152     |

### 8.2 Distribuição por classe de nota

| GradeClass | Descrição       | Quantidade | Percentual |
| ---------- | --------------- | ---------- | ---------- |
| A          | GPA ≥ 3,5       | 107        | **4,47%**  |
| B          | 3,0 ≤ GPA < 3,5 | 269        | **11,25%** |
| C          | 2,5 ≤ GPA < 3,0 | 391        | **16,35%** |
| D          | 2,0 ≤ GPA < 2,5 | 414        | **17,31%** |
| F          | GPA < 2,0       | 1.211      | **50,63%** |

> **Destaque:** Mais da metade dos alunos (50,63%) estão na classe F, com GPA abaixo de 2,0. Isso indica uma distribuição fortemente assimétrica e reforça a urgência de intervenções pedagógicas.

### 8.3 Taxa de aprovação vs reprovação

| Situação                    | Quantidade | Percentual |
| --------------------------- | ---------- | ---------- |
| Aprovado (A, B ou C)        | 767        | **32,07%** |
| Reprovado/Em Risco (D ou F) | 1.625      | **67,93%** |

> **KPI crítico:** Apenas **1 em cada 3 alunos** alcança nota de aprovação. Esse é o principal indicador de negócio que justifica o projeto.

### 8.4 GPA médio por nível de suporte parental

| Suporte Parental | GPA Médio | Qtd. Alunos |
| ---------------- | --------- | ----------- |
| Nenhum           | 1,5401    | 212         |
| Baixo            | 1,7557    | 489         |
| Moderado         | 1,8842    | 740         |
| Alto             | 2,0424    | 697         |
| Muito Alto       | 2,1915    | 254         |

### 8.5 GPA médio por educação dos pais

| Educação dos Pais    | GPA Médio | Qtd. Alunos |
| -------------------- | --------- | ----------- |
| Nenhum               | 1,8930    | 243         |
| Ensino Médio         | 1,9440    | 728         |
| Faculdade Incompleta | 1,9299    | 934         |
| Bacharelado          | 1,8091    | 367         |
| Pós-Graduação        | 1,8158    | 120         |

### 8.6 GPA médio por tutoria (aulas particulares)

| Tutoria | GPA Médio | Qtd. Alunos |
| ------- | --------- | ----------- |
| Não     | 1,8190    | 1.671       |
| Sim     | 2,1083    | 721         |

### 8.7 GPA médio por atividades extracurriculares

| Extracurricular | GPA Médio | Qtd. Alunos |
| --------------- | --------- | ----------- |
| Não             | 1,8383    | 1.475       |
| Sim             | 2,0154    | 917         |

### 8.8 GPA médio por faixa de horas de estudo semanais

| Faixa de Estudo | GPA Médio | Qtd. Alunos |
| --------------- | --------- | ----------- |
| 0–5 horas       | 1,6916    | 595         |
| 5–10 horas      | 1,8491    | 643         |
| 10–15 horas     | 1,9990    | 619         |
| 15–20 horas     | 2,1059    | 535         |

### 8.9 GPA médio por faixa de faltas

| Faixa de Faltas | GPA Médio  | Qtd. Alunos |
| --------------- | ---------- | ----------- |
| 0–10 faltas     | **2,8569** | 845         |
| 11–20 faltas    | 1,8108     | 846         |
| 21–30 faltas    | **0,8753** | 701         |

> **Variável mais crítica:** A diferença de GPA entre alunos com poucas faltas (2,86) e alunos com muitas faltas (0,88) é de **1,98 pontos** — a maior variação observada em todo o dataset.

### 8.10 Perfil dedicado: estudo ≥ 10h/semana E faltas ≤ 10

| Perfil                                | GPA Médio  | Qtd. Alunos |
| ------------------------------------- | ---------- | ----------- |
| Dedicado (estudo ≥ 10h e faltas ≤ 10) | **2,9897** | 409         |
| Demais alunos                         | 1,6827     | 1.983       |

> Alunos "dedicados" têm GPA médio **77,7% superior** ao restante da turma.

### 8.11 Correlação de Pearson com GPA

| Variável            | Correlação com GPA | Interpretação                   |
| ------------------- | ------------------ | ------------------------------- |
| `Absences`          | **−0,9193**        | Correlação negativa muito forte |
| `ParentalSupport`   | +0,1908            | Correlação positiva fraca       |
| `StudyTimeWeekly`   | +0,1793            | Correlação positiva fraca       |
| `Tutoring`          | +0,1451            | Correlação positiva fraca       |
| `Extracurricular`   | +0,0941            | Correlação positiva muito fraca |
| `Music`             | +0,0733            | Correlação positiva muito fraca |
| `Sports`            | +0,0579            | Correlação positiva muito fraca |
| `Volunteering`      | +0,0033            | Sem correlação relevante        |
| `Age`               | +0,0003            | Sem correlação                  |
| `ParentalEducation` | −0,0359            | Sem correlação relevante        |

> **Conclusão estatística:** `Absences` é, de longe, a variável com **maior poder preditivo** sobre o GPA (correlação de −0,92), muito superior a todas as outras variáveis do dataset.

---

## 9. Validação das Hipóteses

### H1 — Mais horas de estudo → melhor GPA

**Status: ✅ CONFIRMADA (parcialmente)**

GPA cresce progressivamente com as horas de estudo: de 1,69 (0–5h) a 2,11 (15–20h). Porém, a correlação de Pearson é de apenas +0,18, indicando uma relação positiva mas moderada. O efeito isolado do estudo é muito menor do que o efeito das faltas.

### H2 — Maior frequência → notas mais altas

**Status: ✅ CONFIRMADA (fortemente)**

Alunos com 0–10 faltas têm GPA médio de 2,86, enquanto alunos com 21–30 faltas têm GPA médio de 0,88. A correlação de −0,92 entre `Absences` e GPA é a mais forte observada no dataset.

### H3 — Extracurricular → melhor engajamento e GPA

**Status: ✅ CONFIRMADA (fracamente)**

Alunos com atividades extracurriculares têm GPA médio ligeiramente superior (2,02 vs 1,84), com correlação de +0,09. O efeito existe mas é pequeno.

### H4 — Maior suporte parental → melhores resultados

**Status: ✅ CONFIRMADA**

Existe uma progressão clara: GPA cresce de 1,54 (sem suporte) a 2,19 (suporte muito alto). A correlação é de +0,19, a mais forte depois de `Absences`.

### H5 — Educação dos pais influencia o desempenho

**Status: ❌ NÃO CONFIRMADA**

Surpreendentemente, não há uma progressão clara. O GPA médio oscila entre 1,81 e 1,94 sem tendência definida, e a correlação é de apenas −0,04. A educação formal dos pais não se traduz em diferença significativa de GPA neste dataset.

### H6 — Histórico de faltas → maior risco de baixo desempenho

**Status: ✅ CONFIRMADA (fortemente)**

Mesma evidência da H2, vista pelo ângulo de risco: alunos com 21–30 faltas têm GPA médio de 0,88, quase inevitavelmente na classe F. É o principal indicador de risco identificado.

### H7 — Idade do aluno influencia o desempenho

**Status: ❌ NÃO CONFIRMADA**

GPA médio por idade: 15 anos (1,90), 16 anos (1,91), 17 anos (1,93), 18 anos (1,89). As diferenças são mínimas e a correlação é de +0,0003 — praticamente nula.

### H8 — Estudo + frequência → notas mais altas

**Status: ✅ CONFIRMADA (fortemente)**

Alunos dedicados (estudo ≥ 10h/semana E faltas ≤ 10) têm GPA médio de 2,99, contra 1,68 dos demais — diferença de 1,31 pontos. A combinação das duas variáveis é muito mais preditiva do que cada uma isoladamente.

### H9 — Combinação hábitos + suporte familiar é fator principal

**Status: ✅ CONFIRMADA (parcialmente)**

As três variáveis mais correlacionadas com GPA são: `Absences` (−0,92), `ParentalSupport` (+0,19) e `StudyTimeWeekly` (+0,18). A combinação delas explica a maior parte da variância no desempenho. A hipótese está correta quanto à relevância combinada, embora `Absences` domine isoladamente.

### H10 — Aulas particulares → maior rendimento

**Status: ✅ CONFIRMADA**

Alunos com tutoria têm GPA médio de 2,11, contra 1,82 dos sem tutoria — diferença de 0,29 pontos. A correlação é de +0,15, confirmando o efeito positivo das aulas particulares.

---

### Resumo da validação

| Hipótese                   | Status                 | Força            |
| -------------------------- | ---------------------- | ---------------- |
| H1 — Horas de estudo       | ✅ Confirmada           | Fraca a moderada |
| H2 — Frequência escolar    | ✅ Confirmada           | **Muito forte**  |
| H3 — Extracurricular       | ✅ Confirmada           | Fraca            |
| H4 — Suporte parental      | ✅ Confirmada           | Moderada         |
| H5 — Educação dos pais     | ❌ Não confirmada       | —                |
| H6 — Faltas e risco        | ✅ Confirmada           | **Muito forte**  |
| H7 — Idade                 | ❌ Não confirmada       | —                |
| H8 — Estudo + frequência   | ✅ Confirmada           | **Forte**        |
| H9 — Combinação de fatores | ✅ Confirmada (parcial) | Moderada a forte |
| H10 — Aulas particulares   | ✅ Confirmada           | Moderada         |

**8 de 10 hipóteses confirmadas (80%)**

---

## 10. Conclusão

Este projeto demonstrou na prática a aplicação da **Arquitetura Medalhão** em um problema educacional real, percorrendo todas as camadas do pipeline de dados:

### O que foi alcançado

1. **Bronze:** Preservação fiel dos 2.392 registros originais, com rastreabilidade completa
2. **Silver:** Dados limpos, tipados, com colunas categóricas decodificadas e a variável sensível `Ethnicity` removida em conformidade com LGPD e princípios de fairness
3. **Gold:** 14 tabelas analíticas — 2 dimensionais, 1 fato e 11 KPIs — prontas para consumo por ferramentas de BI ou modelos de Machine Learning

### Principal descoberta

**A variável `Absences` (número de faltas) possui correlação de −0,92 com o GPA**, sendo o fator mais determinante do desempenho acadêmico neste dataset — muito acima de todas as outras variáveis. Isso sugere que **monitorar e intervir precocemente quando um aluno começa a faltar** é a ação mais eficaz que uma instituição pode tomar.

### Recomendações de negócio

| Recomendação                                                    | Indicador base                                                       |
| --------------------------------------------------------------- | -------------------------------------------------------------------- |
| Implementar alerta automático quando aluno acumular > 10 faltas | `Absences > 10` → GPA médio cai de 2,86 para 1,81                    |
| Ampliar programas de tutoria/reforço                            | Tutoria associada a +0,29 pontos de GPA                              |
| Fortalecer canais de comunicação escola-família                 | Suporte parental associado a +0,65 pontos de GPA (Nenhum→Muito Alto) |
| Criar programas de atividades extracurriculares                 | Extracurricular associado a +0,18 pontos de GPA                      |

### Próximos passos

- **Modelo preditivo:** Usar as tabelas Gold como base para treinar um classificador multiclasse (Random Forest, XGBoost) para prever `GradeClass`
- **Dashboard:** Conectar as tabelas Gold a uma ferramenta de BI (Power BI, Metabase) para monitoramento contínuo
- **Pipeline automatizado:** Substituir a execução manual dos notebooks por um orquestrador (Apache Airflow, Prefect) para atualização periódica dos dados

---

*Relatório gerado em Abril de 2026 — Universidade do Oeste Paulista — Sistemas de Informação*
