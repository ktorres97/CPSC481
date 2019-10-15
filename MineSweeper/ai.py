'''
Start by randomly selecting a cell on the board. Pick a point to consider and
apply the following rules

All these rules consider the 8 cells adjacent to the point of interest
Rule 1:
If the number of unflagged mines in equal to the number of unknown cells, then
all of those cells must be mines
Rule 2:
If the number of flagged mines is equal to the number on the cell,
the rest of those cells are safe
Rule 3:
If there are a series of cells where they share unflagged cells and there is only
one more mine required for one and the other requires more than one, there can
only be one mine in the shared spaces (xx 3 2 1 situation)

If there are no obvious choices, either move to an adjacent unsolved cell and/or
begin to assign probabilities of the adjacent cells being mines

'''
class AI():
    def __init__():
        self.pos = None
        self.target_x = None
        self.target_y = None
        self.targets = None
        self.flag_target = False
        self.total_arrangements = None

    def run_ai(self):
        self.mine_logic()

    def pick_next_target(self):
        pass

    def check_linked(self):
        pass

    def pick_random_target(self):
        pass

    def move(self):
        pass

    def add_hidden_near(self):
        pass

    def pick_target(self):
        pass

    def assign_probabilities(self):
        pass

    def combination_amount(self):
        pass

    def factorial(self):
        pass

    def determine_solutions(self):
        pass

    def validate_solution(self):
        pass

    def violated_a(self):
        pass

    def violated_b(self):
        #there's two for some reason?
        pass

    def add_connected(self):
        pass

    def in_section(self):
        pass

    def mine_logic(self):
        pass
