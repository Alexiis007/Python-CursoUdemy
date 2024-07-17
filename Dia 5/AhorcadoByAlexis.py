from random import choice
lista_palabras = ["Hola"]
palabra_elegida = choice(lista_palabras)
letras_unicas = len(set(palabra_elegida))
print(letras_unicas)