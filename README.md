# guia1_mongodb_crud

#Requerimientos
pymongo==4.1.1
Python 3.6.9
Instalar mongodb: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
#Ejecución en terminal
python3 connect_db

Este programa permite conectarse a la red local mongodb con el puerto por defecto: mongodb://localhost:27017, si no se logra hacer la conexión
tiene que cambiar la variable url que esta en linea 123 del archivo connect_db por los parametros de su conexión.

La primera experiencia del usuario es un menú de 3 opciones:
1. Crear base de dato y colección. -> Es para hacer la creación de una bd en mongodb y agregarle una coleción, tiene que ingresar los nombres.
2. Seleccionar base de dato ->  Muestra las bds, tiene que escoger a cual se conectará por el numero de enumeración y posteriormente sale el CRUD, el cual funciona a través de ir escribiendo el numero de la opción a realizar, y seleccionar datos por el index.
3. Cerrar el programa 



Esquema de la db:

{'name_duenio': 'example_name', 'name_dogs': ['dog1','dog2']}
