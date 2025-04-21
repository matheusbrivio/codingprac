opcao = 0
gasolina = 6.89
diesel = 4.80
totalgasolina = 0
totaldiesel = 0
valortotal = 0
while opcao != 2:
    print("1 - vender combustivel")
    print("2 - sair")
    
    opcao = int(input("Digite a opçao:"))
    if opcao == 1:
        print("1 - gasolina")
        print("2 - diesel")
        subopcao = int(input("digite a opcao:"))
        litros = float(input("digite o total de litros abastecidos"))
        valorpago = float(input("digite o valor pago:"))
        if subopcao == 1:
            valortotal = gasolina * litros
            troco = valorpago - valortotal
            if troco == 0:
                print("O valor pago está correto!")
            elif troco <0:
                print("Voce deve R$",(troco * - 1))
            else:
                print("Seu troco é R$",troco)
            totalgasolina += valortotal
        if subopcao == 2:
            valortotal = diesel * litros
            troco = valorpago - valortotal
            if troco == 0:
                print("O valor pago está correto!")
            elif troco <0:
                print("Voce deve R$",(troco * - 1))
            else:
                print("Seu troco é R$",troco)
            totaldiesel += valortotal
    elif opcao == 2:
        print("O total de gasolina vendido foi:",totalgasolina)
        print("O total de diesel vendido foi:",totaldiesel)
