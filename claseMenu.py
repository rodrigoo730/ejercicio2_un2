from claseViajeroFrecuente import Viajero
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1, 2:self.opcion2, 3:self.opcion3, 4:self.salir}

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,viajero):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(viajero)

    def salir(self,viaje):
        print('Salir')

    def opcion1(self,viajero):
        print('La cantidad de millas es {}'.format(viajero.cantidadTotalMillas()))

    def opcion2(self,viajero):
        millas=int(input('Ingrese millas a acumular: '))
        viajero.acumularMillas(millas)

    def opcion3(self,viajero):
        millas=int(input('Ingrese cantidad de millas a canjear: '))
        viajero.canjearMillas(millas)
