#Programa que demana un pes en kg a l'usuari i retorna el mateix pes convertit en lliures.

pes = input("Quin es el teu pes actual? ")

kg_a_lliures = 2.20462262

pes_en_lliures = float(pes) * kg_a_lliures

print("El teu pes en lliures és: ", pes_en_lliures)
