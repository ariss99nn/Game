class personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        
        
    def damage(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} de daño. Health: {self.salud}")