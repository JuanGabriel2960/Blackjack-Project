import random
import os

#The "player" class receives the name of the players.
class player:
	def __init__(self):
		self.find = []
#The "receive_card" method delivers the card to the player and stores it in the "find" array.
	def receive_card(self, accountant):
		self.find.append(accountant)
#The "show_find" method traces the arrangement of the cards found, shows them and adds their value.
	def show_find(self):
		for accountant in self.find:
			print(str(accountant.values) + accountant.shapes, end = " ")
		print("-> " + str(self.count_find()))
#The count_find method finding aces account to assign if the value will be 1 or 11.
	def count_find(self):
		counter = 0

		for accountant in self.find:
				counter += accountant.get_value()
		return counter
#The money class declares as initial money 1000 and depending on the result obtained proceeds to add or subtract
class Money:
	money = 1000
		
	def Bet_Money(self,bet,win):
		if (win == 0):
			self.money-=bet
			print("Remaining money: $",self.money)
		if (win == 1):
			self.money = self.money + bet
			print("Current money: $",self.money)

class CPU:
	def __init__(self):
		self.find = []
#The "receive_card" method delivers the card to the player and stores it in the "find" array.
	def receive_card(self, accountant):
		self.find.append(accountant)
#The "show_find" method traces the arrangement of the cards found, shows them and adds their value.
	def show_find(self):
		for accountant in self.find:
			print(str(accountant.values) + accountant.shapes, end = " ")
		print("-> " + str(self.count_find()))
#The count_find method finding aces account to assign if the value will be 1 or 11.
	def count_find(self):
		counter = 0

		for accountant in self.find:
				counter += accountant.get_value()
		return counter