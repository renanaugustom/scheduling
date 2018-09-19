# Sistema de Agendamento

Sistema de Agendamento de Salas desenvolvido com FLASK.

## Instalação

Você precisará instalar o Python 3.6 ou posterior para rodar esse projeto. 
De acordo com seu sistema operacional, você pode baixar em: 

  http://www.python.org/getit/


Após clonar o projeto, navegue até a pasta /scheduling e crie um diretório virtual com o seguinte comando:

```
python3 -m venv venv
```

Completado a etapa acima, ative o ambiente virtual: 

- Linux

```
source venv/bin/activate
```

- Windows

Execute o bat activate que se encontra na pasta:

```
venv/Scripts
```

Para instalar as dependências, volte até a raiz do projeto e execute o comando

```
pip install -r requirements.txt
```

## Inicializar a aplicação

Na primeira vez que for inicializar a aplicação, é necessário setar as variáveis de ambiente do FLASK e criar o banco de dados.

Navegue até a pasta /scheduling/schedulingsystem e execute os comandos:
  
<br/>  
Configuração das variáveis de ambiente: 

- Linux:
```
export FLASK_APP='run.py'
```

- Windows:
```
set FLASK_APP='run.py'
```

<br/>  
Criando e atualizando a estrutura do banco de dados

```
flask db init

flask db upgrade
```

Para finalizar, inicialize a aplicação com o comando

```
flask run
```

## Listar as API's 

É possível listar as API's implementadas com seus respectivos endpoints através do comando

```
flask routes
```

## Executando os testes

Os testes foram desenvolvidos com o auxílio da biblioteca pytest. Para executá-los, navegue até a pasta raiz do projeto /scheduling e execute o seguinte comando:

```
pytest -v
```

Também é possível extrair informações de cobertura dos testes a partir da biblioteca coverage. Para isto, execute o comando:
```
py.test --cov=schedulingsystem/
```

## Tecnologias utilizadas

* [FLASK](http://flask.pocoo.org/) - Micro web framework usado para desenvolver a API
* [PyTest](https://docs.pytest.org/en/latest/) - Test Framework
* [Coverage](https://coverage.readthedocs.io/en/coverage-4.5.1a/) - Ferramenta para medir cobertura do código a partir dos testes
* [SqlAlchemy](https://coverage.readthedocs.io/en/coverage-4.5.1a/) - ORM utilizado para desevolver a API