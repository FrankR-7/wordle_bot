import pickle

with open(file="words.pickle", mode="rb") as stream:
    valid_words = pickle.load(stream)

# Game starts

n_letters = set()
y_letters = {}
y_key = []
g_letters = {}
g_key = []

c_words = valid_words[:5]
c_word = "wordle_bot.py"

print(f'Start with {c_words}')
ind =int(input("Which word worked? index: "))
c_word = c_words[ind - 1]
skip_words = c_words[:ind]

for i in range(6):
    temp_words = {}
    response = input("Please insert wordle's response with the notation g for green, y for yellow and n for grey: ")
    if len(response) != 5:
        print("The response must be 5 characters long, try again")
        break
    elif response == "ggggg":
        print("Congrats!")
        exit()

    for (character, letter, pos) in zip(response, c_word, range(5)):
        if character == "n":
            if (letter not in y_key) and (letter not in g_key):
                n_letters.add(letter)
        elif character == "y":
            if letter in n_letters:
                n_letters.remove(letter)
            if letter in y_key:
                y_letters[letter].add(pos)
            else:
                y_letters[letter] = {pos}
        elif character == "g":
            if letter in n_letters:
                n_letters.remove(letter)
            # if letter in y_key:
            #     y_letters.pop(letter)
            if letter in g_key:
                g_letters[letter].add(pos)
            else:
                g_letters[letter] = {pos}

        y_key = list(y_letters.keys())
        g_key = list(g_letters.keys())

    for word in valid_words:
        elo = 0
        if any([letter in n_letters for letter in word]):
            continue
        elif word in skip_words:
            continue
        else:
            for (letter, pos) in zip(word, range(5)):
                if letter in y_key:
                    elo -= 0.5
                if letter in y_key and pos not in y_letters[letter]:
                    elo += 2
                if letter in y_key and pos in y_letters[letter] and letter in g_key and pos not in g_letters[letter]:
                    elo -= 3
                if letter in g_key:
                    elo -= 0.5
                if letter in g_key and pos in g_letters[letter]:
                    elo += 3
            if len(set(word)) != 5:
                elo -= 1.5*(5-len(set(word)))
            temp_words[word] = elo

    temp_words = {key: val for key, val in sorted(temp_words.items(), key=lambda ele: ele[1], reverse=True)}

    valid_words = list(temp_words.keys())

    c_words = valid_words[:5]
    print(f'Try {c_words}')
    ind =int(input("Which word worked? index: "))
    c_word = c_words[ind - 1]
    skip_words = c_words[:ind]
