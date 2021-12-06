from models.carrinho import Carrinho
from models.livro import Livro
from models.game import Game
from models.cliente import Cliente
from models.pedido import Pedido

print("Sequencia de Operacoes\n")

##OPERAÇÃO 1
print("Primeira Operacao:\n")

cliente1 = Cliente("Davi Mesquita", "14727089700", "davicm98@hotmail.com") 
cliente1.adicionarCartao(2000, "Visa", "369", "02/25", "1234567890123456")
cliente1.adicionarCartao(3000, "Mastercard", "963", "02/25", "6543210987654321")
cartao1 = cliente1.getCartoes()[0]

cliente2 = Cliente("Caio Mesquita", "12345678900", "caio@email.com")
cliente2.adicionarCartao(2500, "Visa", "123", "02/25", "2222222222222222")

cliente3 = Cliente("Maria Mesquita", "01234567899", "maria@email.com")
cliente3.adicionarCartao(1500, "Mastercard", "456", "02/25", "3333333333333333")
cliente3.getCartoes()[0].debitar(1499)


print("Cliente1: " + cliente1.getNome())
print("Cartao1.1 || Numero: " + cliente1.getCartoes()[0].getNumero() + "  |  Limite: " + str(cliente1.getCartoes()[0].getUtilizado()) + "/" + str(cliente1.getCartoes()[0].getLimite()) )
print("Cartao1.2 || Numero: " + cliente1.getCartoes()[1].getNumero() + "  |  Limite: " + str(cliente1.getCartoes()[1].getUtilizado()) + "/" + str(cliente1.getCartoes()[1].getLimite()) + "\n")

print("Cliente2: " + cliente2.getNome())
print("Cartao2 || Numero: " + cliente2.getCartoes()[0].getNumero() + "  |  Limite: " + str(cliente2.getCartoes()[0].getUtilizado()) + "/" + str(cliente2.getCartoes()[0].getLimite()) + "\n")

print("Cliente3: " + cliente3.getNome())
print("Cartao3 || Numero: " + cliente3.getCartoes()[0].getNumero() + "  |  Limite: " + str(cliente3.getCartoes()[0].getUtilizado()) + "/" + str(cliente3.getCartoes()[0].getLimite()) + "\n")

##OPERAÇÃO 2
print("\nSegunda Operacao:\n")

game1 = Game(49.99, 5, "Zelda", "Aventura", "Nintendo", "10")
game2 = Game(59.99, 400, "Skyrim", "RPG", "Bethesda", "12")
livro1 = Livro(32.50, 10, "Percy Jackson", "Ficção", "12345678", "234", "Rick Riordan")
livro2 = Livro(35, 2, "Harry Potter", "Ficção", "34567890", "345", "J.K. Rowling")

print("Game1: " + game1.getNomeProduto())
print("Game2: " + game2.getNomeProduto())
print("Livro1: " + livro1.getNomeProduto())
print("Livro2: " + livro2.getNomeProduto())


##OPERAÇÃO 3 e 7
print("\nTerceira e Setima Operacao:\n")

print("Carrinho1 do Cliente1 e sucesso na compra de um cliente com mais cartões\n")
carrinho1 = Carrinho()
carrinho1.insereProduto(livro1, 1)
carrinho1.insereProduto(game2, 1)
carrinho1.finalizarCompra(1, cliente1, cliente1.getCartoes()[0])

print("\nCarrinho2 do Cliente1 e sucesso na compra de um cliente com mais cartões\n")
carrinho2 = Carrinho()
carrinho2.insereProduto(livro2, 2)
carrinho2.finalizarCompra(2, cliente1, cliente1.getCartoes()[1])


##OPERAÇÃO 4, 5 e 6
print("\nQuarta, Quinta e Sexta Operacao:\n")

print("Carrinho3 do Cliente2 e pedido nao efetivado por falta produto no estoque\n")
carrinho3 = Carrinho()
carrinho3.insereProduto(livro2, 1)
carrinho3.finalizarCompra(3, cliente2, cliente2.getCartoes()[0])

print("\nCarrinho4 do Cliente3 e pedido nao efetivado por falta de limite no cartão\n")
carrinho4 = Carrinho()
carrinho4.insereProduto(game2, 1)
carrinho4.finalizarCompra(4, cliente3, cliente3.getCartoes()[0])





