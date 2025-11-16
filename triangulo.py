import time
def parsear_datos(raw_data):
    postes = []
    for line in raw_data.strip().split('\n'):
        if not line.strip():
            continue
        try:
            parts = line.split()
            x = int(parts[0])
            y = int(parts[1])
            if x == -1 and y == -1:
                break
            postes.append((x, y))
        except (ValueError, IndexError):
            print(f"Omitiendo línea mal formada: {line}")
    return postes
def calcular_area_triangulo(p1, p2, p3):
    area = 0.5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    return area
def encontrar_area_maxima(postes):
    n = len(postes)
    if n < 3:
        return 0, None, 0
    area_maxima = 0
    puntos_maximos = (None, None, None)
    combinaciones_totales = (n * (n - 1) * (n - 2)) // 6
    combinaciones_probadas = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                p1 = postes[i]
                p2 = postes[j]
                p3 = postes[k]
                area_actual = calcular_area_triangulo(p1, p2, p3)
                if area_actual > area_maxima:
                    area_maxima = area_actual
                    puntos_maximos = (p1, p2, p3)
                combinaciones_probadas += 1
    return area_maxima, puntos_maximos, combinaciones_probadas
if __name__ == "__main__":
    nombre_archivo = "campo.in"
    try:
        with open(nombre_archivo, 'r') as f:
            datos_del_archivo = f.read()
        print(f"Se esta leyendo el archivo '{nombre_archivo}'")
    except Exception as e:
        print(f"No se encontro el archivo: '{nombre_archivo}'")
        exit()
    postes = parsear_datos(datos_del_archivo)
    if not postes:
        print("No se encontraron postes válidos en el archivo.")
        exit()
    print(f"Se encontraron {len(postes)} postes")
    start_time = time.time()
    area, puntos, num_combinaciones = encontrar_area_maxima(postes)
    end_time = time.time()
    if puntos:
        print("\n"+"¡Encontrado!".center(40))
        print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
        print(f"Se probaron {num_combinaciones} combinaciones de triángulos")
        print("\nEl resultado es:")
        print(f"El área máxima encontrada es: {area}")
        print("Las coordenadas de los postes son:")
        print(f"  Poste 1: {puntos[0]}")
        print(f"  Poste 2: {puntos[1]}")
        print(f"  Poste 3: {puntos[2]}")