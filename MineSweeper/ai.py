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
