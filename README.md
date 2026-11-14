# SmartPark - Sistema de Estacionamento

O SmartPark é um sistema de estacionamento desenvolvido em Python. Ele permite registrar a entrada e a saída de veículos, acompanhar a ocupação das vagas e consultar o faturamento do estacionamento.

O programa possui um menu principal com as opções disponíveis. Por ele, o usuário consegue realizar os registros e consultar as informações do estacionamento.

## Informações do estacionamento

- Capacidade máxima: 20 veículos
- Valor por hora: R$ 5,00
- Horário de funcionamento: das 06h às 22h
- Tempo mínimo cobrado: 1 hora

## Organização dos arquivos

O código está distribuído em cinco arquivos, cada um com uma parte do funcionamento do sistema:

- `main.py`: inicia o programa, mostra o menu e chama as funções dos outros arquivos.
- `config.py`: contém as configurações utilizadas no estacionamento, como capacidade e valor da hora.
- `movimentacao.py`: realiza os registros de entrada e saída dos veículos.
- `financeiro.py`: calcula o valor a ser pago de acordo com o tempo de permanência.
- `relatorios.py`: apresenta informações sobre vagas ocupadas, faturamento e tabela de preços.

## Como executar

Para utilizar o sistema, é necessário ter o Python instalado.

Com o projeto aberto no computador, basta executar o arquivo `main.py`:

```bash
python main.py
```

## Integrantes

- Marina Xavier Barbosa Aguiar
- Danielle Stefhane dos Santos Ataide
- Jhonata Lopes