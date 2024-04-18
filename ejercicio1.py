class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, valor)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.valor = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.valor)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo.valor

    def barrido_preorden(self):
        return self._barrido_preorden_recursivo(self.raiz)

    def _barrido_preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.valor)
            self._barrido_preorden_recursivo(nodo.izquierda)
            self._barrido_preorden_recursivo(nodo.derecha)

    # Implementar barrido inorden, postorden y por nivel de manera similar

    def altura_subarbol_izquierdo(self):
        return self._altura_subarbol(self.raiz.izquierda)

    def altura_subarbol_derecho(self):
        return self._altura_subarbol(self.raiz.derecha)

    def _altura_subarbol(self, nodo):
        if nodo is None:
            return 0
        return 1 + max(self._altura_subarbol(nodo.izquierda), self._altura_subarbol(nodo.derecha))

    def contar_ocurrencias(self, valor):
        return self._contar_ocurrencias_recursivo(self.raiz, valor)

    def _contar_ocurrencias_recursivo(self, nodo, valor):
        if nodo is None:
            return 0
        count = 0
        if nodo.valor == valor:
            count = 1
        return count + self._contar_ocurrencias_recursivo(nodo.izquierda, valor) + self._contar_ocurrencias_recursivo(nodo.derecha, valor)

    def contar_pares_impares(self):
        return self._contar_pares_impares_recursivo(self.raiz)

    def _contar_pares_impares_recursivo(self, nodo):
        if nodo is None:
            return (0, 0)
        pares = 1 if nodo.valor % 2 == 0 else 0
        impares = 1 if nodo.valor % 2 != 0 else 0
        pares_izquierda, impares_izquierda = self._contar_pares_impares_recursivo(nodo.izquierda)
        pares_derecha, impares_derecha = self._contar_pares_impares_recursivo(nodo.derecha)
        return (pares + pares_izquierda + pares_derecha, impares + impares_izquierda + impares_derecha)

# Crear el árbol y cargar 1000 números enteros aleatorios
import random
arbol = ArbolBinarioBusqueda()
for _ in range(1000):
    arbol.insertar(random.randint(1, 10000))

# Ejemplo de uso
print("Barrido preorden:")
arbol.barrido_preorden()

numero_a_buscar = 42
print(f"¿El número {numero_a_buscar} está en el árbol?: {arbol.buscar(numero_a_buscar)}")

# Eliminar tres valores del árbol
for _ in range(3):
    valor_a_eliminar = random.randint(1, 10000)
    print(f"Eliminando el valor {valor_a_eliminar} del árbol...")
    arbol.eliminar(valor_a_eliminar)

print("Altura del subárbol izquierdo:", arbol.altura_subarbol_izquierdo())
print("Altura del subárbol derecho:", arbol.altura_subarbol_derecho())

numero_a_contar = 7
print(f"Número de ocurrencias de {numero_a_contar} en el árbol:", arbol.contar_ocurrencias(numero_a_contar))

pares, impares = arbol.contar_pares_impares()
print("Cantidad de números pares en el árbol:", pares)
print("Cantidad de números impares en el árbol:", impares)
