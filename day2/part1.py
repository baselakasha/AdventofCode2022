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
        round_hands = decrypt_round_hand(round.split(" "))
        
        # draw
        if round_hands[0] == round_hands[1]:
            total_score += scores[round_hands[1]] + 3
            continue

        if do_i_win(round_hands):
            total_score += scores[round_hands[1]] + 6
        else:
            total_score += scores[round_hands[1]]
    
    print(total_score)

def decrypt_round_hand(round_hands):
    if round_hands[1] == "Y":
        round_hands[1] = "B"
    elif round_hands[1] == "X":
        round_hands[1] = "A"
    elif round_hands[1] == "Z":
        round_hands[1] = "C"

    return round_hands

def do_i_win(round_hands):
    if round_hands[0] == "A" and round_hands[1] == "B":
        return True
    elif round_hands[0] == "B" and round_hands[1] == "C":
        return True
    elif round_hands[0] == "C" and round_hands[1] == "A":
        return True
    

if __name__ == "__main__": main()