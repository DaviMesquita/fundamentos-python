class CartaoCredito:
    def __init__(self, limite, bandeira, cvv, validade, numero, nome):
        self._limite = limite
        self._utilizado = 0
        self._bandeira = bandeira
        self._cvv = cvv
        self._validade = validade
        self._numero = numero
        self._nome = nome

    def getLimite(self):
        return self._limite

    def getUtilizado(self):
        return self._utilizado

    def getBandeira(self):
        return self._bandeira

    def getCvv(self):
        return self._cvv
    
    def getValidade(self):
        return self._validade

    def getNumero(self):
        return self._numero
    
    def getNome(self):
        return self._nome

    def debitar(self, valor):
        self._utilizado += valor

    def estornar(self, valor):
        self._utilizado -= valor