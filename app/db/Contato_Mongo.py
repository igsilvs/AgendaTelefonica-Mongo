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
