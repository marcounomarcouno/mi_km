print("""Hola. Bienvenido al conversor de millas - kilómetros. 
Para comenzar elige una opción: """)

opcion = int(input("""
1. Quiero convertir millas a kilómetros
2. Quiero convertir kilómetros a millas
> """))


if opcion == 1:
    millas = int(input("¿Cuántas millas quieres convertir a kilómetros: "))
    mi_km = (millas * 1.609344)
    mi_km = round(mi_km, 2)
    print(str(millas) + " millas equivalen a " + str(mi_km) + " kilómetros") 
elif opcion == 2:
    kilometros = int(input("¿Cuántos kilómetros quieres convertir a millas: "))
    km_mi = kilometros / 1.609344
    km_mi = round(km_mi, 2)
    print(str(kilometros) + " kilómetros equivalen a " + str(km_mi) + " millas") 
else:
    print("Elige una opción válida")