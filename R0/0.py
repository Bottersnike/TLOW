S = 'abcdefghijklmnopqrstuvwxyz'
LG = [.0817,.0149,.0278,.0425,.1270,.0223,.0202,.0609,.0697,
      .0015,.0077,.0402,.0241,.0675,.0751,.0193,.0009,.0599,
      .0633,.0906,.0276,.0098,.0236,.0015,.0197,.0007]

def t0(s):
  return max([
    ''.join(S[S.index(i) - n]
            for i in s if i in S)
    for n in range(26)
  ], key=lambda s: sum(LG[S.index(i)] for i in s) / len(s))

