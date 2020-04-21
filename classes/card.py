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