from LibraryOO.Livro import Livro
from LibraryOO.Usuario import Usuario
from LibraryOO.Biblioteca import Biblioteca

biblioteca = Biblioteca()

def menu():
    print("\n--- Biblioteca Virtual ---")
    print("1. Cadastrar usuário")
    print("2. Cadastrar livro")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Listar livros de um usuário")
    print("6. Sair")

def buscar_usuario(nome):
    for usuario in biblioteca._usuarios:
        if usuario._nome.lower() == nome.lower():
            return usuario
    return None

def buscar_livro(nome):
    for livro in biblioteca._livros:
        if livro._nome.lower() == nome.lower():
            return livro
    return None

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do usuário: ")
        if buscar_usuario(nome):
            print("Usuário já cadastrado.")
        else:
            usuario = Usuario(nome)
            biblioteca.cadastrar_usuario(usuario)
            print(f"Usuário {nome} cadastrado com sucesso.")

    elif opcao == "2":
        nome = input("Nome do livro: ")
        autor = input("Autor do livro: ")
        if buscar_livro(nome):
            print("Livro já cadastrado.")
        else:
            livro = Livro(nome, autor)
            biblioteca.cadastrar_livro(livro)
            print(f"Livro '{nome}' cadastrado com sucesso.")

    elif opcao == "3":
        nome_usuario = input("Nome do usuário: ")
        nome_livro = input("Nome do livro: ")
        usuario = buscar_usuario(nome_usuario)
        livro = buscar_livro(nome_livro)
        biblioteca.emprestar_livro(usuario, livro)

    elif opcao == "4":
        nome_usuario = input("Nome do usuário: ")
        nome_livro = input("Nome do livro: ")
        usuario = buscar_usuario(nome_usuario)
        livro = buscar_livro(nome_livro)
        biblioteca.devolver_livro(livro, usuario)

    elif opcao == "5":
        nome_usuario = input("Nome do usuário: ")
        usuario = buscar_usuario(nome_usuario)
        if usuario:
            usuario.listar_livros()
        else:
            print("Usuário não encontrado.")

    elif opcao == "6":
        print("Saindo da biblioteca virtual...")
        break

    else:
        print("Opção inválida. Tente novamente.")
