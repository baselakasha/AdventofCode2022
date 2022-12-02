# https://adventofcode.com/2022/day/2

from utils import get_input_from_file

scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

def main():
    data = get_input_from_file()
    total_score = 0
    for round in data:
        round_hands = round.split(" ")

        # need to draw
        if round_hands[1] == "Y":
            total_score += scores[round_hands[0]] + 3
            continue
        
        # need to win
        elif round_hands[1] == "Z":
            winning_hand = get_winning_hand(round_hands[0])
            total_score += scores[winning_hand] + 6

        elif round_hands[1] == "X":
            losing_hand = get_losing_hand(round_hands[0])
            total_score += scores[losing_hand]

    
    print(total_score)


def get_winning_hand(thier_hand):
    if thier_hand == "A":
        return "B"
    if thier_hand == "B":
        return "C"
    if thier_hand == "C":
        return "A"

def get_losing_hand(thier_hand):
    if thier_hand == "A":
        return "C"
    if thier_hand == "B":
        return "A"
    if thier_hand == "C":
        return "B"

if __name__ == "__main__": main()