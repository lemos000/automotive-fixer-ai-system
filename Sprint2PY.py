import google.generativeai as genai
import random
import string
from colorama import init, Fore, Back, Style
import time
import sys
genai.configure(api_key="AIzaSyAEholv-jmYQOulH1WFOQg02O9RT14CalI")
model = genai.GenerativeModel('gemini-pro')

#Função para ver os atendimentos agendados e alterá-los
def atendimentosAgendados():
    try:
        c = 0
        for protocolos in protocolosLista:
            print('')
            c+=1
            print(f'{c}.')
            for item, valor in protocolos.items():
                print(f'. {item}: {valor}')
        while True:
            print("\n=== O que você quer fazer? ===")
            print('1. Alterar forma de pagamento')
            print('2. Cancelar agendamento')
            print('3. Visualizar lista de protocolos')
            print('4. Sair')
            while True:
                try:
                    agendOption = int(input('R: '))
                    break
                except:
                    print('Inválido!')
                    
            match agendOption:
                case 1:
                    alteracao =  int(input('Qual agendamento quer alterar? '))
                    alteracao-=1
                    if alteracao >= 0 and alteracao < len(protocolosLista):
                        print(f'Quer cancelar o protocolo de número: {protocolosLista[alteracao]['Num']}')
                        formaAlterar = int(input("Qual forma de pagamento você gostaria?\n1.Débito/PIX\n2.Crédito\n3.Dinheiro\nR:"))
                        if formaAlterar > 0 and formaAlterar < 4:
                            if formaAlterar == 1:
                                protocolosLista[alteracao]['Forma'] = 'Débito/Pix'
                            elif formaAlterar == 2:
                                protocolosLista[alteracao]['Forma'] = 'Crédito'
                            elif formaAlterar == 3:
                                protocolosLista[alteracao]['Forma'] = 'Dinheiro'
                            print(f'Forma de pagamento do protocolo {protocolosLista[alteracao]['Num']} alterada para  {protocolosLista[alteracao]['Forma']}!')
                            break

                        else:
                            print("Inválido")

                        break
                    else:
                        print('Índice inválido!')
                case 2:
                    cancelamento =  int(input('Qual agendamento quer cancelar? '))
                    cancelamento-=1
                    if cancelamento >= 0 and cancelamento < len(protocolosLista):
                        protocolo_cancelado = protocolosLista.pop(cancelamento)
                        print(f'O protocolo cancelado foi: {protocolo_cancelado['Num']}')
                        break
                    else:
                        print('Índice inválido!')
                case 3:
                    c = 0
                    for protocolos in protocolosLista:
                        print('')
                        c+=1
                        print(f'{c}.')
                        for item, valor in protocolos.items():
                            print(f'. {item}: {valor}')

                case 4:
                    break
                case other:
                    print('Inválido')

    except:
        print('Nenhum agendamento encontrado!')

#Função para gerar uma placa de carro
def novaPlaca():
    placa2= ''
    placa1 = ''.join(random.choices(string.ascii_letters, k=3))
    placa1 = placa1.upper()
    for i in range (0, 3):
        numero = random.randint(0,9)
        placa2= placa2+ str(numero)
    placafinal = placa1 + '-' + str(placa2)
    return placafinal


#Menu principal
def menu2():
    print('''
    Selecione uma das opções abaixo:
    1. Solicitar atendimento
    2. Atendimentos agendados
    3. Visualizar planos de seguro
    4. Sair''')

#Lista de protocolos de atendimento
protocolosLista = [
    {'Num': 'REP-123456789', 'Preço': 5000, 'Forma': 'Crédito'}
]

