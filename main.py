# main.py
# Aqui fica o menu principal do SmartPark e o que controla o programa.
# É o único arquivo que roda, os outros só são chamados por ele.

import movimentacao
import relatorios as rel
from financeiro import formatar_moeda

# ---------- ESTADO DO SISTEMA ----------
# O que o programa precisa lembrar enquanto está aberto.
# Os outros arquivos só recebem esses valores e devolvem atualizados.
vagas_ocupadas = 0
total_entradas = 0
total_saidas = 0
faturamento = 0.0

# ---------- MENU ----------
while True:
    print("=" * 40)
    print("      SMARTPARK - SISTEMA")
    print("=" * 40)
    print("1 - Registrar entrada de veículo")
    print("2 - Registrar saída de veículo")
    print("3 - Consultar vagas disponíveis")
    print("4 - Consultar faturamento")
    print("5 - Relatório de movimentações")
    print("6 - Consultar tabela de preços")
    print("0 - Encerrar sistema")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            vagas_ocupadas, total_entradas = movimentacao.registrar_entrada(
                vagas_ocupadas, total_entradas)
        case "2":
            vagas_ocupadas, total_saidas, faturamento = movimentacao.registrar_saida(
                vagas_ocupadas, total_saidas, faturamento)
        case "3":
            rel.mostrar_vagas(vagas_ocupadas)
        case "4":
            rel.mostrar_faturamento(faturamento, total_saidas)
        case "5":
            rel.mostrar_relatorio(total_entradas, total_saidas, vagas_ocupadas, faturamento)
        case "6":
            rel.mostrar_tabela_precos()
        case "0":
            # Mostra os totais antes de fechar o programa
            print("Encerrando o SmartPark. Resumo final:")
            print("Total de entradas:", total_entradas)
            print("Total de saídas:", total_saidas)
            print("Faturamento:", formatar_moeda(faturamento))
            print("Até logo!")
            break
        case _:
            print("Ops, essa opção não existe! Tenta um número do menu.")