from animal import Animal

# Clase hereda de Animal
class Perro(Animal):
  def __init__(self, nombre, edad, raza):
    super().__init__(nombre, edad)
    self.raza = raza

  def hacer_sonido(self):
    print(f"{self.nombre} esta ladrando")
    print("Guau 🐕")
