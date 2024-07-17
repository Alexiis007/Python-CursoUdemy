texto = input("Ingresa un texto:")
texto = texto.lower()

letras = []

letras.append(input("Primer fragmento busqueda").lower())

letras.append(input("Segundo fragmento busqueda").lower())

letras.append(input("Tercero fragmento busqueda").lower())

cantidad1 = texto.count(letras[0])
cantidad2 = texto.count(letras[1])
cantidad3 = texto.count(letras[2])

print(f"1 Fragmento {letras[0]} aparece :{cantidad1} veces")
print(f"2 Fragmento {letras[1]} aparece :{cantidad2} veces")
print(f"3 Fragmento {letras[2]} aparece :{cantidad3} veces")

textoDivididoEnPalabras = texto.split()

print(f"Palabras : {len(textoDivididoEnPalabras)}")

print(f"Primer letra \'{texto[0]}\' ultima letra \'{texto[-1]}\' ")

print(f"Tu texto del revez : {texto[::-1]}")

print(f"Existe la palabra Phyton en tu texto: {"phyton" in texto}")


