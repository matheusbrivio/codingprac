try:
    numero = int(input("digite um numero intero:"))
except:
    numero = int(input("esse numero nao é inteiro!, tente novamente:"))

if numero % 2 == 0:
    print(f"Esse numero é par")
else:
    print(f"Esse numero é impar")
