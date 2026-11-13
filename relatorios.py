
import config


def mostrar_vagas(ocupadas):
    disponiveis = config.CAPACIDADE_MAXIMA - ocupadas
    porcentagem = ocupadas / config.CAPACIDADE_MAXIMA * 100

    print("\n--------------- VAGAS DO ESTACIONAMENTO ---------------")
    print("Vagas ocupadas:", ocupadas)
    print("Vagas disponíveis:", disponiveis)
    print("Ocupação do estacionamento: ", round(porcentagem, 1), "%")


def mostrar_faturamento(faturamento, saidas):
    print("\n--------------- RESUMO DO FATURAMENTO ---------------")
    print("Total recebido: R$", round(faturamento, 2))
    print("Quantidade de saídas:", saidas)

    if saidas > 0:
        media = faturamento / saidas
    else:
        media = 0

    print("Média por saída: R$", round(media, 2))


def mostrar_relatorio(entradas, saidas, ocupadas, faturamento):
    print("\n--------------- RELATÓRIO GERAL ---------------")
    print("Total de entradas:", entradas)
    print("Total de saídas:", saidas)
    print("Carros no estacionamento:", ocupadas)
    print("Total recebido: R$", round(faturamento, 2))


def mostrar_tabela_precos():
    print("\n--------------- TABELA DE PREÇOS ---------------")

    for horas in range(1, 6):
        valor = horas * config.TARIFA_POR_HORA
        print(horas, "hora(s): R$", round(valor, 2))
