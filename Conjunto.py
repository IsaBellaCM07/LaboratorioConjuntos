import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

class Conjunto:
    def __init__(self, conjunto, nombre=""):
        """
        Inicializa el conjunto con los elementos proporcionados y un nombre opcional.
        Ordena los elementos en orden ascendente y elimina duplicados.
        """
        self.conjunto = sorted(set(conjunto))  # Elimina duplicados y ordena los elementos
        self.nombre = nombre

    def __str__(self):
        """
        Devuelve una representación en cadena del conjunto.
        """
        return f"{self.nombre}: {str(self.conjunto)}"

    def union(self, *otros_conjuntos):
        """
        Realiza la unión entre el conjunto actual y uno o más conjuntos adicionales.
        Devuelve un nuevo objeto Conjunto con la unión de todos los conjuntos.
        """
        conjunto_union = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_adicional.conjunto:  # Itera sobre los elementos del conjunto adicional
                if elemento not in conjunto_union:  # Si el elemento no está en el conjunto unión
                    conjunto_union.append(elemento)  # Lo agrega al conjunto unión
        conjunto_union = sorted(set(conjunto_union))  # Elimina duplicados y ordena
        nombres_conjuntos = ", ".join([self.nombre] + [conjunto.nombre for conjunto in otros_conjuntos])
        print(f"Unión de {nombres_conjuntos}: {conjunto_union}")
        return Conjunto(conjunto_union)  # Devuelve un nuevo objeto Conjunto con la unión

    def interseccion(self, *otros_conjuntos):
        """
        Realiza la intersección entre el conjunto actual y uno o más conjuntos adicionales.
        Devuelve un nuevo objeto Conjunto con la intersección de todos los conjuntos.
        """
        conjunto_interseccion = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_interseccion.copy():  # Itera sobre los elementos del conjunto intersección
                if elemento not in conjunto_adicional.conjunto:  # Si el elemento no está en el conjunto adicional
                    conjunto_interseccion.remove(elemento)  # Lo elimina del conjunto intersección
        nombres_conjuntos = ", ".join([self.nombre] + [conjunto.nombre for conjunto in otros_conjuntos])
        print(f"Intersección de {nombres_conjuntos}: {conjunto_interseccion}")
        return Conjunto(conjunto_interseccion)  # Devuelve un nuevo objeto Conjunto con la intersección

    def diferencia(self, *otros_conjuntos):
        """
        Realiza la diferencia entre el conjunto actual y uno o más conjuntos adicionales.
        Devuelve un nuevo objeto Conjunto con la diferencia de todos los conjuntos.
        """
        conjunto_diferencia = self.conjunto.copy()  # Crea una copia del conjunto actual
        for conjunto_adicional in otros_conjuntos:  # Itera sobre los conjuntos adicionales
            for elemento in conjunto_diferencia.copy():  # Itera sobre los elementos del conjunto diferencia
                if elemento in conjunto_adicional.conjunto:  # Si el elemento está en el conjunto adicional
                    conjunto_diferencia.remove(elemento)  # Lo elimina del conjunto diferencia
        nombres_conjuntos = ", ".join([self.nombre] + [conjunto.nombre for conjunto in otros_conjuntos])
        print(f"Diferencia de {nombres_conjuntos}: {conjunto_diferencia}")
        return Conjunto(conjunto_diferencia)  # Devuelve un nuevo objeto Conjunto con la diferencia

    def diferencia_simetrica(self, *otros_conjuntos):
        """
        Realiza la diferencia simétrica entre el conjunto actual y uno o más conjuntos adicionales.
        Un elemento solo permanece si no está en todos los conjuntos.
        Devuelve un nuevo objeto Conjunto con la diferencia simétrica final.
        """
        conjunto_diferencia_simetrica = self.conjunto.copy()  # Crea una copia del conjunto actual
        # Inicializa un diccionario para contar las repeticiones de cada elemento
        contador_repeticiones = {elemento: 1 for elemento in self.conjunto}

        # Itera sobre los conjuntos adicionales
        for conjunto_adicional in otros_conjuntos:
            for elemento in conjunto_adicional.conjunto:  # Itera sobre los elementos del conjunto adicional
                if elemento in conjunto_diferencia_simetrica:  # Si el elemento ya está en el conjunto diferencia_simétrica
                    contador_repeticiones[elemento] += 1  # Incrementa su contador
                else:
                    conjunto_diferencia_simetrica.append(elemento)  # Si no está, lo agrega al conjunto diferencia_simétrica
                    contador_repeticiones[elemento] = 1  # Inicializa su contador en 1

        # Crea un nuevo conjunto para almacenar los elementos que no se repitieron en todos los conjuntos
        conjunto_diferencia_simetrica_final = []
        total_conjuntos = len(otros_conjuntos) + 1  # Calcula el número total de conjuntos

        # Itera sobre los elementos del conjunto diferencia_simétrica
        for elemento in conjunto_diferencia_simetrica:
            if contador_repeticiones[elemento] < total_conjuntos:  # Si el elemento no está en todos los conjuntos
                conjunto_diferencia_simetrica_final.append(elemento)  # Lo agrega al conjunto diferencia_simétrica_final

        conjunto_diferencia_simetrica_final = sorted(conjunto_diferencia_simetrica_final)  # Ordena los elementos
        nombres_conjuntos = ", ".join([self.nombre] + [conjunto.nombre for conjunto in otros_conjuntos])
        print(f"Diferencia simétrica de {nombres_conjuntos}: {conjunto_diferencia_simetrica_final}")
        return Conjunto(conjunto_diferencia_simetrica_final)  # Devuelve un nuevo objeto Conjunto con la diferencia simétrica final

    def es_subconjunto(self, *otros_conjuntos):
        """
        Verifica si el conjunto actual es subconjunto de otros conjuntos adicionales.
        Devuelve una lista de tuplas con el nombre del conjunto adicional y un booleano que indica si el conjunto actual es subconjunto.
        """
        resultados = []
        for conjunto_adicional in otros_conjuntos:
            es_sub = all(elemento in conjunto_adicional.conjunto for elemento in self.conjunto)
            resultados.append((conjunto_adicional.nombre, es_sub))
        return resultados

    def es_superconjunto(self, *otros_conjuntos):
        """
        Verifica si el conjunto actual es superconjunto de otros conjuntos adicionales.
        Devuelve una lista de tuplas con el nombre del conjunto adicional y un booleano que indica si el conjunto actual es superconjunto.
        """
        resultados = []
        for conjunto_adicional in otros_conjuntos:
            es_super = all(elemento in self.conjunto for elemento in conjunto_adicional.conjunto)
            resultados.append((conjunto_adicional.nombre, es_super))
        return resultados

