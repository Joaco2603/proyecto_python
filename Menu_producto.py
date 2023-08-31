#Importa los archivos
from Tienda import *
from Producto import *

#Funcion con while adentro para que sea infinito hasta que su valor sea 0
def generamenuProducto():
    while True:

  
        print("Presiona 1 para guardar un nuevo producto")
        print("Presiona 2 para listar los productos guardados")
        print("Presiona 3 para eliminar un producto")
        print("Presiona 4 para modificar un producto")
        print("Presiona 0 Salir\n")

        opcion = input()
        #Si su valor es 1 Llama a la funcion de guardar primero en inputs permite las entradas y las guarda en una variable, luego llama al objeto cliente en el metodo guardar
        if opcion == "1":
            idfe = input("Escriba el id del nuevo producto\n")
            nombrefe = input("Escriba el nombre del nuevo producto\n")
            descfe = input("Escriba la descripcion de la nueva tienda\n")
            precioxunidadfe = input("Escriba el precio por unidad del producto\n")
            unidaddemedidafe = input("Escriba la  unidad de medida del producto\n")

            print("De las siguientes tiendas, escriba el identificador de la tienda asociada al producto\n")
            tiendita = Tienda()
            for elemento in tiendita.listar():
                print(elemento.id + " " + elemento.nombre)
            
            tiendita.id = input()
            productito = producto()
            productito.id= idfe
            productito.nombre= nombrefe
            productito.descripcion = descfe
            productito.precioxunidad= float(precioxunidadfe)
            productito.unidaddemedida = unidaddemedidafe
            productito.tienda= tiendita
            productito.guardar()
        elif opcion == "2":
            #lista los clientes para verlos utilizando un for para iterar sobre ellos y una funcion que retorna esa lista, que esta dentro del objeto cliente
            productito = producto()
            for elemento in productito.listar():
                print(elemento.id + " " + elemento.nombre)
        elif opcion == "3":
            #Pide el id en un input lo guarda en una varible y luego llama al metodo que esta en cliente
            cedulafe = input("Escriba la cedula a eliminar\n")
            productito = producto()
            productito.id = cedulafe
            productito.eliminar()
        elif opcion == "4":
            #Los inputs permite las entradas y las guarda en una variable, luego llama al objeto cliente en el metodo modificar
            print("De los siguientes productos escriba el id del que quiere modificar\n")
            productito = producto()
            for elemento in productito.listar():
                print(elemento.id + " " + elemento.nombre)
            cedulafe = input()
            productito.id = cedulafe
            productito.nombre = input("Escriba el nuevo nombre del producto\n")
            productito.descripcion = input("Escriba la nueva descripcion del producto\n")
            productito.precioxunidad = input("Escriba el nuevo precio por unidad\n")
            productito.unidaddemedida = input("Escriba la nueva unidad de medida\n")
            tiendita = Tienda()
            for elemento in tiendita.listar():
                print(elemento.id + " " + elemento.nombre)
            productito.tienda = input("Escriba la nueva tienda\n")

            productito.modificar()
        elif opcion == "0":
            break
        else:
            print("Seleccione una opcion correcta")