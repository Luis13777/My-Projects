# lista = [0,1,2,3,4,5,6,7,8,9]

# lista2 = lista[1:7:2]

# print(lista2)

# from typing import List


class Bixo:
    def __init__(self, nome, frase, idade):
        self.nome = nome
        self.frase = frase
        self.idade = idade
        self.proximo = None

class T26:
    def __init__(self):
        self.Cabeca = None

    def adicionarNoFim (self, nome, frase, idade):
        NovoBixo = Bixo(nome, frase, idade)
        if self.Cabeca is None:
            self.Cabeca = NovoBixo
        else:
            last = self.Cabeca
            while (last.proximo is not None):
                last = last.proximo
            last.proximo = NovoBixo

    def adicionarNoComeco (self, nome, frase, idade):
        NovoBixo = Bixo(nome, frase, idade)
        NovoBixo.proximo = self.Cabeca
        self.Cabeca = NovoBixo

    def deletaBixo (self, nome):
        deletar = self.Cabeca
        anterior = self.Cabeca
        if (anterior.nome == nome):
            self.Cabeca = anterior.proximo
            anterior.proximo = None
            anterior = None
            deletar = None
        else:
            while (deletar.nome != nome or deletar.proximo is not None):
                deletar = deletar.proximo
                if (deletar.nome != nome):
                    anterior = anterior.proximo
            if (deletar.nome == nome):
                anterior.proximo = deletar.proximo
                deletar.proximo = None
                anterior = None
                deletar = None

    def MostrarBixaral (self):
        Bixao = self.Cabeca
        while(Bixao is not None):
            print(f"{Bixao.nome}, {Bixao.frase}, tenho {Bixao.idade} anos!")
            Bixao = Bixao.proximo

Bixaral = T26()

Bixaral.adicionarNoComeco("Mastro", "Sou Bixao", 22)
Bixaral.adicionarNoComeco("Diozin", "Sou Bixaummmmmm", 10)
Bixaral.adicionarNoFim("Rodo", "Sou Bixaummmmmm", 69)

Bixaral.MostrarBixaral()

Bixaral.deletaBixo("Diozin")
print("\n")

Bixaral.MostrarBixaral()
