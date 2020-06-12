#The 'Money' class will be in charge of evaluating the bet coins and checking if they rise or fall.
class Money:
    #The variable 'money' declares the initial amount of chips.
	money = 1000
	
	#The 'ber_money' method checks the amount wagered and whether the player wins or loses money.
	def bet_money(self,bet,win):
		#The game pays at a ratio of 2:1 which means you win twice what you bet.
		if win:
			self.money+=bet
			print("Current money: $",self.money)
		else:
			self.money-=bet
			print("Remaining money: $",self.money)