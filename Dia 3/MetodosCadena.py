texto = "Christian Alexis Juarez Rdz"

print(texto.upper())

print(texto.lower())

# Separar y regresa una lista con los datos regresados
print(texto.split("Alexis"))

# Unir cadenas
a = "a"
b = "b"
c = "c"
# El " " es la separacion entre elementos
resultado = "-".join([a,b,c])
print(f"Resultado es: {resultado}")

# Buscar
print(f"La a esta en el puesto {texto.find("a")}")

# Replace emplaza un elemento por otro esto no modifica al valor original solo es momentaneopoo
print(texto.replace("A","8"))

# existe una palabra en una cadena (regresa bool)
print("Existe sol en el texto: "+str("sol" in texto))
print("Existe Alexis en el texto: "+str("Alexis" in texto))
print("No existe sol en el texto: "+str("sol" not in texto))

# Largo de cadenas
print(f"El largo de el xontenido de texto es: {len(texto)}")

# Repetir textos con multiplicacion
print(f"texto * 2 (el doble): {texto*2}")

# Textos largos
textoLargo = """
Christian 
Alexis 
Juarez 
"""


# contar los letras de una cadena
print(texto.count("e"))