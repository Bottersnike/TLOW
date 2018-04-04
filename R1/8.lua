function count_factors(number) local factors = 0;
    for i = 1, number do if number % i == 0 then factors = factors + 1; end end
    return factors;
end
function max_factors(min, max) local max_ints = {}; local max_factors = 0;
    for i = min, max - 1 do
        if count_factors(i) > max_factors then max_factors = count_factors(i); max_ints = {i};
        elseif count_factors(i) == max_factors then table.insert(max_ints, i); end
    end; return max_ints;
end