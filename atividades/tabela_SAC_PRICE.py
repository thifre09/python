import pandas as pd

meses = int(input("Digite a quantidade de parcelas: "))
valor_emprestado = float(input("Digite o valor emprestado: "))
porcentagem = float(input("Digite a porcentagem de juros: "))

amortizacao_sac = valor_emprestado / meses
saldo_sac = valor_emprestado
total_sac = valor_emprestado

pmt = valor_emprestado * ((1 + porcentagem / 100) ** meses * (porcentagem / 100)) / ((1 + porcentagem / 100) ** meses - 1)
saldo_price = valor_emprestado
total_price = valor_emprestado

sac = []
price = []

print("")
print("Tabela SAC")

for i in range(1, meses + 1):
    juros_sac = saldo_sac * (porcentagem / 100)
    parcela_sac = amortizacao_sac + juros_sac
    saldo_devedor_sac = saldo_sac - amortizacao_sac
    total_sac += juros_sac

    sac.append({
        "Mês": i,
        "Dívida": saldo_sac,
        "Amortização": amortizacao_sac,
        "Juros": juros_sac,
        "Parcela": parcela_sac,
        "Saldo Devedor": saldo_devedor_sac
    })

    saldo_sac = saldo_devedor_sac

    juros_price = saldo_price * (porcentagem / 100)
    amortizacao_price = pmt - juros_price
    saldo_devedor_price = saldo_price - amortizacao_price
    total_price += juros_price

    price.append({
        "Mês": i,
        "PMT": pmt,
        "Juros": juros_price,
        "Amortização": amortizacao_price,
        "Saldo Devedor": saldo_devedor_price
    })

    saldo_price = saldo_devedor_price

df = pd.DataFrame(sac)
pd.options.display.float_format = "{:.2f}".format
print(df.to_string(index=False))
print("Valor total pago no SAC: {:.2f}".format(total_sac))

print("")
print("Tabela PRICE")

df = pd.DataFrame(price)
pd.options.display.float_format = "{:.2f}".format
print(df.to_string(index=False))
print("Valor total pago no PRICE: {:.2f}".format(total_price))

# Grupo: Thiago Freitas, Lucas de Souza, Silas de Freitas, Caio de Souza