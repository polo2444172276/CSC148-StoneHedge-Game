"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
import copy
from typing import Any
from game import Game
from game_state import GameState


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def minimax_recursive_strategy(game: Game) -> Any:
    """
    This is the strategy that returns the move that minimizes
    the possible losses for a player implemented recursively
    """

    c_state = copy.deepcopy(game.current_state)
    all_moves = [next_score(game, c_state.make_move(move))
                 for move in game.current_state.get_possible_moves()]
    best_move = game.current_state.get_possible_moves()[all_moves.index(
        max(all_moves))]
    return best_move


def minimax_iterative_strategy(game: Game) -> Any:
    """
    This is the strategy that returns the move that minimizes
    the possible losses for a player implemented iteratively
    """
    g = copy.deepcopy(game)
    storage = Stack()
    root = TreeScore(g.current_state)
    storage.add(root)

    while not storage.is_empty():
        new_tree = storage.remove()
        if new_tree.children != []:
            new_tree.score = min([-child.score for child in
                                  new_tree.children])
        elif not g.is_over(new_tree.value):
            storage.add(new_tree)
            moves = new_tree.value.get_possible_moves()
            for child in [TreeScore(new_tree.value.make_move(move))
                          for move in moves]:
                storage.add(child)
                new_tree.children += [child]
        else:
            if new_tree.value.p1_turn:
                cur_p, opp_p = 'p1', 'p2'
            else:
                cur_p, opp_p = 'p2', 'p1'
            g.current_state = new_tree.value
            if g.is_winner(cur_p):
                new_tree.score = -1
            elif g.is_winner(opp_p):
                new_tree.score = 1
            else:
                new_tree.score = 0
    all_moves = [child.score for child in root.children]
    best_move = game.current_state.get_possible_moves()[all_moves.index(
        max(all_moves))]
    return best_move


def next_score(game: Game, state: GameState) -> float:
    """
    This is a helper function within the recursive strategy
    that implements the game recursively
    """
    g = copy.deepcopy(game)
    new_state = copy.deepcopy(state)
    if new_state.p1_turn:
        cur_p, opp_p = 'p1', 'p2'
    else:
        cur_p, opp_p = 'p2', 'p1'
    if g.is_over(new_state):
        g.current_state = new_state
        if g.is_winner(cur_p):
            fin_score = -1
        elif g.is_winner(opp_p):
            fin_score = 1
        else:
            fin_score = 0
        return fin_score
    moves = new_state.get_possible_moves()
    new_scores = [next_score(game, new_state.make_move(move)
                             )for move in moves]
    return min([-score for score in new_scores])


class Stack:
    """
    Last-in, first-out (LIFO) stack ADT. Helper function
    used in iterative max
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.
        """
        self._storage = []

    def add(self, obj: object)-> None:
        """ Add object obj to top of Stack self.
        """
        self._storage.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty, otherwise
        raises EmptyStackException
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        if self.is_empty():
            raise Exception
        else:
            return self._storage.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(s)
        >>> s.is_empty()
        False
        """
        return len(self._storage) == 0


class TreeScore:
    """
    A modified Tree ADT used in the iterative minimax strategy.
    """
    def __init__(self, value=None, children=None, score=None) -> None:
        """
        Create Tree self with content value and 0 or more children and score
        """
        self.value = value
        self.children = children[:] if children is not None else []
        self.score = score


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
