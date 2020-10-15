from pymongo import MongoClient

def post_contato(contato):
    try:
        client = MongoClient("mongodb+srv://admin:admin@arqtest.oo6sv.mongodb.net/master?retryWrites=true&w=majority")
        mydb = client["master"]
        mycol = mydb["contato"]
    except AttributeError:
        return "Houve um erro na chamada"
    else:
        mycol.insert_one(vars(contato))

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