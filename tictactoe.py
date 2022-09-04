"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    spaces = 0
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == EMPTY:
                spaces += 1
    
    if spaces % 2 != 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == EMPTY:
                actionSet.add((row, col))

    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)
    
    # Check validity of action
    if newBoard[action[0]][action[1]] != EMPTY:
        raise Exception("Position already marked!")
    
    # Make a move in newBoard
    newBoard[action[0]][action[1]] = player(board)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal moves
    for row in range(0, 3):
        count_x = 0
        count_o = 0
        for col in range(0, 3):
            if board[row][col] == X:
                count_x += 1
            elif board[row][col] == O:
                count_o += 1
        if count_x == 3:
            return X
        elif count_o == 3:
            return O

    # Check vertical moves
    for row in range(0, 3):
        count_x = 0
        count_o = 0
        for col in range(0, 3):
            if board[col][row] == X:
                count_x += 1
            elif board[col][row] == O:
                count_o += 1
        if count_x == 3:
            return X
        elif count_o == 3:
            return O

    # Check diagonal moves
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check for winner
    if (winner(board)):
        return True
    
    # Check for spaces
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = winner(board)

    if value == X:
        return 1
    elif value == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    currentPlayer = player(board)
    value = 0
    chosenAction = ()

    # Maximizing player
    if currentPlayer == X:
        value = -math.inf
        for action in actions(board):
            v = max(value, minValue(result(board, action)))
            if v > value:
                chosenAction = action
                value = v

    # Minimizing player
    if currentPlayer == O:
        value = math.inf
        for action in actions(board):
            v = min(value, maxValue(result(board, action)))
            
            if v < value:
                chosenAction = action
                value = v
        
    return chosenAction

def minValue(state):
    value = math.inf

    if terminal(state):
        return utility(state)

    for action in actions(state):
        value = min(value, maxValue(result(state, action)))

    return value


def maxValue(state):
    value = -math.inf

    if terminal(state):
        return utility(state)

    for action in actions(state):
        value = max(value, minValue(result(state, action)))

    return value