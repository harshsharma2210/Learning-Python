import copy
from collections import deque
from typing import List


class State:
    def __init__(self, board):
        self.board = board

    def find_blank(self):
        """return cooordinates of the blank tile"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)

    def moves(self):
        blank_i, blank_j = self.find_blank()

        # names of the moves
        possible_moves = []

        if blank_i == 0:
            # down
            possible_moves.append("D")
        elif blank_i == 1:
            # up
            possible_moves.append("U")
            # down
            possible_moves.append("D")
        elif blank_i == 2:
            # up
            possible_moves.append("U")

        if blank_j == 0:
            # right
            possible_moves.append("R")
        elif blank_j == 1:
            # left
            possible_moves.append("L")
            # right
            possible_moves.append("R")
        elif blank_j == 2:
            # left
            possible_moves.append("L")

        return possible_moves

    def move_left(self, blank_i: int, blank_j: int):
        self.board[blank_i][blank_j] = self.board[blank_i][blank_j - 1]
        self.board[blank_i][blank_j - 1] = 0

    def move_right(self, blank_i: int, blank_j: int):
        self.board[blank_i][blank_j] = self.board[blank_i][blank_j + 1]
        self.board[blank_i][blank_j + 1] = 0

    def move_up(self, blank_i: int, blank_j: int):
        self.board[blank_i][blank_j] = self.board[blank_i - 1][blank_j]
        self.board[blank_i - 1][blank_j] = 0

    def move_down(self, blank_i: int, blank_j: int):
        self.board[blank_i][blank_j] = self.board[blank_i + 1][blank_j]
        self.board[blank_i + 1][blank_j] = 0

    def copy(self):
        """return copy of the state"""
        return State(board=copy.deepcopy(self.board))

    def hash_str(self) -> str:
        """return immutable/hashable value of state"""
        hash_string = ""
        for i in self.board:
            for j in i:
                hash_string += str(j) + "-"
        return hash_string

    def __repr__(self) -> str:
        """return string representation (readable) of the board state"""
        out_string = ""
        for i in self.board:
            for j in i:
                out_string += str(j) + "\t"
            out_string += "\n"
        return out_string


def compare_states(given_state: State, goal_state: State) -> int:
    state_diffs = 0
    for i in range(3):
        for j in range(3):
            if given_state.board[i][j] != goal_state.board[i][j]:
                state_diffs += 1
    return state_diffs


def main():
    init = State([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
    goal = State([[2, 8, 1], [0, 4, 3], [7, 6, 5]])

    print("Initial State:")
    print(init)
    print("-" * 20)

    stack = deque([init])
    visited = {init.hash_str()}

    while len(stack) > 0:

        # BFS (Queue) can be 
        current_state = stack.popleft()

        # DFS (Stack)

        print("Computing:")
        print(current_state)
        if compare_states(goal, current_state) == 0:
            print("Found:")
            print(current_state)
            break

        for move in current_state.moves():
            cp = current_state.copy()
            blank_i, blank_j = cp.find_blank()
            if move == "U":
                cp.move_up(blank_i, blank_j)
            elif move == "D":
                cp.move_down(blank_i, blank_j)
            elif move == "L":
                cp.move_left(blank_i, blank_j)
            elif move == "R":
                cp.move_right(blank_i, blank_j)
            else:
                break

            cp_hashable = cp.hash_str()
            if cp_hashable not in visited:
                visited.add(cp_hashable)
                stack.append(cp)


if __name__ == "__main__":
    main()



