def score(guess, secret):
	assert len(guess) == len(secret)

	bulls = 0
	cows = 0

	secretListTemp = list(secret)

	for i in range(len(guess)):
		if secret[i] == guess[i]:
			bulls += 1
			secretListTemp[i] = "DELETED"
					
	secretList = [e for e in secretListTemp if e != "DELETED"]

	for i in range(len(guess)):
		if guess[i] in secretList:
			cows += 1
			secretList.remove(guess[i])
			
	return (bulls, cows)
#	used = set()


#	for i in range(len(guess)):
#	   if secret[i] == guess[i]:
#		  bulls += 1
#		  used.add(guess[i])
#	   elif guess[i] in secret and guess[i] not in used:
#		  cows += 1
#		  used.add(guess[i])
#	return (bulls, cows)
print(score('ooooo', 'algoo'))