#Database de usuários
database = {
    'Gabriel': {'email': 'rm554819@fiap.com.br', 'senha': '123456'}, 
    'Gondo': {'email': 'gondo@professor.com', 'senha': 'FIAP123'},
    'Admin': {'email': 'admin@admin', 'senha': 'admin'},
}
#Função para solicitar o atendimento com api integrada
def solicitarAtendimento(problema):
    print("As possíveis causas são: ")
    response = model.generate_content(problema)
    print(response.text)
    local = input("\n\nQual seria sua localização no momento?\nR:")
    preciso = input("Você precisa de um guincho no momento?")
    preciso = preciso.upper()
    if preciso == 'SIM':
        print("Ok, um guincho com um mecânico estará a caminho de sua localização agora!")
        print(f"Enviaremos um guincho a {local}, a placa do guincho é {novaPlaca()}")
    elif preciso =="NAO" or preciso == 'NÃO':
        print(f"Ok, então dirija-se a oficina LVS mais próxima de {local}")
    print(f"No momento temos 3 oficinas em São Paulo, uma em Tatuapé, a outra na Japão-Liberdade e a última em Itaim Bibi, qual seria a mais viável a partir de sua localização?")
    while True:
        local_aproximado = input("R: ")
        local_aproximado = local_aproximado.upper()
        if local_aproximado == "ITAIM" or local_aproximado == 'TATUAPÉ' or local_aproximado == 'LIBERDADE':
            print(f'Ok, o carro será levado para {local_aproximado}')
            break
        else:
            print('Insira uma localização existente')
            
    preco = random.randint(500, 6000)
    print(f'O preço aproximado será de R${preco:.2f}')
    while True:
        try:
            forma = int(input("Qual será a forma de pagamento?\n1.Débito/PIX\n2.Crédito\n3.Dinheiro\nR:"))
            if forma >0 and forma <= 3:
                if forma == 1:
                    forma = 'Débito/PIX'
                elif forma ==2:
                    forma = "Crédito"
                elif forma == 3:
                    forma = "Dinheiro"
                break
            
            else:
                print(Fore.RED + "Escolha um número de 1 a 3!")
        except:
            print("Escolha um número de 1 a 3!")
            
    print(f"Tudo bem, o pagamento de R${preco:.2f} será realizado pela forma de pagamento {forma}")
    print("O pagamento deve ser realizado na oficina junto ao mecânico, os interesses devem ser alinhados e, por motivos de segurança, nenhum trabalho além do relatado será realizado!\nTenha um ótimo atendimento LVS!")
    protocolo = 'REP-'+str(random.randint(10000000, 99999999))
    print(f'O protocolo do seu atendimento é {protocolo}')
    adquirirProtocolo = {'Num': protocolo, 'Preço': f'R${preco:.2f}', 'Forma': forma}
    try:
        if plano_assinado in marcas_carro:
            print(f'Vejo aqui que você já tem um plano assinado, seria o {plano_assinado}')
            print(f'Com esse plano você tem direito a {beneficios[plano_assinado]}% de desconto no seu atendimento!')
    except:
        print("Nenhum plano assinado, nenhum desconto incluído")
    return adquirirProtocolo

#Função para visualizar os planos disponíveis
def visualizarPlanos():
    print('Você quer visualizar os planos de seguros possíveis da LVS Seguro? Vou detalhar cada um para você, ok?')
    for plano, marcas in marcas_carro.items():
        print(Style.BRIGHT+ plano + Style.RESET_ALL)
    inf = input('Sobre qual plano você quer mais informações?')
    inf = inf.upper()
    if inf in marcas_carro:
        print('\nOs carros disponíveis são: \n')
        for marca in marcas_carro[inf]:
            print(marca)
        if inf == 'SILVER':
            print("\nÉ o plano mais econômico de todos, você tem acesso a diversos carros populares para alugar no caso de perda total do seu veículo atual,\nalém disso, você ainda tem acesso as oficinas filiadas LVS com prioridade nível 3, aproveite essa chance! Por apenas R$600,00 mensais")
        elif inf == 'GOLD':
            print("\nÉ o plano nível 2 de seguradora LVS, você tem acesso a diversos carros populares e alguns esportivos para alugar no caso de perda total do seu veículo atual, além disso, você ainda tem acesso as oficinas filiadas LVS com prioridade nível 2, ou seja, seu atendimento será mais rápido e eficiente.\nAlém de tudo isso, você aproveita um desconto de 10% na utilização de oficinas com o selo LVS, tudo isso junto a um plano de fidelização com a oficina que você mais gostar.\nAproveite essa chance! Por apenas R$1000,00 mensais")
        elif inf == 'PLATINUM':
            print("\nÉ o plano mais custo-benefício de todos, você tem acesso a diversos carros populares, esportivos e luxo para alugar no caso de perda total do seu veículo atual,\nalém disso, você ainda tem todos os benefícios do plano Gold melhorados (Desconto de 15% em oficinas com selo LVSe plano de fidelização\ncom mais acúmulos de pontos!) e acesso as oficinas filiadas LVS com prioridade nível 1, aproveite essa chance! Por apenas R$1400,00 mensais")
        elif inf == 'PREMIUM':
            print("\nÉ o plano mais luxuoso de todos, você tem acesso a todos os benefícios de todos os outros planos, descontos de até 25% em oficinas LVS\ne acesso aos melhores carros da garagem da LVS, além disso, o assinante Premium tem um contato direto com um\nexecutivo LVS que o auxiliará diretamente com os problemas relacionado ao automóvel! Aproveite essa chance! Por apenas R$3000,00 mensais")

        resp = input(f'Você quer assinar o plano {Style.BRIGHT + inf + Style.RESET_ALL}?')
        resp = resp.upper()
        if resp == 'SIM':
            while True:
                dados_cartao = input("Preencha os dados de transação:\nNúmero do cartão:")
                if len(dados_cartao) < 15 or len(dados_cartao) > 16:
                    print("Número de cartão inválido!")
                else:
                    break
            while True:    
                cvv = input('Código de segurança do cartão: ')
                if len(cvv) != 3:
                    print("Inválido")
                else:
                    break
            nome_cliente = input('Nome no cartão: ')

            print(f"\n{nome_cliente}, agora você já pode usufruir do plano {inf}, os dados de pagamento serão enviados ao e-mail cadastrado no usuário LVS,\nas faturas e os detalhes da transação serão enviadas ao seu e-mail!")
            plano_assinado = inf
            return plano_assinado
        elif resp == 'NÃO' or resp == 'NAO':
            print("Ok, sentimos muito que não preenchemos sua expectativa D:\nMas estamos sempre à disposição caso queira assinar!")
            return False
        else: 
            print('Resposta inválida')

    else:
        print('Plano não existente')

