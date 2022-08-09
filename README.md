# API de E-commerce com Django Rest Framework

Este é o Desafio Final do programa [Construdelas](https://womakerscode.org/construdelas) (treinamento de desenvolvedoras), promovido pela [JuntosSomos+](https://www.juntossomosmais.com.br/) e implementado pela [WoMakersCode](https://womakerscode.org/).

## Objetivo
Criar uma API de e-commerce com Django Rest Framework.

## Requisitos básicos
- Deve ser possível cadastrar e listar clientes
- Deve ser possível cadastrar e listar produtos
- Deve ser possível cadastrar e listar pedidos

## Rodando o projeto
- Faça *fork* do projeto
- No terminal da sua máquina, digite:
    - `git clone git@github.com:<seu_usuario>/api_ecommerce_drf.git`, se você tem uma chave SSH no GitHub, ou
    - `git clone https://github.com/<seu_usuario>/api_ecommerce_drf.git`.
- Em seguida, entre na pasta criada no comando anterior usando `cd api_ecommerce_drf`
- Crie seu ambiente virtual, digitando `python3 -m venv venv`
- Ative seu ambiente virtual, digitando `venv\Scripts\activate` no Windows ou `venv/bin/activate` no Linux ou Mac
- Faça download das dependências do projeto, digitando `python3 -m pip install -r requirements.txt`
- Levante o servidor, digitando `python3 manage.py runserver`
- No navegador, acesse o localhost na porta 8000. Em máquinas Windows, você pode acessar o servidor digitando `http://127.0.0.1:8000/` no navegador. 

## Endpoints
- GET `clientes/`, retorna lista de clientes cadastrados
- GET-PUT-DELETE `clientes/<cpf>`, retorna dados de um cliente específico
- POST `clientes/`, fornece campos para criação de um novo cliente
- GET `produtos/`, retorna lista de produtos cadastrados
- GET-PUT-DELETE `produtos/<id>`, retorna dados de um produto específico
- POST `produtos/`, fornece campos para criação de um novo produto
- GET `pedidos/`, retorna lista de pedidos cadastrados
- GET-PUT-DELETE `pedidos/<id>`, retorna dados de um produto específico
- POST `pedidos/`, fornece campos para criação de um novo pedido
- GET `itens/`, retorna lista de itens cadastrados
- GET-PUT-DELETE `itens/<id>`, retorna dados de um item específico
- POST `pedidos/`, fornece campos para criação de um novo item

## Metodologias ágeis
- [Kanban](https://trello.com/b/EN2fH1QY/time-carmen-portinho)

### Lista de tarefas
- [ ] Adicionar endpoint para consulta de pedidos de um cliente específico
- [ ] Adicionar instruções para rodar o script SQL e popular as tabelas
- [ ] Adicionar instruções de como rodar os testes

