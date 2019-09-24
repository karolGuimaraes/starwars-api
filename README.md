# starwars-api
API que permite o registro dos planetas.


### Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/starwars-api
 - ` python3 -m venv env` ( Criar um ambiente virtual )
 - Acesse a pasta /starwars_api
 - Para executar o projeto `python run.py`

 
### Funcionamento

Acessando ( http://localhost:5000/ ), onde:


- ` GET /listar ` Retorna todos os planetas. 


- ` POST /adicionar ` Adicionar um planeta novo:

	- Envio:
			{
			 	"nome": "nome", 
				"clima": "clima",
				"terreno": "terreno"
			}


- ` DELETE /excluir/<id> ` Excluir um planeta.

- ` GET /buscar_id/<id> ` Buscar um planeta pelo id.

- ` GET /buscar_nome/<nome> ` Buscar um planeta pelo nome.





### Teste

Para executa os teste unitários: 

`$ python test/tests.py`

Resposta similar:

            .........
            ----------------------------------------------------------------------
            Ran 9 tests in 2.110s

            OK





