import math

def search(game, state):
    player = game.player()
    value, move = max_value(game, state, player)
    return move

def max_value(game, state, player):
    if game.isTerminal():
        return game.utility(state, player), None
    v = - math.inf
    for a in game.actions(state):
        v2,a2 = min_value(game, game.result(state, a), player)
        if v2 > v:
            v, move = v2, a
        return v, move


def min_value(game, state, player):
    if game.isTerminal():
        return game.utility(state, player), None
    v = math.inf
    for a in game.actions(state):
        v2,a2 = max_value(game, game.result(state, a))
        if v2 < v:
            v, move = v2, a
        return v, move

