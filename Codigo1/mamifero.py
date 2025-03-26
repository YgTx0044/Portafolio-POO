from animal import Animal

# Clase hereda de Animal
class Mamifero(Animal):
  def __init__(self, nombre, edad, especie="Mamifero"): # Valor por defecto
    super().__init__(nombre, edad)
    self.especie = especie

  def amamantar(self):
    print(f"{self.nombre} esta amamantando")

  def parir(self):
    print(f"{self.nombre} esta pariendo")

  def soy_un(self):
    print(f"Soy un {self.especie}")
