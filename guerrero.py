from personas import Persona
from traje import Traje


class Guerrero(Persona):
    def __init__(self, id, nombre, vida, color):
        super().__init__(id, nombre, vida)
        self.traje = color

    def atacar(self, poder_ataque, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida = max(0, victima.vida - poder_ataque)
            # Si el resultado de vida - ataque es mayor que 0 → lo asigna
            # Si el resultado es menor que 0 → asigna 0 (nunca será negativo).

    """
    def descansar(self):
        vida_anterior = self.vida  # Tomo el antiguo valor
        if self.vida > 0 and self.vida < self.vida_maxima:  # Vida maxima = 3
            self.vida = self.vida_maxima  # Da nuevo valor
            print("--------")
            print(f"El ranger {self.id} esta descansado")
            print(
                f"Soy el Ranger {self.id}. Tenia {vida_anterior} vidas, y ahora tengo {self.vida}"
            )
    """
