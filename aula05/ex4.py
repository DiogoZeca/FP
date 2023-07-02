def allMatches(equipas):
    assert len(equipas) >= 2
    for i in equipas:
        for x in equipas:
            if i != x:
                print(i, x)


equipas = (["SLB", "FCP", "SCP"])
allMatches(equipas)


    
