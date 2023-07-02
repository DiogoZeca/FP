def ispalindrome(s):
    s = s.lower()
    s = s.replace(" ","")
    dif = s[::-1]
    if (dif == s):
        print(True)
    else: 
        print(False)
    
ispalindrome("subi no onibus")
