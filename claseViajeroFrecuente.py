class Viajero:
    __numViajero=''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasAcum = 0

    def __init__(self,num='',dn='',nom='',ape='',mill=int):
        self.__numViajero=num
        self.__dni=dn
        self.__nombre=nom
        self.__apellido=ape
        self.__millasAcum=mill
    def cantidadTotalMillas(self):
        return self.__millasAcum
    def acumularMillas(self,millas):
        self.__millasAcum= int(self.__millasAcum)+millas
        print('millas total acumuladas {}'.format(self.__millasAcum))

    def canjearMillas(self,millas):
        if(int(self.__millasAcum)>=millas):
            self.__millasAcum=int(self.__millasAcum)-millas
            print('millas restantes {}'.format(self.__millasAcum))
        else:print('Error en la operacion')
    def obtenerNumeroViajero(self):
        return self.__numViajero
    def getDNI(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
