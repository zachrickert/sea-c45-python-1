#!/usr/bin/env python

"""
code that tests the circle class defined in trigrams.py

can be run with py.test
"""

import trigrams


def test_open_file():
    trigrams.open_file('wish.txt')


def test_tuple():
    test_phrase = "test phrase"
    assert(trigrams.phrase_to_tuple(test_phrase) == ('test', 'phrase'))


def test_add_trigram():
    phrase = 'test phrase'
    tri = {}
    word1 = 'numb1'
    word2 = 'numb2'
    test_phrase = trigrams.phrase_to_tuple(phrase)
    trigrams.add_trigrams(test_phrase, word1, tri)
    assert(tri == {('test', 'phrase'): ['numb1']})
    trigrams.add_trigrams(test_phrase, word2, tri)
    assert(tri == {('test', 'phrase'): ['numb1', 'numb2']})


def test_pick_next_word():
    phrase1 = ('test', 'numb1')
    phrase2 = ('test', 'numb2')
    tri = {('test', 'numb1'): ['passed'], ('test', 'numb2'): ['a', 'b', 'c']}
    test1 = trigrams.pick_next_word(phrase1, tri)
    test2 = trigrams.pick_next_word(phrase2, tri)
    assert(test1 == 'passed')
    assert(test2 in ('a', 'b', 'c'))


def test_add_word():
    sentance = 'This is just a'
    next_word = 'test'
    sentance = trigrams.append_word(sentance, next_word)
    assert(sentance == 'This is just a test')
