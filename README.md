# API de E-commerce com Django Rest Framework

Este é o Desafio Final do programa [Construdelas](https://womakerscode.org/construdelas) (treinamento de desenvolvedoras), promovido pela [JuntosSomos+](https://www.juntossomosmais.com.br/) e implementado pela [WoMakersCode](https://womakerscode.org/).

## Objetivo
Criar uma API de e-commerce com Django Rest Framework.

## Requisitos básicos
- Deve ser possível cadastrar e listar clientes
- Deve ser possível cadastrar e listar produtos
- Deve ser possível cadastrar e listar pedidos

## Regras de negócio
- O **pedido** é como o carrinho do cliente, onde é possível adicionar itens
- É obrigatório atribuir um **cliente** ao pedido
- Um **item** pode ser entendido como um produto que está no carrinho do cliente
- O **produto**, por sua vez, pode ser entendido como o produto em estoque no sistema de e-commerce
- É obrigatório atribuir um pedido ao item
- Um item tem uma quantidade, que é subtraída da quantidade de produtos em estoque
- É preciso que o produto tenha quantidade suficiente (esteja disponível em estoque) para que a criação do item seja efetuada

## Rodando o projeto

### Clonando o projeto
- No terminal da sua máquina, digite:
    - `git clone git@github.com:<seu_usuario>/api_ecommerce_drf.git`, se você tem uma chave SSH no GitHub, ou
    - `git clone https://github.com/<seu_usuario>/api_ecommerce_drf.git`.
- Em seguida, entre na pasta criada no comando anterior usando `cd api_ecommerce_drf`

### Criando um ambiente virtual
- Crie seu ambiente virtual, digitando `python3 -m venv venv`
- Ative seu ambiente virtual, digitando `.\venv\Scripts\activate` no Windows ou `venv/bin/activate` no Linux ou Mac

### Fazendo download das dependências
- Faça download das dependências do projeto, digitando `python3 -m pip install -r requirements.txt`

### Criando e populando o banco de dados com dados de exemplo
- Crie o banco de dados digitando `python3 manage.py migrate`
- Popule o banco com dados iniciais digitando `python3 manage.py popular_tabelas`. **Atenção:** Este comando deve ser rodado apenas uma vez.

### Testes
- Teste a aplicação digitando `coverage run manage.py test`
- Verifique a cobertura de testes digitando `coverage report -m`

### Criando superusuário (opcional)
- Se preferir, crie um superusuário digitando `python3 manage.py createsuperuser` e siga as intruções para criar seu superusuário

### Acessando a API
- Levante o servidor, digitando `python3 manage.py runserver`
- No navegador, acesse o localhost na porta 8000. Em máquinas Windows, você pode acessar o servidor digitando `http://127.0.0.1:8000/` no navegador.

### Usando a API
- Adicione itens a um pedido no endpoint `itens/`.
- Confira o pedido ao qual você adicionou itens usando o método get no endpoint `pedidos/<id>/`
- Acesse a área administrativa digitando no navegador `http://127.0.0.1:8000/admin/` usando as informaçoes do seu superusuário

## Endpoints

### clientes/
- GET `clientes/`, retorna lista de clientes cadastrados
- POST `clientes/`, fornece campos para criação de um novo cliente
- GET-PUT-DELETE `clientes/<cpf>/`, retorna dados de um cliente específico

### produtos/
- GET `produtos/`, retorna lista de produtos cadastrados
- POST `produtos/`, fornece campos para criação de um novo produto
- GET-PUT-DELETE `produtos/<id>/`, retorna dados de um produto específico

### pedidos/
- GET `pedidos/`, retorna lista de pedidos cadastrados
- POST `pedidos/`, fornece campos para criação de um novo pedido
- GET-PUT-DELETE `pedidos/<id>/`, retorna dados de um produto específico
- GET `pedidos/?cliente=<cpf>`, retorna lista de pedidos cadastrados de um cliente específico

### itens/
- GET `itens/`, retorna lista de itens cadastrados
- GET-PUT-DELETE `itens/<id>/`, retorna dados de um item específico
- POST `itens/`, fornece campos para criação de um novo item

## Metodologias ágeis
- [Kanban](https://trello.com/b/EN2fH1QY/time-carmen-portinho)

