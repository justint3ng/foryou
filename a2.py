from a2_support import *

# Implement your classes here

class Card:

    def __init__(self):
        pass
    """used to initialise the attributes of an object"""

    def get_damage_amount(self):
        return 0
    """return the value 0"""

    def get_block(self):
        return 0
    """return the value """

    def get_energy_cost(self):
        return 1
    """return the value 1"""

    def get_status_modifiers(self):
        return {}
    """return {}"""

    def get_name(self):
        return 'Card'
    """return 'Card'"""

    def get_description(self):
        return 'A card.'
    """return 'A card."""

    def requires_target(self):
        return True
    """returns True"""

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    """converts values to a string in the form of "name: description"""

    def __repr__(self):
        return f'{type(self).__name__}()'
    """returns the string representation of teh value passed"""

class Strike(Card):

    def __init__(self):
        super().__init__()
    """gives access to methods and properties of the card class"""

    def get_damage_amount(self):
        return 6
    """return the value 6"""

    def get_block(self):
        return 0
    """return the value 0"""

    def get_energy_cost(self):
        return 1
    """return the value 1"""

    def get_name(self):
        return 'Strike'
    """returns 'Strike'"""

    def get_description(self):
        return "Deal 6 damage."
    """return Deal 6 Damage"""

    def requires_target(self):
        return True
    """return True"""

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    """converts values to a string in the form of "name: description"""""

    def __repr__(self):
        return f'{type(self).__name__}()'
    """returns the string representation of teh value passed"""

class Defend(Card):

    def __init__(self):
        super().__init__()
    """gives access to the class Card"""

    def get_damage_amount(self):
        return 0
    """returns the value 0"""

    def get_block(self):
        return 5
    """returns the value 5"""

    def get_energy_cost(self):
        return 1
    """returns the value 1"""

    def get_name(self):
        return 'Defend'
    """returns the value "Defend"""

    def get_description(self):
        return "Gain 5 block."
    """returns the value "Gain 5 block."""
    def requires_target(self):
        return False
    """returns False"""

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    """" converts values to a string in the form of "name: description"""

    def __repr__(self):
        return f'{type(self).__name__}()'
    """gives access to methods and properties of the card class"""


class Bash(Card):

    def __init__(self):
        super().__init__()
    """gives access to the class Cards"""

    def get_damage_amount(self):
        return 7
    """returns the value 7"""

    def get_block(self):
        return 5
    """returns the value 5"""

    def get_energy_cost(self):
        return 2
    """returns the value 2"""

    def get_name(self):
        return 'Bash'
    #returns the value 'Bash'

    def get_description(self):
        return "Deal 7 damage. Gain 5 block."
    #returns the value 'Deal 7 damage. Gain 5 block.'

    def requires_target(self):
        return True
    #returns True

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    #returns the value in a string in the form of name: description

    def __repr__(self):
        return f'{type(self).__name__}()'
    #returns the string representation of an object


class Neutralize(Card):

    def __init__(self):
        super().__init__()
    #gives access to the Card class

    def get_damage_amount(self):
        return 3
    #return the value 3

    def get_block(self):
        return 0
    #return the value 0

    def get_energy_cost(self):
        return 0
    # return the value 0

    def get_status_modifiers(self):
        return {'weak': 1, 'vulnerable': 2}
    #returns the value weak:1, vulnerable: 2

    def get_name(self):
        return 'Neutralize'
    #returns the name of the card

    def get_description(self):
        return "Deal 3 damage. Apply 1 weak. Apply 2 vulnerable."
    #returns the description of the card

    def requires_target(self):
        return True
    #returns True

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    #returns the values in a string format in the form of name: description

    def __repr__(self):
        return f'{type(self).__name__}()'
    #returns the string representation of the object


class Survivor(Card):

    def __init__(self):
        super().__init__()
    #gives access to the card calss

    def get_damage_amount(self):
        return 0
    #returns the value 0

    def get_block(self):
        return 8
    #returns the value 8

    def get_energy_cost(self):
        return 1
    #returns the value 1

    def get_status_modifiers(self):
        return {'strength': 1}
    #returns strength: 1

    def requires_target(self):
        return False
    #returns false

    def get_name(self):
        return 'Survivor'
    #returns the name of the card

    def get_description(self):
        return "Gain 8 block and 1 strength."
    #returns the description of the card

    def __str__(self):
        return f'{self.get_name()}: {self.get_description()}'
    #returns the values in a string format in the form of name: description

    def __repr__(self):
        return f'{type(self).__name__}()'
    #returns the string representation of an object
    
class Entity():

    def __init__(self, max_hp: int):
        self.max_hp = max_hp
        self.hp = max_hp
        self.block = 0
        self.strength = 0
        self.weak = 0
        self.vulnerable = 0
    #all these self.values will be the default values when initiated
    def get_name(self):
        return 'Entity'
    #returns the name of the entity
    
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_block(self):
        return self.block

    def get_strength(self):
        return self.strength

    def get_weak(self):
        return self.weak

    def get_vulnerable(self):
        return self.vulnerable

    def reduce_hp(self, amount: int):
        if self.block > 0:
            self.block -= amount
        #subtract the amount from self.block

            if self.block < 0:
                self.hp += self.block #add self.block to self.hp
                self.block = 0

        else:
            self.hp -= amount

        if self.hp < 0:
            self.hp = 0

    def is_defeated(self):
        return self.hp <= 0

    def add_block(self, amount: int):
        self.block += amount #add amount to self.block

    def add_strength(self, amount: int):
        self.strength += amount #add amount to self.strength

    def add_weak(self, amount: int):
        self.weak += amount #add amount to self.weak

    def add_vulnerable(self, amount: int):
        self.vulnerable += amount #add amount to self.vulnerable

    def new_turn(self):
        self.block = 0
        self.weak = max(0, self.weak - 1) #rounding up self.weak by using the max function
        self.vulnerable = max(0, self.vulnerable - 1) #rounding up self.vulenrable by ysing the max function

    def __str__(self):
        return f'{self.get_name()}: {self.hp}/{self.max_hp} HP'
        #return the values in a string in the form of 'name: hp'
    def __repr__(self):
        return f'{self.__class__.__name__}({self.max_hp})'
        #returns the strong representation of the value passed in the form of 'name (hp)'

