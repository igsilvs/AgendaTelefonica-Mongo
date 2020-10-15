from Interfaces.IInsereContato import IInsereContato
from db.Contato_Mongo import post_contato
from models.contato import Contato

class BuscaContato(IInsereContato):
    def cria_contato(self,contato):
        post_contato(contato)


contato = Contato("Igor","9123123213")
c = BuscaContato()
c.post_contato(contato)