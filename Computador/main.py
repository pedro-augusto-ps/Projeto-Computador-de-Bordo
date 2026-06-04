import time
distancia_percoridaM = 0
distancia_percoridaKM = 0
soma_velocidadesMS = 0
cont = 0
distancia_totalKM = float(input("Insira a distância a ser percorrida:(KM) "))
quantia_combustivel = float(input("Insira a quantia de combustível disponível:(L) "))
tempo_desejadoS = int(input("Insira o tempo desejado para percorrer essa distância:(S) "))

velocidade_inicialMS = 0
distancia_percoridaMS = 0
velocidades = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
consumo_litro = [0, 5.5, 4.7, 9.4, 8.1, 10.2, 9.6, 14.7, 13.6, 12.5] 

#TRANSFORMAÇOES
distancia_totalM = distancia_totalKM * 1000
tempo_desejadoMIN = tempo_desejadoS * 60
tempo_desejadoHRS = tempo_desejadoS * 3600

while True:
    print("[0] a [9] variam a velocidade")
    tecla = int(input("Escolha a velocidade: "))

    consumo_atual = consumo_litro[tecla]
    velocidade_inicialMS = velocidades[tecla]
    if tecla != 0:
        cont +=1                             # Esse contador soma os números diferentes de zero para o zero não ir na media
        soma_velocidadesMS += tecla      # Soma velocidades é a variavel usada para somar os valores para média

    ### OPERAÇÕES
    velocidade_inicialKMH = velocidade_inicialMS * 3.6              # TRANSFORMA a velocidade para KM/H
    distancia_percoridaM += velocidade_inicialMS                    #distancia percorrida em metros
    distancia_percoridaKM += velocidade_inicialKMH                  #distancia percorida em KM
    distancia_faltaM = distancia_totalM - distancia_percoridaM      #distancia que faltaM = totalM - disperM
    distancia_faltaKM = distancia_totalKM - distancia_percoridaKM
    velocidade_conclusaoMS = distancia_faltaM / tempo_desejadoMIN
    media_velocidadesMS = soma_velocidadesMS / cont                 #Faz a média em MS da velocidade

    print(f"Velocidade atual:(m/s) {tecla}")
    print(f"Velocidade atual:(Km/h) {velocidade_inicialKMH}")
    print(f"Velocidade média rodando: {media_velocidadesMS}")
    print(f"Velocidade para o tempo desejado de conclusão:(M/S) {velocidade_conclusaoMS}")

    print("-" * 40)
    print("-----Distância-----")
    print("-" * 40)
    print(f"Distância total a percorrer:(KM) {distancia_totalKM}")
    print(f"Distância percorrida:(M/S) {distancia_percoridaM}")

    time.sleep(1)