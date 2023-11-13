"""
We will utilize Q-Learning algorithm to train our agent to play Rock-Paper-Scissors
against 4 different agents.
"""
import random

# The Q-Table will be a dictionary with the following structure:
# {state: [action_1_value, action_2_value, action_3_value]}
# where state is a tuple of the previous opponent's play and our previous play
# and action_1_value, action_2_value, action_3_value are the values for each action
# in the state
q_table = {}

# The learning rate will be 0.1
alpha = 0.1

# The discount factor will be 0.6
gamma = 0.6

# The exploration rate will be 0.1
epsilon = 0.1


# This is the function that will be utilized to play against the agents
def get_reward(prev_play, our_play):
    if prev_play == our_play:
        return 0
    elif (prev_play == 'R' and our_play == 'S') or (prev_play == 'P' and our_play == 'R') or (
            prev_play == 'S' and our_play == 'P'):
        return -1
    else:
        return 1


# prev_play is response of our opponent based on what acton we returned last time
def player(prev_play, opponent_history=[]):
    # Opponent history contains the previous plays of our and us in the form of a list
    # We will update the opponent history with the previous play of our opponent
    action = random.randint(0, 2)
    if len(opponent_history) > 0:
        opponent_history[-1][0] = prev_play
        # Our play is already in the list

        # Now we need to figure our if we won with the action that we took last time
        # We will do this by checking the reward that we got last time
        reward = get_reward(opponent_history[-1][0], opponent_history[-1][1])

        # Now we need to update the Q-Table
        # We will do this by first checking if the state is in the Q-Table
        # If it is not, we will add it to the Q-Table
        # If it is, we will update the Q-Table
        prev_state = (opponent_history[-1][0], opponent_history[-1][1])
        if prev_state not in q_table:
            q_table[prev_state] = [0, 0, 0]
        else:
            # We will convert our previous play to an action
            if opponent_history[-1][1] == 'R':
                action = 0
            elif opponent_history[-1][1] == 'P':
                action = 1
            else:
                action = 2
            # We will update the Q-Table
            # We will do this by first getting the maximum value from the Q-Table
            max_value = max(q_table[prev_state])
            # Now we will update the Q-Table
            q_table[prev_state][action] = (1 - alpha) * q_table[prev_state][action] + alpha * (
                        reward + gamma * max_value)

        # Now we need to figure out what action to take
        # We will first check if the state is in the Q-Table
        if prev_state in q_table:
            # We will check if we should explore or exploit
            if random.random() < epsilon:
                # We will explore
                action = random.randint(0, 2)
            else:
                # We will exploit
                action = q_table[prev_state].index(max(q_table[prev_state]))

    # Now we need to convert the action to a play
    if action == 0:
        play = 'R'
    elif action == 1:
        play = 'P'
    else:
        play = 'S'

    # Now we need to add the play to the opponent history
    opponent_history.append([None, play])

    # Now we need to return the play
    return play
