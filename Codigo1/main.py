# Importacion de las clases
from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago
from ornitorrinco import Ornitorrinco

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
  print("Vida(s) restantes:", gato.vidas)
  print("Atropellado" if not gato.sobrevive() else "VIVE")
  print("Vida(s) restantes:", gato.vidas)
  print("Intoxicado" if not gato.sobrevive() else "VIVE")
  print("Vida(s) restantes:", gato.vidas)
  print("Electrocutado" if not gato.sobrevive() else "VIVE")
  print("Vida(s) restantes:", gato.vidas)
  print("-----------------------------------------")

  ave = Ave("KP", 1)
  ave.hacer_sonido()
  print("-----------------------------------------")

  dracula = Murcielago("Dracula", 100, "Vampiro")
  dracula.hacer_sonido()
  dracula.soy_un()
  print("-----------------------------------------")

  perry = Ornitorrinco("Perry", 5)
  perry.hacer_sonido()
  print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos")
  for i in range(3):
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevos")

  print("-----------------------------------------")

if __name__ == "__main__":
  main()
