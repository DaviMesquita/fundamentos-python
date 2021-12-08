from models.pedido import Pedido

class Carrinho:
    def __init__(self):
        self._produtos = []
        self._valor = 0
    
    def getProdutos(self):
        return self._produtos

    def finalizarCompra(self, num, cliente, cartao):
        pedido = Pedido(num, cliente, self._produtos, self._valor)
        
        for prod in self._produtos:
            if prod[0].getEstoque() < prod[1]: #Caso o cliente peça mais produtos do que existe no estoque
                if prod[0].getEstoque() > 0:  #Caso o cliente peça 2 ou mais unidades, existe algum no estoque mas não o suficiente
                    print("So temos " + prod[0].getEstoque() + " unidades de " + prod[0].getNomeProduto)
                else: #Caso o cliente peça um produto esgotado
                    print(prod[0].getNomeProduto() + " esta em falta.")
                return False
        
        if pedido.faturar(cartao): #Caso o cartão tenha crédito o suficiente
            print("Pagamento Aprovado")
            for prod in self._produtos:
                prod[0].removerEstoque(prod[1])
            return True
        else: #Caso não tenha 
            print("Pagamento Reprovado")
            return False
            

    def insereProduto(self, produto, quant):
        self._produtos.append([produto, quant])
        self._valor += produto.getPreco()*quant
        print("Inserido " + str(quant) + " unidades do produto " + produto.getNomeProduto() + " no carrinho.")

    def removeProduto(self, produto, quant):
        self._produtos.remove([produto, quant])
        self._valor -= produto.getPreco()*quant
        print("Removido " + str(quant) + " unidades do produto " + produto.getNomeProduto() + " do carrinho.")

    def esvazia(self):
        print("Carinho vazio")
        self._produtos = []
