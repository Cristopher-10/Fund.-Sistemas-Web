#oredenamiento de números ingresados por el usuario con un rango de 6 datos
awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))
