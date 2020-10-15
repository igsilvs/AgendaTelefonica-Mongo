from Interfaces.IInsereContato import IInsereContato
from db.Contato_Mongo import post_contato
from models.contato import Contato

class InsereContato(IInsereContato):
    def cria_contato(self,contato):
        post_contato(contato)
