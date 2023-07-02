def evenThenOdd(string):
    # even = ''
    # odd = ''
    # for i in range(len(string)):
    #     if i % 2 == 0:
    #         even += string[i]
    #     else:
    #         odd += string[i]
    # print (even + odd)

    #-------OR----------#

    print(string[::2] + string[1::2])
evenThenOdd("abcd")


def outRepeat(string):
    newString = string[0]
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            newString += string[i]
    print (newString)
outRepeat("Mississippi")


def repeatNumbers(n):
    lst = []
    for i in range(n+1):
        lst += [i] * i
    print(lst)
repeatNumbers(4)


def indexMax(lst):
    maxindex = 0
    for i in range(len(lst)):
        if lst[i] > lst[maxindex]:
            maxindex = i
    print(maxindex)
indexMax([3, 5, 7, 2, 4, 6])
