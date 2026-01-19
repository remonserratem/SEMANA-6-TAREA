from modelos.vehiculo import Vehiculo
from modelos.auto import Auto

class GestorVehiculos:
    """
    Clase que gestiona los vehículos en la concesionaria
    """
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for v in self.vehiculos:
            print(f"Marca: {v.marca}, Velocidad: {v.get_velocidad()} km/h")
            print(v.acelerar())
            print("-" * 30)
