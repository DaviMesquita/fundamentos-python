from models.cartaoCredito import CartaoCredito


class Pedido:
    def __init__(self, numero, cliente, produtos, valor):
        self._numero = numero
        self._statusPagto = False
        self._cliente = cliente
        self._cartao = ""
        self._produtos = produtos
        self._valor = valor
        
    def getNumero(self):
        return self._numero

    def getCliente(self):
        return self._cliente
        
    def getValor(self):
        return self._valor
    
    def getProdutos(self):
        return self._produtos
    
    def getStatusPagto(self):
        return self._statusPagto
    
    def faturar(self, cartaoCredito):
        self._cartao = cartaoCredito
        if self._valor <= cartaoCredito.getLimite() - cartaoCredito.getUtilizado():
            cartaoCredito.debitar(self._valor)
            self._statusPagto = True
            return True
        else:
            return False

    def cancelar(self):
        self._cartao.estornar(self._valor)
        for prod in self._produtos:
            prod[0].adicionarEstoque(prod[1])



    