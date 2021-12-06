from models.cartaoCredito import CartaoCredito


class Cliente:
    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._cartoes = []

    def getNome(self):
        return self._nome
    
    def getCpf(self):
        return self._cpf

    def getEmail(self):
        return self._email
    
    def getCartoes(self):
        return self._cartoes

    def adicionarCartao(self, limite,  bandeira, cvv, validade, numero):
        cartao = CartaoCredito(limite, bandeira, cvv, validade, numero, self._nome)
        self._cartoes.append(cartao)




    