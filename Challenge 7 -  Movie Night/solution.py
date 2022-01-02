# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 17:30:41 2022

@author: javia
"""

import numpy as np
from math import ceil
from copy import deepcopy

# do a version using integer programming with some specific libraries

class Cinema:

    def find_seats(self, rows, seats_per_row, groups):
        # Your code goes here
        if any(x > seats_per_row for x in groups) or sum(groups) > rows * seats_per_row or not groups:
            return -1
        sorted_groups = sorted(groups, reverse=True)
        middle_row = ceil(rows / 2)
        middle_seat = ceil(seats_per_row / 2)
        # The biggest groups go in the middle row. I need to check how many of the first few groups fit in one row.
        # When more then one fits, I should think whether it is better to place it in the same row or below/above
        # Probably deciding to put it on the side or above/below is a matter of computing the minimum between the two options
        # Idea: start with the biggest and put it in the middle, if the next one does not fit on the sides put it above, same for the next one but below. If it fits then compare if it is better there. I should keep a count of the rows to know whether it is possible to add the group to a different row
        # Problem: I may have to change previous configuration, for example, if I have one free slot on each side and I need to fit in 1, I need to move the previous group. I think I can consider that in the moment of the comparison between options (check whether if fits as it is or with a movement, i.e, counting total spaces, and then compare this with choosing a new row if possible)
        group_sits = np.zeros([rows,
                               seats_per_row])  # to be updated with the number people in each group seated in the correspoding seats

        # probably I don't need to carry these structures all the way, I could just keep updating the result, but it would be harder if I don't keep the configuration
        score_sheet = group_sits.copy()
        for i in range(rows):
            for j in range(seats_per_row):
                score_sheet[i, j] = 1 + abs(i + 1 - middle_row) + abs(j + 1 - middle_seat)

        spaces = dict((r, seats_per_row) for r in range(1, rows + 1))
        sorted_rows = sorted(list(spaces.keys()), key=lambda x: abs(middle_row - x))
        sides = dict((r, [None, None]) for r in range(1, rows + 1))
       
        for a in sorted_groups:
            list_of_scores = []
            left_side = (seats_per_row - a) / 2 if a % 2 == 1 else (seats_per_row - a + 1) / 2
            right_side = (seats_per_row - a) / 2 if a % 2 == 1 else (seats_per_row - a + 1) / 2 - 1


            for row in sorted_rows:
                provisional_spaces = spaces.copy()
                provisional_sides = deepcopy(sides)
                provisional_sits = group_sits.copy()
                if provisional_spaces[row] == seats_per_row:
                    provisional_spaces[row] -= a
                    provisional_sides[row] = [left_side, right_side] if a % 2 == 1 else [left_side, right_side]
                    self.place_group(a, row, left_side, provisional_sits)
                    score = self.compute_score(score_sheet, provisional_sits)
                    list_of_scores.append(score)
                    break
                elif provisional_spaces[row] <= a:
                    list_of_scores.append(0)
                    continue
                else:
                    provisional_spaces[row] -= a + 1  # I should also subtract the space between two groups
                    if provisional_sides[row][0] > a and provisional_sides[row][0] == max(provisional_sides[row]):
                        # end=provisional_sides[row][0]-1
                        start = provisional_sides[row][0] - 1 - a
                        self.place_group(a, row, start, provisional_sits)
                        provisional_sides[row][0] -= a + 1
                        score = self.compute_score(score_sheet, provisional_sits)
                        list_of_scores.append(score)
                    elif provisional_sides[row][1] > a:
                        start = seats_per_row - provisional_sides[row][1] + 1
                        # end=seats_per_row-provisional_sides[row][1]+1+a
                        self.place_group(a, row, start, provisional_sits)
                        provisional_sides[row][0] -= a + 1
                        score = self.compute_score(score_sheet, provisional_sits)
                        list_of_scores.append(score)
                    else:  # do the best between shifting on the right or on the best? I think it doesn't matter because symmetry
                        # provisional_sits1=provisional_sits.copy() #because I have to do two calculations and compare them
                        diff = a - provisional_sides[row][0]
                        shift = diff + 1
                        provisional_sides[row][0] = 0
                        provisional_sides[row][1] -= shift
                        self.place_group_shift(a, row, shift, provisional_sits)
                        score = self.compute_score(score_sheet, provisional_sits)
                        list_of_scores.append(score)
            # once I have the list of scores, I compute the greatest, find its index, which corresponds to a row, so in that row I perfom the same condional as before but with the actual data instead of the copies
            # A way to optimize is updating group_sits to be provisional sits only if the score is better than the current score (but that only saves one calculation)
            positive_scores = [score for score in list_of_scores if score > 0]
            sorted_row = list_of_scores.index(min(positive_scores)) if positive_scores else None
            row=sorted_rows[sorted_row] if sorted_row is not None else None
            # block of conditional: should become a function receiving as arguments the data that I am modifying
            if sorted_row is None:
                return -1

            elif spaces[row] == seats_per_row:
                spaces[row] -= a
                sides[row] = [left_side, right_side] if a % 2 == 1 else [left_side, right_side]
                start = left_side
                # end=seats_per_row-right_side
                self.place_group(a, row, start, group_sits)

            else:
                spaces[row] -= a + 1  #
                if sides[row][0] > a and sides[row][0] == max(sides[row]):
                    # end=sides[row][0]-1
                    start = sides[row][0] - 1 - a
                    self.place_group(a, row, start, group_sits)
                    sides[row][0] -= a + 1
                elif sides[row][1] > a:
                    start = seats_per_row - sides[row][1] + 1
                    # end=seats_per_row-sides[row][1]+1+a
                    self.place_group(a, row, start, group_sits)
                    sides[row][0] -= a + 1

                else:  # do the best between shifting on the right or on the best? I think it doesn't matter because symmetry
                    # provisional_sits1=provisional_sits.copy() #because I have to do two calculations and compare them
                    diff = a - sides[row][0]
                    shift = diff + 1
                    sides[row][0] = 0
                    sides[row][1] -= shift
                    self.place_group_shift(a, row, shift, group_sits)

        score = self.compute_score(score_sheet, group_sits)
        return score

    def place_group(self, a, row, start, group_sits):
        # puts the number "a" a times from start=sides[0] to end=sides[1] in the array group_sits
        for i in range(int(start), int(start + a)):
            group_sits[row - 1, i] = a
        # return group_sits

    def place_group_shift(self, a, row, shift, group_sits):
        # puts the number "a" a times on the left, shifting to the right what's necessary for the a's to fit on the array groups_sits
        chosen_row = group_sits[row - 1]
        shifted_row = self.cyclic_perm(chosen_row, int(shift))
        group_sits[row - 1] = shifted_row
        self.place_group(a, row, 0, group_sits)
        return group_sits

    def compare_scores(self, a, row, state, middle_row):
        pass

    def compute_score(self, score_sheet, group_sits):
        seats = group_sits.copy()
        seats[seats>0]=1
        score_matrix = np.multiply(seats, score_sheet)
        score = score_matrix.sum()
        return score

    def cyclic_perm(self, row, places):
        n = len(row)
        b = [row[i - places] for i in range(n)]
        return b


if __name__ == '__main__':
    solution = Cinema()
    solution.find_seats(7, 5, [4, 5, 2, 5, 3, 1])
