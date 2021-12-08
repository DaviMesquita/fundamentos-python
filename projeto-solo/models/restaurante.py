class Restaurante:
    def __init__(self, nome, endereco, horario, estrelas):
        self._nome = nome
        self._endereco = endereco
        self._horario = horario
        self._estrelas = estrelas

    def getNome(self):
        return self._nome
    
    def getEndereco(self):
        return self._endereco

    def getHorario(self):
        return self._horario
    
    def getEstrelas(self):
        return float(self._estrelas)

    def prepararPedido(self, pedido):
        print(f"Pedido do cliente {pedido.getCliente().getNome()} sendo preparado.")
        for prato in pedido.getPratos():
            print(f"Prato {prato.getNome()} adicionado.")

    def finalizarPedido(self, entregador, pedido):
        print(f"Pedido finalizado, chamando o entregador {entregador.getNome()}")
        entregador.setPedido(pedido)
        