#!/usr/bin/env python3
"""
You are given a list of strings representing a paragraph of text. 
Your task is to write a Python function called word_frequency 
that takes in this list as an argument and returns a dictionary 
where the keys are unique words in the paragraph, and the values are the frequencies of those words.

Consider the following requirements:

- The function should treat words in a case-insensitive manner. 
  For example, "apple" and "Apple" should be considered the same word.
- The function should strip leading and trailing whitespace from each word.
- The function should exclude any punctuation marks attached to words. 
  For example, "apple." and "apple," should be considered the same word "apple".
- The function should exclude empty strings as words.
- The function should aim for an optimal time complexity.
"""

import re
from time import time
from collections import defaultdict, Counter
from pprint import pprint


def duration(start):
    """
    duration, μs

What is the Mu (μ)
    """
    return (time() - start) * 1_000_000


def get_words(txt):
    """
    function extracts words from the text
    """
    txt = txt.lower()
    words = re.split(r'[^\w]+', txt)
    return [word for word in words if word]


def word_frequency_1(lst):
    """
    function calculates words frequence
    defaultdict is used
    """
    start = time()
    counter = defaultdict(int)
    for words in (get_words(txt) for txt in lst):
        for word in words:
            counter[word] += 1

    return dict(counter=counter, duration=duration(start))


def word_frequency_2(lst):
    """
    function calculates words frequence
    Counter is used
    """
    start = time()
    all_words = []
    for words in (get_words(txt) for txt in lst):
        all_words += words

    return dict(counter=Counter(all_words), duration=duration(start))


def word_frequency_3(lst):
    """
    function calculates words frequence
    dict is used
    """
    start = time()
    counter = {}
    for words in (get_words(txt) for txt in lst):
        for word in words:
            counter[word] = counter.get(word, 0) + 1

    return dict(counter=counter, duration=duration(start))


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

test_txt = [paragraph, paragraph * 1000]


def execute_test(func, txt, message):
    """
    function executes test using this func
    """
    print(message)
    result = func(txt)
    pprint(result['counter'])
    print(f'Execution time is {result["duration"]:.3f}μs\n')


def main():
    """
    main function
    """
    for idx, txt in enumerate(test_txt):
        print(f'TEST {idx + 1}')

        execute_test(word_frequency_1, txt, 'Function uses defaultdict')
        execute_test(word_frequency_2, txt, 'Function uses Counter')
        execute_test(word_frequency_3, txt, 'Function uses dict')

        print('\n')

    return True


if __name__ == '__main__':
    main()



