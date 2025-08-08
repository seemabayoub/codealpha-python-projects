import random
terms = ['mystic', 'shadow', 'phantom', 'cyborg', 'mirage']
term = random.choice(terms)
screen = []
for char in term:
    screen.append('_')
guessed = []
misses = 0
max_misses = 7
while "_" in screen and misses < max_misses:
    print("\nTerm: ", end="")
    for letter in screen:
        print(letter, end=" ")
    print("\nMisses left:", max_misses - misses)
    print("Used letters: ", end="")
    for ltr in guessed:
        print(ltr, end=" ")
    print()
    attempt = input("Pick a letter: ").lower()
    if attempt in guessed:
        print("Already tried")
        continue
    guessed.append(attempt)
    if attempt in term:
        for i in range(len(term)):
            if term[i] == attempt:
                screen[i] = attempt
        print("Good guess")
    else:
        misses += 1
        print("Incorrect")
print("\nThe term was:", term)
if "_" not in screen:
    print("You won")
else:
    print("Game over")