# financeiro.py
# Responsável apenas pelo cálculo e formatação de valores. Não guarda contador nenhum.

from config import TARIFA_POR_HORA as VALOR_HORA, PERMANENCIA_MINIMA as COBRANCA_MINIMA_HORAS

def calcular_cobranca(horas):
    """Recebe as horas (inteiro) e devolve o valor da cobrança (float)."""
    # Cobrança mínima: qualquer permanência vale no mínimo 1 hora
    if horas < COBRANCA_MINIMA_HORAS:
        horas = COBRANCA_MINIMA_HORAS

    valor = horas * VALOR_HORA
    return valor

def formatar_moeda(valor):
    """Devolve o valor no formato brasileiro, ex.: R$ 15,00."""
    total_centavos = int(valor * 100 + 0.5)
    reais = total_centavos // 100
    centavos = total_centavos % 100
    return f"R$ {reais}, {centavos:02d}"
