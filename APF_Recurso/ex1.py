#Complete a função hyphenate(S) para devolver uma string com hífenes introduzidos entre cada duas letras da string S. Por exemplo, hyphenate("abra") deve devolver "a-b-r-a". A solução tem de ser recursiva e não pode usar ciclos nem os métodos str.join ou str.replace.

#SHOW #ID: 

def hyphenate(s):
	if len(s) <= 1:
		return s
	else:
		return s[0] + "-" + hyphenate(s[1:])

print(hyphenate(''))