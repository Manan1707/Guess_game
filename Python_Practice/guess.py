import random 
num = random.randint(1,100)
print('This is guessing game!')
print('In this game you have to guess the number between 1 to 100')
print('If your guess number is more than 10 then i will tell you COLD!')
print('If your guess number is within the 10 then I will tell you WARM!')
print('If your guess number is closer to the previous guess number then I will tell you COLDER!')
print('If your guess number is farther from the previous guess number then I will tell you WARMER!')
guesses = [0]
while true:
	guess = int(input('I am thinking of a number between 1 to 100 what is your guess ?'))
	if guess<1 or guess > 100 :
		print('Out of bounds! Please try again')
		continue
	if guess == num :
		print(f'Congratulations, You Guessed it in only{len(guesses)} GUESSES!')
		break
	guesses.append(guess)

	if guesses[-2]:
		if abs(num - guess) < abs(num-guesses[-2]):
			print('WARMER')
		else:
			print('COLDER')
	else:
		if abs(num-guess)<=10:
			print('WARM')
		else:
			print('COLD')
