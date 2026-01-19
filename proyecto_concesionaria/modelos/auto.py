from modelos.vehiculo import Vehiculo

class Auto(Vehiculo):
    """
    Clase Auto que hereda de Vehiculo.
    Se sobrescribe el método acelerar (polimorfismo)
    """
    def __init__(self, marca, velocidad, puertas):
        super().__init__(marca, velocidad)  # Llamada al constructor de la clase base
        self.puertas = puertas

    # Polimorfismo: método sobrescrito
    def acelerar(self):
        return f"El auto {self.marca} con {self.puertas} puertas acelera suavemente"
