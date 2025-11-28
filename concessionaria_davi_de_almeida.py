
carros = [
    {
        "modelo": "Meriva",
        "ano": "2012",
        "estoque": 3,
        "fipe": 30000
    },
    {
        "modelo": "Fusca",
        "ano": "1996",
        "estoque": 5,
        "fipe": 56000
    },
    {     
        "modelo": "Camaro",
        "ano": "2009",
        "estoque": 3,
        "fipe": 35000
    },
]


def inicio():
    nome = input("Digite seu nome: ")
    telefone = input("Digite o seu numero de telefone: ") 
    print("Seja bem vindo(a), senhor(a): ", nome, "\n")
    
    estoque()
    
    opcao = -1
    
    while(opcao != 0):
        
        print(nome, ", Escolha uma opção, por gentileza!")
        print("1 para mostrar estoque")
        print("2 para vender um carro")
        print("3 para comprar um carro")
        print("4 para alugar um carro")
        print("0 para sair")
       
        opcao = int(input())
        if (opcao != 0):
            menu(opcao)
        

def menu(opcao):
    match opcao:
        case 1: 
            estoque()
        case 2: 
            vender()
        case 3:
            comprar()
        case 0:
            sair()
        case 4: 
            alugar()   
        

def estoque():
    
    print("----- ESTOQUE DOS CARROS -----")
    
    for carro in carros:
        print("modelo:", carro["modelo"], "--", "ano:", carro["ano"], "--", "Estoque:", carro["estoque"])
        

def vender():
    print("Digite o modelo do carro:")
    modelo = input()
    print("Digite o ano do carro:")
    ano = input()   
    print("Digite o estoque do carro:")
    estoque_2 = int(input())
    print("Digite o fipe do carro: ")
    fipe = int(input())

    carro = {
        "modelo": modelo,
        "ano": ano,
        "estoque": estoque_2
    }

    carros.append(carro)
    print("Carro vendido!!!")


def comprar():
      
    print("Qual carro você deseja comprar:")
    modelo = input()
    estoque()
    for carro in carros:
        if carro["modelo"].lower() == modelo.lower():
            preco = float(carro["fipe"]) * 1.12
            print(f"Você deseja comprar o {carro['modelo']} por R$ {preco:.2f}?") 
            print("1 para confirmar a compra")
            print("2 para cancelar a compra")
            opcao = int(input())
            match opcao:
                case 1:
                    carro["estoque"] -= 1
                    if carro["estoque"] < 0:
                        print("Estoque insuficiente!")
                        carro["estoque"] += 1
                    print(f"Compra realizada com sucesso! Novo estoque do {carro['modelo']}: {carro['estoque']}")
                    return

                case 2:
                    print("Compra cancelada.")
                    return
            
    
    
def alugar():
   
    print("\n--- ALUGAR CARRO ---")
    print("Modelos disponíveis:\n")

    
    for carro in carros:
        print(f"Modelo: {carro['modelo']}  -- Ano: {carro['ano']} -- Estoque: {carro['estoque']}")

    modelo_escolhido = input("\nDigite o modelo do carro que deseja alugar: ")

    
    for carro in carros:
        if carro["modelo"].lower() == modelo_escolhido.lower():

            if carro["estoque"] <= 0:
                print("Este carro não está disponível para aluguel.\n")
                return

            print(f"Você deseja alugar o carro {carro['modelo']} por R$ 1500?")
            print("1 - Confirmar")
            print("2 - Cancelar")

            confirmar = int(input())

            if confirmar == 1:
                carro["estoque"] -= 1
                print(f"Aluguel confirmado! Você alugou o {carro['modelo']}.\n")
            else:
                print("Aluguel cancelado.\n")
            return
    
    print("Modelo não encontrado.\n")
    
        
def sair():
    print("Agradeçemos pela visita e um ótimo dia!")        
        

inicio()


