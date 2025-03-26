from animal import Animal

# Clase hereda de animal
class Ave(Animal):
  def __init__(self, nombre, edad):
    super().__init__(nombre, edad)
