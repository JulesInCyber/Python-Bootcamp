import random

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, values=str,suits=str) -> None:
        self.values = values
        self.suits = suits
    
    def __str__(self):
        return f"{self.values} of {self.suits}"
    
    @classmethod
    def deal(cls,) -> "Card":
        return cls(random.choice(cls.values), random.choice(cls.suits))
    
class Deck:
    def __init__(self) -> None:
        self.cards = []
        for value in Card.values:
            for suit in Card.suits:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return "\n".join(str(card) for card in self.cards)
