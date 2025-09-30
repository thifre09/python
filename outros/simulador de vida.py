import random

class Especie:
    def __init__(self, nome):
        self.nome: str = nome
        self.numero: int = 0
        self.seresVivos: list[SerVivo] = []

class SerVivo:
    def __init__(self, nomeEspecie: str, pai, mae):
        if nomeEspecie not in especies:
            especies[nomeEspecie] = Especie(nomeEspecie)
        self.especie: Especie = especies[nomeEspecie]
        self.especie.numero += 1
        self.especie.seresVivos.append(self)
        self.nome: str = self.especie.nome + self.especie.numero
        self.pai: "SerVivo" = pai
        self.mae: "SerVivo" = mae
        self.caracteristicas: dict = {
            "idade": 0,
            "expectativa_vida": random.randint(5, 100),
            "saude": 100.0,
            "fertilidade": random.uniform(0.1, 1.0),

            "tamanho": random.uniform(0.1, 2.0),   # metros
            "peso": random.uniform(1, 100),        # kg
            "velocidade": random.uniform(0.1, 20), # m/s
            "forca": random.randint(1, 10),
            "sexo": random.choice(["M", "F"]),

            "agressividade": random.randint(0, 100),
            "inteligencia": random.randint(1, 10),
            "sociabilidade": random.randint(0, 100),

            "habitat": random.choice(["terra", "agua", "ar"]),
            "alimentacao": random.choice(["herbívoro", "carnívoro", "onívoro"])
        }

class Habitate:
    def __init__(self, nome: str, caracteristicasVantajosas: list[str]):
        self.nome: str = nome
        self.caracteristicasVantajosas: list[str] = caracteristicasVantajosas

especies: dict[str, Especie] = {}
habitates: dict[str, Habitate] = {}

if __name__ == "__main__":
    print("ola")