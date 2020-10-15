from Controller.InsereContato import post_contato
from models.contato import Contato
from Controller.BuscaContato import get_contatos
from db.Contato_Mongo import valida_contato

contato = Contato("Igor","9123123213")

contato2 = Contato("Luis","32323123213")


# post_contato(contato)

a = valida_contato(contato)
print(a)