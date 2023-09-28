import numpy as np
import time

class CardGame:
    
    def __init__(self):
        self.deck = self.get_deck()
        self.original_deck = self.deck.copy()
        self.table_set = {i: [] for i in range(1, 14)}

        self.final_table_set = self.final_table_set()
        self.success = self.test_success(self.final_table_set)
        self.near_success = self.test_near_success(self.final_table_set)

    def final_table_set(self):
        while not self.test_success(self.table_set):
            for place in self.table_set: 
                if not self.deck:
                    break

                if (place not in self.table_set[place]) and (self.deck[0] == place):
                    self.deck.extend(self.table_set[place])
                    self.table_set[place] = [self.deck[0]]
                    self.deck.pop(0)
                if place not in self.table_set[place]:
                    self.table_set[place].append(self.deck[0])
                    self.deck.pop(0)

            if not self.deck:
                break
        return self.table_set
    
    @property
    def correctly_placed_cards(self):
        return sum(1 for place in self.table_set if place in self.table_set[place])
    
    @staticmethod
    def test_near_success(table_set):
        count_false = sum(1 for place in table_set if place not in table_set[place])
        if count_false == 1:
            return 1
        else:
            return 0
    
    @staticmethod
    def test_success(table_set):
        if all(place in table_set[place] for place in table_set):
            return int(1)
        else:
            return 0
    
    @staticmethod
    def get_deck():
        deck = []
        [deck.extend(range(1,14)) for i in range(4)]
        np.random.shuffle(deck)
        return deck
    
    
def simulation():
    start_time = time.time()
    success, near_success ,correct_cards = 0, 0, []

    for _ in range(10_000):
 
        game = CardGame()
        success += game.success
        near_success += game.near_success
        correct_cards.append(game.correctly_placed_cards)
      

    final_time = time.time()
    simulation_length = final_time - start_time

    print('Simulations: 10,000')
    print(f'Execution time: {round(simulation_length,2)} seconds.')
    print(f'Probability of completion: {(success)/100}%')
    print(f'Probability of completion to n-1: {(near_success)}% ')
    print(f'Standard deviation {round(np.std(correct_cards),2)}')

    



if __name__ == '__main__':
    simulation()
    