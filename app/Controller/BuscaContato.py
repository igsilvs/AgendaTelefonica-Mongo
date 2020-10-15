from Interfaces.IBuscaContato import IBuscaContato
from db.Contato_Mongo import get_contatos

class BuscaContato(IBuscaContato):
    def buscar_contatos(self, contato):
        return get_contatos()