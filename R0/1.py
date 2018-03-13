import re
lex = set(open('dict/enable2k.txt').read().split('\n'))
def caesar26(string):
  bestwords, beststring, string = 0, string, string.lower()
  for i in range(26):
    string = ''.join(map(lambda x: chr(ord(x)+1) if ord('a') <= ord(x) <= ord('y') else ('a' if x == 'z' else x), string))
    if len(set(re.split('[^a-zA-Z]', string))&lex) > bestwords:
      bestwords, beststring = len(set(re.split('[^a-zA-Z]', string))&lex), string
  return beststring

