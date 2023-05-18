from MDP import TransportationMDP
import os

mdp = TransportationMDP(N=10)

def valueIteration(mdp: TransportationMDP):
    V = {} # State -> Uopt[state]
    for state in mdp.states:
        V[state] = 0.

    def Q(state, action):
        return sum((prob * (reward + mdp.discount * V[new_state]) for new_state, prob, reward in mdp.transition_and_reward(state, action)))

    while True:
        new_V = {}
        for state in mdp.states:
            if mdp.isEnd(state):
                new_V[state] = 0.
            else:
                new_V[state] = max(Q(state, action) for action in mdp.actions(state))
        
        # Convergence
        if max(abs(V[i_state] - new_V[i_state]) for i_state in mdp.states) < mdp.epsilon:
            break

        V = new_V

        # Read policy
        pi = {}
        for state in mdp.states:
            if mdp.isEnd(state):
                pi[state] = 'none'
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]

        # print
        print('{:15} {:15} {:15}'.format('s', 'V(s)', 'pi(s)'))
        for state in mdp.states:
            print('{:15} {:15} {:15}'.format(state, V[state], pi[state]))
        input()

print(mdp.transition_and_reward(3, 'walk'))
print(mdp.transition_and_reward(3, 'tram'))
print(valueIteration(mdp))
