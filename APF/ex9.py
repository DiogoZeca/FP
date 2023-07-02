def numberOfDigits(n):
	if n//10 < 10 and n%10 != 0:
		digits = 1
	else:
		digits = 1 + numberOfDigits(n//10)
	return digits

print(numberOfDigits(12345678910))