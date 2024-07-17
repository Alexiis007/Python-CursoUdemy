listaCosas = ["a","b","c",True,False,1,2,3]

alexis = {
    "Nombre":"Alexis",
    "Edad":20,
    "Inteligente":True,
    "NickNames":["Alexis007", "Alexsiseytor225"]
}

print("listado")
for item in listaCosas:
    print(item)

print("\nobjeto")
for item in alexis.values():
    print(item)


for i in range(0,10):
    print("hola")


lista_indices = list(enumerate("Python"))
print(lista_indices)