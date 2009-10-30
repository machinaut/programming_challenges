#!/usr/bin/env python
import sys

def edits1(word):
    """
    this is from Peter Norvig's 21-line Python Spell Checker. Its amazing
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in s if b]
    replaces   = [a + c + b[1:] for a, b in s for c in alphabet if b]
    inserts    = [a + c + b     for a, b in s for c in alphabet]
    return set(deletes + replaces + inserts)

def calc(words, wordlist):
    """
    iteratively apply edits1 to sets of words to find their score
    """
    score = 0
    for word in words:
        if word in wordlist:
            continue
        displace = 1
        dwords = edits1(word)
        while True:
            if dwords & wordlist != set():
                break
            displace += 1
            cwords = set(dwords)
            for dispword in cwords:
                dwords |= edits1(dispword)
        score += displace
    return score

if __name__ == "__main__":
    if len(sys.argv) < 2: print 'Please provide inputfile'; exit(1)
    words = open(sys.argv[1]).readline().split()
    if len(sys.argv) == 2:
        wordfile = 'var/tmp/twl06.txt'
    else:
        wordfile = sys.argv[2]
    wordlist = set(map(lambda a: a.strip().lower(),open(wordfile).readlines()))
    print calc(words, wordlist)
