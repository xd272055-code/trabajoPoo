from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def obtener_marca(self):
        return self.__marca
    
    def obtener_modelo(self):
        return self.__modelo

    @abstractmethod
    def arrancar(self):
        pass

    def __str__(self):
        return f"{self.__marca} {self.__modelo}"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def arrancar(self):
        return "El coche está encendiendo su motor V8... ¡Brum brum!"


class Moto(Vehiculo):
    def arrancar(self):
        return "La moto está encendiendo... ¡Mec mec rapidísimo!"


def arrancar_flota(lista_de_vehiculos):
    print("--- Probando el Polimorfismo ---")
    for vehiculo in lista_de_vehiculos:
        print(f"El {vehiculo.obtener_marca()} dice: {vehiculo.arrancar()}")


if __name__ == "__main__":
    mi_coche = Coche("Toyota", "Corolla", 4)
    mi_moto = Moto("Honda", "CBR500")

    print("--- Probando Encapsulamiento ---")
    print(f"La marca del coche es: {mi_coche.obtener_marca()}\n")

    mi_flota = [mi_coche, mi_moto]

    arrancar_flota(mi_flota)
