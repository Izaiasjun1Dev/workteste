# Teste avaliativo Api Crud
<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/44451704?v=4" width="100px;" alt="foto Izaias git"/><br>
        <sub>
          <b>Izaias Junior</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## Projeto desenvolvido com intuido avaliativo para processo seletivo de programador back-end

# 🛠 Tecnologias usadas neste projeto

## As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://docs.python.org/3/)
- [Django](https://www.djangoproject.com/start/)
- [DRF(django rest framework)](https://www.django-rest-framework.org/api-guide/requests/)
- [PostgresSQL](https://www.postgresql.org/about/)
- [Anaconda3](https://www.anaconda.com/)

# Getting Started

## Projeto avaliativo api crud ```Candidates```


# ```Rotas da aplicação```
- URI /candidates/
- URI /candidates/1/
- URI /contacts/
- URI /contacts/1/

## Banco de dados

## Configure o motor database do Django
Alterando a varivavel de ambiente ```Databases``` banco de dados em core/settings.py
da sequinte forma:

```
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

```
assim a aplicação criará uma intacia de banco de dados para testes sqlite3


# Em sequida...

## Baixe o [anaconda3](https://www.anaconda.com/products/individual#Downloads) e crie um ambiente virtual, em seguida corra em seu terminal:


No seu cmd ou promt de comando corra as linhas de comanado abaixo:

```bash
$ conda project-env/bin/activate ou activate <nome do seu ambiente>
$ pip install requirements.txt


$ cd work/
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

```




