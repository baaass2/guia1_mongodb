import pymongo

class conectar_db():
    def __init__(self, url):
        # Replace the uri string with your MongoDB deployment's connection string.
        conn_str = url

        try:
            # set a 5-second connection timeout
            self.client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
        except Exception:
            print("Unable to connect to the server.")
        
    def ver_data(self, collection, database):
        db = self.client[database]
        mycol = db[collection]
        print("------------------------------------------")
        contador = 0
        for x in mycol.find():
            print("Nombre del dueño: "+ x['name_duenio'])
            print("Nombre de los perros")
            for i in x['name_dogs']:
                print("",end="    ")
                print(i)
            print("index: "+str(contador) )
            contador=contador+1
        print("------------------------------------------")
        return mycol.find()
    def select_db(self):
        return self.client.list_database_names()

    def select_coll(self, opc2):
         db = self.client[opc2]
         return db.list_collection_names()

    def crear_db(self):

        print("Nombre de db: ")
        name_db = input()
        print("Nombre de collection: ")
        name_coll = input()

        db = self.client[name_db]
        coll = db[name_coll]
        
        mydict = {'name_duenio':'example1', 'name_dogs': ['example1'] }

        coll.insert_one(mydict)
        return 0
    
    def insert(self, collection, database):
        print("Nombre del dueño: ")
        name_boss = input()

        dogs = []
        print("¿Cuantos perros ingresará?: ")
        n_dogs = input()

        for i in range(0,int(n_dogs)):
            print("Nombre del perro "+i+" :")
            name_dog = input()
            dogs.append(name_dog)

        mydict = {'name_duenio':name_boss, 'name_dogs': dogs }

        mycoll = self.client[database][collection]

        mycoll.insert_one(mydict)
    
    def delete(self,collection, database, data):
        mycoll = self.client[database][collection]
        print("Escribe el index del dato a eliminar: ")
        opc = input()
        _id = data[int(opc)]['_id']
        mycoll.delete_one({'_id': _id})

    def update(self,collection, database, data):
        mycoll = self.client[database][collection]
        print("Escribe el index del dato a actualizar: ")
        opc = input()
        _id = data[int(opc)]['_id']
        print("Nombre del dueño: ")
        print("Nombre del dueño: ")
        name_boss = input()
        
        dogs = []
        print("¿Cuantos perros ingresará?: ")
        n_dogs = input()

        for i in range(0,int(n_dogs)):
            print("Nombre del perro "+n_dogs+" :")
            name_dog = input()
            dogs.append(name_dog)

        mydict = {'name_duenio':name_boss, 'name_dogs': dogs }
        mycoll.update_one({'_id': _id},{"$set":mydict})


def crud(database, collection, db):

    end = "0"
    while(end != "1"):
        print("-------------------MENU-----------------------")
        print("1. Ver data")
        print("2. Ingresar dato")
        print("3. Eliminar dato ")
        print("4. Actualizar dato")
        print("----------------------------------------------")
        opc = input()
        if(opc == "1"):
            db.ver_data(collection, database)
        elif(opc == "2"):
            db.insert(collection, database)
        
        elif(opc == "3"):
            data = db.ver_data(collection,database)
            db.delete(collection, database, data)
        elif(opc == "4"):
            data = db.ver_data(collection,database)
            db.update(collection, database, data)
        else:end="1"

url = "mongodb://localhost:27017"
db = conectar_db(url)
end = 0
while (end != 1):
    print("-------------------MENU-----------------------")
    print("1. Crear base de dato y colección.")
    print("2. Seleccionar base de dato.")
    print("3. Cerrar el programa.")
    print("----------------------------------------------")
    opc = input()

    if (opc == "1"):
        
        db.crear_db()

    elif(opc == "2"):
        dbs = db.select_db()

        print("Seleccionar base da dato:")
        for i in range(0, len(dbs)):
            print(str(i)+". " +dbs[i])
        opc2 = input()
        print("Seleccionar colección: ")
        #nombre de la db
        database = dbs[int(opc2)]

        colls = db.select_coll(database)

        for i in range (0, len(colls)):
            print(str(i)+". "+colls[i])
        opc2 = input()

        #coleccion a crud
        collection = colls[int(opc2)]

        crud(database, collection, db)

    elif(opc != "1" or opc != "2"):
        print("Se cierra el programa...")
        end = 1

