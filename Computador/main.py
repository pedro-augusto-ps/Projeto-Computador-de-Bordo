import time
import msvcrt
import os

distancia = float(input("DISTÂNCIA A SER PERCORRIDA:(KM) "))                #Valores fornecidos pelo usuario
combustivel = float(input("COMBUSTÍVEL DISPONÍVEL:(L)"))                           #Valores fornecidos pelo usuario
tempo_desejado = int(input("TEMPO DESEJADO DE CONCLUSÃO:(SEG)"))   #Valores fornecidos pelo usuario

consumo = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5]
distancia = distancia * 1000     #Converto a distancia para metros de cara
cont = 0                                    
tempo = 0                                   
tempo_parado = 0                                                      
tempo_acima25 = 0   
velocidade = 0
velocidade_somada = 0                              
distancia_percorida = 0                     
consumo_atual = 0
consumo_somado = 0                          
combustivel_restante = combustivel     #Variavel para não perder o combustível inicial com as contas               
cambio = 0                          #Carro começa parado

while True:
    tempo += 1                                  
    tempo_restante = tempo_desejado - tempo
    print("TECLAS [0] a [9] VARIAM A VELOCIDADE")
    print("APERTE Q PARA SAIR")
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
        tempo_parado += 1
        velocidade = 0
        consumo_atual = 0
    else:
        consumo_atual = consumo[cambio]                
        velocidade = cambio                      
        velocidade_somada += velocidade          
        cont += 1
        consumo_somado += consumo_atual
        combustivel_restante -= (velocidade / 1000) / consumo_atual

    distancia_percorida += velocidade
    distancia_faltante_metros = distancia - distancia_percorida
    velocidadeKMH = velocidade * 3.6
    if velocidadeKMH > 25:
        tempo_acima25 += 1

    #EXIBIÇÃO DAS INFORMAÇÕES:
    ## :.2f significa formatar para aparecer 2 numeros apos .
    print("===========================================")
    print("           COMPUTADOR DE BORDO")
    print("===========================================\n")

    if cambio == 0:
        print("---Veículo PARADO---")
        print(f"TEMPO: {tempo}")
        
    if combustivel_restante <= 0:
        print("---SEM COMBUSTÍVEL---")
        break
    if distancia_faltante_metros <= 0:
        print("===VOCÊ CHEGOU AO SEU DESTINO===")
        break
    if tempo > tempo_desejado:
        print("===TEMPO DESEJADO ULTRAPASSADO===")
    if cambio > 0:    #Só printa as informações se "cambio" > 0, evita erro por div 0
        print("==================VELOCIDADE==================")
        print(f"Velocidade atual:(M/S) {cambio}")
        print(f"Velocidade atual:(Km/h) {cambio * 3.6}")
        print(f"Velocidade média rodando: {velocidade_somada / cont:.2f}")
        if tempo_restante > 0:
            print(f"Velocidade para o tempo desejado de conclusão:(M/S) {distancia_faltante_metros / tempo_restante:.2f}")
        else:
            print("Tempo insuficiente para a estimativa de velocidade")

        print("==================DISTÂNCIA==================")
        print(f"Distância total a percorrer:(KM) {distancia /1000}")  #divido por mil, pq no inicio multipliquei para virar M
        print(f"Distância percorrida:(M) {distancia_percorida}")
        print(f"Distância percorrida:(KM) {distancia_percorida / 1000:.2f}")
        print(f"Distância que falta para chegar:(M) {distancia_faltante_metros:.2f}")
        print(f"Distância que falta para chegar:(KM) {distancia_faltante_metros / 1000:.2f}")

        print("==================TEMPO==================")
        print(f"Tempo parado: {tempo_parado}")
        print(f"Tempo desejado de viagem(S) {tempo_desejado}, (M) {tempo_desejado / 60:.2f}, (H) {tempo_desejado / 3600:.2f} ")
        print(f"Tempo ja viajado:(S) {tempo}")
        print(f"Tempo de viagem:(HH:MM:SS) {tempo // 3600}:{(tempo % 3600)//60}:{tempo % 60} ")
        print(f"Tempo de velocidade > 25KM/H: {tempo_acima25}(S)")

        print("==================COMBUSTÍVEL==================")
        print(f"Total de combustível no tanque:(L) {combustivel_restante:.2f}")
        print(f"Consumo Médio:(KM/L) {consumo_somado / cont:.2f}")
        print(f"Consumo atual:(KM/L) {consumo_atual:.2f}")


    time.sleep(1)
    os.system('cls')