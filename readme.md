# Wordle Bot
---
What else did you expect, it solves (or at least tries to solve) Wordle.

### How it works
It takes in a dictionary and ranks each word depending on an elo ranking that depends on how frequent the letters in it are, how frequent the word itself is and how many repeated letters it has. Every time you give it feedback it removes words and re-ranks this list of words again until you get today's word.

### How To Use
Just run `wordle_bot.py` and follow the on-screen instructions.

It will first show you a list of words that are more likely to be today's word. Type these one by one into the game until the game accepts one (there is actually a small chance that it will reject a word but it's also there in case you don't like the best answer as much as the bot).

Give it the index in the range of 1-5 of the word that you gave Wordle and tap Enter.

Then type in the colors that Wordle gave each letter, in the notation g for green, y for yellow and n for grey. For example, if for a word it gave you yellow-green-yellow-grey-grey you'd type in `ygynn` and hit Enter.

The program will give you another list of words to try. Rinse and repeat until you get `ggggg`.