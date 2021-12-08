class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._telefone = telefone

    def getNome(self):
        return self._nome
    
    def getCpf(self):
        return self._cpf

    def getEmail(self):
        return self._email
    
    def getTelefone(self):
        return self._telefone

    def realizarPedido(self):
        return 'something'