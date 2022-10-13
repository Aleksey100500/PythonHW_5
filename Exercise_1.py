# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect
import sys
import random
import re

def check_number():
    try:
        number = int(input('Enter your number: '))
        print(f'Number of words: {number}')
        if number < 0:
            sys.exit('The data is incorrect.')
        return number
    except ValueError:
        print('Try again.')
        return check_number()

def generator_rand_words(length,slovo):
    letters = slovo
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def its_text(number):
    new_text = ''
    word = str(input('Enter your word: '))
    word_len = len(word)
    for i in range(number):
        a = generator_rand_words(word_len, word)
        new_text = a + ' ' + new_text
    print(new_text)
    return new_text

def finder(text):
    deleted_word = str(input('Word to be deleted: '))
    poped_text = re.sub(rf'{deleted_word}+\s?', '', text).strip()
    return poped_text


def Main():
    digit = check_number()
    find_text = its_text(digit)
    result = finder(find_text)
    print(result)
Main()