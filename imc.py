def altura():
    alt = input('\nPor favor introduza a sua altura em cm:\n')
    while True:
        if alt.isdigit():
            break
        else:
            alt = input('Por favor tente novamente:\n')
    return int(alt)


def peso():
    kgs = input('\nPor favor introduza o seu peso em kg (sem casas decimais):\n')
    while True:
        if kgs.isdigit():
            break
        else:
            kgs = input('Por favor tente novamente:\n')
    return int(kgs)


def tabela(indice):
    if indice < 17:
        return 'muito abaixo do peso'
    elif 17 <= indice < 18.5:
        return 'abaixo do peso'
    elif 25 <= indice < 30:
        return 'acima do peso'
    elif 30 <= indice < 35:
        return 'com Obesidade de nível I'
    elif 35 <= indice < 40:
        return 'com Obesidade Severa (de nível II)'
    elif indice >= 40:
        return 'com Obesidade Mórbida (de nível III)'
    else:
        return 'com peso normal'


def peso_ideal(alt):
    minimo = (18.5 * (alt ** 2.5)) / 1.3
    maximo = (24.99 * (alt ** 2.5)) / 1.3
    return round((minimo + maximo) / 2)

print('====================================================')
print('CALCULADORA DE ÍNDICE DE MASSA CORPORAL E PESO IDEAL')
print('====================================================')
nome = input('\nPor favor introduza o seu nome:\n')
m = altura() / 100
kg = peso()
imc = round((1.3 * kg) / (m ** 2.5), 2)
print(f'\n{nome}, o seu IMC é {imc}, você está {tabela(imc)}.')
if 18.5 <= imc < 25:
    print('O seu peso é ideal, mantenha-se assim')
else:
    print(f'O seu peso ideal é {peso_ideal(m)}Kg.\n')
print('====================================================')
print('         Programa por André Barbosa - 2020          ')
print('====================================================')
