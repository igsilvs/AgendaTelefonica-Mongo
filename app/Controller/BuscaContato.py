from Interfaces.IBuscaContato import IBuscaContato
from db.Contato_Mongo import get_contatos,get_phones

class BuscaContato(IBuscaContato):
    def buscar_telefones(self, nome_contato):
        ret = get_phones(nome_contato)
        if len(ret) >= 1:
            return ret
        else:
            return "Não há dados com este nome de contato" 
    
    def buscar_todos_contatos(self):
        return get_contatos()
        