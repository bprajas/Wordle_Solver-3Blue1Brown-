import pandas as pd
import numpy as np

df=pd.read_csv('/content/valid-words.csv')
df.columns=['matches']
display(df.head())
print(len(df))

def pattern_match(guess, answer):
    pattern=[0]*5
    answer_chars=list(answer)
    for i in range(5):
        if guess[i]==answer[i]:
            pattern[i]=2
            answer_chars[i]=None
    for i in range(5):
        if pattern[i]==0 and guess[i] in answer_chars:
            pattern[i]=1
            answer_chars[answer_chars.index(guess[i])] = None
    return pattern

base_words=[w.upper() for w in df['matches'].values]
guesses=base_words.copy()

history=[]

while True:
    wrd=input("Enter guessed word (5 letters, or STOP): ").upper()
    if wrd=="STOP":
        break

    patt=input("Enter pattern (0 grey, 1 yellow, 2 green): ")
    patt=[int(x) for x in patt]

    history.append((wrd, patt))

    candidates=base_words.copy()
    for g, p in history:
        candidates = [w for w in candidates if pattern_match(g, w) == p]

    if len(candidates)==0:
        print("No Candidates remaining.")
        break

    if len(candidates)==1:
        print("Solution: ", candidates[0])
        break

    entropies=[]
    for guess in guesses:
        pattern_counts={}
        for answer in candidates:
            code = tuple(pattern_match(guess, answer))
            pattern_counts[code]=pattern_counts.get(code, 0) + 1

        total = len(candidates)

        entropy = 0
        for count in pattern_counts.values():
            p = count/total
            entropy+=-1*p*np.log2(p)
        entropies.append(entropy)

    best_index = np.argmax(entropies)

    print("Remaining candidates:", len(candidates))
    print("Next guess:", guesses[best_index])
    print("Entropy:", entropies[best_index])
