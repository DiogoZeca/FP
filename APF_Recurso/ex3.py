"""
Imagine que pediu um empréstimo de 1000.00 € e o banco cobra-lhe uma taxa de juro de 1% por mês. Tem de pagar a dívida em prestações mensais fixas, mas pode escolher o valor da prestação, desde que seja superior ao juro no primeiro mês.

Complete o programa para pedir o valor da prestação e mostrar uma tabela com o juro, a prestação paga e a dívida no fim de cada mês, como no exemplo seguinte.

Prestação? 300
Mes      Juro Prestação    Divida
  1     10.00    300.00    710.00
  2      7.10    300.00    417.10
  3      4.17    300.00    121.27
  4      1.21    122.48      0.00
Note que:

O valor da prestação tem de ser superior ao valor do juro no primeiro mês. Se não for, o programa deve mostrar um erro e voltar a pedir, como mostra o Test 1.
O juro em cada mês resulta da multiplicação da taxa pela dívida no início do mês. Por exemplo, no mês 1, o juro é 0.01 \times 1000.00 = 10.00, no mês 2, é 0.01 \times 710.00 = 7.10.
A dívida no fim do mês obtém-se adicionando o juro à dívida anterior e subtraindo a prestação. Por exemplo no mês 1, a dívida é 1000.00 + 10.00 - 300.00 = 710.00.
A prestação é sempre a mesma, excepto quando supera a dívida e juro em falta. Nesse último mês, a prestação deve ser a necessária para anular a dívida. No exemplo acima, a última prestação é 121.27 + 1.21 = 122.48.
O programa termina quando a dívida for anulada.
Tente respeitar o formato da tabela (cabeçalho, casas decimais e alinhamento das colunas).
"""

divida = 1000.00
taxa = 0.01

# Aproveite esta instrução:
prestacao = float(input("Prestação?\n"))

while prestacao <= divida * taxa:
	prestacao = float(input("Prestação?\n"))

print('{:>10} {:>5} {:>15} {:>6}'.format("Mês", "Juro", "Prestação", "Divida"))

mes = 1

while divida > 0:
	juro = divida * taxa
	dividaMensal = divida + juro - prestacao

	if dividaMensal <= 0:
		dividaMensal = 0
		prestacao = divida + juro
	
	print('{:>10} {:>5.2f} {:>15.2f} {:>6.2f}'.format(mes, juro, prestacao, dividaMensal))

	divida -=  prestacao - juro
	mes += 1
