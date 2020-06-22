#import python 'random' module to scramble the array of cards.
import random

#The 'Pack' class creates the deck of cards with all possible combinations and then proceeds to shuffle them.
class Pack:
    def __init__(self):
        #The 'pack' arrangement belongs to the possible numerical combinations of the cards.
        self.pack = []
        #The 'shapes_pack' arrangement belongs to the possible combinations of card shapes.
        self.shapes_pack = []
        #The pack arrangement belongs to the combined cards and is used to be displayed on the screen.
        self.find = []

        #In these nested loops all possible card combinations are created.
        for shapes_of_the_cards in ['♥','♦','♣','♠']:
            for values_of_the_cards in range(2,11):
                self.pack.append(int(values_of_the_cards))
                self.shapes_pack.append(str(shapes_of_the_cards))
            for values_of_the_cards in ["J","Q","K","A"]:
                self.pack.append(str(values_of_the_cards))
                self.shapes_pack.append(str(shapes_of_the_cards))

        #Making use of the 'random' function the card arrangements are randomly mixed.
        random.shuffle(self.pack)
        random.shuffle(self.shapes_pack)