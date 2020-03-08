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

while(True):
	#Build the "hand" object of the "pack" class.
	h = pack()

	print("------------------------------------------------------------------------------------------------------------------")
	print(" ")
	print("Croupier cards")
	print(" ")

	#Build the first player and proceed to deliver 2 cards.
	CR = CPU()
	h.give_one_card(CR)

	#The 2 cards are shown.
	CR.show_find()

	#The user is asked how much they want to bet.
	print(" ")
	Bet=int(input("How much do you want to bet?: "))
	print("Remaining money: $",Chip.money - Bet)

	print(" ")
	print("Player cards")
	print(" ")

	#Build the first player and proceed to deliver 2 cards.
	p = player()
	h.give_one_card(p)
	h.give_one_card(p)

	#The 2 cards are shown.
	p.show_find()

	#The player is asked to ask for request a card or stand.
	while(p.count_find() < 21):
		print(" ")
		print("What would you like to do?")
		print("1-Request a card")
		print("2-Stand")
		Answer = int(input())
		print(" ")
		if(Answer == 1):
			h.give_one_card(p)
			p.show_find()
		if(Answer == 2):
			h.give_one_card(CR)
			CR.show_find()
			while (CR.count_find()<=16):
				h.give_one_card(CR)
				CR.show_find()
			if CR.count_find() > p.count_find() and CR.count_find() < 21:
				print("Dealer wins")
				Chip.Bet_Money(Bet,0)
				break
			else:
				print("Player wins")
				Chip.Bet_Money(Bet,1)
				break

	if (p.count_find() > 21):
		print("Dealer wins")
		Chip.Bet_Money(Bet,0)
	elif (p.count_find() == 21):
		print("Blackjack! The player wins")
		Chip.Bet_Money(Bet,1)