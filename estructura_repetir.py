
iteraciones = int(input('Ingresa el numero de iteraciones: '))

acumulador = 0

while True:
    acumulador += 1
    print(f'valor de acumulador: {acumulador}')
    if acumulador % 2==0:
        print('El acumulador es par')
        continue
    print(f'Iteracion: {acumulador}')
    if acumulador >= iteraciones:
        print('El acumulador es menor o igual que las iteraciones')
        break