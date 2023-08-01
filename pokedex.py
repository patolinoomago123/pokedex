pokedex = []
def listar_arquivo():
    with open("pokedex.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    print("Nome: \t Tipo:")    
    for linha in linhas:
        nome, tipo = linha.strip().split('/')
        print(f"{nome}\t{tipo}")

def cadastrar_arquivo():
    nome = input("Digite o nome: ")
    tipo = input("Digite o tipo: ")
    with open("pokedex.txt", "a") as arquivo:
	    arquivo.write(f"{nome}/{tipo}\n")
    
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
        cadastrar_arquivo()
    elif opcao == 2 :
        listar_arquivo()
    else:
        print("Até a proxima.")
        break