# Given a string s, return the longest prefix that is repeated somewhere else in the string. 
# For example, "abcdabejf" would return "ab" as "ab" starts at the beginning of the string
# and is repeated again later. Do not use the find method.

def longestPrefixRepeated(s):
   if len(s) == 0:
      return ''
   final = ''
   for i in range(len(s)):
      for j in range(i+1, len(s)):
         if s[i:j] in s[j:]:
            if len(s[i:j]) > len(final):
               final = s[i:j]

   return final
         
