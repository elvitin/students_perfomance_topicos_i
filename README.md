# Projeto de Engenharia de Dados — Arquitetura Medalhão

Análise de desempenho acadêmico de estudantes aplicando a **Arquitetura Medalhão** (Bronze → Silver → Gold) sobre um lakehouse SQLite local.

## Estrutura do projeto

```
eng_dados/
├── requirements.txt                          ← Dependências do projeto
├── data/
│   ├── student_performance_dataset.csv       ← Dataset original (Kaggle)
│   └── data_lakehouse.db                     ← SQLite gerado automaticamente
├── src/
│   └── students_performance/
│       ├── bronze.ipynb                      ← Ingestão dos dados brutos
│       ├── silver.ipynb                      ← Limpeza e enriquecimento
│       └── gold.ipynb                        ← Modelo dimensional e KPIs
└── docs/
    ├── relatorio_students_performance.md     ← Relatório completo
    └── relatorio_students_performance.pdf    ← Relatório em PDF
```

## Pré-requisitos

- Python 3.10 ou superior
- pip

## Instalação

```bash
# 1. Acesse o diretório do projeto
cd eng_dados

# 2. Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Registre o kernel Jupyter
python -m ipykernel install --user --name python3
```

## Execução

Execute os notebooks **em sequência**:

```bash
jupyter nbconvert --to notebook --execute --inplace src/students_performance/bronze.ipynb
jupyter nbconvert --to notebook --execute --inplace src/students_performance/silver.ipynb
jupyter nbconvert --to notebook --execute --inplace src/students_performance/gold.ipynb
```

Ou abra os notebooks manualmente no Jupyter e execute célula a célula:

```bash
jupyter notebook
```

Ao final da execução, o arquivo `data/data_lakehouse.db` conterá todas as tabelas das três camadas.

## Camadas

| Camada     | Notebook       | Descrição                                                                                                |
| ---------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| **Bronze** | `bronze.ipynb` | Ingestão sem transformações — espelho do CSV original                                                    |
| **Silver** | `silver.ipynb` | Limpeza, validação de tipos/ranges, remoção de coluna sensível (`Ethnicity`) e adição de labels legíveis |
| **Gold**   | `gold.ipynb`   | Modelo dimensional (`dim_aluno`, `fato_desempenho`) e 11 tabelas de KPIs para análise de desempenho      |

## Dependências

| Pacote       | Versão mínima | Finalidade                          |
| ------------ | ------------- | ----------------------------------- |
| `pandas`     | 2.0.0         | Manipulação de dados                |
| `numpy`      | 1.24.0        | Operações numéricas                 |
| `jupyter`    | 1.0.0         | Ambiente de notebooks               |
| `nbconvert`  | 7.0.0         | Execução dos notebooks via terminal |
| `ipykernel`  | 6.0.0         | Kernel Python para Jupyter          |
| `markdown`   | 3.5.0         | Conversão de Markdown para HTML     |
| `weasyprint` | 60.0          | Geração de PDF a partir de HTML     |

> `sqlite3` faz parte da biblioteca padrão do Python e não requer instalação separada.

## Relatório

O relatório completo com contexto, arquitetura, resultados e validação de hipóteses está disponível em:

- [`docs/relatorio_students_performance.md`](docs/relatorio_students_performance.md)
- [`docs/relatorio_students_performance.pdf`](docs/relatorio_students_performance.pdf)

## Gerar o PDF

Com o ambiente virtual ativado, execute a partir da raiz do projeto:

```bash
python docs/gerar_pdf.py
```

O script lê [`docs/relatorio_students_performance.md`](docs/relatorio_students_performance.md) e sobrescreve [`docs/relatorio_students_performance.pdf`](docs/relatorio_students_performance.pdf). As dependências `markdown` e `weasyprint` já estão declaradas no `requirements.txt`.
