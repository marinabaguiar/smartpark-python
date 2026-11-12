# main.py
# Menu principal e controle da execução do SmartPark.
# É o único arquivo executável. Aqui ficam as variáveis de estado.


import movimentacao
import relatorios as rel


# ---------- ESTADO DO SISTEMA ----------
# Só existem aqui. Os outros arquivos recebem por parâmetro e devolvem por return.
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
           # Resumo final antes de encerrar
           print("Encerrando o SmartPark. Resumo final:")
           print("Total de entradas:", total_entradas)
           print("Total de saídas:", total_saidas)
           print(f"Faturamento: R$ {faturamento:.2f}")
           print("Até logo!")
           break
       case _:
           print("Opção inválida! Escolha um número do menu.")