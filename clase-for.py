#Realizar un ciclo que pinte la siguiente figura:
#    *
#   ***
#  *****
# *******

espacios = 4
asteriscos = 1

str_espacios = ''
str_asteriscos = ''

#Abstraida

while espacios >= 0:
    print(' '*espacios + '*'*asteriscos)
    espacios -= 1
    asteriscos += 2
    pass

#Extensa

while espacios >= 0:
    for i in range(espacios):
        str_espacios=str_espacios + ' '
    for i in range(asteriscos):
        str_asteriscos+='*'
    print(str_espacios + str_asteriscos)
    str_espacios = ''
    str_asteriscos = ''
    espacios -= 1
    asteriscos += 2