# Solicitar la cantidad de conjuntos
while True:
    num_conjuntos = int(input("¿Cuántos conjuntos desea ingresar? (mínimo 2, máximo 3): "))
    if 2 <= num_conjuntos <= 3:
        break
    print("Número inválido. Intente de nuevo.")

# Solicitar los conjuntos al usuario
conjuntos = []
for i in range(num_conjuntos):
    nombre = chr(65 + i)  # Genera "A", "B", "C", etc.
    num_datos = int(input(f"Conjunto {nombre}: ¿Cuántos datos desea? "))
    conjunto = []
    for j in range(num_datos):
        dato = input(f"Ingrese el dato {j + 1} para el conjunto {nombre}: ")
        while dato in conjunto:  # Validar que el dato no se repita en el mismo conjunto
            print("Dato repetido. Ingrese un dato diferente.")
            dato = input(f"Ingrese el dato {j + 1} para el conjunto {nombre}: ")
        conjunto.append(dato)
    conjuntos.append(Conjunto(conjunto, f"Conjunto {nombre}"))

# Asignar los conjuntos a variables
conjunto_a = conjuntos[0]
conjunto_b = conjuntos[1]
conjunto_c = conjuntos[2] if num_conjuntos == 3 else None

print(f"\n{conjunto_a}")
print(f"{conjunto_b}")
if conjunto_c:
    print(f"{conjunto_c}\n")

# Unión
union = conjunto_a.union(conjunto_b, conjunto_c) if conjunto_c else conjunto_a.union(conjunto_b)

# Intersección
interseccion = conjunto_a.interseccion(conjunto_b, conjunto_c) if conjunto_c else conjunto_a.interseccion(conjunto_b)

# Diferencia
diferencia = conjunto_a.diferencia(conjunto_b, conjunto_c) if conjunto_c else conjunto_a.diferencia(conjunto_b)

# Diferencia Simétrica
diferencia_s = conjunto_a.diferencia_simetrica(conjunto_b)

# Subconjunto
subconjunto_resultados = conjunto_b.es_subconjunto(conjunto_c) if conjunto_c else conjunto_b.es_subconjunto(conjunto_a)
for nombre, es_sub in subconjunto_resultados:
    print(f"{conjunto_b.nombre} es subconjunto de {nombre}: {es_sub}")

