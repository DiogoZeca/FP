def shorten(text):
    lst = ""
    for i in range(len(text)):
        if text[i].isupper():
            lst += text[i]
        else:
            lst += ""
    print(lst)
shorten("Ola Amigo")
