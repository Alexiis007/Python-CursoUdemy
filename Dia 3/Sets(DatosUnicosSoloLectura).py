# Los sets son de solo lectura ya que no pueden ser modificados y tambieen deben ser unicos
# Muy parecidos a los tuples pero no admiten valores mutables como los arrays
# No se admiten arrays 😒
mi_set = set((1,2,3,4,5))
print(mi_set)


# Para agregar un nuevo item en el set lo acemos con add
mi_set.add("Alexis")
print(mi_set)

# Para elmiminar remove()
# si se agrega una posicion que no existe aun marca error
# Si elmiminas con el pop() en este caso con los sets es aleatorio
# ya que no son ordenados
mi_set.remove(1)
print(mi_set)

# el discard() es igual que el remove pero en la parte de mandar error si una posicion no existe
# se la salta (No da el error)
mi_set.discard(1)
print(mi_set)

# Union de 2 sets

mi_set2 = set(('a','b','c','d','e'))

mi_set_3 = mi_set.union(mi_set2)

print(mi_set_3)