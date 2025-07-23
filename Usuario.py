class Usuario:
    def __init__(self, nome):
        self._nome = nome
        self._livros_emprestados = []

    def pegar_livro(self, Livro):
        self._livros_emprestados.append(Livro)

    def listar_livros(self):
        print(f'Livros Emprestados de {self._nome}')
        for livro in self._livros_emprestados:
            print(f'{livro} \n')

    def devolver_livro(self, Livro):
        try:
            self._livros_emprestados.remove(Livro)
        except Exception as e:
            print(f'erro: {e}')

    def __str__(self):
        return f'{self._nome}'
