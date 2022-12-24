while True:
    prompt = input("Word: ")
    for (letter, pos) in zip(word, range(5)):
            if letter in n_letters:
                valid_words.remove(word)
                break
            elif letter in y_key and pos in y_letters[letter]:
                valid_words.remove(word)
                break
            elif letter in g_key and g_letters[letter] != pos:
                valid_words.remove(word)
                break