# Fes la funció factorial utilitzant un bucle for.

factorial = int(input("Introdueix un número: "))
resultat = 1
for i in range(1,factorial+1):
    resultat = resultat*i
    print(resultat)
