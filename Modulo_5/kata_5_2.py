# Almacenar las entradas del usuario
planeta1 = input('Introduzca la distancia del sol para el primer planeta en KM:   ')
planeta2 = input('Introduzca la distancia desde el sol para el segundo planeta en KM:   ')

planeta1 = int(planeta1)
planeta2 = int(planeta2)

dist_km = planeta2 - planeta1
print(dist_km)

dist_mi = dist_km * 0.621
print(abs(dist_mi))