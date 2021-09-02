from Core.TratamentoStrFloat import ObjTratamento


active = True

while active:
    try:
        print("-" * 53)
        print(" " * 22, "VOLTZ", " " * 22)
        print("-" * 53, "\n")

        gas_input_recebendo = str(input("Informe o preço da gasolina ou S para sair: "))
        gas_input, active = ObjTratamento.tratamento(gas_input_recebendo, active)

        if active == False:
            raise ValueError("SAINDO!")

        km_litro_recebendo = str(input("Informe quantos Km/L seu veículo realiza na estrada ou S para sair: "))
        km_litro, active = ObjTratamento.tratamento(km_litro_recebendo, active)

        if active == False:
            raise ValueError("SAINDO!")

        tanque_vol_recebendo = str(input("Informe o tamanho do tanque do seu veículo: "))
        tanque_vol, active = ObjTratamento.tratamento(tanque_vol_recebendo, active)

        if active == False:
            raise ValueError("SAINDO!")

        km_viagem_recebendo = str(input("Informe a distância em km de sua viagem ou S para sair: "))
        km_viagem, active = ObjTratamento.tratamento(km_viagem_recebendo, active)

        if active == False:
            raise ValueError("SAINDO!")

        calc_litros = km_viagem / km_litro
        calc_litros = round(calc_litros, 2)

        calc_valor = calc_litros * gas_input
        calc_valor = round(calc_valor, 2)

        calc_moto = (5.0 * 2.4) * 0.9  # R$ 10.8 -> 120 km
        calc_moto = round(calc_moto, 2)
        calc2_moto = (calc_moto * km_viagem) / 120.0
        calc2_moto = round(calc2_moto, 2)

        tanque_cheio = tanque_vol * gas_input
        tanque_cheio = round(tanque_cheio)

        km_total = tanque_vol * km_litro
        km_total = round(km_total, 2)

        print(f"Obrigado pelas informações!\nAgora perceba o quanto as motos elétricas Voltz são muito mais econômicas: \n{km_viagem}km com seu veículo dão exatamente R$ {calc_valor}\n{km_viagem}km com a Voltz dão exatamente R$ {calc2_moto}\n")

        if calc_valor > calc2_moto:
            calc3_fim = calc_valor - calc2_moto
            calc3_fim = round(calc3_fim, 2)
            print(f"Com a moto elétrica Voltz você economizará R$ {calc3_fim}\nPara encher o tanque de seu veículo você gastará: -> R$ {tanque_cheio} e percorrerá {km_total}km\nPara uma carga completa na sua Voltz você gastará: -> R$ {calc_moto} e percorrerá 120km")
            raise  ValueError("REINICIANDO!")
        elif calc_valor <= calc2_moto:
            print(f"Curiosamente a moto Voltz não é mais econômica que o seu veículo e com base no nosso banco de dados você muito provavelmente mentiu para nós!")
            print("Adeus!")
            active = False
            raise ValueError("NUNCA MAIS VOLTE!")

    except ValueError as e:
        print("LOG: -> ", e)
