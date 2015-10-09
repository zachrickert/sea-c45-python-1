import random


def open_file(file_to_open):
    file = open(file_to_open, 'r')
    return file


def create_word_dictionary(file):
    lines = file.readlines()
    words = []
    trigrams = {}

    for line in lines:
        words += line.split()

    for i in (range(len(words) - 2)):
        phrase = (words[i], words[i + 1])
        next_word = words[i + 2]
        add_trigrams(phrase, next_word, trigrams)
    return trigrams


def add_trigrams(phrase, next_word, trigrams):
    if (phrase in trigrams):
        trigrams[phrase].append(next_word)
    else:
        trigrams[phrase] = [next_word]


def phrase_to_tuple(phrase):
    word1 = phrase.split()[0]
    word2 = phrase.split()[1]

    return (word1, word2)


def pick_next_word(phrase, trigrams):
    numb_of_words = len(trigrams[phrase]) - 1
    i = random.randint(0, numb_of_words)
    list_words = trigrams[phrase]
    return list_words[i]


def append_word(sentance, word):
    return sentance + ' ' + word


def main():
    file_to_open = "wish.txt"
    file = open_file(file_to_open)

    start_phrase = "I wish"
    trigrams = create_word_dictionary(file)

    phrase = phrase_to_tuple(start_phrase)

    sentance = start_phrase

    done = False
    j = 0

    while not done:
        j = j + 1
        if (phrase in trigrams):
            new_word = pick_next_word(phrase, trigrams)
            sentance = append_word(sentance, new_word)
            phrase = (phrase[1], new_word)
        else:
            done = True

    print(sentance)

    file.close()

if __name__ == '__main__':
    main()
