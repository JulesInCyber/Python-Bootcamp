import random

card_values = {
        "2": 2,
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "J": 11, 
        "Q": 12, 
        "K": 13, 
        "A": 14
    }


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
        return card_values[self.values]
    
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
        self.score = 0

    def show_hand(self) ->str:
        return "\n".join(str(card) for card in self.hand)

def highCard(p1, p2, d1):
    d1.shuffle()
    c1 = d1.draw_card()
    c2 = d1.draw_card()
    
    print(f"{p1.name} draws: {c1}")
    p1.hand.append(c1)
    print(f"{p2.name} draws: {c2}")
    p2.hand.append(c2)

    if c1.get_value() > c2.get_value():
        print(f"{p1.name} wins!")
        p1.score += 1
    elif c1.get_value() < c2.get_value():
        print(f"{p2.name} wins!")
        p2.score += 1
    else:
        print("Draw!")

def main():
    p1 = Player("Julian")
    p2 = Player("Not-Julian")
    d1 = Deck()

    for i in range(5):
        highCard(p1, p2, d1)
        print("-----")
    print(f"{p1.name}: {p1.score} Points")
    print(f"{p2.name}: {p2.score} Points")

    if p1.score > p2.score:
        print(f"{p1.name} is the winner")
    elif p1.score < p2.score:
        print(f"{p2.name} is the winner!")
    else:
        # Need to check if possible
        print("No winner could be dertermined")


if __name__ == "__main__":
    main()
