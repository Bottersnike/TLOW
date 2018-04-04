def factors(num)
    (1..num).select { |n| num % n == 0 }.length
end

def r1(a, b)
    most_factors = (a..b).map { |n| factors(n) }.max
    return (a..b).select { |n| factors(n) == most_factors }
end
