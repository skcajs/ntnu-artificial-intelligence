from helper import plot
from agent import Agent
from snake import Snake

if __name__ == '__main__':
    scores = []
    mean_scores = []
    total_score = 0
    record = 0
    agent = Agent(initial_epsilon=0.4)
    game = Snake()
    while True:
        # get state
        state = game.get_state()
        # get action
        action = agent.get_action(state)
        
        # perform action and get next state
        reward, done, score = game.play_step(action)
        next_state = game.get_state()

        # train short memory
        agent.train_short_memory(state, action, reward, next_state, done)

        # remeber
        agent.remember(state, action, reward, next_state, done)

        if done:
            # train long memory -> also called experienced replay, the game replays all previous memories.
            # plot results
            game.reset()
            agent.episodes += 1
            agent.train_long_memory()
            agent.decay_epsilon()

            if score > record:
                record = score
                agent.model.save()

            print('Game ', agent.episodes, 'Score ', score, 'Record ', record)

            scores.append(score)
            total_score += score
            mean_score = total_score / agent.episodes
            mean_scores.append(mean_score)
            plot(scores, mean_scores, 'episodes', 'score', agent.epsilon)