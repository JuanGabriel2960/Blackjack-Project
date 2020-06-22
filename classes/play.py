#Since I make use of class inheritance, I proceed to link both documents using the modules.
from classes.pack import Pack

#The 'Play' class is responsible for creating, delivering and adding player cards.
class Play(Pack):
    #The 'sum' variable will be in charge of adding the total value of the cards.
    sum = 0

    #The 'deliver_card' method delivers the cards to the players.
    def deliver_card(self):
        self.find.append(str(self.pack[0])+str(self.shapes_pack[0]))
        if(self.pack[0] in ["J","Q","K"]):
            #If the card is a 'J,Q,K' it will proceed to be worth 10.
            self.sum = self.sum + 10
        elif(self.pack[0] in ["A"]):
            #If the card is a 'A' it will proceed to be worth 11.
            self.sum = self.sum + 11
        else:
            #Otherwise it will proceed to what its number indicates.
            self.sum = self.sum + self.pack[0]
        #Proceed to print the arrangement of the cards found complete.
        print(str(self.find)[1:-1])
        print('Total value of cards: {}\n'.format(self.sum))
        #The cards you touch will proceed to be removed from the deck.
        self.pack.pop(0)
        self.shapes_pack.pop(0)

    # The 'count_card' method will keep the total value of the cards at bay to proceed to be evaluated.
    def count_card(self):
        return self.sum
        
        
        
        
        

    
        