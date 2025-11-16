import time
import matplotlib.pyplot as plt
def parsear_datos(raw_data):
    postes = []
    for line in raw_data.strip().split('\n'):
        if not line.strip(): continue
        try:
            parts = line.split()
            x, y = int(parts[0]), int(parts[1])
            if x == -1 and y == -1: break
            postes.append((x, y))
        except (ValueError, IndexError):
            continue
    return list(set(postes))
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def obtener_convex_hull(points):
    n = len(points)
    if n <= 2: return points
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def calcular_area_triangulo(p1, p2, p3):
    return 0.5 * abs(p1[0] * (p2[1] - p3[1]) +  p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
def resolver_optimizado(postes):
    hull = obtener_convex_hull(postes)
    h = len(hull)
    print(f"-> Reducción masiva: De {len(postes)} postes totales a solo {h} que están en la envolvente.")
    if h < 3: return 0, None, 0
    area_maxima = 0
    puntos_maximos = (None, None, None)
    combinaciones = 0
    for i in range(h):
        for j in range(i + 1, h):
            for k in range(j + 1, h):
                area = calcular_area_triangulo(hull[i], hull[j], hull[k])
                if area > area_maxima:
                    area_maxima = area
                    puntos_maximos = (hull[i], hull[j], hull[k])
                combinaciones += 1
    return area_maxima, puntos_maximos, combinaciones, hull
def visualizar_optimizado(postes, hull, puntos_max):
    plt.figure(figsize=(10, 10))
    tx, ty = zip(*postes)
    plt.scatter(tx, ty, s=10, color='lightgray', label='Puntos Interiores')
    hull_cycle = hull + [hull[0]] 
    hx, hy = zip(*hull_cycle)
    plt.plot(hx, hy, 'g--', linewidth=1, label='Envolvente Convexa')
    plt.scatter(hx, hy, s=20, color='green')
    if puntos_max:
        p1, p2, p3 = puntos_max
        tri_x = [p1[0], p2[0], p3[0], p1[0]]
        tri_y = [p1[1], p2[1], p3[1], p1[1]]
        plt.plot(tri_x, tri_y, 'r-', linewidth=2.5, label='Triángulo Máx.')
        plt.scatter([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color='red', s=50, zorder=5)
    plt.title('Optimización: Envolvente Convexa + Triángulo Máximo')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 1000); plt.ylim(0, 1000)
    plt.gca().set_aspect('equal')
    plt.savefig("resultado_optimizado.png")
    print("Gráfico guardado como 'resultado_optimizado.png'")
if __name__ == "__main__":
    try:
        with open("campo.in", 'r') as f: data = f.read()
    except:
        print("Error: No se encuentra campo.in"); exit()
    postes = parsear_datos(data)
    start = time.time()
    area, tri_puntos, combs, hull = resolver_optimizado(postes)
    end = time.time()
    print(f"\n---RESULTADO OPTIMIZADO---")
    print(f"Tiempo: {end - start:.6f} seg")
    print(f"Combinaciones calculadas: {combs} (vs {len(postes)**3 // 6} en fuerza bruta)")
    print(f"Área Máxima: {area}")
    print(f"Vértices: {tri_puntos}")
    if tri_puntos:

        visualizar_optimizado(postes, hull, tri_puntos)
