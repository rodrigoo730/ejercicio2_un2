import csv
from claseViajeroFrecuente import Viajero

class ManejadorViajero:
    __listViajeros=[]

    def __init__(self):
        self.__listViajeros=[]
    def testViajeros(self,archi):
        reader = csv.reader(archi,delimiter=';')
        for fila in reader:
            print('')
            if not fila[0].isdigit():
                print('numero de viajero no valido, viajero no cargado')
            elif not fila[1].isdigit():
                print('DNI no valido, viajero no cargado\n')
            elif not fila[2].isalpha():
                print('nombre no valido, viajero no cargado\n')
            elif not fila[3].isalpha():
                print('apellido no valido, viajero no cargado\n')
            elif not fila[4].isdigit():
                print('millas no validas, viajero no cargado\n')
            else:
                viajero = Viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listViajeros.append(viajero)
                #print('viajero cargado')

    def mostrarViajeros(self):
        for i in range(len(self.__listViajeros)):
            viajero = self.__listViajeros[i]
            print('viajero: numero:{} DNI:{}  nombre:{} apellido:{}  millas:{}'.format(viajero.obtenerNumeroViajero(),viajero.getDNI(),viajero.getNombre(),viajero.getApellido(),viajero.cantidadTotalMillas()))


    def buscarViajero(self, nume, bool):
        i=0
        while(i < len(self.__listViajeros)) and (bool==False):
            if (self.__listViajeros[i].obtenerNumeroViajero() == nume):
                bool=True
            else:i+=1
        return bool, i
    def obtenerViajero(self,ind):
        return self.__listViajeros[ind]





