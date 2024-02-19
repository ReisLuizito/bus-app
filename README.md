# Bus App

Este é um aplicativo que permite visualizar informações de ônibus, calcular tempos de viagem e receber notificações por e-mail quando um ônibus está a 10 minutos de distância.

## Pré-requisitos

Certifique-se de ter o seguinte instalado em sua máquina antes de começar:

* Python (versão 3.6 ou superior)
* Node.js e npm (para a parte frontend em React)
* Redis (necessário para Celery)

### Clone o repositório:

* https://github.com/ReisLuizito/bus-app.git

### Navegue até o diretório backend

* cd bus-app/backend

### Crie um ambiente virtual e ative-o:

* python -m venv venv
* source venv/bin/activate  # No Windows: venv\Scripts\activate

### Instale as dependências:

* pip install -r requirements.txt

### Inicie o servidor:

* uvicorn main:app --reload

### Em um terminal separado, inicie o Celery para processar tarefas em segundo plano:

* redis-cli

# Configuração do Frontend (React)

### Navegue até o diretório do frontend:

* cd bus-app/frontend

### Instale as dependências do Node.js:

* npm install

### Inicie o servidor de desenvolvimento:

* npm start

# Uso 

* Abra o aplicativo no navegador: http://localhost:3000.
* Preencha a localidade ou ponto desejado na barra de pesquisa.
* Selecione uma linha de ônibus após a pesquisa.
* Visualize as informações sobre ônibus da linha selecionada.
* Para limpar a pesquisa, clique no botão "Limpar Pesquisa".
* Escolha o horário de partida para receber uma notificação por e-mail 10 minutos antes do  ônibus chegar ao ponto cadastrado.
 
