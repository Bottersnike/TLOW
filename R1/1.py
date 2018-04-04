def f(ω,σ,_=range):ε=[(α,len([ψ for(ψ)in _(1,α)if α%ψ==0]))for(α)in _(ω,σ+1)];return[α[0]for(α)in(ε)if α[1]==max(ε,key=lambda α:α[1])[1]]
