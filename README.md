# markov-text-generator
A program which generates text using the Markov Chain model, with experimental probabilities calculated from a source text.

The program reads through text from a source file, calculates the probability of each word in the text following a given word (by counting), and uses these probabilities to create a transition matrix.

A random word is then selected and the program generates a 100-word text using the matrix.

The source text used is an extract of the book "Winter Sports in Switzerland".

## Dependencies

[Numpy](https://github.com/numpy/numpy)
