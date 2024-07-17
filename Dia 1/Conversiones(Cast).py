# Cast Dinamico (Implicito)
num1 = 10
num2 = 10.12

num1 = num1 + num2

print("Numero 1 ("+str(num1)+") (antes int): "+str(type(num1)))

print("Numero 2 ("+str(num2)+") (Float): "+str(type(num2)))

# num1 paso de int a float

print("-----------------------------------------------")

# De float a int
num2 = int(num2)

print("Num2 ("+str(num2)+") de float a int: "+str(type(num2)))


print("-----------------------------------------------")

edad = int(input("Cual es tu edad \n"))
print(type(edad))
print("Tu edad es: "+str(edad))
