from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, id, nombre, vida):
        self.nombre = nombre
        self.id = id
        self.vida_maxima = vida
        self.vida = self.vida_maxima

    @abstractmethod
    def atacar(self, poder_ataque, victima):
        pass
