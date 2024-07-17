from random import *
palabras_secretas = ['AlexisA', 'AlexisA']
palabra_secreta = " ".join(choice(palabras_secretas).lower()).split(' ')
letras_encontradas = list('_'*len(palabra_secreta))
vidas = 6
teminarJuego = False


def ingrese_letra():
    abc = "abcdefghijklmnñopqrstuvwxyz"
    bandera = False
    letra = ''
    print("---------------------------------------------------")
    # Comprobacion de la validez de la letra
    while not bandera:
        letra = input("Ingrese una letra: ").lower()
        if letra in abc and len(letra) == 1:
            bandera = True
        else:
            print("Esa no es una letra correcta!")
    # La letra existe en la palabra secreta
    if letra in palabra_secreta:
        while letra in palabra_secreta:
            indice = palabra_secreta.index(letra)
            letras_encontradas[indice] = letra
            palabra_secreta.pop(indice)
        print("Atinaste la palabra")
        return True
    # La letra no existe en la palabra secreta
    elif letra not in palabra_secreta:
        print("Fallaste la palabra")
        return False


print("Bienvenido al ahorcado")
while not teminarJuego:
    print(f"Letras encontradas: {str(letras_encontradas)}")
    if ingrese_letra():
        print(f"Vidas {vidas}")
        print(f"letras numero {len(palabra_secreta)} ")
    else:
        vidas -= 1
        print(f"Vidas {vidas}")
        if vidas == 0:
            print("----- Perdiste -----")
            print(f"La palabra era: {letras_encontradas}")
            teminarJuego = True


