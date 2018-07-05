#!/usr/bin/env python

## Riddler: https://fivethirtyeight.com/features/what-are-the-odds-world-cup-teams-play-each-other-twice/

## 2018-7-3

## Joseph Hostyk

import itertools
import collections

###################################################################################################

### Original:

###################################################################################################


def getAllCombinations(numDigits, passwordLength):

	permuter = itertools.product(range(numDigits), repeat=passwordLength)
	return ["".join([str(i) for i in Tuple]) for Tuple in permuter]

def getAllGuesses(numDigits, passwordLength, requiredPressesForNonOverFlowSolution):
	return itertools.chain.from_iterable(itertools.product(range(numDigits), repeat = presses) for presses in range(passwordLength,requiredPressesForNonOverFlowSolution))


def checkAguess(guessSolution, allPossible):

	guessSolutionDeque = collections.deque(str(guessSolution))
	firstChunk = [guessSolutionDeque.popleft() for i in range(passwordLength-1)]
	currentPasswordDeque = collections.deque(firstChunk, maxlen = passwordLength)
	while len(allPossible) > 0 and len(guessSolutionDeque) > 0:
		currentPasswordDeque.append(guessSolutionDeque.popleft())
		currentPassword = "".join(i for i in currentPasswordDeque)
		if currentPassword in allPossible:
			allPossible.pop(allPossible.index(currentPassword))
	if len(allPossible) == 0:
		return guessSolution
	return None

def bruteAllGuesses(numDigits, passwordLength):

	requiredPressesForNonOverFlowSolution = (numDigits ** passwordLength)*numDigits
	allPossiblePasswords = getAllCombinations(numDigits, passwordLength)
	for guess in getAllGuesses(numDigits, passwordLength, requiredPressesForNonOverFlowSolution):
		guess = "".join([str(i) for i in guess])
		print "current guess:", guess
		allPossibleCopy = [password for password in allPossiblePasswords]
		solution = checkAguess(guess, allPossibleCopy)
		if solution:
			print "Shortest solution:", guess
			break


if __name__ == '__main__':
	
	numDigits = 2
	passwordLength = 4
	bruteAllGuesses(numDigits, passwordLength)

