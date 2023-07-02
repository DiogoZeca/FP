# if C1[E] < Q:
# 	return 'NO-STOCK'

# if C2['EUR'] < stocks[E] * Q:
# 	return 'NO-MONEY'
	
# C1[E] = C1.get(E, 0) - Q
# C2[E] = C2.get(E, 0) + Q

# C1['EUR'] += stocks[E] * Q
# C2['EUR'] -= stocks[E] * Q

# return 'OK'