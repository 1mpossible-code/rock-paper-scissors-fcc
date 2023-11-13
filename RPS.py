# Description: Rock Paper Scissors AI
# I use the same strategy as Abbey, but I use a more tracking (4 layers instead of 2)
# Based on my tests, the best results are achieved with 4 layers and start with 'S'
# However, you can balance try it out to play with different starts and values since they affect the results a lot
LAYERS = 4
START = 'S'

play_order = [{}]
CHOICES = ('R', 'P', 'S')


def player(prev_play, opponent_history=[]):
    if not prev_play:
        for i in range(3 ** LAYERS):
            play_order[0][''.join([CHOICES[(i // (3 ** j)) % 3] for j in range(LAYERS)])] = 0
        opponent_history.clear()

    if not prev_play:
        prev_play = START
    opponent_history.append(prev_play)
    lasts = START * (LAYERS - 1)

    last_n = "".join(opponent_history[-LAYERS:])
    if len(last_n) == LAYERS:
        play_order[0][last_n] += 1
        lasts = last_n[-(LAYERS - 1):]

    potential_plays = [
        lasts + "R",
        lasts + "P",
        lasts + "S",
    ]

    sub_order = {
        k: play_order[0][k] for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
