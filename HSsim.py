import random

# example: 20 ATTACK C'THUN versus ONYXIA and A SLIGHTLY UNHEALTHY HERO

NUM_OF_SHOTS = 16
DMG_PER_SHOT = 1
FACE_HEALTH = 10

minion_list = list()
minion_list = [10]


TRIALS = 300000


def simulate(minions_on_board):
    num_of_targets = 1 + len(minions_on_board)
    face_dmg = 0

    for i in range(NUM_OF_SHOTS):
        target = random.randint(-1, num_of_targets - 2)
        if target == -1:
            face_dmg += DMG_PER_SHOT
            continue
        minions_on_board[target] -= DMG_PER_SHOT
        if minions_on_board[target] <= 0:
            minions_on_board.pop(target)
            num_of_targets -= 1

    # print("end board state: " + str(minions_on_board))
    # print("face was hit for " + str(face_dmg) + " damage.")
    status = dict()
    if len(minions_on_board) == 0:
        status["board clear"] = True
    else:
        status["board clear"] = False
    if FACE_HEALTH - face_dmg <= 0:
        status["lethal"] = True
    else:
        status["lethal"] = False
    # print(str(status) + "\n\n")
    return status


def main(minions_on_board):
    print("RUnning simulation with " +str(NUM_OF_SHOTS)+ " shots and " +str(FACE_HEALTH)+ " face health.")
    print("Minion board state "+str(minions_on_board))
    print()

    lethal_num = 0
    board_clear_num = 0

    for i in range(TRIALS):
        ret = simulate(list(minions_on_board))  # make a copy of the minions on board and run a single simulation
        if ret["lethal"] == True:
            lethal_num += 1
        if ret["board clear"] == True:
            board_clear_num += 1

    LETHAL_PROBABILITY = lethal_num / TRIALS
    BOARD_CLEAR_PROBABILITY = board_clear_num / TRIALS
    lethal_percent = LETHAL_PROBABILITY * 100
    b_clear_percent = BOARD_CLEAR_PROBABILITY * 100

    print("Lethal probability is " + str(LETHAL_PROBABILITY) + "  (" + str(lethal_percent) + "%)")
    print()
    print("Board Clear probability is " + str(BOARD_CLEAR_PROBABILITY) + "  (" + str(b_clear_percent) + "%)")
    pass


main(minion_list)
