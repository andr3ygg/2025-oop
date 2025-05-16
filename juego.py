import random


class Traje:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"color: {self.color}"


# Composition: Los attributes del Guerrero son other object
class Guerrero:
    def __init__(self, color, id, vida):
        self.color = color
        self.id = id
        self.vida_maxima = vida
        self.vida = self.vida_maxima

    """
    def herido(self, poder_ataque):
        # Es herido
        self.vida -= poder_ataque

        if self.vida <= 0:
            print(f"El guerrero {self.color} ha muerto")
        else:
            print(f"Vidas restantes del guerrero {self.color}: {self.vida}")

    """

    def atacar(self, poder_ataque, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida -= poder_ataque
            print(f"Ranger {self.color} ataca a enemigo {victima.nombre}")

    def descansar(self):
        vida_anterior = self.vida  # Tomo el antiguo valor
        if self.vida > 0 and self.vida < self.vida_maxima:  # Vida maxima = 3
            self.vida = self.vida_maxima  # Da nuevo valor
            print("--------")
            print(f"El ranger {self.id} esta descansado")
            print(
                f"Soy el Ranger {self.id}. Tenia {vida_anterior} vidas, y ahora tengo {self.vida}"
            )
            # print(f" * Al  {self.color} aun le quedan {self.vida} vidas")


class Enemigo:
    def __init__(self, id, vida):
        self.nombres = ["Enemigo 0", "Enemigo 1", "Enemigo 2", "Enemigo 3", "Enemigo 4"]
        self.id = id
        self.vida_maxima = vida
        self.vida = self.vida_maxima
        self.nombre = self.nombres[self.id]

    """
    def herido(self, poder_ataque):
        # Es herido
        self.vida -= poder_ataque

        if self.vida <= 0:
            print(f"El guerrero {self.color} ha muerto")
        else:
            print(f"Vidas restantes del guerrero {self.color}: {self.vida}")

    """

    def atacar(self, poder_ataque, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida -= poder_ataque
            print(f"Enemigo {self.id} ataca a Ranger {victima.color}")


class Juego:
    def __init__(self):
        self.rangers = []
        self.enemigos = []

        self.crear_rangers()
        self.crear_enemigos()
        # self.presentar()
        self.pelear()

        # self.descansar()

    def crear_rangers(self):
        colores = [
            Traje("rojo"),
            Traje("verde"),
            Traje("azul"),
            Traje("amarillo"),
            Traje("rosa"),
        ]

        for i in range(5):
            color = colores.pop(0)
            vida = 3
            self.rangers.append(Guerrero(color, i, vida))
            # COLOR, ID, VIDA

        return self.rangers

    def crear_enemigos(self):
        vida = 3
        # for i in range(len(self.rangers)):
        for i in range(5):
            self.enemigos.append(Enemigo(i, vida))

        return self.enemigos

    def pelear(self):
        numero_partidas = 1
        for _ in range(numero_partidas):

            for ranger in self.rangers:
                """
                #ranger_que_ataca = self.rangers[ranger]
                #ranger_que_ataca = self.rangers[random.randint(0, len(self.rangers) - 1)]
                #ranger_atacado = self.enemigos[random.randint(1, len(self.enemigos) - 1) ]
                #ranger_atacado = self.rangers[random.randint(0, len(self.rangers) - 1) ]
                """
                # Si el ranger està vivo:
                if ranger.vida > 0:
                    # Elige un enemigo al azar
                    enemigo_objetivo = random.choice(self.enemigos)

                    # Si el enemigo está vivo:
                    if enemigo_objetivo.vida > 0:
                        ranger.atacar(1, enemigo_objetivo)

            for enemigo in self.enemigos:
                """
                #enemigo_que_ataca = self.enemigos[random.randint(0, len(self.enemigos) - 1)]
                #enemigo_atacado = self.rangers[random.randint(1, len(self.rangers) - 1) ]
                #enemigo_atacado = self.enemigos[random.randint(0, len(self.enemigos) - 1) ]
                """
                if enemigo.vida > 0:
                    ranger_objetivo = random.choice(self.rangers)

                    if ranger_objetivo.vida > 0:
                        enemigo.atacar(1, ranger_objetivo)

            """
            #ranger_que_ataca.atacar(1, enemigo_atacado)
            #enemigo_que_ataca.atacar(1, ranger_atacado)
            """
        print("Muertos")
        for ranger in self.rangers:
            if ranger.vida <= 0:
                print(f"El ranger {ranger.color} ha muerto")

        for enemigo in self.enemigos:
            if enemigo.vida <= 0:
                print(f"El enemigo {enemigo.id} ha muerto")

        # Mostrar Estado Después de fight
        print()
        print()
        print("ESTADO DE LOS RANGERS DESPUES DE LA PELEA")
        for ranger in self.rangers:
            print(f"Ranger {ranger.color} con {ranger.vida} de vida")

        print("ESTADO DE LOS ENEMIGOS DESPUES DE LA PELEA")
        for enemigo in self.enemigos:
            print(f"{enemigo.nombre} con {enemigo.vida} de vida")

        # return self.rangers

    """
    def descansar(self):
        for ranger in self.rangers:
            ranger.descansar()
    """


if __name__ == "__main__":
    Juego()
