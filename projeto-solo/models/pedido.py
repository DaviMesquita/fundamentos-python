class Pedido:
    def __init__(self, numero, cliente, restaurante):
        self._numero = numero
        self._restaurante = restaurante
        self._cliente = cliente
        self._pratos = []
        self._valor = 0
        
    def getNumero(self):
        return self._numero

    def getCliente(self):
        return self._cliente
        
    def getValor(self):
        return float(self._valor)
    
    def getPratos(self):
        return self._pratos
    
    def getRestaurante(self):
        return self._restaurante

    def acrescentarPrato(self, prato):
        self._pratos.append(prato)
        self._valor += prato.getValor()
    
    def removerPrato(self, prato):
        self._pratos.remove(prato)
        self._valor -= prato.getValor()