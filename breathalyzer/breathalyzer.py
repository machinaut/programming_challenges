#!/usr/bin/env python
import string, sys 

wordlist = set(map(string.lower,open('twl06.txt').readlines()[:-2]))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# this is from Peter Norvig's 21-line Python Spell Checker. Its amazing. Check it out.
def edits1(word):
   s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in s if b]
   replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
   inserts    = [a + c + b     for a, b in s for c in alphabet]
   return set(deletes + replaces + inserts)

# iteratively apply edits1 to sets of words to find their score
words = open(sys.argv[1]).readline().split()
score = 0
for word in words:
    print 'doing word', word
    if word in wordlist:
        print 'found wrod on 0', word
        continue
    print 'not found word on 0', word
    displace = 1
    dwords = edits1(word)
    print 'dwords', dwords
    while True:
        print 'whiles'
        if dwords & wordlist == set():
            print 'found'
        print 'not found'
        displace += 1
        cwords = set(dwords)
        for dispword in cwords:
            dwords |= edits1(dispword)
    score += displace

