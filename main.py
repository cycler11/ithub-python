import random

class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def to_text(self):
        return ' '.join(str(card) for card in self.cards)

class SuitsFactory:
    def create_suits(self):
        return [Suit("Spades", "♠"), Suit("Hearts", "♥"), Suit("Diamonds", "♦"), Suit("Clubs", "♣")]

class DeckBuilder:
    def __init__(self, suits):
        self.suits = suits

    def build_deck(self, card_count):
        deck = Deck()
        for i in range(2, 11):
            for suit in self.suits:
                deck.add_card(Card(str(i), str(suit)))

        for face in ["J", "Q", "K", "A"]:
            for suit in self.suits:
                deck.add_card(Card(face, str(suit)))

        return deck

def main():
    suits_factory = SuitsFactory()
    suits = suits_factory.create_suits()
    deck_builder = DeckBuilder(suits)
    deck1 = deck_builder.build_deck(36)
    deck2 = deck_builder.build_deck(52)

    print("total cards: 36")
    print(deck1.to_text())

    print("\ntotal cards: 52")
    print(deck2.to_text())

    deck1.shuffle()
    deck2.shuffle()

    print("\nShuffled decks:")
    print("total cards: 36")
    print(deck1.to_text())

    print("\ntotal cards: 52")
    print(deck2.to_text())

if __name__ == "__main__":
    main()
