class Conjunto:
    def __init__(self, conjunto):
        """
        Inicializa el conjunto con los elementos proporcionados.
        """
        self.conjunto = conjunto

    def __str__(self):
        """
        Devuelve una representación en cadena del conjunto.
        """
        return str(self.conjunto)
    
    def union(self, *otros_conjuntos):
        """
        Realiza la unión entre el conjunto actual y uno o más conjuntos adicionales.
        """
        conjunto_union = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_adicional.conjunto:  # Itera sobre los elementos del conjunto adicional
                if elemento not in conjunto_union:  # Si el elemento no está en el conjunto unión
                    conjunto_union.append(elemento)  # Lo agrega al conjunto unión
        return Conjunto(conjunto_union)  # Devuelve un nuevo objeto Conjunto con la unión
    
    def interseccion(self, *otros_conjuntos):
        """
        Realiza la intersección entre el conjunto actual y uno o más conjuntos adicionales.
        """
        conjunto_interseccion = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_interseccion.copy():  # Itera sobre los elementos del conjunto intersección
                if elemento not in conjunto_adicional.conjunto:  # Si el elemento no está en el conjunto adicional
                    conjunto_interseccion.remove(elemento)  # Lo elimina del conjunto intersección
        return Conjunto(conjunto_interseccion)  # Devuelve un nuevo objeto Conjunto con la intersección

    def diferencia(self, *otros_conjuntos):
        """
        Realiza la diferencia entre el conjunto actual y uno o más conjuntos adicionales.
        """
        conjunto_diferencia = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_diferencia.copy():  # Itera sobre los elementos del conjunto diferencia
                if elemento in conjunto_adicional.conjunto:  # Si el elemento está en el conjunto adicional
                    conjunto_diferencia.remove(elemento)  # Lo elimina del conjunto diferencia
        return Conjunto(conjunto_diferencia)  # Devuelve un nuevo objeto Conjunto con la diferencia


# Ejemplo de uso
conjunto_a = Conjunto(["a", "b", "c"])
conjunto_b = Conjunto(["b", "c"])
conjunto_c = Conjunto(["c", "b", "f"])

print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print(f"Conjunto C: {conjunto_c} \n")

# Unión
union_ab = conjunto_a.union(conjunto_b, conjunto_c)
print(f"Union: {union_ab}")  # Imprime la unión de los conjuntos

# Intersección
interseccion_ab = conjunto_a.interseccion(conjunto_b, conjunto_c)
print(f"Interseccion: {interseccion_ab}")  # Imprime la intersección de los conjuntos

# Diferencia
diferencia_ab = conjunto_a.diferencia(conjunto_b, conjunto_c)
print(f"Diferencia: {diferencia_ab}")  # Imprime la diferencia de los conjuntos
