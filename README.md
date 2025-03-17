
<p align="center"><img src="https://raw.githubusercontent.com/Oliveira-Renato/commerce/production/auctions/static/auctions/images/logo.png" width="60px"></p>

<p align="center"><img src="https://raw.githubusercontent.com/Oliveira-Renato/commerce/production/auctions/static/auctions/images/this.png"></p>

---------------------------------------

# :hammer_and_wrench: Configurando a Aplicacao Django

## :test_tube: Tecnologias Utilizadas:

### Backend:
- **Python 3.12:** Linguagem de programacao principal para o desenvolvimento do backend.
- **Django 3.0.2:** Framework web em Python utilizado para construir a estrutura da aplicacao.
- **SQLite:** Banco de dados leve e embutido utilizado para armazenar os dados da aplicacao.
- **pip:** Gerenciador de pacotes do Python, utilizado para instalar dependencias.
- **venv:** Ambiente virtual para gerenciar dependencias do projeto.

### Ferramentas Adicionais:
- **Git:** Sistema de controle de versao utilizado para gerenciar o codigo-fonte do projeto.
- **GitHub:** Plataforma de hospedagem de codigo-fonte e colaboracao.

## :computer: Pre-requisitos

### Python e pip

- [Baixe e instale o Python](https://www.python.org/downloads/) (certifique-se de instalar a versao 3.12 ou superior).
- Verifique se o `pip` esta instalado corretamente executando:
  ```bash
  python3 -m ensurepip --default-pip
  ```
- Caso nao tenha, instale com:
  ```bash
  sudo apt install python3-pip
  ```

## :gear: Configuracao do Projeto

### 1. **Clonar o Repositorio:**

- Clone o repositorio do seu projeto para o seu ambiente local:
  ```bash
  git clone https://github.com/Oliveira-Renato/seu-repositorio.git
  cd seu-repositorio
  ```

### 2. **Criar e Ativar um Ambiente Virtual:**

- Criar um ambiente virtual:
  ```bash
  python3 -m venv venv
  ```
- Ativar o ambiente virtual:
  ```bash
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate  # Windows
  ```

### 3. **Instalar Dependencias:**

- Com o ambiente virtual ativado, instale as dependencias do projeto:
  ```bash
  pip install -r requirements.txt
  ```

### 4. **Configurar Variaveis de Ambiente:**

- Criar um arquivo `.env` na raiz do projeto e adicionar:
  ```
  SECRET_KEY=sua-secret-key-aqui
  ```
- Caso nao tenha uma `SECRET_KEY`, gere uma com:
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- Instale a biblioteca para carregar o `.env` automaticamente:
  ```bash
  pip install python-dotenv
  ```

### 5. **Executar as Migracoes do Banco de Dados:**

- Aplicar as migracoes para criar as tabelas no banco de dados:
  ```bash
  python manage.py migrate
  ```

### 6. **Executar a Aplicacao:**

- Iniciar o servidor de desenvolvimento do Django:
  ```bash
  python manage.py runserver
  ```
- Acesse a aplicacao pelo navegador:
  ```
  http://127.0.0.1:8000/
  ```

### Observacoes Importantes

- Caso ocorra erro de permissao ao rodar `pip`, use `pip install --user`.
- Sempre ative o ambiente virtual (`source venv/bin/activate`) antes de rodar comandos do Django.
- Nao compartilhe sua `SECRET_KEY` publicamente.
- Para ambiente de producao, utilize um banco de dados mais robusto (PostgreSQL, MySQL, etc.).



# commerce

EBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

This project was developed during the  CS50's Web Programming with Python and JavaScript course, offered by [HarvardX](https://www.edx.org/).

### Site hosted on the [HEROKU](https://dashboard.heroku.com/) plataform, **[click here](https://auctionslisting.herokuapp.com)** to check it out


## :scroll: Lincense

This project is under the MIT license. 
