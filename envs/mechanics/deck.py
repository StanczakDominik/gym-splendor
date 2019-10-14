import random
from typing import List

from envs.mechanics.noble import Noble
from envs.mechanics.enums import Row
from envs.mechanics.card import Card

class Deck:
    """This class is used to store three decks of cards used in the game: cheap deck, medium deck and expensive deck."""
    def __init__(self,
                 list_of_cards: List[Card],
                 list_of_nobles: List[Noble]) -> None:
        self.decks_dict = {row : [] for row in Row}

        #Here we put every card from the list_of_card to an appropriate deck:
        for card in list_of_cards:
            self.decks_dict[card.row].append(card)

        self.deck_of_nobles = list_of_nobles

    def pop_card(self,
            row: Row) -> Card:
        """Pops a card from a given row. Returns this card and removes it from the deck."""
        if self.decks_dict[row]:
            return self.decks_dict[row].pop(0)

    def pop_many_from_one_row(self,
                 row: Row,
                 number: int = 4) -> List[Card]:
        """Pops many cards from a given row."""
        return [self.pop(row) for _ in range(number)]

    def pop_many_nobles(self,
                        number: int = 3) -> List[Noble]:
        """Pops many nobles from the deck."""
        return self.nobles_deck[0:number]

    def shuffle(self) -> None:
        """Shuffles both deck of cards and deck of nobles."""
        for list_of_cards in self.decks_dict.values():
            random.shuffle(list_of_cards)

        random.shuffle(self.deck_of_nobles)

    def how_many_cards_left(self, row: Row) -> int:
        """Returns number of unrevealed card in a given row."""
        return len(self.decks_dict[row])