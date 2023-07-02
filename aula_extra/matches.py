# def matchesPattern(s, pattern):
#    # Complete 
#     s = s.lower()
#     pattern = pattern.lower()
#     for c in s:
#         for l in pattern:
#             if l == '?':
#                 continue
#             elif c == l:
#                 return True
            
#     return False

def matchesPattern(s, pattern):
    # Complete 
    s = s.lower()
    pattern = pattern.lower()
    for c in s:
        for l in pattern:
            if l == '?':
                continue
         #Match caracter from s with caracter from pattern
            elif c == l:
                return True
            else:
                return False