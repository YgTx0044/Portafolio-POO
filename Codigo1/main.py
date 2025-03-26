# Importacion de las clases
from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago

# Cuerpo principal (Main)
def main():
  leon = Animal("Lion", 5)
  leon.hacer_sonido()
  print("-----------------------------------------") # Print eunicamente estetico

  perro = Perro("Churro", 3, "Salchicha")
  perro.hacer_sonido()
  print("-----------------------------------------")

  gato = Gato("Michi", 2, 7)
  gato.hacer_sonido()
  print("-----------------------------------------")

  ave = Ave("KP", 1)
  ave.hacer_sonido()
  print("-----------------------------------------")

  dracula = Murcielago("Dracula", 100, "Vampiro")
  dracula.hacer_sonido()
  dracula.soy_un()
  print("-----------------------------------------")

if __name__ == "__main__":
  main()
