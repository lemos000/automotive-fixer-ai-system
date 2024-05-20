import google.generativeai as genai
import random
import string

genai.configure(api_key="AIzaSyAEholv-jmYQOulH1WFOQg02O9RT14CalI")
model = genai.GenerativeModel('gemini-pro')


def novaPlaca():
    placa2= ''
    placa1 = ''.join(random.choices(string.ascii_letters, k=3))
    placa1 = placa1.upper()
    for i in range (0, 3):
        numero = random.randint(0,9)
        placa2= placa2+ str(numero)
    placafinal = placa1 + '-' + str(placa2)
    return placafinal



def menu2():
    print('''
    Selecione uma das opções abaixo:
    1. Solicitar atendimento
    2. Solicitar locação de carro
    3. Visualizar planos de seguro
    4. Sair''')

database = {
    'Gabriel': {'email': 'rm554819@fiap.com.br', 'senha': '123456'}, 
    'Gondo': {'email': 'gondo@professor.com', 'senha': 'admin'}
}

def visualizarPlanos():
    print('Você quer visualizar os planos de seguros possíveis da Porto Seguro? Vou detalhar cada um para você, ok?')
    for plano, marcas in marcas_carro.items():
        print(plano)
    inf = input('Sobre qual plano você quer mais informações?')
    if inf in marcas_carro:
        print('\nOs carros disponíveis são: \n')
        for marca in marcas_carro[inf]:
            print(marca)
        if inf == 'Silver':
            print("\nÉ o plano mais econômico de todos, você tem acesso a diversos carros populares para alugar no caso de perda total do seu veículo atual,\nalém disso, você ainda tem acesso as oficinas filiadas Porto com prioridade nível 3, aproveite essa chance! Por apenas R$600,00 mensais")
        elif inf == 'Gold':
            print("\nÉ o plano nível 2 de seguradora Porto, você tem acesso a diversos carros populares e alguns esportivos para alugar no caso de perda total do seu veículo atual, além disso, você ainda tem acesso as oficinas filiadas Porto com prioridade nível 2, ou seja, seu atendimento será mais rápido e eficiente.\nAlém de tudo isso, você aproveita um desconto de 10% na utilização de oficinas com o selo PortoREPEX, tudo isso junto a um plano de fidelização com a oficina que você mais gostar.\nAproveite essa chance! Por apenas R$1000,00 mensais")
        elif inf == 'Platinum':
            print("\nÉ o plano mais custo-benefício de todos, você tem acesso a diversos carros populares, esportivos e luxo para alugar no caso de perda total do seu veículo atual,\nalém disso, você ainda tem todos os benefícios do plano Gold melhorados (Desconto de 15% em oficinas com selo PortoREPEXe plano de fidelização\ncom mais acúmulos de pontos!) e acesso as oficinas filiadas Porto com prioridade nível 1, aproveite essa chance! Por apenas R$1400,00 mensais")
        elif inf == 'Premium':
            print("\nÉ o plano mais luxuoso de todos, você tem acesso a todos os benefícios de todos os outros planos, descontos de até 25% em oficinas PortoREPEX\ne acesso aos melhores carros da garagem da Porto, além disso, o assinante Premium tem um contato direto com um\nexecutivo Porto que o auxiliará diretamente com os problemas relacionado ao automóvel! Aproveite essa chance! Por apenas R$3000,00 mensais")

        resp = input(f'Você quer assinar o plano {inf}?')
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

            print(f"{nome_cliente}, agora você já pode usufruir do plano {inf}, os dados de pagamento serão enviados ao e-mail cadastrado no usuário PortoREPEX,\nas faturas e os detalhes da transação serão enviadas ao seu e-mail!")
            plano_assinado = inf
            return plano_assinado
        elif resp == 'NÃO' or resp == 'NAO':
            print("Ok, sentimos muito que não preenchemos sua expectativa D:\nMas estamos sempre à disposição caso queira assinar!")
            return False
        else: 
            print('Resposta inválida')

    else:
        print('Plano não existente')




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



marcas_carro = {
    "Silver": ["Toyota", "Ford", "Chevrolet", "Honda", "Volkswagen", "Nissan", "Hyundai", "Kia"],
    "Gold": ["BMW", "Mercedes-Benz", "Audi", "Subaru", "Porsche", "Jeep"],
    "Platinum": ["Tesla", "Land Rover", "Jaguar", "Aston Martin"],
    "Premium": ["Ferrari", "Lamborghini"]
}
beneficios = {
    'Silver': 0,
    'Gold': 10,
    'Platinum': 15,
    'Premium': 25,
}

print('-'*20)
print('''
┏┓          
┃┃┏┓┏┓╋┏┓   
┣┛┗┛┛ ┗┗┛   
┏┓          
┗┓┏┓┏┓┓┏┏┓┏┓
┗┛┗ ┗┫┗┻┛ ┗┛
     ┛
REPAIR EXPRESS SYSTEM''')
print('-'*20)
print('Bem-vindo ao atendimento digital da Porto™')
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
                print(f"Ok, então dirija-se a oficina PortoREPEX mais próxima de {local}")
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
            forma = input("Qual será a forma de pagamento?\n1.Débito/PIX\n2.Crédito\n3.Dinheiro")
            print(f"Tudo bem, o pagamento de {preco} será realizado pela forma de pagamento {forma}")
            print("O pagamento deve ser realizado na oficina junto ao mecânico, os interesses devem ser alinhados e, por motivos de segurança, nenhum trabalho além do relatado será realizado!\nTenha um ótimo atendimento PortoREPEX!")
            try:
                if plano_assinado in marcas_carro:
                    print(f'Vejo aqui que você já tem um plano assinado, seria o {plano_assinado}')
                    print(f'Com esse plano você tem direito a {beneficios[plano_assinado]} no seu atendimento!')

            except:
                print("Nenhum plano assinado, nenhum desconto incluído")







        case 3:
            plano_assinado = visualizarPlanos()
                       

            













        case 4:
            print("Adeus, obrigado por utilizar o atendimento digital da Porto!")
            break
        case other:
            print('Selecione uma opcão válida')