# Superconjunto
superconjunto_resultados = conjunto_a.es_superconjunto(conjunto_b)
for nombre, es_super in superconjunto_resultados:
    print(f"{conjunto_a.nombre} es superconjunto de {nombre}: {es_super}")


def crear_diagrama_venn(conjuntos):
    """
    Crea un diagrama de Venn para 2 o 3 conjuntos, mostrando los valores del conjunto, evidenciando
    principalmente la intersección en rojo.
    """

    num_conjuntos = len(conjuntos)
    if num_conjuntos == 2:
        # Para 2 conjuntos
        set_a = set(conjuntos[0].conjunto)
        set_b = set(conjuntos[1].conjunto)
        interseccion = set_a & set_b
        solo_a = set_a - interseccion
        solo_b = set_b - interseccion

        # Crear la representación del diagrama de Venn
        venn = venn2(subsets={'10': len(solo_a), '01': len(solo_b), '11': len(interseccion)},
                     set_labels=(conjuntos[0].nombre, conjuntos[1].nombre),
                     set_colors=('lightblue', 'lightgreen'),
                     alpha=0.7)

        # Resaltar la intersección en rojo
        if venn.get_patch_by_id('11'):
            venn.get_patch_by_id('11').set_color('red')
            venn.get_patch_by_id('11').set_alpha(0.4)

        # Establecer los textos, incluso si las áreas están vacías
        if venn.get_label_by_id('10'):
            venn.get_label_by_id('10').set_text(', '.join(solo_a))
        if venn.get_label_by_id('01'):
            venn.get_label_by_id('01').set_text(', '.join(solo_b))
        if venn.get_label_by_id('11'):
            venn.get_label_by_id('11').set_text(', '.join(interseccion))

        plt.title("Diagrama de Venn de 2 Conjuntos")

    elif num_conjuntos == 3:
        # Para 3 conjuntos
        set_a = set(conjuntos[0].conjunto)
        set_b = set(conjuntos[1].conjunto)
        set_c = set(conjuntos[2].conjunto)
        interseccion_ab = set_a & set_b
        interseccion_ac = set_a & set_c
        interseccion_bc = set_b & set_c
        interseccion_abc = set_a & set_b & set_c
        solo_a = set_a - (interseccion_ab | interseccion_ac | interseccion_abc)
        solo_b = set_b - (interseccion_ab | interseccion_bc | interseccion_abc)
        solo_c = set_c - (interseccion_ac | interseccion_bc | interseccion_abc)

        # Crear la representación del diagrama de Venn
        venn = venn3(subsets={'100': len(solo_a), '010': len(solo_b), '001': len(solo_c),
                              '110': len(interseccion_ab - interseccion_abc),
                              '101': len(interseccion_ac - interseccion_abc),
                              '011': len(interseccion_bc - interseccion_abc),
                              '111': len(interseccion_abc)},
                     set_labels=(conjuntos[0].nombre, conjuntos[1].nombre, conjuntos[2].nombre),
                     set_colors=('lightblue', 'lightgreen', 'lightyellow'),
                     alpha=0.7)

        # Resaltar la intersección de los 3 conjuntos en rojo
        if venn.get_patch_by_id('111'):
            venn.get_patch_by_id('111').set_color('red')
            venn.get_patch_by_id('111').set_alpha(1)

        # Establecer los textos, incluso si las áreas están vacías
        ids = ['100', '010', '001', '110', '101', '011', '111']
        textos = [
            ', '.join(solo_a),
            ', '.join(solo_b),
            ', '.join(solo_c),
            ', '.join(interseccion_ab - interseccion_abc),
            ', '.join(interseccion_ac - interseccion_abc),
            ', '.join(interseccion_bc - interseccion_abc),
            ', '.join(interseccion_abc)
        ]

        for id, texto in zip(ids, textos):
            if venn.get_label_by_id(id):
                venn.get_label_by_id(id).set_text(texto)

        plt.title("Diagrama de Venn de 3 Conjuntos")

    else:
        print("Número de conjuntos inválido. Se necesita 2 o 3 conjuntos.")
        return

    plt.show()

# Crear la lista de objetos Conjunto para usar en la función
conjuntos_venn = [conjunto_a, conjunto_b]
if conjunto_c:
    conjuntos_venn.append(conjunto_c)

crear_diagrama_venn(conjuntos_venn)