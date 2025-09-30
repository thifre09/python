import random
from enum import Enum
import tkinter

class Sexo(Enum):
    MACHO = 1
    FEMEA = 2

class Alimentacao(Enum):
    HERBIVORO = 1
    CARNIVORO = 2
    ONIVORO = 3

class Especie:
    def __init__(self, nome):
        self.nome: str = nome
        self.numero: int = 0
        self.seresVivos: list[SerVivo] = []

class Habitate:
    def __init__(self, nome: str, caracteristicasVantajosas: list[str]):
        self.nome: str = nome
        self.caracteristicasVantajosas: list[str] = caracteristicasVantajosas

class SerVivo:
    def __init__(self, nomeEspecie: str, expectativa_vida: int, fertilidade: float, tamanho: float, peso: float, 
                 velocidade: float, forca: int, sexo: Sexo, agressividade: int, inteligencia: int, sociabilidade: int, 
                 habitate: Habitate, alimentacao: Alimentacao, pai: "SerVivo"=None, mae: "SerVivo"=None):
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
            "expectativa_vida": validarNumero(expectativa_vida, 1, 10000),
            "saude": 100.0,
            "fertilidade": validarNumero(fertilidade, 0, 100),

            "tamanho": validarNumero(tamanho, 0.001, 1000),   # metros
            "peso": validarNumero(peso, 0.00000001, 10000000),        # kg
            "velocidade": validarNumero(velocidade, 0.000001, 1000), # m/s
            "sexo": sexo,

            "forca": validarNumero(forca, 1, 100),
            "agressividade": validarNumero(agressividade, 1, 100),
            "inteligencia": validarNumero(inteligencia, 1, 100),
            "sociabilidade": validarNumero(sociabilidade, 1, 100),

            "habitat": habitate,
            "alimentacao": alimentacao
        }


especies: dict[str, Especie] = {}
habitates: dict[str, Habitate] = {}

def validarNumero(num, min, max):
    if num < min:
        return min
    elif num > max:
        return max
    

def start():
    nomePrimeiroEspecie = input("Digite o nome da primeira espécie:")
    primeiroEspecie = Especie(nomePrimeiroEspecie)
    especies[nomePrimeiroEspecie] = primeiroEspecie


    primeiroSerVivo = SerVivo()

def ciclo():
    pass

if __name__ == "__main__":
    pass