class Entregador:
    def __init__(self, nome, cpf, transporte, telefone):
        self._nome = nome
        self._cpf = cpf
        self._transporte = transporte
        self._telefone = telefone
        self._pedido = ""

    def getNome(self):
        return self._nome
    
    def getCpf(self):
        return self._cpf

    def getEmail(self):
        return self._transporte
    
    def getTelefone(self):
        return self._telefone

    def getPedido(self):
        return self._pedido

    def setPedido(self, pedido):
        self._pedido = pedido

    def entregarPedido(self):
        print(f"Pedido do cliente {self._pedido.getCliente().getNome()} entregue.")