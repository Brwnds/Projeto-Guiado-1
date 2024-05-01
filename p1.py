dataset = [ 
    {'ano_receita': 2022, 'mes_receita': '1', 'faturamento': 49179, 'despesas': 6295},
    {'ano_receita': 2022, 'mes_receita': '2', 'faturamento': 12018, 'despesas': 43329},
    {'ano_receita': 2022, 'mes_receita': '3', 'faturamento': 23524, 'despesas': 49376},
    {'ano_receita': 2022, 'mes_receita': '4', 'faturamento': 29615, 'despesas': 16973},
    {'ano_receita': 2022, 'mes_receita': '5', 'faturamento': 26527, 'despesas': 43742},
    {'ano_receita': 2022, 'mes_receita': '6', 'faturamento': 48400, 'despesas': 11447},
    {'ano_receita': 2022, 'mes_receita': '7', 'faturamento': 27219, 'despesas': 25593},
    {'ano_receita': 2022, 'mes_receita': '8', 'faturamento': 46787, 'despesas': 19018},
    {'ano_receita': 2022, 'mes_receita': '9', 'faturamento': 32306, 'despesas': 13522},
    {'ano_receita': 2022, 'mes_receita': '10', 'faturamento': 27106, 'despesas': 15969},
    {'ano_receita': 2022, 'mes_receita': '11', 'faturamento': 15255, 'despesas': 20105},
    {'ano_receita': 2022, 'mes_receita': '12', 'faturamento': 23864, 'despesas': 32509},
    {'ano_receita': 2023, 'mes_receita': '1', 'faturamento': 47240, 'despesas': 55776},
    {'ano_receita': 2023, 'mes_receita': '2', 'faturamento': 42771, 'despesas': 36819},
    {'ano_receita': 2023, 'mes_receita': '3', 'faturamento': 18008, 'despesas': 35853},
    {'ano_receita': 2023, 'mes_receita': '4', 'faturamento': 21857, 'despesas': 6940},
    {'ano_receita': 2023, 'mes_receita': '5', 'faturamento': 29735, 'despesas': 59626},
    {'ano_receita': 2023, 'mes_receita': '6', 'faturamento': 33704, 'despesas': 30072},
    {'ano_receita': 2023, 'mes_receita': '7', 'faturamento': 26515, 'despesas': 12129},
    {'ano_receita': 2023, 'mes_receita': '8', 'faturamento': 18149, 'despesas': 21663},
    {'ano_receita': 2023, 'mes_receita': '9', 'faturamento': 46176, 'despesas': 12564},
    {'ano_receita': 2023, 'mes_receita': '10', 'faturamento': 24649, 'despesas': 58127},
    {'ano_receita': 2023, 'mes_receita': '11', 'faturamento': 44484, 'despesas': 5304},
    {'ano_receita': 2023, 'mes_receita': '12', 'faturamento': 30840, 'despesas': 5055},
    {'ano_receita': 2024, 'mes_receita': '1', 'faturamento': 28726, 'despesas': 25133},
    {'ano_receita': 2024, 'mes_receita': '2', 'faturamento': 34962, 'despesas': 26537},
    {'ano_receita': 2024, 'mes_receita': '3', 'faturamento': 49424, 'despesas': 29649},
    {'ano_receita': 2024, 'mes_receita': '4', 'faturamento': 42698, 'despesas': 54170},
    {'ano_receita': 2024, 'mes_receita': '5', 'faturamento': 37237, 'despesas': 48453},
    {'ano_receita': 2024, 'mes_receita': '6', 'faturamento': 30665, 'despesas': 8782},
    {'ano_receita': 2024, 'mes_receita': '7', 'faturamento': 39597, 'despesas': 12261},
    {'ano_receita': 2024, 'mes_receita': '8', 'faturamento': 49326, 'despesas': 18862},
    {'ano_receita': 2024, 'mes_receita': '9', 'faturamento': 19043, 'despesas': 48517},
    {'ano_receita': 2024, 'mes_receita': '10', 'faturamento': 24464, 'despesas': 24215},
    {'ano_receita': 2024, 'mes_receita': '11', 'faturamento': 11635, 'despesas': 8190},
    {'ano_receita': 2024, 'mes_receita': '12', 'faturamento': 39303, 'despesas': 14418}
]


def adicionar_registro():
    ano = int(input("Digite o ano da receita: "))
    mes = input("Digite o mês da receita: ")
    faturamento = int(input("Digite o faturamento: "))
    despesas = int(input("Digite as despesas: "))
    dataset.append({'ano_receita': ano, 'mes_receita': mes, 'faturamento': faturamento, 'despesas': despesas})
    print("Registro adicionado com sucesso!")

def calcular_receita_ano():
    ano = int(input("Digite o ano para calcular a receita: "))
    receita_ano = sum(data['faturamento'] for data in dataset if data['ano_receita'] == ano)
    print(f"A receita total para o ano de {ano} foi de: {receita_ano}")

def mes_maior_lucro():
    mes_lucro_max = max(dataset, key=lambda x: x['faturamento'])
    print(f"O mês com maior lucro foi: {mes_lucro_max['mes_receita']}")

def mes_maior_despesa():
    mes_despesa_max = max(dataset, key=lambda x: x['despesas'])
    print(f"O mês com maiores despesas foi: {mes_despesa_max['mes_receita']}")

def ano_melhor_receita():
    receita_por_ano = {}
    for data in dataset:
        ano = data['ano_receita']
        receita = data['faturamento']
        if ano in receita_por_ano:
            receita_por_ano[ano] += receita
        else:
            receita_por_ano[ano] = receita
    ano_melhor = max(receita_por_ano, key=lambda x: receita_por_ano[x])
    print(f"O ano com melhor receita foi: {ano_melhor}")

def ano_pior_receita():
    receita_por_ano = {}
    for data in dataset:
        ano = data['ano_receita']
        receita = data['faturamento']
        if ano in receita_por_ano:
            receita_por_ano[ano] += receita
        else:
            receita_por_ano[ano] = receita
    ano_pior = min(receita_por_ano, key=lambda x: receita_por_ano[x])
    print(f"O ano com pior receita foi: {ano_pior}")

def menu():
    while True:
        print("\n---- Menu ----")
        print("1. Adicionar novo registro")
        print("2. Calcular receita para um ano")
        print("3. Exibir mês com maior lucro")
        print("4. Exibir mês com maiores despesas")
        print("5. Exibir ano com melhor e pior receita")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_registro()
        elif escolha == '2':
            calcular_receita_ano()
        elif escolha == '3':
            mes_maior_lucro()
        elif escolha == '4':
            mes_maior_despesa()
        elif escolha == '5':
            ano_pior_receita()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
