from models.prato import Prato
from models.restaurante import Restaurante
from models.entregador import Entregador
from models.cliente import Cliente
from models.pedido import Pedido

cliente1 = Cliente("Davi", "14727089700", "davicm98@hotmail.com", "21987623774")
restaurante1 = Restaurante("Burguer King", "Na esquina", "Até as 23:00", 4.8)
prato1 = Prato("Stacker Duplo", 19.99, True, False)
entregador1 = Entregador("Fulano", "12345678900", "Moto", "2123456789")


pedido1 = Pedido(1, cliente1, restaurante1)
pedido1.acrescentarPrato(prato1)
restaurante1.prepararPedido(pedido1)
restaurante1.finalizarPedido(entregador1, pedido1)
entregador1.entregarPedido()
