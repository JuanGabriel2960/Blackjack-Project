from Controller import *
os.system("cls")

#The "card" class receives the form (S) and the value (V) of the cards as parameters.
class card:
	def __init__(self,shape,value):
		self.shapes = shape
		self.values = value
#The "get_value" method assigns the numerical value to letters with letters and returns the value of the numerical letters.
	def get_value(self):
		if(self.values in ["J","Q","K"]):
			return 10
		if(self.values in ["A"]):
			return 11
		return self.values

#The "pack" class combines the value of the cards and their form and groups them in the "pack" arrangement.
class pack:
	def __init__(self):
		self.pack = []
		for shapes in ['♥','♦','♣','♠']:
			for values in range(2,11):
				self.pack.append(card(shapes,values))
			for values in ["J","Q","K","A"]:
				self.pack.append(card(shapes,values))
		random.shuffle(self.pack)
#The show_pack method, traces each element (card) of the "pack" arrangement.
	def show_pack(self):
		for accountant in self.pack:
			print(str(accountant.values) + accountant.shapes)
#The "give_one_card" method give a card to the player and proceed to remove it from the pack.
	def give_one_card(self, player_1):
		player_1.receive_card(self.pack[0])
		self.pack.remove(hand.pack[0])

Chip = Money()

while(Chip.money > 0 and Chip.money < 5000 ):

	print("\n$1 min - $5,000 max / To keep playing at the table")
	print("Current money: $",Chip.money)

	#Build the "hand" object of the "pack" class.
	hand = pack()

	print("------------------------------------------------------------------------------------------------------------------")
	print("\nCroupier cards\n")

	#Build the first player and proceed to deliver 2 cards.
	Croupier = CPU()
	hand.give_one_card(Croupier)

	#The 2 cards are shown.
	Croupier.show_find()

	#The user is asked how much they want to bet.
	while(True):
		try:
			Bet=int(input("\nHow much do you want to bet?: "))
			if type(Bet) != int:
				raise ValueError
			if Bet < 1 or Bet > Chip.money:
				raise TypeError 
			break
		except (ValueError):
			print("Enter a numeric value")
		except (TypeError):
			if Bet < 1:
				print("Enter a positive value")
			if Bet > Chip.money:
				print("Enter a lower bet")

	print("Remaining money: $",Chip.money - Bet)

	print("\nPlayer cards\n")

	#Build the first player and proceed to deliver 2 cards.
	player_1 = player()
	hand.give_one_card(player_1)
	hand.give_one_card(player_1)

	#The 2 cards are shown.
	player_1.show_find()

	#The player is asked to ask for request a card or stand.
	while(player_1.count_find() < 21):
		
		while (True):
			try:
				print("\nWhat would you like to do?")
				print("1-Request a card")
				print("2-Stand")
				Answer = int(input())
				print(" ")
				if type(Answer) != int:
					raise ValueError
				if Answer < 1 or Answer > 2:
					raise TypeError 
				break
			except (ValueError):
				print("Enter a numeric value")
			except (TypeError):
				print("Enter a value between 1 or 2")

		#If the answer is 1, another card is given to the player.
		if(Answer == 1):
			hand.give_one_card(player_1)
			player_1.show_find()
		#If the answer is 2, the player stands and the remaining cards are given to the Croupier.
		if(Answer == 2):
			hand.give_one_card(Croupier)
			Croupier.show_find()
			#As long as the dealer's cards total less than 16, he must ask for another.
			while (Croupier.count_find()<=16):
				hand.give_one_card(Croupier)
				Croupier.show_find()
			#If the dealer's cards are greater than the player's, but at the same time less than or equal to 21, he wins.
			if Croupier.count_find() > player_1.count_find() and Croupier.count_find() <= 21:
				print("\nDealer wins")
			#The "Bet_Money" function is called with the Boolean parameter 0 to indicate that the player lost.
				Chip.Bet_Money(Bet,0)
				break
			else:
			#The "Bet_Money" function is called with the Boolean parameter 1 to indicate that the player won,
				print("\nPlayer wins")
				Chip.Bet_Money(Bet,1)
				break
	#If the player does not get to stand at any time and automatically goes over 21, the dealer wins.
	if (player_1.count_find() > 21):
		print("\nDealer wins")
		Chip.Bet_Money(Bet,0)
	#If the player does not get to stand at any time, but adds 21 he has blackjack and automatically wins.
	elif (player_1.count_find() == 21):
		print("\nBlackjack! The player wins")
		Chip.Bet_Money(Bet,1)

	Next=(input("\nPress enter to continue: "))
	os.system("cls")
		
#If the player's chips run out, he must leave the table and end the game.
if (Chip.money < 1):
	print("\nInsufficient chip, must leave the table")
else:
#If the player's coins exceed the maximum allowed, he must leave the table and end the game.
	print("\nMaximum chip for this table")