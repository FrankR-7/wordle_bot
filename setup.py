import string
import pickle

with open(file="words.txt", mode="r") as stream:
    dictionary = stream.readlines()

for (word, pos) in zip(dictionary, range(len(dictionary))):
    dictionary[pos] = word.strip()

with open(file="frequent.txt", mode="r") as stream:
    frequent = stream.readlines()

for (word, pos) in zip(frequent, range(len(frequent))):
    frequent[pos] = word.strip()

frequent = [word for word in frequent if len(word) == 5]

valid_words = []

for word in dictionary:
    if len(word) == 5 and not any([letter.isupper() for letter in word]):
        valid_words.append(word)

letter_freq = dict.fromkeys(string.ascii_lowercase, 0)
word_value = dict.fromkeys(valid_words, 0)

for word in valid_words:
    for letter in word:
        letter_freq[letter] += 1

letter_freq = {key: val for key, val in sorted(letter_freq.items(), key=lambda ele: ele[1], reverse=True)}
letter_freq = dict(zip(letter_freq.keys(), [i for i in reversed(range(26))]))

for word in word_value:
    for letter in word:
        word_value[word] += letter_freq[letter]
    if word in frequent:
        word_value[word] += word_value[word]/5
    if len(set(word)) != len(word):
        word_value[word] -= word_value[word]/6

word_value = {key: val for key, val in sorted(word_value.items(), key=lambda ele: ele[1], reverse=True)}

data = list(word_value.keys())

with open(file="words.pickle", mode="wb") as stream:
    pickle.dump(data, stream)
