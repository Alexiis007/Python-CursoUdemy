numero = 5.8
print("Numero : "+str(numero)+" De tipo:"+str(type(numero)))

# Los input por defecto reciben siempre strings
edad = int(input("Cual es tu edad: "))
print(type(edad))
# Como en el print antes de la suma de edad mas edad ahy un str el resultado que regresara es str
# Ya que toma como str a tod0 lo que sigue
# print("Tu edad al doble seria: "+(edad+edad))
print(f"Tu edad al doble seria: {edad + edad}")
print(edad + edad)
