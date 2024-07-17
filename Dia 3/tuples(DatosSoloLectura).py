# Son como objetos en los que sus items son de solo lectura pero los contenidos de estos items
# pueden ser modificados
# Si aceptan arrays
Tuple=(1,'a',(3,3.1),4,[12,12],{"alexis":"alexis"})
print(Tuple)
print(Tuple[0])
print(Tuple[2][1])

# Desestrcuturacion completa (se deben recivir el numero de variables existentes (Solo las padre))
# Esto funciona en arrays y objetos tambien
a,b,c,d,e,f = Tuple
print(a,b,c,d,e,f)

num1 = Tuple[0]
print(num1)

Tuple[4][1]=13
print(Tuple)

Tuple[5]["alexis"]="brayan"
print(Tuple)

