pokedex = []
def cadastrar():
    nome = input("Digite o nome: ")
    tipo = input("Digite o tipo: ")
    pokemon = [nome, tipo]
    pokedex.append(pokemon)

def listar():
    print("Nome: \t Tipo:")

    for pokemon in pokedex:
        nome, tipo = pokemon
        print(f"{nome}\t{tipo}")

while True :
    print(" 1:cadastrar \n 2:listar \n 3:sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1 :
        cadastrar()
    elif opcao == 2 :
        listar()
    else:
        print("Até a proxima.")
        break