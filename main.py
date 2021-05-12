#from claseViajeroFrecuente import Viajero
from claseManejadorViajero import ManejadorViajero
from claseMenu import  Menu
import os
import csv
def test():
    archivo = open('csv pasajeros_test.csv')
    manejador.testViajeros(archivo)
    print('archivo test cargado \n')
    manejador.mostrarViajeros()
    os.system('pause')

if __name__ == '__main__':

    #p1
    manejador = ManejadorViajero()
    p = input('Desea ejecutar test  1:si  2:no   :')
    if p =='1':
        test()
    #p2
    archivo = open('csv pasajeros.csv')
    manejador.testViajeros(archivo)
    print('archivo viajero cargado (5 viajeros cargados)')
    num=(input('Ingrese numero de viajero a buscar : '))
    if num.isdigit():
        bol = False
        bol, indice = manejador.buscarViajero(num, bol)
        if (bol == False):
            print('no se encontro el viajero')
        else:
            print('si se encontro el viajero')
            viajero = manejador.obtenerViajero(indice)
            menu = Menu()
            bandera = False
            while not bandera:
                print(
                    "\n------------Menu------------\n1. Consultar cantidad de millas 1\n2. Acumular Millas 2\n3. Canjear millas \n4. Salir")
                op = int(input('Ingrese una opcion: '))
                menu.opcion(op, viajero)
                if op == 4:
                    bandera = True
    else:
        print('Error al ingresar el numero de viajero \n')


