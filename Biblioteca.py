from LibraryOO.Livro import Livro
from LibraryOO.Usuario import Usuario

class Biblioteca:
    def __init__(self):
        self._usuarios = []
        self._livros = []

    def cadastrar_usuario(self, Usuario):
        self._usuarios.append(Usuario)

    def cadastrar_livro(self, Livro):
        self._livros.append(Livro)

    def emprestar_livro(self, Usuario = Usuario, Livro = Livro):
        if Usuario in self._usuarios:
            print('Usuario Cadastrado')
            if Livro in self._livros:
                print('livro cadastrado')
                if(Livro._disponivel):
                    Usuario.pegar_livro(Livro)
                    Livro.alterar_disponibilidade_livro()
                else:
                    print(f'Livro {Livro._nome} não disponivel')            
            else:
                print(f'Livro {Livro._nome} não cadastrado na biblioteca')
        else:
            print(f'Usuario {Usuario._nome} não cadastrado na biblioteca')

    def devolver_livro(self, Livro = Livro, Usuario = Usuario):
        if not Livro._disponivel:
            if Livro in Usuario._livros_emprestados:
                Livro.alterar_disponibilidade_livro()
                Usuario.devolver_livro(Livro)
            else:
                print('Livro não emprestado para esse usuario')
        else:
            print('Livro disponivel')