#Função para criar conta e salvá-lo no pseudo banco de dados    
def criar_conta(database):
    print("=== Criação de Conta ===")
    username = input("Digite o nome de usuário desejado: ")
    if username in database:
        print("Nome de usuário já existe. Tente novamente.")
        return
    email = input("Digite o e-mail: ")
    password = input("Digite a senha desejada: ")
    database[username] = {'email': email, 'senha': password}
    print("Conta criada com sucesso!")

# Função para fazer login
def fazer_login(database):
    print("=== Login ===")
    username = input("Nome de usuário: ")
    password = input("Senha: ")
    if username in database and database[username]['senha'] == password:
        print(f"Login bem-sucedido! Olá, {username}")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
# Função do menu principal

def menu(database):
    print("=== Bem-vindo ===")
    print("1. Criar conta")
    print("2. Fazer login")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_conta(database)
    elif opcao == "2":
        if (fazer_login(database)):
            return True
    elif opcao == "3":
        print("Até logo!")
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        menu(database)

def mostrar_pontinhos():
    n=0
    while n<4:
        n+=1
        for i in range(4):
            pontinhos = '.' * i
            sys.stdout.write('\rPesquisando' + pontinhos)
            sys.stdout.flush()
            time.sleep(0.25)

marcas_carro = {
    "SILVER": ["Toyota", "Ford", "Chevrolet", "Honda", "Volkswagen", "Nissan", "Hyundai", "Kia"],
    "GOLD": ["BMW", "Mercedes-Benz", "Audi", "Subaru", "Porsche", "Jeep"],
    "PLATINUM": ["Tesla", "Land Rover", "Jaguar", "Aston Martin"],
    "PREMIUM": ["Ferrari", "Lamborghini"]
}

beneficios = {
    'SILVEER': 0,
    'GOLD': 10,
    'PLATINUM': 15,
    'PREMIUM': 25,
}


#Início do programa

print('-'*24)
print(Back.BLACK + Fore.CYAN + '''
LVS                   
REPAIR EXPRESS SYSTEM   ''' + Style.RESET_ALL)
print('-'*24)
print('Bem-vindo ao atendimento digital da LVS™')
while True:
    if menu(database):
        break
while True:
    menu2()
    while True:
        try: #Validação de dados
            opcao = int(input("R: "))
            break
        except:
            print("Insira um número válido.")
    match opcao:
        case 1:
            print("Perfeito, estamos sempre dispostos a te ajudar!")
            problema = input("Poderia descrever o problema do carro detalhadamente?\nR:")
            newProtocol = solicitarAtendimento("Fingindo que você é um mecânico de carros de alta qualidade, dê possíveis motivos para o problema: " + problema)
            protocolosLista.append(newProtocol)
        case 2:
            c = 0
            print("Vamos ver se há algum agendamento LVS no seu usuário!")
            mostrar_pontinhos()
            atendimentosAgendados()
        case 3:
            plano_assinado = visualizarPlanos()
        case 4: 
            print("Adeus, obrigado por utilizar o atendimento digital da LVS!")
            break
        case other:
            print('Selecione uma opcão válida')