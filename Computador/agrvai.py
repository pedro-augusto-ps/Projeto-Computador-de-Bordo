import time
import msvcrt

distancia = float(input("Insira a distância a ser percorrida: "))                #Valores fornecidos pelo usuario
combustivel = float(input("Insira o combustível:(L)"))                           #Valores fornecidos pelo usuario
tempo_desejado = int(input("Insira o tempo desejado de conclusão:(Segundos)"))   #Valores fornecidos pelo usuario
cambio = 0
tempo = 0
tempo_parado = 0
consumo = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5]
cont = 0
distancia_percorrida = 0
velocidade_atual = 0
velocidade_somada = 0
while True:
    tempo += 1
    tempo_restante = tempo_desejado - tempo
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla.isdigit():
            valor = int(tecla)
            if 0 <= valor <=9:
                cambio = valor
        elif tecla == b'Q'.lower():
            print("Sair selecionado")
            break
    if cambio == 0:
        print("Carro parado")
        tempo_parado += 1
        consumo_atual = 0
    else:
        consumo_atual = consumo[cambio]
        velocidade_atual = cambio
        cont += 1

    velocidade_somada += velocidade_atual
    distancia_percorrida += velocidade_atual
    distancia_faltante_metros = distancia - distancia_percorrida

if cont > 0:
    print(f"Velocidade atual:(m/s) {velocidade_atual}")
    print(f"Velocidade atual:(Km/h) {velocidade_atual * 3.6}")
    print(f"Velocidade média rodando: {velocidade_somada / cont}")
    print(f"Velocidade para o tempo desejado de conclusão:(M/S) {distancia_faltante_metros / tempo_restante}")