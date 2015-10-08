import random


def open_file(file):
    file = open("test.txt", 'r')
    return file


def create_word_dictionary(file):
    lines = file.readlines()
    words = []
    trigrams = {}

    for line in lines:
        words += line.split()

    for i in (range(len(words) - 2)):
        phrase = (words[i], words[i + 1])
        if (phrase in trigrams):
            trigrams[phrase].append(words[i + 2])
        else:
            trigrams[phrase] = [words[i + 2]]

    return trigrams


def phrase_to_tuple(phrase):
    word1 = phrase.split()[0]
    word2 = phrase.split()[1]

    return (word1, word2)


def pick_next_word(phrase, trigrams):
    numb_of_words = len(trigrams[phrase]) - 1
    i = random.randint(0, numb_of_words)
    list_words = trigrams[phrase]
    return list_words[i]


def main():
    file = open_file("test.txt")
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
            sentance = sentance + " " + new_word
            phrase = (phrase[1], new_word)
        else:
            done = True

    print(sentance)

    file.close()


main()
