alexis = {
    "nombre":"Alexis",
    "edad":20,
    "cosasFavoritos":[8,"Azul",True],
    "mascota":{
        "nombre":"kelo",
        "Edad":5
    }
    #Tambien se puden con objetos pero me dio peresa
}
print(f"Hola {alexis["nombre"]} encerio tienes {alexis["edad"]} ?")
print(f"Cosas favoritas: {alexis["cosasFavoritos"]} numero favorito: {alexis["cosasFavoritos"][0]}")
print(f"Mascota: {alexis["mascota"]} nombre mascota: {alexis["mascota"]["nombre"]}")
print(alexis)
# Keys regresa los elementos no sus contenidos
print(alexis.keys())
# Values regresa sus valores
print(alexis.values())
# items trae los elementos y sus resultados
print((alexis.items()))