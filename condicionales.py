#pedimos un valor para n desde consola
n = int(input("Ingresa un número"))
#n es truthy
a = 0
# a es falsy
x= None
#x es falsy

mi_cadena = ''


if n:
    print(f"Este es el valor de n {n}")

if not a:
    print("variable a no existe o es cero {a}".format(a = a))
if x:
    print('Variable x existe y es truthy')
else:
    print('x no existe o es nula y es falsy')

if not mi_cadena:
    print("MI cadena es vacía : {string}".format(string = mi_cadena))
else:
    print(f'Mi cadena es truthy : {mi_cadena}')
