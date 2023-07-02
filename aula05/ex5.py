
def countDigits(string):
    count = 0
    for c in string:
        if c.isdigit():
            count += 1
    print(count)

countDigits("23 mil 456")
