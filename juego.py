import random
from guerrero import Guerrero
from enemigo import Enemigo
from traje import Traje


class Juego:
    def __init__(self):
        self.rangers = []
        self.enemigos = []

        self.crear_rangers()
        self.crear_enemigos(7)
        self.pelear()
        self.mostrar_estado()

    def crear_rangers(self):
        colores = [
            {"nombre": "ranger 1", "traje": Traje("rojo")},
            {"nombre": "ranger 2", "traje": Traje("verde")},
            {"nombre": "ranger 3", "traje": Traje("azul")},
            {"nombre": "ranger 4", "traje": Traje("amarillo")},
            {"nombre": "ranger 5", "traje": Traje("rosa")},
        ]
        for i in range(len(colores)):
            ranger = Guerrero(i, colores[i]["nombre"], 3, colores[i]["traje"])
            self.rangers.append(ranger)

    def crear_enemigos(self, qty):
        vida = 3
        for i in range(qty):
            self.enemigos.append(Enemigo(i, f"Masilla {i}", vida))

    def pelear(self):
        def areAlive(target):
            for guerrero in target:
                if guerrero.vida > 0:
                    return True

            return False

        def tanda_de_ataques(atacantes, defensores):
            for atacante in [a for a in atacantes if a.vida > 0]:
                defensores_en_pie = [d for d in defensores if d.vida > 0]
                if len(defensores_en_pie) <= 0:
                    return

                defensor = random.choice(defensores_en_pie)
                atacante.atacar(defensor)

        while areAlive(self.rangers) and areAlive(self.enemigos):
            tanda_de_ataques(self.rangers, self.enemigos)
            tanda_de_ataques(self.enemigos, self.rangers)

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
