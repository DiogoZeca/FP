def onlyCaps(s):
   # NOTE: ch.isupper() -> True if ch is uppercase.
   if s == '':
      return ''
   if s[0].isupper():
      return s[0] + onlyCaps(s[1:])
   return onlyCaps(s[1:])