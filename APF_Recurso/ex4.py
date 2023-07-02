"""
Hamilton
O Método de Hamilton permite fazer a repartição de deputados eleitos para uma assembleia de forma proporcional aos votos de cada partido. Considerando que V_i é o número de votos obtidos pelo partido i, o método determina o número N_i de lugares a atribuir a esse partido.

O método começa por aplicar uma regra da proporcionalidade para obter a quota ideal de deputados,

Q_i = V_i * N/V,

onde N é o número total de deputados a eleger e V = \sum V_i é o número total de votos expressos.

Depois, atribui-se os deputados iniciais segundo as partes inteiras dessas quotas.

N_i = \lfloor Q_i \rfloor

Os lugares que sobrarem (N - \sum N_i) são distribuídos igualmente pelos partidos que têm quotas Q_i com as maiores partes decimais. Em caso de igualdade das partes decimais, favorece-se o partido mais votado.

Por exemplo, para distribuir N = 6 lugares por quatro partidos que tiveram as votações [7000, 12000, 6000, 5000] o processo deve seguir os passos abaixo.

Votos:     [7000, 12000, 6000, 5000]
Quotas:    [1.4,  2.4,   1.2,  1.0 ]
N inicial: [1,    2,     1,    1   ]  Total: 5  Falta: 1
P decimal: [0.4,  0.4,   0.2,  0.0 ]
N final:   [1,    3,     1,    1   ]
Note que depois da atribuição inicial, falta atribuir um deputado. Como há dois partidos com a parte decimal mais alta, atribui-se o lugar ao partido mais votado. (É possível usar os quocientes e restos de divisões inteiras para evitar números reais.)

Implemente uma função hamilton(votes, numseats) que, dada uma lista com os números de votos em cada um partidos e dado o número de lugares disponíveis, calcule e devolva uma lista com a repartição de deputados para cada partido. Por exemplo, hamilton([7000, 12000, 6000, 5000], 6) deve devolver [1, 3, 1, 1].
"""

def hamilton(votes, numseats):
	quotas = [round(v * (numseats / sum(votes)), 1) for v in votes]
	seats = [int(q) for q in quotas]
	decimal = [round(q - int(q), 1) for q in quotas]
	while sum(seats) < numseats:
		max_decimal = max(decimal)
		max_decimal_indexes = [i for i, x in enumerate(decimal) if x == max_decimal]
		max_index = max(max_decimal_indexes, key=lambda x: votes[x])

		seats[max_index] += 1
		decimal[max_index] = 0
	return seats

print(hamilton([7000, 12000, 6000, 5000], 6))