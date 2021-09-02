from Core.TratamentoStrFloat import ObjTratamento


active = True

while active:
    try:
        saque_recebendo = str(input("Informe quanto deseja sacar ou S para sair: "))
        saque, active = ObjTratamento.tratamento(saque_recebendo, active)
        saque = int(saque)
        if active == False:
            raise ValueError("SAINDO!")

        if not 0 <= saque <= 150000:
            raise ValueError("Limite para saque é até 15k! Escolha um valor menor!\nREINICIANDO!")
        else:
            qnt = len(str(saque)) # quantidade de dígitos
            cont = int(qnt) # reforçando o tipo
        notas_cem = 0
        notas_cinquenta = 0
        notas_vinte = 0
        notas_dez = 0
        notas_cinco = 0
        inicio = cont  # mantendo o registro inicial da quantidade
        saque_str = str(saque)
        
        for i in range(qnt):            
            if 3 <= cont <= 6: # 3:1 4:10 5:100 6:1000
                if cont == 6:
                    saque_int = int(saque_str[i])
                    notas_cem = notas_cem + (saque_int * 1000)
                elif cont == 5:
                    saque_int = int(saque_str[i])
                    notas_cem = notas_cem + (saque_int * 100)
                elif cont == 4:
                    saque_int = int(saque_str[i])
                    notas_cem = notas_cem + (saque_int * 10)
                elif cont == 3:
                    saque_int = int(saque_str[i])
                    notas_cem = notas_cem + (saque_int * 1)
            if cont == 2:
                saque_int = int(saque_str[i])
                if saque_int >= 5:
                    notas_dez = notas_dez + ( saque_int - 5)
                    notas_cinquenta = notas_cinquenta + 1
                elif saque_int < 5:
                    notas_dez = saque_int
            elif cont == 1:
                saque_int = int(saque_str[i])
                if saque_int >= 5:
                    notas_um = saque_int - 5
                    notas_cinco = notas_cinco + 1
                elif saque_int < 5:
                    notas_um = saque_int
            i += 1
            cont -= 1
        if 3 <= inicio <= 10:
            if notas_um == 0:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                raise ValueError("Nenhum valor válido selecionado!")
                            else:
                                print(f"Você receberá no caixa: \n{notas_cem} notas de cem\n")    
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta")
                            else:
                                print(f"Você receberá no caixa: \n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta")
                    else:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_dez} notas de dez")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_dez} notas de dez")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez")
                else:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinco} notas de cinco")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco")
                    else:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
            else:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_um} notas de um")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_um} notas de um")
                    else:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_dez} notas de dez\n{notas_um} notas de um")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_um} notas de um")
                else:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                    else:
                        if notas_cinquenta == 0:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                        else:
                            if notas_cem == 0:
                                print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                            else:
                                print(f"Você receberá no caixa:\n{notas_cem} notas de cem\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
        elif inicio == 2:
            if notas_um == 0:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            raise ValueError("Nenhum valor válido selecionado!")   
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta")
                    else:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_dez} notas de dez")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez")
                else:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco")
                    else:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
            else:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_um} notas de um")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_um} notas de um")
                    else:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_um} notas de um")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_um} notas de um")
                else:
                    if notas_dez == 0:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                    else:
                        if notas_cinquenta == 0:
                            print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                        else:
                            print(f"Você receberá no caixa:\n{notas_cinquenta} notas de cinquenta\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
        elif inicio == 1:
            if notas_um == 0:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        raise ValueError("Nenhum valor válido selecionado!")
                    else:
                        print(f"Você receberá no caixa:\n{notas_dez} notas de dez")
                else:
                    if notas_dez == 0:
                        print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco")
                    else:
                        print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco")
            else:
                if notas_cinco == 0:
                    if notas_dez == 0:
                        print(f"Você receberá no caixa:\n{notas_um} notas de um")
                    else:
                        print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_um} notas de um")
                else:
                    if notas_dez == 0:
                        print(f"Você receberá no caixa:\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
                    else:
                        print(f"Você receberá no caixa:\n{notas_dez} notas de dez\n{notas_cinco} notas de cinco\n{notas_um} notas de um")
        else:
            raise ValueError("DADO INCORRETO!")

    except ValueError as e:
        print("LOG: -> ", e )
