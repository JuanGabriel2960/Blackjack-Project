#The money class declares as initial money 1000 and depending on the result obtained proceeds to add or subtract
class Money:
	money = 1000
		
	def bet_money(self,bet,win):
		if win:
			self.money+=bet
			print("Current money: $",self.money)
		else:
			self.money-=bet
			print("Remaining money: $",self.money)