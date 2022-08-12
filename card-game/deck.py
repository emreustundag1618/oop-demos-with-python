import random

class Deck:
    
    card_types = ["diamonds","hearts","spades","clubs"]
    card_values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    
    def __init__(self):
        self.cards_in_deck = [Card(t,v) for t in Deck.card_types for v in Deck.card_values]
        
    def countCards(self):
        return len(self.cards_in_deck)
    
    def shuffleCards(self):
        if self.countCards() < 52:
            raise ValueError("You cannot shuffle cards without full deck")
        else:
            random.shuffle(self.cards_in_deck)
            
    def dealCards(self, amount):
        deck_amount = self.countCards()
        if deck_amount == 0:
            raise ValueError("All cards dealed")
        amount = min([deck_amount, amount])
        cards_out_deck = self.cards_in_deck[-amount:]
        self.cards_in_deck = self.cards_in_deck[:-amount]
        return cards_out_deck
    
    def playCard(self):
        return self.dealCards(1)[0]
   
deck = Deck()
deck.shuffleCards()
print(deck.dealCards(3))
for i in deck.dealCards(13):
    print(i.getCard())
    
# If you wish, you can develop a Hearts Game from here. =)