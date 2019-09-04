import numpy
import string


with open("Text.txt", "r", encoding="utf-8") as f:
    original = f.read()

original = original.replace("\n", " ").split()

punc = [x for x in string.punctuation]
punc.remove("-")
punc = "".join(punc)
accepted = [x for x in string.ascii_letters]
accepted.append("-")
source = []

for x in original:
    x = list(x)

    for y in x:
        if y not in accepted:
            x.remove(y)

    x = "".join(x).lower()
    source.append(x)

# reads the source text, converts to lowercase and strips all punctuation
# stores all of the words in order in a list

words = []
for x in source:
    if x not in words:
        words.append(x)

size = len(words)

matrix = [[0 for y in range(size)] for x in range(0, size)]
# an empty matrix to store all of the probabilities
index = {y: x for x, y in enumerate(words)}
# gives the position of every word in the row

length = len(source) - 1

for i, x in enumerate(source):
    if i == length:
        break
    first = index[x]
    second = index[source[i+1]]
    matrix[first][second] += 1
    # counts the occurrence of two consecutive words in the matrix

for x in matrix:
    total = sum(x)
    for i, y in enumerate(x):
        y /= total  # divides the count by the total sample space to find prob
        x[i] = y

state = numpy.random.choice(words)  # initial state, randomly chosen word

output = [state]
text_len = 100

for x in range(text_len):
    pos = words.index(state)
    dist = matrix[pos]
    state = numpy.random.choice(words, p=dist)
    output.append(state)
    # transitions between states (words) using the experimental probabilities
    # only the current state (last word) is remembered

output = " ".join(output)
print(output)
