from Controller import *

#The "card" class receives the form (S) and the value (V) of the cards as parameters.
class card:
	def __init__(self,s,v):
		self.shape = s
		self.value = v
#The "get_value" method assigns the numerical value to letters with letters and returns the value of the numerical letters.
	def get_value(self):
		if(self.value in ["J","Q","K"]):
			return 10
		if(self.value in ["A"]):
			return 11
		return self.value

#The "pack" class combines the value of the cards and their form and groups them in the "pack" arrangement.
class pack:
	def __init__(self):
		self.pack = []
		for shape in ['♥','♦','♣','♠']:
			for value in range(2,11):
				self.pack.append(card(shape,value))
			for value in ["J","Q","K","A"]:
				self.pack.append(card(shape,value))
		random.shuffle(self.pack)
#The show_pack method, traces each element (card) of the "pack" arrangement.
	def show_pack(self):
		for c in self.pack:
			print(str(c.value) + c.shape)
#The "give_one_card" method give a card to the player and proceed to remove it from the pack.
	def give_one_card(self, p):
		p.receive_card(self.pack[0])
		self.pack.remove(h.pack[0])

Chip = Money()

print("$1 min - $5,000 max / To keep playing at the table")

while(Chip.money > 0 and Chip.money < 5000 ):
	#Build the "hand" object of the "pack" class.
	h = pack()

	print("------------------------------------------------------------------------------------------------------------------")
	print("\nCroupier cards\n")

	#Build the first player and proceed to deliver 2 cards.
	CR = CPU()
	h.give_one_card(CR)

	#The 2 cards are shown.
	CR.show_find()

	#The user is asked how much they want to bet.
	while(True):
		try:
			print(" ")
			Bet=int(input("How much do you want to bet?: "))
			if Bet < 1 or Bet > Chip.money:
				raise ValueError 
			break
		except:
			print("Error!")

	print("Remaining money: $",Chip.money - Bet)

	print("\nPlayer cards\n")

	#Build the first player and proceed to deliver 2 cards.
	p = player()
	h.give_one_card(p)
	h.give_one_card(p)

	#The 2 cards are shown.
	p.show_find()

	#The player is asked to ask for request a card or stand.
	while(p.count_find() < 21):
		
		while (True):
			try:
				print("\nWhat would you like to do?")
				print("1-Request a card")
				print("2-Stand")
				Answer = int(input())
				print(" ")
				if Answer < 1 or Answer > 2:
					raise ValueError
				break
			except:
				print("Error!")
		#If the answer is 1, another card is given to the player.
		if(Answer == 1):
			h.give_one_card(p)
			p.show_find()
		#If the answer is 2, the player stands and the remaining cards are given to the Croupier.
		if(Answer == 2):
			h.give_one_card(CR)
			CR.show_find()
			#As long as the dealer's cards total less than 16, he must ask for another.
			while (CR.count_find()<=16):
				h.give_one_card(CR)
				CR.show_find()
			#If the dealer's cards are greater than the player's, but at the same time less than or equal to 21, he wins.
			if CR.count_find() > p.count_find() and CR.count_find() <= 21:
				print("Dealer wins")
			#The "Bet_Money" function is called with the Boolean parameter 0 to indicate that the player lost.
				Chip.Bet_Money(Bet,0)
				break
			else:
			#The "Bet_Money" function is called with the Boolean parameter 1 to indicate that the player won,
				print("Player wins")
				Chip.Bet_Money(Bet,1)
				break
	#If the player does not get to stand at any time and automatically goes over 21, the dealer wins.
	if (p.count_find() > 21):
		print("Dealer wins")
		Chip.Bet_Money(Bet,0)
	#If the player does not get to stand at any time, but adds 21 he has blackjack and automatically wins.
	elif (p.count_find() == 21):
		print("Blackjack! The player wins")
		Chip.Bet_Money(Bet,1)
		
#If the player's chips run out, he must leave the table and end the game.
if (Chip.money < 1):
	print("\nInsufficient chip, must leave the table")
else:
#If the player's coins exceed the maximum allowed, he must leave the table and end the game.
	print("\nMaximum chip for this table")