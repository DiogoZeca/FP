def Surname():
    with open("names.txt", "r") as f:
        for line in f:
            name = [line.split()[-1] for line in f]
            for i in name:
                if i != name:
                    print(i)
Surname()

