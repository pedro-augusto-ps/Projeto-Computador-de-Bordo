import time
import msvcrt
import os

distancia = float(input("Insira a distância a ser percorrida: "))                #Valores fornecidos pelo usuario
combustivel = float(input("Insira o combustível:(L)"))                           #Valores fornecidos pelo usuario
tempo_desejado = int(input("Insira o tempo desejado de conclusão:(Segundos)"))   #Valores fornecidos pelo usuario

cont = 0                                    #Conta a cada repetição que o carro não esta parado, usado para as médias

tempo = 0                                   #Inicializo o tempo para contar a cada repetição
tempo_parado = 0                            #Inicializo o tempo para contar a cada repetição(Parado)                          
tempo_acima25 = 0                           #Inicializo o tempo para contar a cada repetição(Que está acima de 25KM/h)

velocidade_somada = 0                       #Usado para somar as velocidades posteriormente        
distancia_percorida = 0                     #Usado para verificar a distância percorrida

consumo_somado = 0                          
combustivel_usado = combustivel                   
cambio = 0
velocidade = 0
consumo = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5]
consumo_atual = 0
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
                                              #Alternador de "marchas/velocidade"
    if cambio == 0:                                                 #Se velocidade 0, carro parado.
        tempo_parado += 1
    else:
        consumo_atual = consumo[cambio]                #Consumo = consumo[no indice fornecido anteriormente, coincidentemente, 1 representa consumo 1]
        velocidade = cambio                      #Velocidade será = o input do usuário
        velocidade_somada += velocidade          #Soma toda velocidade a cada segundo
        cont += 1
        consumo_somado += consumo_atual

    velocidadeKMH = velocidade * 3.6
    combustivel_usado -= consumo_atual

    if velocidadeKMH > 25:
        tempo_acima25 += 1

    distancia_percorida += velocidade
    distancia_faltante_metros = distancia - distancia_percorida
    tempo_javiajado = tempo + tempo_parado
    if combustivel_usado <= 0:
        print("Cabou a gasosa")
        break
    if cambio > 0:
        print(f"Velocidade atual:(m/s) {cambio}")
        print(f"Velocidade atual:(Km/h) {cambio * 3.6}")
        print(f"Velocidade média rodando: {velocidade_somada / cont}")
        print(f"Velocidade para o tempo desejado de conclusão:(M/S) {distancia_faltante_metros / tempo_restante}")

        print("-" * 40)
        print("-----Distância-----")
        print("-" * 40)
        print(f"Distância total a percorrer:(KM) {distancia}")
        print(f"Distância percorrida:(M) {distancia_percorida}")
        print(f"Distância percorrida:(KM) {distancia_percorida / 1000}")
        print(f"Distância que falta para chegar:(M) {distancia_faltante_metros}")
        print(f"Distância que falta para chegar:(KM) {distancia_faltante_metros / 1000}")

        print("-" * 40)
        print("-----Tempo-----")
        print("-" * 40)
        print(f"Tempo desejado de viagem(S) {tempo_desejado}, (M) {tempo_desejado / 60}, (H) {tempo_desejado / 3600} ")
        print(f"Tempo ja viajado:(S) {tempo_javiajado}")
        print(f"Tempo de viagem:(HH:MM:SS) ")
        print(f"Tempo de velocidade > 25KM/H: {tempo_acima25}(S)")

        print("-" * 40)
        print("-----Combustível-----")
        print("-" * 40)
        print(f"Total de combustível no tanque:(L) {combustivel_usado}")
        print(f"Consumo Médio:(KM/L) {consumo_somado / cont}")
        print(f"Consumo atual:(KM/L) {consumo_atual}")
        time.sleep(2)
        os.system('cls')