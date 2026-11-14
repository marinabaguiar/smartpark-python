# movimentacao.py
# Entrada e saída de veículos.
# Sem contador global: tudo chega por parâmetro e volta por return.

from config import CAPACIDADE_MAXIMA as TOTAL_VAGAS, HORA_ABERTURA, HORA_FECHAMENTO
import financeiro as fin


def dentro_do_horario():
    # Pergunta a hora atual (0 a 23) e diz se o estacionamento está aberto
    hora = -1
    while hora < 0 or hora > 23:
        texto = input("Hora atual (0 a 23): ")
        try:
            hora = int(texto)
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")
            hora = -1
        else:
            if hora < 0 or hora > 23:
                print("Hora inválida! Digite um valor entre 0 e 23.")
    return HORA_ABERTURA <= hora < HORA_FECHAMENTO


def registrar_entrada(ocupadas, entradas):
    # Lotado: impede a entrada e não altera nada
    if ocupadas >= TOTAL_VAGAS:
        print("Estacionamento lotado! Entrada recusada.")
        return ocupadas, entradas

    # Fora do horário: impede a entrada e não altera nada
    if not dentro_do_horario():
        print(f"Estacionamento fechado! Funcionamos das {HORA_ABERTURA}h às {HORA_FECHAMENTO}h.")
        return ocupadas, entradas

    # Há vaga e está aberto: atualiza os dois contadores
    ocupadas = ocupadas + 1
    entradas = entradas + 1

    print("Entrada registrada com sucesso!")
    print(f"Vagas disponíveis: {TOTAL_VAGAS - ocupadas}")
    return ocupadas, entradas


def registrar_saida(ocupadas, saidas, faturamento):
    # Sem veículo estacionado, não existe saída
    if ocupadas <= 0:
        print("Não há veículos estacionados. Saída recusada.")
        return ocupadas, saidas, faturamento

    # Repete até receber um número inteiro positivo
    horas = 0
    horas_validas = False
    while not horas_validas:
        texto = input("Tempo de permanência (horas inteiras): ")
        try:
            horas = int(texto)
        except ValueError:
            print("Valor inválido! Digite apenas números inteiros (ex: 2).")
        else:
            if horas <= 0:
                print("Valor inválido! O tempo deve ser maior que zero.")
            else:
                horas_validas = True
        finally:
            print()  # linha em branco, roda sempre

    # Saída válida: calcula o valor (a tarifa e o mínimo estão no financeiro)
    valor = fin.calcular_cobranca(horas)

    ocupadas = ocupadas - 1
    saidas = saidas + 1
    faturamento = faturamento + valor

    print("---- COMPROVANTE DE SAÍDA ----")
    print(f"Permanência: {horas} hora(s)")
    print(f"Total a pagar: {fin.formatar_moeda(valor)}")
    print("-----------------------------------")
    return ocupadas, saidas, faturamento