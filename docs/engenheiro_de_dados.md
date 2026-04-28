<!-- Slide number: 1 -->
# Engenharia de Dados
João Guelfi
2026

### Notes:

<!-- Slide number: 2 -->
Problema Real
Uma empresa possui diferentes fontes de dados
Venda diária (arquivo csv)
Clientes (Banco de dados relacional)
Dólar (API externa)

Seus executivos querem desenvolver Dashboards criar um modelo de IA para prever a demanda do próximo mês.

Problemas encontrados
Dados espalhados
Dados inconsistentes
Atualização manual
sem governança

### Notes:

<!-- Slide number: 3 -->
Stack
Orquestração
Apache Airflow
Databricks
Modelagem e transformação
dbt
SQL
Python
Visualização
Power BI
Qliksense
Versionamento e DevOps
Github
Gitlab
Linguagens
Python
SQL
Armazenamento
PostgreSQL
DuckDB
Amazon S3
Azure Data Lake
Processamento
Apache Spark
Pandas

### Notes:

<!-- Slide number: 4 -->
Fato X Dimensão
Tabela Fato
Tabela que representa eventos do negócio. Contém métricas (valores numéricos) e cresce rapidamente possuindo chaves estrangeiras.
Nomenclatura com prefixo fat.

Tabela Dimensão
Tabela que descreve o contexto dos fatos. Dados são descritivos e têm baixa volumetria, usada para filtros e agrupamentos.
Nomenclatura com prefixo dim.
dim_cliente
fat_vendas
| data_id    | cliente_id | produto_id | valor |
| ---------- | ---------- | ---------- | ----- |
| 1          | 10         | 100        | 200   |
| 2          | 12         | 101        | 150   |
| cliente_id | nome       | cidade     | idade |
| ---        | ---        | ---        | ---   |
| 10         | João       | SP         | 30    |
| 12         | Maria      | RJ         | 25    |

### Notes:

<!-- Slide number: 5 -->
Arquitetura Medalhão

![](GoogleShape130g3d6128f313f_0_36.jpg)

### Notes:

<!-- Slide number: 6 -->
Arquitetura Medalhão

![](GoogleShape136g3d6128f313f_0_41.jpg)
Dados brutos, exatamente como chegam.
Sem tratamento, pode conter erros e alta volumetria.

### Notes:

<!-- Slide number: 7 -->
Arquitetura Medalhão

![](GoogleShape144g3d6128f313f_0_51.jpg)
Dados limpos e padronizados. Com remoção de inconsistências, tratamento de nulos, tipagem correta e deduplicação.

### Notes:

<!-- Slide number: 8 -->
Arquitetura Medalhão

![](GoogleShape152g3d6128f313f_0_62.jpg)
Dados prontos para negócio. Agregações, KPIs e modelagem dimensional (fato/dimensão)

### Notes:

<!-- Slide number: 9 -->
Arquitetura Medalhão
vendas.csv
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
produtos.csv
| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |

### Notes:

<!-- Slide number: 10 -->
Arquitetura Medalhão
vendas.csv
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |

### Notes:

<!-- Slide number: 11 -->
Arquitetura Medalhão
vendas.csv
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| ---      | ---        | ---        | ---        | ---   | ---          |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
vendas - Bronze

### Notes:

<!-- Slide number: 12 -->
Arquitetura Medalhão
vendas - Bronze
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |

### Notes:

<!-- Slide number: 13 -->
Arquitetura Medalhão
vendas - Bronze
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 2        | 2026-01-01 | 11         | 99         | -50   | Maria        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| ---      | ---        | ---        | ---        | ---   | ---          |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
vendas - Silver

### Notes:

<!-- Slide number: 14 -->
Arquitetura Medalhão
vendas - Silver

| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |

### Notes:

<!-- Slide number: 15 -->
Arquitetura Medalhão
vendas - Silver

| order_id | data       | cliente_id | produto_id | valor | nome_cliente |
| -------- | ---------- | ---------- | ---------- | ----- | ------------ |
| 1        | 2026-01-01 | 10         | 100        | 200   | Pedro        |
| 3        | 2026-01-01 | 10         | 104        | 175   | Pedro        |
fat_vendas - Gold

dim_cliente - Gold

| order_id   | data         | cliente_id | produto_id | valor |
| ---------- | ------------ | ---------- | ---------- | ----- |
| 1          | 2026-01-01   | 10         | 100        | 200   |
| 3          | 2026-01-01   | 10         | 104        | 175   |
| cliente_id | nome_cliente |
| ---        | ---          |
| 10         | Pedro        |

### Notes:

<!-- Slide number: 16 -->
Arquitetura Medalhão
produtos.csv
| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |

### Notes:

<!-- Slide number: 17 -->
Arquitetura Medalhão
produtos.csv
produtos - Bronze
| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |
| produto_id | produto_nome |
| ---        | ---          |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |

### Notes:

<!-- Slide number: 18 -->
Arquitetura Medalhão
produtos - Bronze
| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |

### Notes:

<!-- Slide number: 19 -->
Arquitetura Medalhão
produtos - Bronze
produtos - Silver
| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
|            | D            |
| produto_id | produto_nome |
| ---        | ---          |
| 100        | A            |
| 99         | B            |
| 104        | C            |
| 105        | D            |

### Notes:

<!-- Slide number: 20 -->
Arquitetura Medalhão
produtos - Silver

| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
| 105        | D            |

### Notes:

<!-- Slide number: 21 -->
Arquitetura Medalhão
produtos - Silver

dim_produto - Gold

| produto_id | produto_nome |
| ---------- | ------------ |
| 100        | A            |
| 99         | B            |
| 104        | C            |
| 105        | D            |
| produto_id | produto_nome |
| ---        | ---          |
| 100        | A            |
| 99         | B            |
| 104        | C            |
| 105        | D            |

### Notes:

<!-- Slide number: 22 -->

### Notes:
