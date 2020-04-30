class player:
	def __init__(self):
		self.find = []
#The "receive_card" method delivers the card to the player and stores it in the "find" array.
	def receive_card(self, accountant):
		self.find.append(accountant)
#The "show_find" method traces the arrangement of the cards found, shows them and adds their value.
	def show_find(self):
		for accountant in self.find:
			print(str(accountant.values_of_the_cards) + accountant.shapes_of_the_cards, end = " ")
		print("-> " + str(self.count_find()))
#The count_find add the numerical value of the cards and thus be able to compare it.
	def count_find(self):
		counter = 0

		for accountant in self.find:
				counter += accountant.get_value()
		return counter