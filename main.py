#Import the classes stored in the different modules of the main package.
from classes.greeting import Greeting
from classes.pack import Pack
from classes.play import Play
from classes.money import Money

#Import python own modules to clean screen and add delay for each play.
import time
import os

os.system("cls")

player_name = str(input('Enter player name: '))
os.system("cls")

#Create the 'player' object belonging to the 'Greeting' class through which it will get the name by parameter.
player = Greeting(player_name)
player.greet()

print('1-Yes, I want to read the rules of the game')
print('2-No, I know how to play\n')
read_rules = int(input())

player.read(read_rules)
next=(input('Press enter to continue: '))
os.system("cls")

chip = Money()

#The basic rules are established to continue playing that are nothing more than complying with that interval of coins.
while(chip.money > 0 and chip.money < 5000 ):

	print('\n$1 min - $5,000 max / To keep playing at the table')
	print('Current money: $',chip.money)

	print('------------------------------------------------------------------------------------------------------------------------')
	print('\nCroupier cards\n')

	#Build the 'CPU' player and proceed to deliver 1 cards.
	CPU = Play()
	CPU.deliver_card()
	
	#The user is asked how much they want to bet.
	while(True):
		try:
			player_bet=int(input('\nHow much do you want to bet?: '))
			if type(player_bet) != int:
				raise ValueError
			if player_bet < 1 or player_bet > chip.money:
				raise TypeError 
			break
		except (ValueError):
			print('Enter a numeric value (●__●)')
		except (TypeError):
			if player_bet < 1:
				print('Enter a positive value (●__●)')
			if player_bet > chip.money:
				print('Enter a lower bet (●__●)')

	print('Remaining money: $',chip.money - player_bet)

	print('\nPlayer cards\n')

	#Build the 'player' and proceed to deliver 2 cards.
	player = Play()
	player.deliver_card()
	player.deliver_card()

	#The player is asked to ask for request a card or stand.
	while(player.count_card() < 21):
		#Validated by 'try' that the player's answer is correct.
		while (True):
			try:
				print('What would you like to do?')
				player_answer = int(input('1-Request a card / 2-Stand: '))
				print('\n')
				if type(player_answer) != int:
					raise ValueError
				if player_answer < 1 or player_answer > 2:
					raise TypeError 
				break
			except (ValueError):
				print('\nEnter a numeric value ಠ_ಠ\n')
			except (TypeError):
				print('\nEnter a value between 1 or 2 ಠ_ಠ\n')

		#If the answer is 1, another card is given to the player.
		if(player_answer == 1):
			time.sleep(1)
			player.deliver_card()
		#If the answer is 2, the player stands and the remaining cards are given to the Croupier.
		if(player_answer == 2):
			time.sleep(2)
			CPU.deliver_card()
			#As long as the dealer's cards total less than 16, he must ask for another.
			while (CPU.count_card()<=16):
				time.sleep(2)
				CPU.deliver_card()
			#If the dealer's cards are greater than the player's, but at the same time less than or equal to 21, he wins.
			if CPU.count_card() > player.count_card() and CPU.count_card() <= 21:
				print('\nDealer wins (ᴗ˳ᴗ)')
			#The "bet_money" function is called with the Boolean parameter 'False' to indicate that the player lost.
				chip.bet_money(player_bet,False)
				break
			else:
			#The "bet_money" function is called with the Boolean parameter 'True' to indicate that the player won.
				print('\nPlayer wins (ง^ᗜ^)ง')
				chip.bet_money(player_bet,True)
				break
	#If the player does not get to stand at any time and automatically goes over 21, the dealer wins.
	if (player.count_card() > 21):
		print('\nDealer wins (ᴗ˳ᴗ)')
		chip.bet_money(player_bet,False)
	#If the player does not get to stand at any time, but adds 21 he has blackjack and automatically wins.
	elif (player.count_card() == 21):
		print('\nBlackjack! The player wins (ง^ᗜ^)ง')
		chip.bet_money(player_bet,True)

	next_clear_console=(input('\nPress enter to continue: '))
	os.system("cls")
		
#If the player's chips run out, he must leave the table and end the game.
if (chip.money < 1):
	print('\nInsufficient chip, must leave the table (╥_╥)')
else:
#If the player's coins exceed the maximum allowed, he must leave the table and end the game.
	print('\nMaximum chip for this table, you win ฅ^•ﻌ•^ฅ')
