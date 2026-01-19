from modelos.vehiculo import Vehiculo
from modelos.auto import Auto
from servicios.gestor_vehiculos import GestorVehiculos

def main():
    # Crear instancias
    v1 = Vehiculo("Toyota", 120)
    a1 = Auto("Honda", 150, 4)

    # Crear gestor
    gestor = GestorVehiculos()
    gestor.agregar_vehiculo(v1)
    gestor.agregar_vehiculo(a1)

    # Mostrar vehículos
    gestor.mostrar_vehiculos()

    # Probar encapsulación
    print("Velocidad actual de Honda:", a1.get_velocidad())
    a1.set_velocidad(180)
    print("Velocidad modificada de Honda:", a1.get_velocidad())

if __name__ == "__main__":
    main()
