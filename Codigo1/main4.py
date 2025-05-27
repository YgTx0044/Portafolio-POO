# Importamos las clases Animal, Perro, Gato y Ave desde el módulo animal2
from animal2 import Animal, Perro, Gato, Ave

# Definimos la función principal del programa


def main():
    # Creamos una instancia de la clase Perro
    churro = Perro()
    # Llamamos al método comer del objeto churro, pasando un alimento como argumento
    churro.comer("🍕")
    # Llamamos al método dormir del objeto churro
    churro.dormir()
    # Imprimimos el tipo de objeto que es churro
    print(type(churro))

    # Creamos una instancia de la clase Gato
    michi = Gato()
    # Llamamos al método comer del objeto michi, pasando un alimento como argumento
    michi.comer("🌮")
    # Llamamos al método dormir del objeto michi
    michi.dormir()
    # Imprimimos el tipo de objeto que es michi
    print(type(michi))

    # Creamos una instancia de la clase Ave
    kyalo = Ave()
    # Llamamos al método comer del objeto kyalo, pasando un alimento como argumento
    kyalo.comer("🐥")


if __name__ == "__main__":
    main()
