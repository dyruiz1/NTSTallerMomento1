# 3.Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el producto (+0.4)
# 5. Digitar 0 para SALIR
# Finalmente, versione y comparta el repositorio según las indicaciones dadas+(1.4)

 
print("***MENU***")
print("1. agregar producto")
print("2. Mostrar producto")
print("3. Buscar y editar")
print("4. Buscar y eliminar producto")
print("5. SALIR")
opcion = 0


productos=[]

while(opcion!=5):
    producto={}
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
     
        producto['codigo']=input("digite codigo del producto: ")
        producto['nombre']=input("digite nombre de producto: ")
        producto['precio']=input("digite precio de venta: ")
        productos.append(producto)
        print("agregando productos")
    elif(opcion==2):   
        print(productos)
        print("Mostrando productos")
        
    elif(opcion==3):
        codigo = input("Digite el producto que desea buscar y editar: ")
        for auxiliar in productos:
            if auxiliar['codigo']== codigo:
                print(auxiliar)
                auxiliar['precio'] = input("digite el nuevo precio: ")
                break
        else:
            print("no se encuentra la producto")
       
    elif(opcion==4):
        codigo = input("Digite el codigo que desea buscar y eliminar: ")
        index=[x['codigo'] for x in productos].index(codigo)
        productos.pop(index)
        print(productos)
    else:
        print("digite una opcion valida")
else:
    print("fin")
