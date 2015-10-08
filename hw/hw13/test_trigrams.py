#!/usr/bin/env python

"""
code that tests the circle class defined in trigrams.py

can be run with py.test
"""

import pytest  # used for the exception testing
# import StringIO

import trigrams


def test_open_file():
    trigrams.open_file('sherlock_small.txt')


def test_tuple():
    test_phrase = "test phrase"
    assert(trigrams.phrase_to_tuple(test_phrase) == ('test', 'phrase'))


def test_create_word_dictionary():
    text = ("I wish I may I wish I might")
    # text_file = StringIO.StringIO(text)
    my_dict = {('I', 'may'): ['I'], ('may', 'I'): ['wish'],
               ('I', 'wish'): ['I', 'I'], ('wish', 'I'): ['may', 'might']}

    assert(trigrams.create_word_dictionary(text) == my_dict)
