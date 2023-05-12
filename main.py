from classes import *

dc_cliente = {}
dc_funcionario = {}
dc_pedido = {}
preco_tot = []

Desconto.register(Pedido)

cont = 0


def mostrar_cardapio():
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=CARDAPIO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('-----------COMIDAS----------------|-----------BEBIDAS-------------|')
    print('1-Hamburguer ........12,00 a 15,00| 7-Refrigerante ........8,00   |')
    print('2-Pizza .............40,00 a 50,00| 8-Água mineral ........2,00   |')
    print('3-Coxinha ...........3,00 a 4,00  | 9-Água de coco ........4,00   |')
    print('4-Bomba .............3,00         | 10-Cerveja ............8,00   |')
    print('5-Pastel ............3,00 a 4,00  |                               |')
    print('6-Salsichão .........3,00         |                               |')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def hamburguer():
    print('1-X_Bacon.........12,00')
    print('2-X_Salada........13,00')
    print('3-X_Delicia.......14,00')
    print('4-X_Calabresa.....15,00')
    print('5-Sair')

def pizza():
    print('1-Mexicana.........50,00')
    print('2-Frango...........40,00')
    print('3-Calabresa........40,00')
    print('4-Nordestina.......50,00')
    print('5-Sair')

def coxinha():
    print('1-Frango....................3,00')
    print('2-Frango com Cheddar........4,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print('5-Sair')

def pastel():
    print('1-Frango....................3,00')
    print('2-Frango com Cheddar........4,00')
    print('3-Frango com catupiry.......4,00')
    print('4-Carne.....................3,00')
    print('5-Sair')

def refrigerante():
    print('1-Coca cola.................8,00')
    print('2-Guaraná...................8,00')
    print('3-Fanta laranja.............8,00')
    print('4-Fanta uva.................8,00')
    print('5-Sair')


while True:
    print('-----------MENU-----------')
    print('1 - cadastrar funcionário')
    print('2 - cadastrar cliente')
    print('3 - realizar um pedido')
    print('4 - consultar um pedido')
    print('5 - cárdapio')
    print('6 - sair')
    print('--------------------------')
    op = int(input('escolha uma opção:'))
    if op == 1:
        try:
            nome = str(input('Nome:'))
            cpf = str(input('CPF:'))
            if cpf in dc_funcionario.keys():
                print('Um Funcionário já possui este CPF!')
            else:
                dt_nasc = str(input('Data de nascimento:'))
                salario = float(input('Salário:'))
                cargo = str(input('cargo:'))
                f = Funcionario(nome, cpf, dt_nasc, salario, cargo)
                dc_funcionario[cpf] = f
                print('Funcionário cadastrado com sucesso! ✅')
        except:
            print('Você digitou dados errados!')
    elif op == 2:
        try:
            nome = str(input('Nome:'))
            cpf = str(input('CPF:'))
            if cpf in dc_cliente.keys():
                print('Um Cliente já possui este CPF!')
            else:
                dt_nasc = str(input('Data de nascimento:'))
                cliente = Cliente(nome, cpf, dt_nasc)
                dc_cliente[cpf] = cliente
                print('Cliente cadastrado com sucesso! ✅')
        except:
            print('Você digitou dados errados!')
    elif op == 3:
        cpf = str(input('CPF:'))
        if cpf not in dc_cliente.keys():
            print('CPF do cliente não foi cadastrado!')
        elif cpf in dc_cliente.keys():
            preco_tot.clear()
            while True:
                cliente = dc_cliente[cpf]
                print(f'Muito bem {cliente.nome}, Vamos realizar o seu pedido!')
                mostrar_cardapio()
                print('11-Calcular preço')
                print('12-Finalizar pedido')
                print('')
                opc = int(input(f'Escolha um lanche {cliente.nome}:'))
                if opc == 1:
                    print(f'HUMMMM! Hambuguer, Ótima escolha {cliente.nome}')
                    hamburguer()
                    escolha = int(input('Escolha um tipo de Hambuguer:'))
                    if escolha == 1:
                        print('X_Bacon')
                        preco = desconto = preco_desconto = 0
                        valor = 12.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 2:
                        print('X_Salada')
                        preco = desconto = preco_desconto = 0
                        valor = 13.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 3:
                        print('X_Delicia')
                        preco = desconto = preco_desconto = 0
                        valor = 14.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')
                    elif escolha == 4:
                        print('X_Calabresa')
                        preco = desconto = preco_desconto = 0
                        valor = 15.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                elif opc == 2:
                    print(f'HUMMMM! Pizza, Ótima escolha {cliente.nome}')
                    pizza()
                    escolha = int(input('Escolha um tipo de Pizza:'))
                    if escolha == 1:
                        print('Pizza Mexicana:')
                        preco = desconto = preco_desconto = 0
                        valor = 50.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 2:
                        print('Pizza de Frango:')
                        preco = desconto = preco_desconto = 0
                        valor = 40.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 3:
                        print('Pizza de Calabresa:')
                        preco = desconto = preco_desconto = 0
                        valor = 40.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 4:
                        print('Pizza Nordestina:')
                        preco = desconto = preco_desconto = 0
                        valor = 50.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                elif opc == 3:
                    print(f'HUMMMM! Coxinha, Ótima escolha {cliente.nome}')
                    coxinha()
                    escolha = int(input('Escolha um tipo de Coxinha:'))
                    if escolha == 1:
                        print('Coxinha de Frango:')
                        preco = desconto = preco_desconto = 0
                        valor = 3.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')
                    elif escolha == 2:
                        print('Coxinha de Frango com Cheddar:')
                        preco = desconto = preco_desconto = 0
                        valor = 4.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 3:
                        print('Coxinha de Frango com catupiry:')
                        preco = desconto = preco_desconto = 0
                        valor = 4.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 4:
                        print('Coxinha de Carne:')
                        preco = desconto = preco_desconto = 0
                        valor = 3.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')
                elif opc == 4:
                    print(f'HUMMMM! Bomba, Ótima escolha {cliente.nome}')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    dc_pedido[cliente.cpf] = p
                    preco_tot.append(valor)
                    print('Pedido realizado!')
                elif opc == 5:
                    print(f'HUMMMM! Pastel, Ótima escolha {cliente.nome}')
                    pastel()
                    escolha = int(input('Escolha um tipo de Pastel:'))
                    if escolha == 1:
                        print('Pastel de Frango:')
                        preco = desconto = preco_desconto = 0
                        valor = 3.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 2:
                        print('Pastel de Frango com Cheddar:')
                        preco = desconto = preco_desconto = 0
                        valor = 4.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 3:
                        print('Pastel de Frango com catupiry:')
                        preco = desconto = preco_desconto = 0
                        valor = 4.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 4:
                        print('Pastel de Carne:')
                        preco = desconto = preco_desconto = 0
                        valor = 3.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                elif opc == 6:
                    print(f'HUMMMM! Salsichão, Ótima escolha {cliente.nome}')
                    preco = desconto = preco_desconto = 0
                    valor = 3.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    dc_pedido[cliente.cpf] = p
                    preco_tot.append(valor)
                    print('Pedido realizado!')

                elif opc == 7:
                    print(f'HUMMMM! Refrigerante, Ótima escolha {cliente.nome}')
                    refrigerante()
                    escolha = int(input('Escolha um tipo de Pastel:'))
                    if escolha == 1:
                        print('Coca cola:')
                        preco = desconto = preco_desconto = 0
                        valor = 8.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 2:
                        print('Guaraná:')
                        preco = desconto = preco_desconto = 0
                        valor = 8.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 3:
                        print('Fanta laranja:')
                        preco = desconto = preco_desconto = 0
                        valor = 8.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                    elif escolha == 4:
                        print('Fanta uva:')
                        preco = desconto = preco_desconto = 0
                        valor = 8.00
                        p = Pedido(preco, desconto, preco_desconto, cliente)
                        dc_pedido[cliente.cpf] = p
                        preco_tot.append(valor)
                        print('Pedido realizado!')

                elif opc == 8:
                    print(f'HUMMMM! Água mineral, Ótima escolha {cliente.nome}')
                    preco = desconto = preco_desconto = 0
                    valor = 2.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    dc_pedido[cliente.cpf] = p
                    preco_tot.append(valor)
                    print('Pedido realizado!')

                elif opc == 9:
                    print(f'HUMMMM! Água de coco, Ótima escolha {cliente.nome}')
                    preco = desconto = preco_desconto = 0
                    valor = 4.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    dc_pedido[cliente.cpf] = p
                    preco_tot.append(valor)
                    print('Pedido realizado!')

                elif opc == 10:
                    print(f'HUMMMM! Cerveja, Ótima escolha {cliente.nome}')
                    preco = desconto = preco_desconto = 0
                    valor = 8.00
                    p = Pedido(preco, desconto, preco_desconto, cliente)
                    dc_pedido[cliente.cpf] = p
                    preco_tot.append(valor)
                    print('Pedido realizado!')

                elif opc == 11:
                    retorno = dc_pedido[cliente.cpf].calcular_preco(preco_tot)
                    if retorno <= 20:
                        print('Preço:', retorno)

                    elif retorno > 20 and retorno <= 50:
                        des = 2/100
                        desct = dc_pedido[cliente.cpf].calcular_desconto(des)
                        cal_des = dc_pedido[cliente.cpf].calcular_preco_com_desconto()
                        print('Preço:', retorno)
                        print('desconto:',desct)
                        print('PREÇO FINAL = ', cal_des)

                    elif retorno > 50 and retorno <= 100:
                        des = 3/100
                        desct = dc_pedido[cliente.cpf].calcular_desconto(des)
                        cal_des = dc_pedido[cliente.cpf].calcular_preco_com_desconto()
                        print('Preço:', retorno)
                        print('desconto:', desct)
                        print('PREÇO FINAL = ', cal_des)

                    elif retorno > 100 and retorno <= 200:
                        des = 4/100
                        desct = dc_pedido[cliente.cpf].calcular_desconto(des)
                        cal_des = dc_pedido[cliente.cpf].calcular_preco_com_desconto()
                        print('Preço:', retorno)
                        print('desconto:', desct)
                        print('PREÇO FINAL = ', cal_des)

                    elif retorno > 200:
                        des = 5/100
                        desct = dc_pedido[cliente.cpf].calcular_desconto(des)
                        cal_des = dc_pedido[cliente.cpf].calcular_preco_com_desconto()
                        print('Preço:', retorno)
                        print('desconto:', desct)
                        print('PREÇO FINAL = ', cal_des)



                elif opc == 12:
                    cont += 1
                    print(f'Seu pedido foi o {cont}º da lista')
                    print(f'Obrigado pela preferência! {cliente.nome}')
                    break
                else:
                    print('opção inválida! escolha uma opção do cardápio.')


    elif op == 4:
        cpf = str(input('CPF:'))
        if cpf not in dc_pedido.keys():
            print('Cliente não realizou um pedido!')
        elif cpf in dc_pedido.keys():
            print('CPF = ', cpf)
            print('cliente = ', dc_pedido[cpf].cliente.nome)
            print('preço = ', dc_pedido[cpf].preco)
            print('desconto = ', dc_pedido[cpf].desconto)
            if dc_pedido[cpf].preco_desconto != 0:
                print('VALOR FINAL = ', dc_pedido[cpf].preco_desconto)
            else:
                print('VALOR FINAL = ', dc_pedido[cpf].preco)

    elif op == 5:
        mostrar_cardapio()
    elif op == 6:
        print('Obrigado pela preferência! volte sempre')
        break
    else:
        print('Nenhuma opção foi escolhida! por favor escolha uma opção')
