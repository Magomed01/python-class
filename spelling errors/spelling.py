#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

An altered version of Peter Norvig's spelling corrector
(Source: http://norvig.com/spell-correct.html)

"""
from collections import Counter
import re

# Get the whitespace-delimited words from a text, minus any punctuation
def words(text): return re.findall('[a-z]+', text.lower()) 

# Count the frequency with which each word occurs
def train(features):
    model = Counter()
    for f in features:
        model[f] += 1
    return model    

# Run training using a book with words we'll consider to be spelled correctly
NWORDS = train(words(file('big.txt').read()))

# Get strings with an edit distance of 1 from the given word
def edits1(word):
   alphabet   = 'abcdefghijklmnopqrstuvwxyz'
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

# Get strings with an edit distance of 2 from the given word
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

# Get any known words matching the given mutated words
def known(words):
    return set(w for w in words if w in NWORDS)

# Suggest a correction by mutating a word and choosing the most likely replacement
# based on how often the mutated words appear in the trained model NWORDS
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    print candidates
    return max(candidates, key=NWORDS.get)

# Get the likeliest correctly-spelled word
def closest_nearby_word(word):
    nearby = set()
    for e in known(edits1(word) or known_edits2(word)):
        if (e != word):
            nearby.add(e)
    if not nearby: return set()
    return max(nearby, key=NWORDS.get)

#print correct('speling')

# Run some test cases for finding "nearby" words
for w in frozenset(['rational', 'woman', 'rogue', 'effect', 'started', 'rein',
                    'scalded', 'mislead', 'reality', 'whit', 'marshal', 'voila',
                    'aide', 'tiered', 'county', 'fires', 'stated', 'soldier',
                    'beset', 'affect', 'vice', 'wreck', 'spayed', 'complimentary',
                    'their', 'principal', 'moral', 'especially', 'steal',
                    'personal', 'why', 'heroine', 'descendant', 'baited',
                    'interested', 'sole', 'think', 'physics', 'corps', 'discrete']):
    print w, "-", closest_nearby_word(w)
