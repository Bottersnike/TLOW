def caesar26(string):
  code = """common_bigrams = [code[i]+code[i+1] for i in range(len(code)-1)] #this line is just to compute which bigrams appear with no discrimination.
beststring, bestval = "", 0 #hello here is some very messy and probably quite inaccurate code.  clearly the best way to provide a good sample of bigrams
for j in range(26): # is to feed the source code itself as a very small corpus for analysis! however, it still needs some additional text to fill things
  string = ''.join(list(map(lambda x: chr(ord(x)-1) if ord('b') <= ord(x) <= ord('z') else ('z' if x == 'a' else x), string))) #up. so please enjoy this
  if sum([string.count(b) for b in common_bigrams]) > bestval: # fairly arbitrary text that has nothing to do with the code itself, but should be pretty
    beststring, bestval = string, sum([string.count(b) for b in common_bigrams]) #representative of english language. it's also very safe, secure code"""
  locals_ = locals()
  exec(code, locals_, locals_)
  return locals_['beststring']
