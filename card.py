#The "card" class receives the form (S) and the value (V) of the cards as parameters.
class card:
	def __init__(self,shape,value):
		self.shapes_of_the_cards = shape
		self.values_of_the_cards = value
#The "get_value" method assigns the numerical value to letters with letters and returns the value of the numerical letters.
	def get_value(self):
		if(self.values_of_the_cards in ["J","Q","K"]):
			return 10
		if(self.values_of_the_cards in ["A"]):
			return 11
		return self.values_of_the_cards