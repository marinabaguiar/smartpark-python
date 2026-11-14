import config
from financeiro import calcular_cobranca, formatar_moeda


def mostrar_vagas(ocupadas):
    disponiveis = config.CAPACIDADE_MAXIMA - ocupadas
    porcentagem = ocupadas / config.CAPACIDADE_MAXIMA * 100

    print("\n--------------- VAGAS DO ESTACIONAMENTO ---------------")
    print("Capacidade total:", config.CAPACIDADE_MAXIMA)
    print("Vagas ocupadas:", ocupadas)
    print("Vagas disponíveis:", disponiveis)
    print("Ocupação do estacionamento: ", round(porcentagem, 1), "%")


def mostrar_faturamento(faturamento, saidas):
    print("\n--------------- RESUMO DO FATURAMENTO ---------------")
    print("Total recebido:", formatar_moeda(faturamento))
    print("Quantidade de saídas:", saidas)

    # Sem saídas não dá pra dividir: a média fica 0
    if saidas > 0:
        media = faturamento / saidas
    else:
        media = 0.0

    print("Média por saída:", formatar_moeda(media))


def mostrar_relatorio(entradas, saidas, ocupadas, faturamento):
    disponiveis = config.CAPACIDADE_MAXIMA - ocupadas

    print("\n--------------- RELATÓRIO GERAL ---------------")
    print("Total de entradas:", entradas)
    print("Total de saídas:", saidas)
    print("Carros no estacionamento:", ocupadas)
    print("Vagas disponíveis:", disponiveis)
    print("Total recebido:", formatar_moeda(faturamento))


def mostrar_tabela_precos():
    print("\n--------------- TABELA DE PREÇOS ---------------")
    print("Tarifa por hora:", formatar_moeda(config.TARIFA_POR_HORA))

    for horas in range(1, 6):
        valor = calcular_cobranca(horas)
        print(horas, "hora(s):", formatar_moeda(valor))