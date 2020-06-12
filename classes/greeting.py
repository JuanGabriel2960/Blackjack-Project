#The 'Greeting' class is used to welcome the user and explain the rules.
class Greeting:
    def __init__(self,name):
        self.name = name

    # The greeting method welcomes the user with their name previously entered.
    def greet(self):
        print('Hi {}! •ᴗ• Welcome to the table, do you want to read the rules before you start playing?...\n'.format(self.name))

    #The 'read' method shows the rules to the user or not depending on his choice.
    def read(self,choice):
        if choice == 1:
            print('\nBlackjack Rules (ง •̀_•́)ง  ผ(•̀_•́ผ)\n')
            print('1-The game consists of adding a value as close to 21 but without going over.')
            print('2-The player at the table plays only against the dealer, trying to get a better play than this.')
            print('3-The dealer is required to ask for a card as long as his score totals 16 or less.')
            print('4-And forced to stand if he adds 17 or more.')
            print('5-The number cards add up to their value, the figures add up to 10 and the Ace is worth 11.\n')
        else:
            print('\nOK, good luck! ｡◕‿◕｡\n')
