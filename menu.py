OPCAO = 0
moradores = 0
peso = 0
nome = ""
carro = 0
bicicleta = 0
primeirapessoa = ""
ultimapessoa = ""
maismagra = 0
maisvelha = 0
nomevelha = ""
nomemagra = ""
somaidade = 0
somapeso = 0
while OPCAO != 3 and moradores < 300:
    print("1 - Entrevistar morador.")
    print("2 - Apresentar resultado parcial.")
    print("3 - Sair.")
    OPCAO = int(input("digite a opcao:"))
    if OPCAO == 1:
        nome = input("Digite seu nome:")
        if moradores == 0:
            primeirapessoa = nome
        ultimapessoa = nome
        idade = int(input("digite a idade:"))
        if moradores == 0:
            maisvelha = idade
            nomevelha = nome
        elif idade > maisvelha:
            maisvelha = idade
            nomevelha = nome
        somaidade += idade
        peso = float(input("Digite o peso:"))
        somapeso += peso
        if moradores == 0:
            maismagra = peso
        elif peso < maismagra:
            maismagra = peso
            nomemagra = nome
        transporte = input("Digite o transporte mais utilizado:").upper()
        if transporte == "CARRO":
            carro += 1
        elif transporte == "BICICLETA":
            bicicleta += 1
        else:
            print("Opcao invalida!")
        moradores += 1
    elif OPCAO == 2:
        print("1 - media parcial das idades.")
        print("2 - nome da pessoa mais magra.")
        print("3 - nome da pessoa mais velha.")
        print("4 - porcentagem dos que usam carro ou bicicleta.")
        subopcao = int(input("Digite a opção:"))
        mediaidade = somaidade / moradores
        if subopcao == 1:
            print("A media parcial das idades é:",mediaidade)
        elif subopcao == 2:
            print("O nome da pessoa mais magra é:", nomemagra)
        elif subopcao == 3:
            print("O nome da pessoa mais velha é:", nomevelha)
        elif subopcao == 4:
            porcentagembike = bicicleta / moradores * 100
            porcentagemcarro = carro / moradores * 100
            print("A porcentagem de pessoas que usam bicicleta é:", porcentagembike)
            print("A porcentagem de pessoas que usam carro é:", porcentagemcarro)
    elif OPCAO == 3:
        mediaidade = somaidade / moradores
        mediapeso = somapeso / moradores
        print("A media parcial das idades é:",mediaidade)
        print("A primeira pessoa intrevistada foi:", primeirapessoa)
        print("A ultima pessoa intrevistada foi:", ultimapessoa)
        print("A media de peso é:", mediapeso) 
    else:
        print("opção invalida, tente novamente!")

             
        



        
