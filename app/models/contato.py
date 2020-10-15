class Contato(object):
    def __init__(self, nome_contato, numero_telefone):
        if len(nome_contato) > 200:
            raise ValueError("Nome deve ser menor que 200 caracteres")
        if len(numero_telefone) > 25:
            raise ValueError("Telefone deve ser menor que 25 caracteres")
        
        self.nome_contato = nome_contato
        self.numero_telefone = numero_telefone