from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, id, nombre, vida):
        self.nombre = nombre
        self.id = id
        self.vida_maxima = vida
        self.vida = self.vida_maxima

    def atacar(self, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida = max(0, victima.vida - self.poder_ataque)
            # Si el resultado de vida - ataque es mayor que 0 → lo asigna
            # Si el resultado es menor que 0 → asigna 0 (nunca será negativo).
