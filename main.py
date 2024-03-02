import json, os
from time import sleep

def mostrarUser(nome, saldo, idade):
    print("-------------------------")
    print(f"NOME:  {nome}\nSALDO: {saldo}\nIDADE: {idade}")
    print("-------------------------")
    r = str(input("[0] Para voltar: "))
    if r == "0":
        entrada()

def carregar():
    with open("data.json", "r") as f:
        return json.load(f)
    
def salvar(cadastro):
    with open("data.json", "w") as f:
        json.dump(cadastro, f, indent=4)

def criar_conta(nome, senha, idade, saldo):
    os.system('cls')
    template = {
        "nome": str(nome), 
        "idade": int(idade),
        "senha": str(senha), 
        "saldo": int(saldo)
    }

    cadastro = carregar()
    cadastro["users"].append(template)
    salvar(cadastro)

    print("Cadastro criado com sucesso. Voltando ao início em 3s")
    sleep(3)
    entrada()

def acessar_conta(nome):
    os.system('cls')

    cadastros = carregar()

    if cadastros:
        for cadastro in cadastros["users"]:
            if cadastro["nome"] == nome:
                print("Cadastro encontrado")
                user_input_password = str(input("Digite sua senha: "))
                if user_input_password == cadastro["senha"]:
                    os.system('cls')
                    print("Acessando conta.....")
                    mostrarUser(cadastro["nome"],cadastro["saldo"],cadastro["idade"])
                break
def entrada():
    os.system('cls')
    print(f"--------------------------------+")
    print(f"[1] Acessar sua conta           |")
    print(f"[2] Criar uma conta             |")
    print(f"--------------------------------+")

    escolha = str(input("> "))

    if escolha == "1": # acessar
        print(f"Você escolheu acessar sua conta...")
        user_input = str(input("Digite seu nome: ").upper())
        if user_input == "0": # voltar
            print("Aguarde 1s")
            sleep(1)
            entrada()
        else:
            acessar_conta(user_input)

    elif escolha == "2": # criar
        os.system('cls')
        print(f"Você escolheu criar uma nova conta...\nSeu nome deve ter no minimo 4 dígitos\nDigite [0] para retornar agora\n")
        user_input = str(input("Digite seu nome: ").upper())

        if user_input == "0": # voltar
            print("Aguarde 1s")
            sleep(1)
            entrada()
        else:
            if len(user_input) >= 4:
                try:
                    user_input_password = str(input("Crie uma senha: "))
                    user_input_idd = int(input("Insira sua idade atual: "))
                    if user_input_idd != 0 and user_input_password:
                        criar_conta(user_input, user_input_password, user_input_idd, 0)
                    else:
                        print("idade não pode ser '0' e/ou password inválida, Aguarde 1s e tente novamente\n")
                        sleep(1)
                        entrada()
                except Exception as err:
                    print(f" Erro{err}\nAlgo deu errado, tentando novamente em 3s")
                    sleep(3)
                    entrada()
            else:
                print(f"Seu nome deve ter no minimo 4 dígitos, Aguarde 1s e tente novamente\n")
                sleep(1)
                entrada()
    else:
        print("Argumento inválido, tente novamente em 3s.")
        sleep(3)
        entrada()

if __name__ == "__main__":
    entrada()