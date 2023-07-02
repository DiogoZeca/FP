def countLetters(document):
    letters = {}
    with open (document, 'r') as f:
        for line in f:
            for letter in line:
                if letter != ' ' and letter != '\n':
                    if letter in letters:
                        letters[letter] += 1
                    else:
                        letters[letter] = 1
    return letters


def main():
    doc = input('Introduza o nome do ficheiro: ')
    order = (countLetters(doc))
    for i in sorted(order, key = order.get, reverse = True):  # type: ignore 
       print(i, order[i])
        
main()