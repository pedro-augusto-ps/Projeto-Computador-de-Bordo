import time

distancia = float(input("Insira a distância a ser percorrida: "))
combustivel = float(input("Insira o combustível:(L)"))
tempo_desejado = int(input("Insira o tempo desejado de conclusão:(Segundos)"))
tempo = 0
tempo_parado = 0
cont = 0
velocidade_somada = 0
distancia_percorida = 0
while True:
    tempo += 1
    consumo = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5] 
    cambio = int(input("Insira a velocidade:[1] a [9]"))
    if cambio == 0:
        tempo_parado += 1
    else:
        consumo = consumo[cambio]
        velocidade = cambio
        velocidade_somada += velocidade
        tempo_restante = tempo_desejado - 1
        cont += 1
    distancia_percorida += velocidade
    distancia_faltante_metros = distancia - distancia_percorida
    print(f"Velocidade atual:(m/s) {cambio}")
    print(f"Velocidade atual:(Km/h) {cambio * 3.6}")
    print(f"Velocidade média rodando: {velocidade_somada / cont}")
    print(f"Velocidade para o tempo desejado de conclusão:(M/S) {distancia_faltante_metros / tempo_restante}")

    print("-" * 40)
    print("-----Distância-----")
    print("-" * 40)
    print(f"Distância total a percorrer:(KM) {distancia}")
    print(f"Distância percorrida:(M/S) {distancia_percorida}")
    print(f"Distância que falta para chegar:(M) {distancia_faltante_metros}")
    print(f"Distância que falta para chegar:(KM) {distancia_faltante_metros / 1000}")
