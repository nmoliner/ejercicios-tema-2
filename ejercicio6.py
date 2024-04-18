class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos(arbol):
    if arbol is None:
        return 0
    contador = 1
    for hijo in arbol.hijos:
        contador += contar_nodos(hijo)
    return contador

def contar_hojas(arbol):
    if arbol is None:
        return 0
    if len(arbol.hijos) == 0:
        return 1
    contador = 0
    for hijo in arbol.hijos:
        contador += contar_hojas(hijo)
    return contador

def nodos_hojas(arbol):
    if arbol is None:
        return []
    if len(arbol.hijos) == 0:
        return [arbol.valor]
    hojas = []
    for hijo in arbol.hijos:
        hojas.extend(nodos_hojas(hijo))
    return hojas

def encontrar_padre(arbol, valor_nodo):
    if arbol is None:
        return None
    if arbol.valor == valor_nodo:
        return None
    for hijo in arbol.hijos:
        if hijo.valor == valor_nodo:
            return arbol.valor
        padre = encontrar_padre(hijo, valor_nodo)
        if padre is not None:
            return padre
    return None

def altura_arbol(arbol):
    if arbol is None:
        return 0
    if len(arbol.hijos) == 0:
        return 1
    alturas = []
    for hijo in arbol.hijos:
        alturas.append(altura_arbol(hijo))
    return max(alturas) + 1

# Ejemplo de uso
# Crear el árbol
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

raiz.hijos.append(nodo2)
raiz.hijos.append(nodo3)
nodo2.hijos.append(nodo4)
nodo2.hijos.append(nodo5)
nodo3.hijos.append(nodo6)

# Contar el número de nodos del árbol
num_nodos = contar_nodos(raiz)
print("Número de nodos:", num_nodos)

# Determinar el número de hojas del árbol
num_hojas = contar_hojas(raiz)
print("Número de hojas:", num_hojas)

# Mostrar la información de los nodos hojas
hojas = nodos_hojas(raiz)
print("Nodos hojas:", hojas)

# Determinar el padre de un nodo
valor_nodo = 6
padre = encontrar_padre(raiz, valor_nodo)
if padre is None:
    print("El nodo", valor_nodo, "no tiene padre.")
else:
    print("El padre del nodo", valor_nodo, "es:", padre)

# Determinar la altura del árbol
altura = altura_arbol(raiz)
print("Altura del árbol:", altura)