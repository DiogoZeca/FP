"""
Numa autoestrada com portagens automáticas, os automóveis pagam consoante as portagens por onde passam. O programa define um dicionário custos com o custo de cada portagem de uma autoestrada.

Crie uma função custoTrajeto(custos, T) que calcule o custo total de um trajeto T, indicado por uma sequência de portagens. Se o trajeto tiver portagens desconhecidas, deve considerar que essas têm um custo fixo de 0.10 € cada.

Observe os exemplos de chamadas na função main e execute para conferir os resultados.
"""

def custoTrajeto(custos, T):
	if len(T) == 0:
		return 0
	elif T[0] in custos:
		return custos[T[0]] + custoTrajeto(custos, T[1:])
	else:
		return 0.10 + custoTrajeto(custos, T[1:])