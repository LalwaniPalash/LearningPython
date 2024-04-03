def main():
	card = None
	while card is None:
		try:
			card = int(input("Enter a card number: "))
			card = str(card)
		except ValueError:
			print("Invalid Input.")

	checksumBool = False
	cardDigits = [int(digit) for digit in card]
	reversedCardDigits = cardDigits[::-1]
	secondLastCardDigits = reversedCardDigits[1::2]
	sumSecondLastCardDigits = 0

	for i in secondLastCardDigits:
		n = i * 2
		if n > 9:
			n -= 9	
		sumSecondLastCardDigits += n

	remainingDigits = reversedCardDigits[0::2]
	sumRemainingCardDigits = 0
	for i in remainingDigits:
		sumRemainingCardDigits += i

	totalSumCardDigits = sumSecondLastCardDigits + sumRemainingCardDigits

	if totalSumCardDigits % 10 == 0:
		checksumBool = True
	else:
		pass

	if (checksumBool) and (len(card) == 15) and (cardDigits[0] == 3) and (cardDigits[1] == 4 or cardDigits[1] == 7):
		print("AMEX")
	elif (checksumBool) and (len(card) == 16) and (cardDigits[0] == 5) and (cardDigits[1] in [1, 2, 3, 4, 5]):
		print("MASTERCARD")
	elif (checksumBool) and (len(card) == 13 or len(card) == 16) and (cardDigits[0] == 4):
		print("VISA")
	else: 
		print("INVALID")

main()
