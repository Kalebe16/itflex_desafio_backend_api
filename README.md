# itflex_desafio_backend_api

<h1 align="center">API Rest [ITFLEX]</h1>

<h3>Descrição do projeto:</h3>
<p><strong>- API desenvolvida utilizando Python, Flask, SQLAlchemy</strong></p>
<p><strong>- CRUD básico para gerenciamento de certificados</strong></p>
<p><strong>- Link da API: <a href="https://certificatemanagerapi.herokuapp.com/">https://certificatemanagerapi.herokuapp.com/</a></strong></p>

<hr>



<h3>Pré requisitos:</h3>
<p><strong>- Ter o python instalado.</strong></p>
<hr>

<h3>Para rodar o projeto:</h3>
<p><strong>1- git clone https://github.com/Kalebe16/itflex_desafio_backend_api.git</strong></p>
<p><strong>2- pip install -r requirements.txt</strong></p>
<p><strong>3- python api.py</strong></p>
<hr>



<h3>Endpoints da api</h3>

| Método   | Endpoint | Descrição  |
| -------- | -------- | ---------- |
| `GET`    | /certificados  | Obtém todos os certificados. | 
| `GET`    | /certificados/`ID` | Obtém um certificado pelo seu `ID`. |
| `POST`   | /certificados  | Cadastra um novo certificado. |
| `PUT`    | /certificados/`ID` | Edita um certificado pelo seu `ID`. |
| `DELETE` | /certificados/`ID` | Deleta um certificado pelo seu `ID`. |
<hr>

<h3>Respostas</h3>

| Código  | Descrição                                                              |
| ------- | ---------------------------------------------------------------------- |
| `200`     | Requisição executada com sucesso.                                      |
| `201`     | Requisição bem sucedida, um novo certificado foi criado como resultado.|
| `404`     | Certificado pesquisado não encontrado.                                 |
| `422`     | Dados informados estão fora do escopo definido para um ou mais campos. |

<hr>




## `GET`/certificados

```
[
    {
        "created_at": "2022-11-16 00:30:05-03:00",
        "description": "Lorem ipsum dolor sit amet",
        "expirated_at": "2022-12-06 00:30:05-03:00",
        "expiration": 20,
        "id": 1,
        "name": "Eren Yger",
        "updated_at": "",
        "username": "cavalofesteir8000"
    },
    {
        "created_at": "2022-11-16 00:31:00-03:00",
        "description": "",
        "expirated_at": "2022-12-06 00:31:00-03:00",
        "expiration": 20,
        "id": 2,
        "name": "Fabio Akita",
        "updated_at": "2022-11-16 00:31:15-03:00",
        "username": "Akita01"
    }
]
```
<hr>


## `GET`/certificados/`ID`

```
{
    "created_at": "2022-11-16 00:36:54-03:00",
    "description": "",
    "expirated_at": "2023-09-12 00:36:54-03:00",
    "expiration": 300,
    "id": 3,
    "name": "Kalebe Chimanski de Almeida",
    "updated_at": "",
    "username": "Kalebe16"
}
```
<hr>


## `POST`/certificados
```
{
    "mensagem": "CERTIFICADO CADASTRADO COM SUCESSO"
}
```
<hr>


## `PUT`/certificados/`ID`
```
{
    "mensagem": "CERTIFICADO EDITADO COM SUCESSO"
}
```
<hr>


## `DELETE`/certificados/`ID`
```
{
    "mensagem": "CERTIFICADO DELETADO COM SUCESSO"
}
```
<hr>



