from pymongo import MongoClient

def post_contato(contato):
    try:
        client = MongoClient("mongodb+srv://admin:admin@arqtest.oo6sv.mongodb.net/master?retryWrites=true&w=majority")
        mydb = client["master"]
        mycol = mydb["contato"]
    except AttributeError:
        print("-------------------------------")
        print("Houve um erro ao inserir")
        print("-------------------------------")
    else:
        mycol.insert_one(vars(contato))

def valida_contato_existente(contato):
    try:
        client = MongoClient("mongodb+srv://admin:admin@arqtest.oo6sv.mongodb.net/master?retryWrites=true&w=majority")
        mydb = client["master"]
        mycol = mydb["contato"]
    except AttributeError:
        return "Houve um erro na chamada"
    else:
        ret = mycol.find({ "nome_contato": contato.nome_contato, "numero_telefone": contato.numero_telefone })
        if ret.count() == 0:
            return False
        else:
            return True

def get_contatos():
    try:
        client = MongoClient("mongodb+srv://admin:admin@arqtest.oo6sv.mongodb.net/master?retryWrites=true&w=majority")
        mydb = client["master"]
        mycol = mydb["contato"]
    except AttributeError:
        return "Houve um erro na chamada"
    else:
        lista = []
        for x in mycol.find({}, {"_id":0, "nome_contato": 1, "numero_telefone": 1 }):  
            lista.append(x) 
        return lista

def get_phones(nome_contato):
    try:
        client = MongoClient("mongodb+srv://admin:admin@arqtest.oo6sv.mongodb.net/master?retryWrites=true&w=majority")
        mydb = client["master"]
        mycol = mydb["contato"]
    except AttributeError:
        return "Houve um erro na chamada"
    else:
        lista = []
        for x in mycol.find({ "nome_contato": nome_contato},{"_id":0, "nome_contato": 1, "numero_telefone": 1 }):  
            lista.append(x)
        return lista
        