# Pipeline de Dados com Apache Airflow
Este projeto é um pipeline de dados automatizado construído com Apache Airflow que extrai dados climáticos da API da Visual Crossing, processa-os e os salva em arquivos CSV. O pipeline é agendado para rodar semanalmente.

## Tecnologias Utilizadas
- Python: Linguagem de programação principal.

- Apache Airflow: Orquestrador de workflows para agendamento e execução do pipeline.

- Pandas: Biblioteca para manipulação e processamento dos dados.

- Visual Crossing Weather API: Fonte dos dados climáticos.

### Configuração e Execução
Siga os passos abaixo para configurar e rodar o projeto em sua máquina.

#### 1. Pré-requisitos
Certifique-se de que você tem o Python (versão 3.8 ou superior) e o pip instalados.

#### 2. Clonar o Repositório
Abra seu terminal e execute o comando git clone para baixar o projeto:

```bash
git clone https://github.com/lucasghidini/pipeline_airflow_dados_climaticos.git
```
Em seguida, navegue até a pasta do projeto:
```Bash

cd pipeline_airflow_dados_climaticos
```
#### 3. Configurar o Ambiente
É altamente recomendado usar um ambiente virtual para isolar as dependências do projeto.

```bash

python -m venv venv
source venv/bin/activate
```
Agora, instale as bibliotecas necessárias listadas no requirements.txt:

```bash

pip install -r requirements.txt
```
#### 4. Configurar a Chave da API
Este projeto usa uma chave de API para acessar os dados. Para mantê-la segura, você deve criar um arquivo de variáveis de ambiente.

* Crie uma conta na Visual Crossing Weather para obter sua chave de API.

* Crie um novo arquivo chamado .env na pasta principal do projeto.

Adicione sua chave de API ao arquivo, conforme o exemplo abaixo:
```
KEY='sua_chave_de_api_aqui'
```
#### 5. Executar o Airflow
Siga os comandos abaixo para inicializar o Airflow, criar o banco de dados e iniciar o servidor web.

```

airflow db init
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@example.com
airflow standalone
```
##### Acesse a interface do Airflow em seu navegador (geralmente em http://localhost:8080), encontre o DAG chamado dados_climatico e ative-o. O pipeline será executado automaticamente de acordo com seu agendamento.

### Como o Pipeline Funciona
#### O pipeline consiste em duas tarefas principais:

* criar_pasta: Uma tarefa BashOperator que cria uma pasta com a data da execução para organizar os arquivos de saída.

* extrair_dados: Uma tarefa PythonOperator que faz a chamada à API, extrai os dados, e salva os arquivos CSV na pasta criada pela primeira tarefa. Os dados são divididos em três arquivos separados:

dados_brutos.csv (todos os dados da API);

temperaturas.csv (dados de temperatura);

condicoes.csv (descrição das condições climáticas)

Feito por Lucas Ghidini
