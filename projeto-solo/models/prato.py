class Prato:
    def __init__(self, nome, valor, gluten, vegano):
        self._nome = nome
        self._valor = valor
        self._gluten = gluten
        self._vegano = vegano

    def getNome(self):
        return self._nome
    
    def getValor(self):
        return float(self._valor)

    def getGluten(self):
        return self._gluten
    
    def getVegano(self):
        return self._vegano