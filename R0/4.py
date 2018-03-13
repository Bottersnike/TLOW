from requests import get
words = get('https://htcraft.ml/words').text.split('\n')

letters = 'abcdefghijklmnopqrstuvwxyz'
def tlow(sentence):
    decoded = [''.join(
            letters[letters.index(c)-i] if c in letters else c for c in sentence.lower() 
        ) for i in range(26)]

    return max([(
        len([word for word in possible.split(" ")[:100] if word in words]), possible
        ) for possible in decoded])[1]
