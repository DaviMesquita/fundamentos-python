from models.produto import Produto

class Livro(Produto):
    def __init__(self, preco, estoque, nomeProduto, genero, isbn, paginas, autor):
        super().__init__(preco, estoque, nomeProduto, genero)
        self._isbn = isbn
        self._paginas = paginas
        self._autor = autor

    
    def getIsbn(self):
        return self._isbn

    def getPaginas(self):
        return self._paginas

    def getAutor(self):
        return self._autor