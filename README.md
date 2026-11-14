# SmartPark - Sistema de Estacionamento

O SmartPark é um sistema de estacionamento desenvolvido em Python. Ele permite registrar a entrada e a saída de veículos, acompanhar a ocupação das vagas e consultar o faturamento do estacionamento.

O programa possui um menu principal com as opções disponíveis. Por ele, o usuário consegue realizar os registros e consultar as informações do estacionamento.

Projeto da disciplina de Programação em Linguagem Estruturada (Unifacisa).

## Funcionalidades

- Registrar a entrada de veículos, com controle de lotação e do horário de funcionamento
- Registrar a saída de veículos, com cálculo da cobrança e comprovante
- Consultar as vagas disponíveis e a taxa de ocupação
- Consultar o faturamento (total, número de saídas e média por saída)
- Exibir o relatório geral de movimentações
- Consultar a tabela de preços (simulação de 1 a 5 horas)
- Encerrar o sistema com um resumo final

## Informações do estacionamento

- Capacidade máxima: 20 veículos
- Valor por hora: R$ 5,00
- Horário de funcionamento: das 06h às 22h (o operador informa a hora atual a cada entrada)
- Tempo mínimo cobrado: 1 hora

## Organização dos arquivos

O código está distribuído em cinco arquivos, cada um com uma parte do funcionamento do sistema:

- `main.py`: inicia o programa, mostra o menu e chama as funções dos outros arquivos. É onde ficam os contadores do sistema.
- `config.py`: contém as configurações utilizadas no estacionamento, como capacidade, valor da hora e horário de funcionamento.
- `movimentacao.py`: realiza os registros de entrada e saída dos veículos e valida os dados digitados.
- `financeiro.py`: calcula o valor a ser pago de acordo com o tempo de permanência e formata os valores em reais.
- `relatorios.py`: apresenta informações sobre vagas ocupadas, faturamento e tabela de preços.

## Requisitos

- Python 3.10 ou superior (o projeto usa `match...case`)
- Nenhuma biblioteca externa

## Como executar

Com o projeto aberto no computador, basta executar o arquivo `main.py`:

```bash
python main.py
```

## Integrantes

- Marina Xavier Barbosa Aguiar
- Danielle Stefhane dos Santos Ataide
- Jhonata Lopes Bezerra de Araújo

## Divisão de responsabilidades

- Marina: `main.py` e `config.py`
- Jhonata: `movimentacao.py` e `financeiro.py`
- Danielle: `relatorios.py` e `README.md`
