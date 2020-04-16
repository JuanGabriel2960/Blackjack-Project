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