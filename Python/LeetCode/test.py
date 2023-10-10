class MinhaClasse():
    def __init__(self, nome):
        self.__nome = nome

    def FalarNome (self):
        print(f"Meu nome e: {self.__nome}")

    def __FuncaoPrivada(self):
        print("Funcao privada")

classe = MinhaClasse("Luis")
classe.FalarNome()
# print(classe.__nome)
classe.__FuncaoPrivada()