class Produto:
    def __init__(self, preco, estoque, nomeProduto, genero):
        self._preco = preco
        self._estoque = estoque
        self._nomeProduto = nomeProduto
        self._genero = genero

    def getPreco(self):
        return float(self._preco)

    def getEstoque(self):
        return self._estoque

    def getNomeProduto(self):
        return self._nomeProduto
      
    def getGenero(self):
        return self._genero

    def adicionarEstoque(self, quant):
        print(str(quant) + " unidades de " + self._nomeProduto + " adicionadas ao estoque" )
        self._estoque += quant
    
    def removerEstoque(self, quant):
        print(str(quant) + " unidades de " + self._nomeProduto + " abatidas do estoque" )
        self._estoque -= quant

    
        
