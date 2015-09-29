import random
file = open("test.txt", 'r')

lines = file.readlines()
words = []
trigrams = {}
start_phrase = "I wish"

for line in lines:
    words += line.split()

for i in (range(len(words) - 2)):
    phrase = words[i] + " " + words[i + 1]
    if (phrase in trigrams):
        trigrams[phrase].append(words[i + 2])
    else:
        trigrams[phrase] = [words[i + 2]]

done = False

word_2 = start_phrase.split()[0]
word_1 = start_phrase.split()[1]
sentance = start_phrase
j = 0

while not done:
    j = j + 1
    phrase = word_2 + " " + word_1
    if (phrase in trigrams):
        numb_of_words = len(trigrams[phrase]) - 1
        i = random.randint(0, numb_of_words)
        list_words = trigrams[phrase]
        new_word = list_words[i]
        sentance = sentance + " " + new_word
        word_2 = word_1
        word_1 = new_word

    else:
        done = True

print(sentance)

file.close()
