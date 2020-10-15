from Controller.InsereContato import post_contato
# from models.contato import Contato
from Controller.BuscaContato import get_contatos

# contato = Contato("Igor","9123123213")
# post_contato(contato)

a = get_contatos()
print(a)