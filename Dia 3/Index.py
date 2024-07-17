nombre = "Alexis"
print(f"La cuarta deltra de Alexis es {nombre[4]}")

# Buscar letras (de izquierda a derecha, osea busca la primera)
print(f"La l de alexis esta en la posicion: {nombre.index('l')}")

#Si se buscan palabras completas solo nos arroja el comienzo de la palabra
print(f"Alexis esta en la posicion: {nombre.index('Alexis')}")

# inicia la busqueda desde el indice que quieras
print(f"La posicion de la primera x desde la posicion 2: {nombre.index('x',2)}")

# inicia la busqueda desde el indice que quieras y hasta donde tu quieras
print(f"La posicion de la primera x desde la posicion 2 hasta la posicion 4: {nombre.index('x',2,4)}")

# rindex busca de derecha a izquierda