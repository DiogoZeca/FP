"""
Numa autoestrada com portagens automáticas, os automóveis pagam consoante as portagens por onde passam. O programa define um dicionário custos com os custos de cada portagem de uma autoestrada e importa as variáveis pass1, pass2, pass3, que têm registos de passagens de automóveis pelas várias portagens, com um formato semelhante ao abaixo.

pass1 = [('Gaia', 'HW-78-55'), ('Gaia', '41-TL-68'), ...]
Complete a função custoPorMatricula(custos, lst) que, dado o dicionário de custos das portagens e uma lista de passagens em portagens, crie e devolva um dicionário que associe a cada matrícula o custo total do seu trajeto.

Para fazer isso, pode invocar as funções custoTrajeto e trajetoPorMatricula, soluções dos exercícios anteriores, que estão disponíveis aqui.

Observe os exemplos de chamadas na função main e execute para conferir os resultados esperados.
"""

def custoTrajeto(custos, T):
	if len(T) == 0:
		return 0
	elif T[0] in custos:
		return custos[T[0]] + custoTrajeto(custos, T[1:])
	else:
		return 0.10 + custoTrajeto(custos, T[1:])

def trajetoPorMatricula(lst):
    newDict = {}
    for t in lst:
        matricula = t[1]
        portagem = t[0]
        if matricula not in newDict:
            newDict[matricula] = []
        newDict[matricula].append(portagem)
    return newDict

def custoPorMatricula(custos, lst):
	newDict = trajetoPorMatricula(lst)
	for k in newDict.keys():
		newDict[k] = custoTrajeto(custos, newDict[k])
	return newDict