import random

class Especie:
    def __init__(self, nome):
        self.nome = nome

especies: dict[str: Especie] = {}

class SerVivo:
    def __init__(self, nomeEspecie):
        self.especie: Especie = especies[nomeEspecie]
        self.nome: str = self.especie.nome + random.randint(1, 1000000)