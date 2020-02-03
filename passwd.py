#!/usr/bin/env python 
import os
import sys
import random

dictionary = [
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
  "z",
  "0",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9"
]

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

# Generate a random boolean
def is_upper():
  return bool(random.getrandbits(1))

# Extract a random letter or number from dictionary
def random_letter():
  letter = random.choice(dictionary)
  if letter in used_letters:
    if used_letters[letter] is options["max_repeats"]:
      return random_letter()
    else:
      used_letters[letter] += 1
  else:
    used_letters[letter] = 1
  if is_upper() : letter = letter.upper()
  return letter

# Extract a random password
def generate_password():
  password = ""
  for i in range (0, options["words"]):
    for j in range(0, options["word_length"]):
      password += random_letter()
    password += options["separator"]
  # removes the last unwanted separator
  return password[:-1]

sys.stdout.write(generate_password())
