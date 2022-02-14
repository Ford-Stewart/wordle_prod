#https://www.youtube.com/watch?v=v68zYyaEmEA
#crane is best
#OLD NEWS salet is new best crate closely following
#soare is my FAV
import json
known = {}
pos = list("qwertyuiopasdfghjklzxcvbnm")
yellow_charecters = {}

class ValidWordException(Exception):
    def __init__(self, message='ValidWord'):
        super(ValidWordException, self).__init__(message)

def make_guess():
    global known, pos, yellow_charecters
    guesses = []
    (pos1, pos2, pos3, pos4, pos5) = (pos.copy(), pos.copy(), pos.copy(), pos.copy(), pos.copy())
    try:
        pos1.remove(yellow_charecters[0])
    except:
        pass
    try:
        pos2.remove(yellow_charecters[1])
    except:
        pass
    try:
        pos3.remove(yellow_charecters[2])
    except:
        pass
    try:
        pos4.remove(yellow_charecters[3])
    except:
        pass
    try:
        pos5.remove(yellow_charecters[4])
    except:
        pass

    for key, value in known.items():
        if key == 0:
            pos1 = list(value * len(pos))
        if key == 1:
            pos2 = list(value * len(pos))
        if key == 2:
            pos3 = list(value * len(pos))
        if key == 3:
            pos4 = list(value * len(pos))
        if key == 4:
            pos5 = list(value * len(pos))
    done_precent = 0
    for i1 in pos1:
        for i2 in pos2:
            for i3 in pos3:
                for i4 in pos4:
                    for i5 in pos5:
                        guesses.append(i1+i2+i3+i4+i5)
        done_precent += 100 / len(pos)
        print(f"{int(done_precent)}% done making guesses table")
    print("Created guesses table now removing duplicates")
    pre_size = len(guesses)
    guesses = list(set(guesses))
    print("Removed duplicates")
    print(f"shunk size by {pre_size / len(guesses) * 100}%")
    pre_size = len(guesses)
    if yellow_charecters != {}:
        print("now removing words without yellow charecters")
        yellow_guesses = []
        [yellow_guesses.append(y) for y in guesses if all([x in y for x in yellow_charecters.values()])]
        print("Removed choices invalidated due to not having yellow charecters")
        print(f"shunk size by {pre_size / len(guesses) * 100}%")
        guesses = yellow_guesses
        print("Removing duplicates again")
        pre_size = len(guesses)
        guesses = list(set(guesses))
        print("Removed duplicates")
        print(f"shunk size by {pre_size / len(guesses) * 100}%")
    print("now checking validity of words")
    file = open("words_dictionary.json", "r")
    word_list = json.loads(file.read())
    valid_words_found = []
    def valid_word_operations(arg):
        nonlocal valid_words_found
        valid_words_found.append(arg)
        if len(set(arg)) == len(arg):
            global guess_recomendation
            guess_recomendation = arg
            raise ValidWordException
    guesses.sort()
    for x in guesses:
        [valid_word_operations(y) for y in word_list if x == y]
    file.close()
    return(valid_words_found[0])

print("""Hi this a tool used to solve wordle puzzles
I made myself cause I was tired,
tired of being on my final guess looking through
yes a literal dictionary tying to win

anyhow heres the actual program
""")
guess_recomendation = "salet"
while True:
    to_parse = list(input(f"Guess the word {guess_recomendation} now\n\nNow type the *last* letter of each resulting color from the guess below\nEX: \u001b[33mw\u001b[37myy\u001b[32mn\u001b[37my\n"))
    for i in range(5):
        char = guess_recomendation[i]
        on_parse = to_parse[i]
        if on_parse == "y":
            pos.remove(char)
        elif on_parse == "w":
            yellow_charecters[i] = char
        elif on_parse == "n":
            known[i] = char
        else:
            raise Exception(f"Invalid charecter used in user input in column {i}")
    try:
        guess_recomendation = make_guess()
    except ValidWordException: 
        pass