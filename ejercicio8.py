class NodoDecision:
    def __init__(self, pregunta):
        self.pregunta = pregunta
        self.si = None
        self.no = None

class NodoSuperheroe:
    def __init__(self, nombre):
        self.nombre = nombre

def construir_arbol_decision():
    # Crear nodos hoja (superhéroes)
    guardianes_de_la_galaxia = NodoSuperheroe("Guardianes de la Galaxia")
    ant_man = NodoSuperheroe("Ant-Man")
    hulk = NodoSuperheroe("Hulk")
    capitan_america = NodoSuperheroe("Capitán América")
    capitana_marvel = NodoSuperheroe("Capitana Marvel")
    spider_man = NodoSuperheroe("Spider-Man")
    black_widow = NodoSuperheroe("Black Widow")
    iron_man = NodoSuperheroe("Iron Man")
    doctor_strange = NodoSuperheroe("Doctor Strange")
    thor = NodoSuperheroe("Thor")

    # Crear nodos de decisión (preguntas)
    pregunta_1 = NodoDecision("¿La misión es intergaláctica?")
    pregunta_2 = NodoDecision("¿La misión requiere infiltrarse sin ser detectado?")
    pregunta_3 = NodoDecision("¿La misión requiere destrucción masiva?")
    pregunta_4 = NodoDecision("¿La misión es de defensa?")
    pregunta_5 = NodoDecision("¿La misión requiere viajar por distintas galaxias?")
    pregunta_6 = NodoDecision("¿La misión requiere habilidad y agilidad?")
    pregunta_7 = NodoDecision("¿La misión requiere infiltrarse con personas del lugar?")
    pregunta_8 = NodoDecision("¿La misión requiere planificación y tecnología avanzada?")
    pregunta_9 = NodoDecision("¿La misión requiere moverse rápidamente y tomar decisiones lógicas?")

    # Construir árbol de decisión
    pregunta_1.si = guardianes_de_la_galaxia
    pregunta_1.no = pregunta_2
    pregunta_2.si = ant_man
    pregunta_2.no = pregunta_3
    pregunta_3.si = hulk
    pregunta_3.no = pregunta_4
    pregunta_4.si = capitan_america
    pregunta_4.no = pregunta_5
    pregunta_5.si = capitana_marvel
    pregunta_5.no = pregunta_6
    pregunta_6.si = spider_man
    pregunta_6.no = pregunta_7
    pregunta_7.si = black_widow
    pregunta_7.no = pregunta_8
    pregunta_8.si = iron_man
    pregunta_8.no = pregunta_9
    pregunta_9.si = doctor_strange
    pregunta_9.no = thor

    # Retornar nodo raíz del árbol
    return pregunta_1

def superheroe_para_mision(arbol_decision, respuesta):
    nodo_actual = arbol_decision
    while isinstance(nodo_actual, NodoDecision):
        if respuesta == 'si':
            nodo_actual = nodo_actual.si
        else:
            nodo_actual = nodo_actual.no
    return nodo_actual.nombre

# Ejemplo de uso
arbol_decision = construir_arbol_decision()
respuesta = input("¿La misión es intergaláctica? (si/no): ").lower()
superheroe_asignado = superheroe_para_mision(arbol_decision, respuesta)
print("Superhéroe asignado:", superheroe_asignado)
