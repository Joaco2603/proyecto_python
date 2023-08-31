#Importa el archivo tienda
from Tienda import *



#Funcion con while adentro para que sea infinito hasta que su valor sea 0
def generamenuTienda():
    while True:

  
        print("Presiona 1 para guardar un nueva tienda")
        print("Presiona 2 para listar las tiendas guardadas")
        print("Presiona 3 para eliminar las tiendas")
        print("Presiona 4 para modificar las tiendas")
        print("Presiona 0 Salir")

        opcion = input()
        #Si su valor es 1 Llama a la funcion de guardar primero en inputs permite las entradas y las guarda en  una variable, luego llama al objeto cliente en el    metodo guardar
        if opcion == "1":
            idfe = input("Escriba el id de la nueva tienda")
            nombrefe = input("Escriba el nombre de la nueva tienda")
            descfe = input("Escriba la descripcion de la nueva tienda")
            direccionfe = input("Escriba la direccion de la nueva tienda")
            telefonosfe = input("Escriba los telefonos de la nueva tienda")
         
            nuevatienda = Tienda()
            nuevatienda.id = idfe
            nuevatienda.nombre = nombrefe
            nuevatienda.descripcion = descfe
            nuevatienda.direccion = direccionfe
            nuevatienda.telefonod = telefonosfe
    
            nuevatienda.guardar()
        elif opcion == "2":
            #lista los clientes para verlos utilizando un for para iterar sobre ellos y una funcion que retorna esa lista, que esta dentro del objeto cliente
            nuevatienda = Tienda()
            for elemento in nuevatienda.listar():
                print(elemento.id + " " + elemento.nombre)
        elif opcion == "3":
            #Los inputs permite las entradas y las guarda en una variable, luego llama al objeto cliente en el metodo modificar
            cedulafe = input("Escriba la tienda a eliminar\n")
            tiendita = Tienda()
            tiendita.id = cedulafe
            tiendita.eliminar()
        elif opcion == "4":
            #Pide el id en un input lo guarda en una varible y luego llama al metodo que esta en cliente
            print("De las siguientes tiendas escriba el id que quiere modificar\n")
            tiendita = Tienda()
            for elemento in tiendita.listar():
                print(elemento.id + " " + elemento.nombre)
            cedulafe = input()
            tiendita.id = cedulafe
            tiendita.nombre = input("Escriba el nuevo nombre de la tienda\n")
            tiendita.descripcion = input("Escriba la nueva descripcion de la tienda\n")
            tiendita.direccion = input("Escriba la nueva direccion\n")
            tiendita.telefonos = input("Escriba el nuevo telefono\n")
            tiendita.modificar()
        elif opcion == "0":
            break
        else:
            print("Seleccione una opcion correcta")