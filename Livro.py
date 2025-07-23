class Livro:
    def __init__(self, nome, autor):
        self._nome = nome
        self._autor = autor
        self._disponivel = True

    def alterar_disponibilidade_livro(self):
        self._disponivel = not self._disponivel

    def __str__(self):
        return f'Nome: {self._nome} Autor: {self._autor} {"disponivel" if self._disponivel else "emprestado"}'
