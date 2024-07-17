listaStrings = ['a','b','c','d']
listaNumeros = [1,2,3,4,5]
listaVariada = [1,'dos',True]

# Las listas son de tipo list
print(type(listaVariada))

print(len(listaVariada))

# Agregar elemento (Como el push)
print(f"lista de strings antes : {listaStrings}")
listaStrings.append("Pausa")
print(f"lista de strings despues : {listaStrings}")

#Elminar pop
# Si no se le indica la posicion del elemento al pop agarra el ultimo
# El pop modifica al array y la funcion tambien devuelve el valor extraido
ElementoElminado = listaStrings.pop(4)
print(f"Eliminamos el ultimo elemento: que seria Pausa: {listaStrings}")
print(f"Elemento elminado: {ElementoElminado}")

# Acomodar por alfabeto o mayor a menor, sort devuelve una variable pero no es necesaria la obtencion de esta
# Con simplemente ejecutarla ya realiza su trabajo
listaStrings.sort()
print(listaStrings)

# reverse es como el sort pero alrevez
listaStrings.reverse()
print(listaStrings)
