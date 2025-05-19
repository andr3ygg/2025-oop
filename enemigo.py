from personas import Persona


class Enemigo(Persona):
    def __init__(self, id, nombre, vida):
        super().__init__(id, nombre, vida)

    def atacar(self, poder_ataque, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida = max(0, victima.vida - poder_ataque)