
#Importamos todas los archivos de python para poder utilizarlos y llamar a sus funciones
from Menu_cliente import *
from Menu_tienda import *
from Menu_producto import *
from Menu_venta import *


#Despliega el menu visual en consola
def mostrar_menu():
    print (30 * "-", "MENU", 30 * "-")
    print("1. Menu Cliente")
    print("2. Menu Productos")
    print("3. Menu Tienda")
    print("4. Menu Venta")
    print("0. Salir")

#Un while que permite llamar a las funciones con if adentro hasta que el valor sea 0, con esto logramos que sea infinito hasta que sea 0
while True:
    mostrar_menu()
    #Input que permite la seleccion de opciones
    seleccion = input("Selecciona una opción: ")

    if seleccion == "1":
        #Llama la funcion del menu cliente
        generamenu()
    elif seleccion == "2":
        #Llama la funcion del menu producto
        generamenuProducto()
    elif seleccion == "3":
        #Llama la funcion del menu tienda
        generamenuTienda()
    elif seleccion == "4":
        #Llama la funcion del menu Venta
        generamenuVenta()
    elif seleccion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")