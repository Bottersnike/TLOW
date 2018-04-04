f=lambda ω,σ,_=range:[α[0]for(α)in([(α,len([ψ for(ψ)in _(1,α)if α%ψ==0]))for(α)in _(ω,σ+1)])if α[1]==max([(α,len([ψ for(ψ)in _(1,α)if α%ψ==0]))for(α)in _(ω,σ+1)],key=lambda α:α[1])[1]]

#f=lambda n,i=1:i/n or(n%i<1)+f(n,i+1)
#[ψ for(ψ)in _(1,α)if α%ψ==0]

def f(ω,σ,_=range):ε=[(α,len([ψ for(ψ)in _(1,α)if α%ψ==0]))for(α)in _(ω,σ+1)];return[α[0]for(α)in(ε)if α[1]==max(ε,key=lambda α:α[1])[1]]
def f(ω,σ,_=range):ε=[(sum(α%-~ψ<1for(ψ)in _(α)),α)for(α)in _(ω,σ+1)];return[α[1]for(α)in(ε)if α[0]==max(ε)[0]]

import random
for i in range(5):
    a = random.randint(1, 500)
    b = a + random.randint(1, 500)

    print(f'`{a}, {b} -> {f(a, b)}`')
