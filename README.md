
  
# API de Gerenciamento de Consultas Médicas
 
Este projeto é uma API para gerenciar consultas médicas, permitindo o cadastro, edição, remoção de consultas e de profissionais de saúde. A API foi construída usando o framework **Django** e **Django Rest Framework** (DRF), seguindo o padrão REST.

## Funcionalidades da API

-   **Cadastro, edição e exclusão de profissionais** com os campos:
    
    -   Nome completo;
    -   Nome social (opcional);
    -   Profissão;
    -   Endereço;
    -   Contato;
-   **Cadastro, edição e exclusão de consultas**, com a data e o profissional vinculado.    
-   **Pesquisa de consultas** pelo ID do profissional.

## 📋 Pré-requisitos  

**Sistema operacional:** Windows 7 (com Service Pack 1) ou superior, incluindo Windows 10.
- Arquitetura: O Clion que suporta sistemas operacionais de 32 e 64 bits.
- Processador: Processador Intel Pentium 4 ou posterior compatível com a tecnologia SSE2.

**Requisitos:**
-   Python 3.8+
-   Django 4.2+
-   Django Rest Framework 3.14+

## 🔧 Como executar o projeto
#### Passo 1: Clonar o repositório

```bash
https://github.com/ThiagoFoganholo/API-gerenciamento-de-consultas.git
cd consultas-api
```
#### Passo 2: Criar e ativar o ambiente virtual
#### No Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
#### Passo 3: Instalar as dependências
```bash
pip install -r requirements.txt
```
#### Passo 4: Configurar o banco de dados

Execute as migrações para criar as tabelas no banco de dados.
```bash
python manage.py migrate
```
#### Passo 5: Rodar o servidor de desenvolvimento
```bash
python manage.py runserver
```
A API estará disponível em `http://localhost:8000/`

### Passo 6: Criar um superusuário (opcional)

Se desejar acessar a interface de administração do Django para gerenciar os dados:
```bash
python manage.py createsuperuser
```
## 🚀 Endpoints da API

A API responde aos seguintes Endpoints:

### Profissionais

-   **`GET /profissionais/`**: Lista todos os profissionais cadastrados.
-   **`POST /profissionais/`** : Cria um novo profissional. Exemplo de corpo da 	requisição:
- **`GET /profissionais/{id}/`**: Retorna os detalhes de um profissional específico.
- **`PUT /profissionais/{id}/`**: Atualiza os dados de um profissional existente.
- **`DELETE /profissionais/{id}/`**: Deleta um profissional.
```json
{
    "nome_completo": "Maria da Silva",
    "nome_social": "Maria",
    "profissao": "Médica",
    "endereco": "Rua Exemplo, 123",
    "contato": "9999-9999"
}
```

#### Pesquisa por Profissional especifico

-   **`GET /consultas/?profissional_id={id}`**: Lista todas as consultas vinculadas ao profissional com o ID especificado.

### Consultas

-   **`GET /consultas/`**: Lista todas as consultas cadastradas.
-   **`POST /consultas/`**: Cria uma nova consulta. Exemplo de corpo da requisição:
-   **`GET /consultas/{id}/`**: Retorna os detalhes de uma consulta específica.
-   **`PUT /consultas/{id}/`**: Atualiza os dados de uma consulta existente.
-   **`DELETE /consultas/{id}/`**: Deleta uma consulta.
```json
{
    "data_consulta": "2024-09-06T03:09:02Z",
    "profissional": 4
}
```

## Validações de Segurança

-   **Sanitização de inputs**: Todas as entradas de dados são validadas pelo Django Rest Framework para garantir que sejam seguras e consistentes.

## 🛠️ Escolhas de Arquitetura

-   **Django Rest Framework**: Foi utilizado o DRF para facilitar a implementação da API seguindo o padrão REST.
-   **Modelos Separados para Profissional e Consulta**: O relacionamento entre profissionais e consultas é feito usando uma chave estrangeira, garantindo que cada consulta esteja vinculada a um profissional específico.

##  Referências

- Django REST Framework - Build an API from Scratch https://www.youtube.com/watch?v=i5JykvxUk_A&t=1s

- Como criar uma API em Django - Criando um CRUD - Aula Completa https://www.youtube.com/watch?v=Q2tEqNfgIXM&t=444s

- The web framework for perfectionists with deadlines | Django https://www.djangoproject.com/

- Home - Django REST framework 
https://www.django-rest-framework.org/

## ✒️ Autor
* **Desenvolvedor ** - *Trabalho de desenvolvimento do código, * - [Thiago Foganholo](https://github.com/ThiagoFoganholo) ;

## 📄 Licença

Este projeto está sob a licença livre - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.
