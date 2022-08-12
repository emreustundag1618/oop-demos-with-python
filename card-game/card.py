class Card:
    
    def __init__(self, card_type, card_value):
        self.card_type = card_type
        self.card_value = card_value
        
    def getCard(self):
        return {"Card type": self.card_type, "Value": self.card_value}
    
    # or you can use __repr__ method instead of getCard
    # def __repr__(self):
    #    return f"Type: {self.card_type}, value: {self.card_value}"
    
card1 = Card("spades", "5")
card2 = Card("hearts", "8")
card1.getCard()
# repr(card2)