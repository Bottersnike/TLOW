alphabet = "abcdefghijklmnopqrstuvwxyz"
syllables = "ing er a ly ed i es re tion in e con y ter ex al de com o di en an ty ry u ti ri be per to pro ac ad ar ers ment or tions ble der ma na si un at dis ca cal man ap po sion vi el est la lar pa ture for is mer pe ra so ta as col fi ful get low ni par son tle day ny pen pre tive car ci mo an aus pi se ten tor ver ber can dy et it mu no ple cu fac fer gen ic land light ob of pos tain den ings mag ments set some sub sur ters tu af au cy fa im li lo men min mon op out rec ro sen side tal tic ties ward age ba but cit cle co cov daq dif ence ern eve ies ket lec main mar mis my nal ness ning n't nu oc pres sup te ted tem tim tri tro up"

def caesar_decipher(text):
    result = (-1, text) # Item 0 is score, item 1 is text

    for i in range(26): # Decode ciphertext, then record number of commonly used syllables present, favouring longer syllables
        decoded = "".join([(alphabet[i:] + alphabet[:i])[alphabet.index(c)] if c in alphabet else c for c in text]) 

        score = sum(decoded.count(s) * 2 ** len(s) for s in syllables.split(' '))

        if score > result[0]:
            result = (score, decoded) # Keep track of max

    return "".join(result[1]) # Done!
