# Wordle Solver 3Blue1Brown Style
Learning attempt based on 3Blue1Brown's approach to solving Wordle.

 # Requirements 
 Numpy,
 Pandas,
 All possible Wordle Guesses as a csv or txt file.

 # Features
Pattern-based filtering,
Shannon Entropy-based ranking of word choice options.

# Model
The input which is comprised of a word and a pattern is used as data to filter out words from the initial list of all possible guesses, and then the next best guess is derived from the sorted list of Shannon Entropies of all the words in the input based filtered list. 
The model repeats this till it has narrowed the list to one solution.
It solves Wordle on average in 3-4 chances.
This model is an educational project.
