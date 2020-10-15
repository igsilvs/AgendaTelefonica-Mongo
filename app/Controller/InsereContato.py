from Interfaces.IInsereContato import IInsereContato
from db.Contato_Mongo import post_contato, valida_contato_existente

class InsereContato(IInsereContato):
    def cria_contato(self,contato):
        if valida_contato_existente(contato) == False:
            post_contato(contato)
            print("Contato Incluído com Sucesso !")
        else:
            print("Já existe um contato com essas informações !")
