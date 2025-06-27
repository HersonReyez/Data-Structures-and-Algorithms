# Programacion Orientada a Objetos #
class Personaje:
    # Constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Atributos
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa 
        self.vida = vida

    # Metodos
    def atributos(self):
        #Imprime Atributos
        print(self.nombre, ":")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, "ha realizado", damage, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
        

class Guerrero(Personaje):
    #Clase Padre Personaje
    #Clase hijo Guerrero

    #Sobre escribir metodos
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)

    def damage(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
    # Nuevos Metodos
    def cambiar_arma(self):
        opcion = int(input("Eligue un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero incorrecto")

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro:", self.libro)

    def damage(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa


# Funcion Combate #
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("Turno", turno)
        print(">>> Accion de ", jugador_1.nombre, ":") 
        jugador_1.atacar(jugador_2)
        print(">>> Accion de ", jugador_2.nombre, ":") 
        jugador_2.atacar(jugador_1)
        print()
    
    if jugador_1.esta_vivo():
        print("Ha ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("Ha ganado", jugador_2.nombre)
    else:
        print("Empate")

## Código##
goku = Personaje("Goku", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 10, 4, 100, 4)
vanessa = Mago("Vanessa", 5, 15, 4, 100, 3)

# Simulacion combate
combate(guts, vanessa)