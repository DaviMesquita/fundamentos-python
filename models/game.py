from models.produto import Produto

class Game(Produto):
    def __init__(self, preco, estoque, nomeProduto, genero, desenvolvedor, classificacao):
        super().__init__(preco, estoque, nomeProduto, genero)
        self._desenvolvedor = desenvolvedor
        self._classificacao = classificacao #classificação indicativa


    def getDesenvolvedor(self):
        return self._desenvolvedor

    def getClassificacao(self):
        return self._classificacao