moneda = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
veces = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = len(moneda)

monto = float(input("Ingrese el monto a pagar: "))

for i in range(n):
    if abs(monto - moneda[i]) < 0.000005:
        veces[i] = 1
        monto = 0
    else:
        veces[i] = int(monto // moneda[i])
        monto = monto - (veces[i] * moneda[i])
        if abs(monto - moneda[i]) < 0.000005:
            veces[i] = veces[i] + 1
            monto = 0

print("\nLista de cantidades por denominacion:")
print(veces)

print("\nRespuesta:")
for i in range(n):
    if veces[i] > 0:
        print(f"{veces[i]} de S/{moneda[i]}")