#Importa el archivo cliente
from Cliente import *

#Funcion con while adentro para que sea infinito hasta que su valor sea 0
def generamenu():
    while True: 
        print("Presiona 1 para guardar un nuevo cliente")
        print("Presiona 2 para listar los clientes guardados")
        print("Presiona 3 para eliminar")
        print("Presiona 4 para modificar")
        print("Presiona 0 Salir\n")
        #Si su valor es 1 Llama a la funcion de guardar primero en inputs permite las entradas y las guarda en una variable, luego llama al objeto cliente en el metodo guardar
        opcion = input()
        if opcion == "1":
            cedulafe = input("Escriba la cedula del nuevo cliente\n")
            nombrefe = input("Escriba el nombre del nuevo cliente\n")
            pafe = input("Escriba el primer apellido del nuevo cliente\n")
            safe = input("Escriba el segundo apellido del nuevo cliente\n")
            direccionfe = input("Escriba la direccion del nuevo cliente\n")
            correolectronicofe = input("Escriba el correo electronico del nuevo cliente\n")
            tipofe = input("Escriba el tipo del nuevo cliente\n")
            clavefe   = input("Escriba la clave  del nuevo cliente\n")
            nuevocliente = Cliente()
            nuevocliente.cedula = cedulafe
            nuevocliente.nombre = nombrefe
            nuevocliente.primerapellido = pafe
            nuevocliente.segundoapellido = safe
            nuevocliente.direccion = direccionfe
            nuevocliente.correolectronico = correolectronicofe
            nuevocliente.tipo = tipofe
            nuevocliente.clave = clavefe
            print(nuevocliente)
            nuevocliente.guardar()

        elif opcion == "2":
            #lista los clientes para verlos utilizando un for para iterar sobre ellos y una funcion que retorna esa lista, que esta dentro del objeto cliente
            nuevocliente = Cliente()
            for elemento in nuevocliente.listar():
                print(elemento.cedula + " " + elemento.nombre)
        elif opcion == "3":
            #Pide el id en un input lo guarda en una varible y luego llama al metodo que esta en cliente
            cedulafe = input("Escriba la cedula a eliminar\n")
            nuevocliente = Cliente()
            nuevocliente.cedula = cedulafe
            nuevocliente.eliminar()
            break
        elif opcion == "4":
            #Los inputs permite las entradas y las guarda en una variable, luego llama al objeto cliente en el metodo modificar
            print("De las siguientes clientes escriba la cedula del que quiere modificar\n")
            nuevocliente = Cliente()
            for elemento in nuevocliente.listar():
                print(elemento.cedula + " " + elemento.nombre)
            cedulafe = input()
            nuevocliente.cedula = cedulafe
            nuevocliente.nombre = input("Escriba el nuevo nombre del cliente\n")
            nuevocliente.primerapellido = input("Escriba el nuevo primer apellido del cliente\n")
            nuevocliente.segundoapellido = input("Escriba el nuevo segundo apellido del cliente\n")
            nuevocliente.direccion = input("Escriba la nueva direccion del cliente\n")
            nuevocliente.correoelectronico = input("Escriba el nuevo correo del cliente\n")
            nuevocliente.tipo = input("Escriba el nuevo tipo del cliente\n")
            nuevocliente.clave = input("Escriba la nueva clave del cliente\n")

            nuevocliente.modificar()
            break
        elif opcion == "0":
            break
        else:
            print("Seleccione una opcion correcta\n")
