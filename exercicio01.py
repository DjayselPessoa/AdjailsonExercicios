from Core.TratamentoStrFloat import ObjTratamento


active = True

while active:
    try:
        valor_consumo_recebido = str(input("Informe o consumo mensal em kWh ou S para sair: "))
        valor_consumo, active = ObjTratamento.tratamento(valor_consumo_recebido, active)

        if active == False:
            raise ValueError("DESLIGANDO!")

        if valor_consumo <= 100.0:
            valor_consumo_final = valor_consumo * 0.9
            print(f"O valor não possui acréscimo de bandeira por estar abaixo de 100.0kWh!\nValor total: -> {valor_consumo}kWh = R$ {round(valor_consumo_final)}")
            sair = str(input("S para sair ou C para continuar: "))
            if sair in "Ss":
                active = False
                raise ValueError("DESLIGANDO!")
            elif sair in "Cc":
                active = True
                raise ValueError("REINICIANDO!")

        elif valor_consumo > 100.0:
            valor_consumo_100 = valor_consumo - 100.0
            valor_consumo_amarela = valor_consumo_100 * 1.874
            valor_consumo_amarela = round(valor_consumo_amarela, 2)
            valor_consumo_vermelha = valor_consumo_100 * 3.971
            valor_consumo_vermelha = round(valor_consumo_vermelha, 2)
            valor_consumo_final = 100.0 * 0.9
            valor_consumo_final = round(valor_consumo_final, 2) 
            print(f"Até 100.0kWh a tarifa é R$ 0.90: -> R$ {valor_consumo_final}\ntodo valor além dos 100.0kWh depende da bandeira:\nAmarela: -> RS {valor_consumo_amarela} + R$ {valor_consumo_final} = R$ {valor_consumo_amarela + valor_consumo_final}\nVermelha: -> R$ {valor_consumo_vermelha} + R$ {valor_consumo_final} = R$ {valor_consumo_vermelha + valor_consumo_final}")
            sair = str(input("S para sair ou C para continuar: "))
            if sair in "Ss":
                active = False
                raise ValueError("DESLIGANDO!")
            elif sair in "Cc":
                active = True
                raise ValueError("REINICIANDO!")
    except ValueError as e:
        print("LOG: -> ", e)
