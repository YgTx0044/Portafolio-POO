from animal import Animal

# Clase hereda de Animal
class Gato(Animal):
  def __init__(self, nombre, edad, vidas):
    super().__init__(nombre, edad)
    self.vidas = vidas

  def hacer_sonido(self):
    print(f"{self.nombre} esta maullando")
    print("Miau 🐈")
