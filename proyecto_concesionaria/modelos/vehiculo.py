class Vehiculo:
    """
    Clase base Vehiculo.
    Se aplica encapsulación en el atributo _velocidad (protegido)
    """
    def __init__(self, marca, velocidad):
        self.marca = marca
        self._velocidad = velocidad  # Encapsulado: no se accede directamente desde fuera

    # Método getter
    def get_velocidad(self):
        return self._velocidad

    # Método setter
    def set_velocidad(self, nueva_velocidad):
        if nueva_velocidad >= 0:
            self._velocidad = nueva_velocidad
        else:
            print("La velocidad no puede ser negativa")

    # Método general
    def acelerar(self):
        return f"El vehículo {self.marca} acelera"
