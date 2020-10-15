from Interfaces.IBuscaContato import IBuscaContato
# from db.ContatoMongo import get_contato

class BuscaContato(IBuscaContato):
    def get_contato(self, contato):
        # return 