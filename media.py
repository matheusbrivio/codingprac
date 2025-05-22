
def somamedia(lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista [i]
    media = soma / len(lista)
    return media


def main():
    lista = []
    qtdnumeros = int(input("Digite a quantidade de numero que quer na lista:"))
    for i in range (qtdnumeros):
        numero = int(input("Digite um numero:"))
        lista.append(numero)
    media = somamedia(lista)
    print("O resultado da média é:", media)

main()
