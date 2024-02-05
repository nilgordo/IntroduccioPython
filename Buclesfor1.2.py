# Fes un programa que pregunti un número i et tregui la seva taula de multiplicar.
num = int(input("Introdueix un número: "))
for i in range(1,11):
    resultat = num*i
    print(num,"multiplicat per ",i, "és igual a ",resultat)
