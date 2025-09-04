def Score_calculator(word):
    word = word.upper()
    total_score = 0
 
    for letter in word:
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'L' or letter == 'N' or letter == 'S' or letter == 'T' or letter == 'R':
            total_score += 1

        elif letter == 'D' or letter == 'G':
            total_score += 2
        elif letter == 'B' or letter == 'C' or letter == 'M' or letter == 'P':
            total_score += 3
        elif letter == 'F' or letter == 'H' or letter == 'V' or letter == 'W' or letter == 'Y':
            total_score += 4
        elif letter == 'K':
            total_score += 5
        elif letter == 'J' or letter == 'X':
            total_score += 8
        elif letter == 'Q' or letter == 'Z':
            total_score += 10
    return total_score

print("Welcome to Scrabble!")
print("Here both the players will enter a word and the player with the highest score wins!")
a = input("Player 1, enter a word:\t")
b = input("Player 2, enter a word:\t")

score_a = Score_calculator(a)
score_b = Score_calculator(b)

print(f"\nPlayer 1 scored: {score_a}")
print(f"Player 2 scored: {score_b}\n")

if score_a > score_b:
    print("Player 1 wins!")
elif score_b > score_a:
    print("Player 2 wins!")
else:
    print("It's a tie!")




    