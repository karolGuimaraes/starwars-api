# starwars-api
API que permite o registro dos planetas.

## Droids-API

### Configurando
 - Clonar o projeto: git clone https://github.com/karolGuimaraes/starwars-api
 - ` python3 -m venv env` ( Criar um ambiente virtual )
 - Acesse a pasta /starwars_api
 - Para executar o projeto `python run.py`

 
### Funcionamento

Acessando ( http://localhost:5000/ ), onde:

- ` POST /usuario `  Criar um usuário (Administrador ou Anunciante):
	
	Criar um usuário para adicionar uma demanda.
	
	Se o 'admin' for sim, o usuário é marcado como Administrador.
	
	O username é único.

	- Envio:
		{ 
			"telefone": "000000000", 
			"username":"user_test", 
			"first_name":"test", 
			"email": "user.silva@gmail.com", 
			"password": 12345, 
			"admin": "Sim"
		}



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

- ` GET /buscar_nome/<id> ` Buscar um planeta pelo nome.





### Teste

Para executa os teste unitários: 

`$ python test/tests.py`

Resposta similar:

            .........
            ----------------------------------------------------------------------
            Ran 9 tests in 2.110s

            OK





