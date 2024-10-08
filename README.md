# Projeto de CRUD de Livros

Este projeto é uma API RESTful para gerenciamento de livros, implementada usando Django e Django Rest Framework.

## Funcionalidades

- Listar todos os livros
- Criar um novo livro
- Visualizar detalhes de um livro específico
- Atualizar informações de um livro
- Deletar um livro

## Estrutura do Projeto

O projeto consiste em três modelos principais:

1. `Categoria`: Representa as categorias dos livros
2. `Autor`: Representa os autores dos livros
3. `Livro`: Representa os livros, com relações para Categoria e Autor

## Endpoints da API

- `GET /livros/`: Lista todos os livros
- `POST /livros/create`: Cria um novo livro
- `GET /livros/<id>/`: Retorna detalhes de um livro específico
- `PUT /livros/<id>/`: Atualiza um livro específico
- `DELETE /livros/<id>/`: Deleta um livro específico

## Instalação e Configuração

1. Clone o repositório:
   ```
   git clone [git@github.com:JOAO2666/biblioteca-django-v2..git
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Execute as migrações:
   ```
   python ./biblioteca/manage.py migrate
   ```

4. Inicie o servidor:
   ```
   python ./biblioteca/manage.py runserver
   ```

## Mock de dados no banco

```bash
python ./biblioteca/manage.py populate_db
```

## Teste

```bash
python ./biblioteca/manage.py test
```
