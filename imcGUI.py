import PySimpleGUI as sg
sg.theme('Default1')


def altura():
    alt_layout = [
        [sg.Text('Por favor introduza a sua altura em cm:', key='alt_mensagem')],
        [sg.Text('Altura', size=(15, 1)), sg.InputText()],
        [sg.Submit('Submeter'), sg.Cancel('Cancelar')]
    ]

    alt_window = sg.Window('CALCULADORA DE IMC E PESO IDEAL', alt_layout)
    while True:
        alt_event, alt_values = alt_window.read()
        if alt_event == 'Submeter':
            alt = alt_values[0]
        else:
            return alt_event
        if alt.isdigit():
            break
        else:
            alt_window['alt_mensagem'].update('Por favor tente novamente:')
    alt_window.close()
    return int(alt)


def peso():
    kgs_layout = [
        [sg.Text('Por favor introduza o seu peso em kg (sem casas decimais):', key='kgs_mensagem')],
        [sg.Text('Peso', size=(15, 1)), sg.InputText()],
        [sg.Submit('Submeter'), sg.Cancel('Cancelar')]
    ]

    kgs_window = sg.Window('CALCULADORA DE IMC E PESO IDEAL', kgs_layout)
    while True:
        kgs_event, kgs_values = kgs_window.read()
        if kgs_event == 'Submeter':
            kgs = kgs_values[0]
        else:
            return kgs_event
        if kgs.isdigit():
            break
        else:
            kgs_window['kgs_mensagem'].update('Por favor tente novamente:')
    kgs_window.close()
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


layout1 = [
    [sg.Text('Calculadora de Índice de Massa Corporal e peso ideal.')],
    [sg.Text('versão 0.4')],
    [sg.Submit('Começar')]
]

window1 = sg.Window('CALCULADORA DE IMC E PESO IDEAL', layout1)
event1 = window1.read()
window1.close()


while True:
    layout = [
        [sg.Text('Qual é o seu nome?'), ],
        [sg.Text('Nome', size=(15, 1)), sg.InputText()],
        [sg.Submit('Submeter'), sg.Cancel('Cancelar')]
    ]

    window = sg.Window('CALCULADORA DE IMC E PESO IDEAL', layout)
    event, values = window.read()
    window.close()
    if event == 'Submeter':
        nome = values[0]
    else:
        break

    m = altura()
    if m == 'Cancelar':
        break
    else:
        m = m / 100

    kg = peso()
    if kg == 'Cancelar':
        break
    imc = round((1.3 * kg) / (m ** 2.5), 2)
    if 18.5 <= imc < 25:
        res_mensagem = 'O seu peso é ideal, mantenha-se assim'
    else:
        res_mensagem = f'O seu peso ideal é {peso_ideal(m)}Kg.'

    res_layout = [
        [sg.Text(f'{nome}, o seu IMC é {imc}, você está {tabela(imc)}.')],
        [sg.Text(res_mensagem)],
        [sg.Submit('OK')]
    ]

    res_window = sg.Window('CALCULADORA DE IMC E PESO IDEAL', res_layout)
    res_event = res_window.read()
    res_window.close()
    break
end_layout = [
    [sg.Text('Obrigado por usar este programa.')],
    [sg.Text('André Barbosa - 2020')],
    [sg.Submit('Fechar')]
]

end_window = sg.Window('CALCULADORA DE IMC E PESO IDEAL', end_layout)
end_event = end_window.read()
end_window.close()
