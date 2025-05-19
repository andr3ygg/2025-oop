from abc import ABC, abstractmethod
import random


class Persona(ABC):
    def __init__(self, id, nombre, vida):
        self.nombre = nombre
        self.id = id
        self.vida_maxima = vida
        self.vida = self.vida_maxima

    @abstractmethod
    def atacar(self, poder_ataque, victima):
        pass


class Traje:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"color {self.color}"


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


class Enemigo(Persona):
    def __init__(self, id, nombre, vida):
        super().__init__(id, nombre, vida)

    def atacar(self, poder_ataque, victima):
        if victima.vida > 0 and victima.vida <= victima.vida_maxima:
            victima.vida = max(0, victima.vida - poder_ataque)


class Juego:
    def __init__(self):
        self.rangers = []
        self.enemigos = []

        self.crear_rangers()
        self.crear_enemigos()
        self.pelear()
        self.mostrar_estado()

    def crear_rangers(self):
        colores = [
            Traje("rojo"),
            Traje("verde"),
            Traje("azul"),
            Traje("amarillo"),
            Traje("rosa"),
        ]
        nombres = ["ranger 1", "ranger 2", "ranger 3", "ranger 4", "ranger 5"]
        for i in range(5):
            color = colores.pop(0)
            nombre = nombres.pop(0)
            vida = 3
            self.rangers.append(Guerrero(i, nombre, vida, color))
        return self.rangers

    def crear_enemigos(self):
        nombres = ["Enemigo 0", "Enemigo 1", "Enemigo 2", "Enemigo 3", "Enemigo 4"]
        vida = 3
        for i in range(5):
            nombre = nombres.pop(0)
            self.enemigos.append(Enemigo(i, nombre, vida))
        return self.enemigos

    def pelear(self):
        numero_partidas = 10
        for _ in range(numero_partidas):

            for ranger in self.rangers:
                if ranger.vida > 0:
                    # Elige un enemigo al azar
                    enemigo_objetivo = random.choice(self.enemigos)

                    # Si el enemigo está vivo:
                    if enemigo_objetivo.vida > 0:
                        ranger.atacar(1, enemigo_objetivo)

            for enemigo in self.enemigos:

                if enemigo.vida > 0:
                    ranger_objetivo = random.choice(self.rangers)

                    if ranger_objetivo.vida > 0:
                        enemigo.atacar(1, ranger_objetivo)

    def mostrar_estado(self):
        print("Muertos")
        for ranger in self.rangers:
            if ranger.vida <= 0:
                print(f"El ranger {ranger.traje} ha muerto")

        for enemigo in self.enemigos:
            if enemigo.vida <= 0:
                print(f"El enemigo {enemigo.id} ha muerto")

        # Mostrar Estado Después de fight
        print()
        print("ESTADO DE LOS RANGERS DESPUES DE LA PELEA")
        for ranger in self.rangers:
            print(f"Ranger {ranger.traje} con {ranger.vida} de vida")

        print("ESTADO DE LOS ENEMIGOS DESPUES DE LA PELEA")
        for enemigo in self.enemigos:
            print(f"{enemigo.nombre} con {enemigo.vida} de vida")


if __name__ == "__main__":
    Juego()
