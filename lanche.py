dias = 1
valor = 0
total = 0

while dias <= 5:
      valor = float(input('qual o valor gasto?'))
      total = total + valor
      dias = dias + 1

print('o valor total e: {:.2f}' .format(total))

