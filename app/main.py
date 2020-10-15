from Controller.BuscaContato import BuscaContato
from Controller.InsereContato import InsereContato
from models.contato import Contato

busca_contato = BuscaContato()
insere_contato = InsereContato()
print(" ------------------- Bem Vindo a Agenda ------------- ")

while True:
    func  = int(input("Qual função deseja realizar ? \n 1 - Criar Usuario \n 2 - Buscar Telefone \n 3 - Todos os Contatos \n 4 - Sair \n ..............: "))
    if func == 1:
        nome_contato = str(input("Digite o Nome do Contato: "))
        telefone_contato = str(input("Digite o telefone do Contato: "))
        novo_contato = Contato(nome_contato,telefone_contato)
        insere_contato.cria_contato(novo_contato)
    elif func == 2:
        nome_contato = str(input("Digite o Nome do Contato: "))
        busca_contato.buscar_telefones(nome_contato)
    elif func == 3:
        print(busca_contato.buscar_todos_contatos())
    elif func == 4:
        break

print("Até Mais !")
