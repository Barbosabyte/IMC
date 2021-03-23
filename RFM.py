def altura():
    alt = input('\nPor favor introduza a sua altura em cm:\n')
    while True:
        if alt.isdigit():
            break
        else:
            alt = input('Por favor tente novamente:\n')
    return int(alt)


def cintura():
    circ = input('\nPor favor introduza a medida da sua cintura em cm:\n')
    while True:
        if circ.isdigit():
            break
        else:
            circ = input('Por favor tente novamente:\n')
    return int(circ)


def tabela(s, m, c):
    if s == 'f':
        rfm = 64 - (20 * m / c)
        if rfm > 33.9:
            return "você precisar reduzir a sua massa gorda"
        else:
            return 'você está bem'
    else:
        rfm = 76 - (20 * m / c)
        if rfm > 22.8:
            return "você precisar reduzir a sua massa gorda"
        else:
            return 'você está bem'

print('====================================================')
print('        CALCULADORA DE MASSA GORDA RELATIVA         ')
print('====================================================')
nome = input('\nPor favor introduza o seu nome:\n')
sexo = input('\nPor favor introduza o seu género (m/f):\n')
sexos = ['m', 'f']
while sexo not in sexos:
    sexo = input('\nPor favor introduza o seu género (m/f):\n')
metros = altura()
cinta = cintura()
print(f'\n{nome}, {tabela(sexo, metros, cinta)}.')
print('====================================================')
print('         Programa por André Barbosa - 2020          ')
print('====================================================')
