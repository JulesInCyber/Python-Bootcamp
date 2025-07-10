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
    def deal(cls) -> "Card":
        return cls(random.choice(cls.values), random.choice(cls.suits))
    
    def get_value(self):
        pass
    
class Deck:
    def __init__(self) -> None:
        self.cards = []
        for value in Card.values:
            for suit in Card.suits:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        return "\n".join(str(card) for card in self.cards)
    
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> None:
        drawn_card = self.cards[0]
        self.cards.pop(0)
        return drawn_card

    def draw_x(self, n:int=5) -> list[Card]:
        drawn_cards = []
        for i in range(n):
            drawn_cards.append(self.draw_card())
        return drawn_cards

class Player:
    def __init__(self, name:str="John Doe") -> None:
        self.name = name
        self.hand = []

print(Card().deal())