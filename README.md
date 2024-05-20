## FLASK PRUEBA TECNICA

### Pasos para hacer correr el proyecto:

##### PASO 1: <p>Crear entorno virtual

` virtualenv -p python3 env o  python3 -m venv env`</p>

##### PASO 2: Activar el entorno virtual ejecutando

##### Windows

`.\env\Scripts\activate`

##### macOS o Linux

`source env/bin/activate`

##### PASO 3: <p>Ya dentro del entorno virtual puedes instalar flask con el comando:

### En requirements estan todas las dependencias que usan, algunas son de versiones especificas, tener cuidado

`pip install flask`

##### IMPORTANTE : <p>Puedes solo crear tu entorno virtual y posicionarte en el mismo, luego ejecutar el siguiente comando: </p>

`pip install -r requirements.txt`

### Tener en cuenta el nombre de la base de datos : flask_crud

### Se trabaja con MySQL usando ORM Flask-SQLAlchademy
