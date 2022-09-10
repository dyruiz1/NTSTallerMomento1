
# 2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
# salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
# mismo tiempo en sentido inverso al ingresado+(1)


frutas = []

for i in range(0, 11):
    fruta = {}
    fruta['nombre']=input("digite nombre de la fruta: ")
    fruta['color']=input("digite color: ")
    fruta['precio']=input("digite precio: ")

    frutas.append(fruta)
    frutas.reverse()
    print (f"{frutas} lista de ciudades")

