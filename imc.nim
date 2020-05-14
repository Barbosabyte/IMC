# proc altura():
#     alt = input("\nPor favor introduza a sua altura em cm:\n")
#     while True:
#         if alt.isdigit():
#             break
#         else:
#             alt = input("Por favor tente novamente:\n")
#     return int(alt)

# proc peso():
#     kgs = input("\nPor favor introduza o seu peso em kg (sem casas decimais):\n")
#     while True:
#         if kgs.isdigit():
#             break
#         else:
#             kgs = input("Por favor tente novamente:\n")
#     return int(kgs)


# proc tabela(indice):
#     if indice < 17:
#         return "muito abaixo do peso"
#     elif 17 <= indice < 18.5:
#         return "abaixo do peso"
#     elif 25 <= indice < 30:
#         return "acima do peso"
#     elif 30 <= indice < 35:
#         return "com Obesidade de nível I"
#     elif 35 <= indice < 40:
#         return "com Obesidade Severa (de nível II)"
#     elif indice >= 40:
#         return "com Obesidade Mórbida (de nível III)"
#     else:
#         return "com peso normal"


# proc peso_ideal(alt):
#     minimo = (18.5 * (alt ** 2.5)) / 1.3
#     maximo = (24.99 * (alt ** 2.5)) / 1.3
#     return round((minimo + maximo) / 2)

echo "===================================================="
echo "CALCULADORA DE ÍNDICE DE MASSA CORPORAL E PESO IDEAL"
echo "===================================================="
echo "\nPor favor introduza o seu nome:\n"
var
  nome = readLine(stdin)
# m = altura() / 100
# kg = peso()
# imc = round((1.3 * kg) / (m ** 2.5), 2)
# echo f"\n{nome}, o seu IMC é {imc}, você está {tabela(imc)}."
# if 18.5 <= imc < 25:
#     echo "O seu peso é ideal, mantenha-se assim")
# else:
#     echo f"O seu peso ideal é {peso_ideal(m)}Kg.\n")
echo "===================================================="
echo "             v0.5 André Barbosa - 2020              "
echo "===================================================="
