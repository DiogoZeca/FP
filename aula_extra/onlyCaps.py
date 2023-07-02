# def OnlyCaps(s):
#     str = ''
#     for i in s:
#         if i.isupper():
#             str += i
#     return str

#Recursive way

def OnlyCaps(s):
    if s == '':                             #Caso base, se tentarmos Onlycaps(''), vai dar ''
        return ''
    else:
        if s[0].isupper():                  #Se o primeiro caracter for maiusculo
            return s[0] + OnlyCaps(s[1:])   #Retorna o primeiro caracter + OnlyCaps do resto da string, sem a 1º letra, pq essa ja foi avaliada
        else:
            return OnlyCaps(s[1:])          #Senão retorna o OnlyCaps do resto da string, sem a 1º letra, pq essa ja era minuscula
        
        

        