import time

distancia_percorrida = float(input("Insira a distância a ser percorrida: "))
quantia_combustivel = float(input("Insira a quantia de combustível disponível: "))
tempo_desejado = int(input("Insira o tempo desejado para percorrer essa distância:(segundos) "))

km_para_m = distancia_percorrida * 1000
velocidade_inicial = 0

while True:
    print("Consumo (Km/L)	Velocidade (m/s)")
    print("     0	                0")
    print("    5.5	                1")
    print("    4.7	                2")
    print("    9.4	                3")
    print("    8.1	                4")
    print("    10.2	                5")
    print("    9.6	                6")
    print("    14.7	                7")
    print("    13.6	                8")
    print("    12.5	                9")