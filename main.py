import random


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Card:
    def __init__(self, rank, suit, lang='english'):
        self.rank = rank
        self.suit = suit
        self.lang = lang

    def __str__(self):
        if self.lang == 'english':
            return f"{self.rank} {self.suit.symbol}"
        elif self.lang == 'russian':
            rank_names = {6: 'Шестёрка', 7: 'Семёрка', 8: 'Восьмёрка', 9: 'Девятка', 10: 'Десятка', 11: 'Валет',
                          12: 'Дама', 13: 'Король', 14: 'Туз'}
            suit_names = {'Hearts': 'черви', 'Diamonds': 'бубны', 'Clubs': 'трефы', 'Spades': 'пики'}
        elif self.lang == 'french':
            rank_names = {6: 'Six', 7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix', 11: 'Valet', 12: 'Dame', 13: 'Roi',
                          14: 'As'}
            suit_names = {'Hearts': 'Coeurs', 'Diamonds': 'Carreaux', 'Clubs': 'Trèfles', 'Spades': 'Piques'}

        full_rank = rank_names.get(self.rank, str(self.rank))
        full_suit = suit_names.get(self.suit.name, self.suit.name)
        return f"{full_rank} {full_suit}"


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
    def get_standard_suits(self):
        return [Suit('Hearts', '\u2665'),
                Suit('Diamonds', '\u2666'),
                Suit('Clubs', '\u2663'),
                Suit('Spades', '\u2660')]


class DeckBuilder:
    def __init__(self):
        self.suits_factory = SuitsFactory()

    def build_deck(self, num_cards):
        deck = Deck()
        suits = self.suits_factory.get_standard_suits()
        for suit in suits:
            for rank in range(6, min(15, num_cards + 6)):  # Ensure not to exceed 14 ranks
                card = Card(rank, suit)
                deck.add_card(card)
        return deck


def main():
    deck_builder = DeckBuilder()
    deck1 = deck_builder.build_deck(36)
    deck2 = deck_builder.build_deck(52)

    print("Total cards in deck 1:", len(deck1.cards))
    print(deck1.to_text())

    print("\nTotal cards in deck 2:", len(deck2.cards))
    print(deck2.to_text())

    deck1.shuffle()
    deck2.shuffle()

    print("\nShuffled deck 1:")
    print(deck1.to_text())
    print("\nShuffled deck 2:")
    print(deck2.to_text())


if __name__ == "__main__":
    main()
