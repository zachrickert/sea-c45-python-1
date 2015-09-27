file = open("sherlock_small.txt", r)

lines = file.readlines()
words = []
trigrams = {}

for line in lines:
    words += line.split(' ')

for i, word in enumerate(words):
    trigrams[(word, words[i+1])] = words[i+2]

print(str(words))
print(str(trigrams))
