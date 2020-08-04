#!/usr/bin/env python 
import os
import sys
import random
import json
import uuid

alpha_dict = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "v",
  "w",
  "x",
  "y",
  "z"
]

num_dict = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]

options = {
  "words": int(os.environ.get('words') or 4),
  "word_length": int(os.environ.get('word_length') or 3),
  "separator": os.environ.get('separator') or "-",
  "max_repeats": int(os.environ.get('max_repeats') or 2),
}

'''
Store the alredy used password letters count
in order to check for max repeating letters
'''
used_letters = {}
have_number = False
have_upper = False

# Generate a random boolean
def random_bool():
  return bool(random.getrandbits(1))

# Extract a random letter or number from dictionary
def random_letter():
  letter = random.choice(alpha_dict)
  if letter in used_letters:
    if used_letters[letter] is options["max_repeats"]:
      return random_letter()
    else:
      used_letters[letter] += 1
  else:
    used_letters[letter] = 1
  return letter

# Replace a random character from a word in a word list with the uppercase
# version or with a random number
def replace(word_list, number=False):
	word_id = random.randint(0, 2)
	rnd_word = word_list[word_id]
	letter_id = random.randint(0, len(rnd_word)) - 1
	if number:
		replacement = random.choice(num_dict)
	else:
		replacement = rnd_word[letter_id].upper()
	rnd_word = rnd_word[:letter_id] + replacement + rnd_word[letter_id:]
	word_list[word_id] = rnd_word
	return word_list

# Create random password
def generate_password():
	word_list = []
	for i in range (0, options["words"]):
		new_word = ""
		for j in range(0, options["word_length"]):
			new_word += random_letter()
		word_list.append(new_word)
	word_list = replace(word_list)
	word_list = replace(word_list, True)
	return options["separator"].join(str(x) for x in word_list)

'''
Generates a new random password then creates the script filter
object used by alfred to show the password in the result list
'''
new_password = generate_password()
script_filter_result = json.dumps({
  "items": [
    {
      "uid": str(uuid.uuid4()),
      "title": new_password,
      "subtitle":  "Action this item to copy this password to the clipboard",
      "arg": new_password,
      "text": {
        "copy": new_password,
        "largetype": new_password
      }
    }
  ]
})
sys.stdout.write(script_filter_result)