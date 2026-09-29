cajas_base = [
    ["A", 4.0, 10.0],
    ["B", 3.0, 4.0],
    ["C", 3.0, 7.0],
    ["D", 2.0, 5.0],
    ["E", 1.0, 3.0],
    ["F", 2.0, 3.0],
    ["G", 1.8, 2.0],
    ["H", 3.0, 3.0]
]

cajas = []
for elemento in cajas_base:
    nombre = elemento[0]
    soles = elemento[1]
    kg = elemento[2]
    ratio = soles / kg
    cajas.append([nombre, soles, kg, ratio])

cantidad = len(cajas)
for pasada in range(cantidad):
    for actual in range(0, cantidad - pasada - 1):
        if cajas[actual][3] < cajas[actual + 1][3]:
            cajas[actual], cajas[actual + 1] = cajas[actual + 1], cajas[actual]

print("--- TABLA ORDENADA (C | S/ | Kg | S/ / Kg) ---")
for fila in cajas:
    print(f"Caja {fila[0]} | S/ {fila[1]} | {fila[2]} Kg | Ratio: {round(fila[3], 3)}")

m = float(input("\nIngrese el peso maximo m que puede llevar la mochila: "))

peso_total = 0.0
soles_totales = 0.0
seleccionadas = []

for pos in range(cantidad):
    if m == 0:
        break
        
    nombre = cajas[pos][0]
    soles = cajas[pos][1]
    kg = cajas[pos][2]
    ratio = cajas[pos][3]

    if kg <= m:
        kg_cargar = kg
        pago = soles
        m = m - kg
    else:
        kg_cargar = m
        pago = kg_cargar * ratio
        m = 0

    peso_total = peso_total + kg_cargar
    soles_totales = soles_totales + pago
    seleccionadas.append([nombre, kg_cargar, pago])

print("\n--- CAJAS SELECCIONADAS ---")
for item in seleccionadas:
    print(f"Caja: {item[0]} | Kg a cargar: {round(item[1], 2)} Kg | Me pagan: S/ {round(item[2], 2)}")

print(f"\nPeso total cargado: {round(peso_total, 2)} Kg")
print(f"Soles totales obtenidos: S/ {round(soles_totales, 2)}")