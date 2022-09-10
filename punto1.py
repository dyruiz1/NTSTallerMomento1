# Construir un programa que permita ingresar N (cantidad digitada por
# el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
# fueron ingresados (+1)


vueltas = int(input("DiGITA la cantidad de vueltas que desea dar: "))
count = 0
suma1 = 0
suma2 = 0


for x in range (vueltas):
    numero= int(input("DiGITA UN Número: "))
    if(numero % 2 ==0):          
        suma1 += 1
    elif(numero % 3 ==0):
        suma2 += 1

print (f"{suma1} son multiplos de 2")
print (f"{suma2} son multiplos de 3")



