import json
import os

ARQUIVO = "usuarios.json"

# Função responsável por carregar os usuários do arquivo JSON
def carregar_usuarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# Função responsável por salvar os usuários no arquivo JSON
def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# Função responsável por cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    
    nome = input("Digite o nome do usuário: ").strip()
    idade = input("Digite a idade do usuário: ").strip()
    email = input("Digite o email do usuário: ").strip()

    if not idade.isdigit():
        print("Idade Invalida! Digite apenas números.")
        return
    if not nome or not email:
        print("Nome e Email não podem estar vazios!")
        return
    usuario = {"nome": nome,"idade": int(idade),"email": email}

    usuarios.append(usuario)

    salvar_usuarios(usuarios)

    print("Usuário cadastrado com sucesso!")

# Função responsável por listar todos os usuários cadastrados
def listar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário foi cadastrado!")
        return
    
    print("\n--- Lista de Usuários ---")

    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}")

# Função principal que controla o menu do sistema
def menu():
    usuarios = carregar_usuarios()

    while True:
        print("\n=== SISTEMA DE CADASTRO ===")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios)
        elif opcao == "2":
            listar_usuarios(usuarios)
        elif opcao == "3":
            print("Encerrando o programa.....")
            break
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    menu()





    