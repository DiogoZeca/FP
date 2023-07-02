# Given a string s and a string t, return a string in which all the characters 
# of s that occur in t have been replaced by a _ sign. The comparisons are 
# case sensitive.


def replaceCharactersWithUnderscores(s, t):
   for i in range(len(s)):
      for j in range(len(t)):
         if s[i] == t[j]:
            s = s.replace(s[i], "_")
   return s