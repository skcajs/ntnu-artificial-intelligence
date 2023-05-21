import numpy as np
import random

def create_board(n = 4):
    state = np.zeros(n**2).reshape(n,n)
    for i in state:
        i[random.randint(0,n-1)] = 1
    return state

def successors(state):
    successors = []
    for i in range(len(state)):
        ind = np.where(state[i] == 1.)[0][0]
        state[i][ind] = 0.
        for j in range(len(state[i])):
            if j == ind:
                continue
            state_copy = state.copy()
            state_copy[i][j] = 1.
            successors.append(state_copy)
        state[i][ind] = 1.
    return successors

def heuristic(state):
    # Check Vertical by transposing state
    heuristic = 0
    s = state.transpose()
    for i in s:
        queens = len(np.where(i == 1.)[0])
        heuristic += sum(queen for queen in range(queens))

    queens_cn = queens_cp = 0
    
    # Diagonal Checks RHS
    for a in range(len(s)):
        i = 0
        j = a+1

        queens_rp = queens_lp = queens_rn = queens_ln = 0

        if s[a,a] == 1:
            queens_cp += 1
        if s[-(a+1), a] == 1:
            queens_cn += 1
        
        for _ in range(len(s[i])-1):
            if (i >= len(s) or j >= len(s)): break
            if s[i, j] == 1.:
                queens_rn += 1
            if s[j, i] == 1.:
                queens_ln += 1
            if s[j, -(i+1)] == 1.:
                queens_rp += 1
            if s[i,-(j+1)] == 1.:
                queens_lp += 1
            i += 1
            j += 1

        heuristic += sum(queen for queen in range(queens_rn))
        heuristic += sum(queen for queen in range(queens_ln))
        heuristic += sum(queen for queen in range(queens_rp))
        heuristic += sum(queen for queen in range(queens_lp))
    
    heuristic += sum(queen for queen in range(queens_cp))
    heuristic += sum(queen for queen in range(queens_cn))

    return heuristic