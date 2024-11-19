x = 1
quadrados = 0
quadrado_click = 1

import random

def evento_raro(chance_percentual):
    return random.random() < (chance_percentual / 100.0)

# Configurações
chance_de_evento = 10  # 1% de chance
numero_de_testes = 10000
contador_de_eventos = 0

# Executando os testes
while x == 1:
    algo = input()

    if algo == "":
        quadrados += quadrado_click
        menu = ""
        if evento_raro(chance_de_evento):
            contador_de_eventos += 1

# Resultados
    print(f"O evento raro aconteceu {contador_de_eventos} vezes em {quadrados} testes.")

