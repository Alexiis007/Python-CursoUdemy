from random import *
numero_secreto = randint(0,100)
respuesta = 0

for i in range(0,8):
    print("---------------------------------------------------")
    print(f"Adivina el numero secreto de entre 0 a 100, intento {i+1}:")
    respuesta = int(input())

    if respuesta==numero_secreto:
        print(f"Adivinaste bien, es el {respuesta}")
        break
    if respuesta == numero_secreto+1:
        print("Te fuiste un poquitito arriva")
    if respuesta == numero_secreto-1:
        print("Te fuiste un poquitito abajo")
    if respuesta > numero_secreto+1:
        print("Te fuiste muy arriva")
    if respuesta < numero_secreto-1:
        print("Te fuiste muy abajo")