class Player(Entity):

    def __init__(self, max_hp: int, cards: list[Card] | None = None):
        super().__init__(max_hp)
        self.energy = 3
        self.hand = []
        self.deck = cards if cards is not None else []
        self.discarded = []
        #these values are the default values when the class gets initiated

    def get_name(self):
        return 'Player'
    
    def get_energy(self):
        return self.energy

    def get_hand(self):
        return self.hand

    def get_deck(self):
        return self.deck

    def get_discarded(self):
        return self.discarded

    def start_new_encounter(self):
        assert not self.hand
        self.deck += self.discarded #add discarded cards to the deck
        self.discarded = []

    def end_turn(self):
        self.discarded += self.hand #add the cards in the hand to the discarded pile
        self.hand = []

    def new_turn(self):
        self.energy = 3
        draw_cards(self.deck, self.hand, self.discarded) #a function call that passes in the current player's deck, hand and discard pile to another function

    def play_card(self, card_name: str):
        for card in self.hand:
            if card.get_name() == card_name and card.get_energy_cost() <= self.energy:
                self.discarded.append(card)
                self.hand.remove(card)
                self.energy -= card.get_energy_cost()
                return card
        return None

    #goes through the player's cards in hand with a name that matches the input. if the card matches the input and if the player has enough energy to play it, then the card is removed from the hand and added to the discard list
    #if no card is found, then this function will return with "None"

    def __repr_no_deck(self):
        return f'{self.__class__.__name__}({self.max_hp})'

    def __repr__(self):
            return f'{self.__class__.__name__}({self.max_hp}, {self.deck})'


class IronClad(Player):
    def __init__(self):
        super().__init__(80)
        self.deck = [Strike() for _ in range(5)] + [Defend() for _ in range(4)] + [Bash()]
    #this will initiate the player with 5 instances of the strike class, 4 instances of the defend class and 1 instance of the bash class
    #these instances represents the cards that the player has

    def get_name(self):
        return 'IronClad'

    def __repr__(self):
        return f'{type(self).__name__}()'

class Silent(Player):
    def __init__(self):
        super().__init__(70)
        self.deck = [Strike() for _ in range(5)] + [Defend() for _ in range(5)] + [Neutralize()] + [Survivor()]
    #this will initiate the player with 5 strike cards, 5 defend cards, 1 neutralise and 1 survivor card.

    def get_name(self):
        return 'Silent'

    def __repr__(self):
        return f'{type(self).__name__}()'
    
class Monster(Entity):
    id = 0
    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.id = Monster.id
        Monster.id += 1
    #the moment this is initiated, the monster's id will be 1 and every time it is initiated, the id will increase by 1

    def get_name(self):
        return 'Monster'

    def get_id(self):
        return self.id

    def another_monster(self):
        return Monster(self.max_hp)

    def action(self):
        raise NotImplementedError

class Louse(Monster):
    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.damage_amount = random_louse_amount()
    #utilises the function from the a2_support.py file

    def get_name(self):
        return 'Louse'

    def action(self):
        return{'damage': self.damage_amount}

class Cultist(Monster):
    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.num_calls = 0 #to represent the number of times the function was called
        self.weak_amount = 0


    def get_name(self):
        return 'Cultist'

    def action(self):
        if self.num_calls == 0:
            self.damage_amount = 0
        else:
            self.damage_amount = 6 + self.num_calls

        weak_amount = self.weak_amount
        self.weak_amount = (self.weak_amount + 1) % 2

        self.num_calls += 1 #implemented so everytime the function is called, it will go up by 1 count

        return {'damage': self.damage_amount, 'weak': weak_amount}

class JawWorm(Monster):
    def __init__(self, max_hp: int):
        super().__init__(max_hp)
        self.damage = 0
        self.block = 0
        self.num_call = 0
        #to initialise the function with these default values

    def get_name(self):
        return 'JawWorm'

    def block(self):
        return self.block

    def action(self):
        if self.num_call == 0:
            self.damage = 0
        else:
            self.damage = max(self.damage//2, 2) #rounded up to the nearest whole number by using the max function
            self.block += self.damage

        self.num_call += 1
        return {'damage': self.damage}

    def reduce_hp(self, amount: int):
        half_amount = -(-amount // 2)  #to round up to the nearest whole number
        self.block += half_amount
        self.hp -= amount

    def __str__(self):
        return f'{self.get_name()}: {self.max_hp}/{self.max_hp} HP'


class Encounter:

    def __init__(self, player: Player, monsters: list):
        self.player = player
        self.monster = []
        for name, max_hp in monsters:
            self.monsters.append(Monster(name, max_hp))
        self.start_new_turn()
        self.get_hand = []

    def start_new_turn(self):
        self.player.start_new_turn()
        for monster in self.monster:
            monster.new_turn()

    def end_player_turn(self):
        self.player.end_turn()
        for monster in self.monster:
            monster.new_turn()

    def get_player(self):
        return self.player

    def get_monsters(self):
        return self.monster

    #def is_active(self):

    #def player_apply_card(self):

    #def enemy_turn(self):





##def main():
    # Implement this only once you've finished and tested ALL of the required
    # classes.
    pass



##if __name__ == '__main__':
    #main()
