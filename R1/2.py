num_factors = lambda x: sum(x % y is 0 for y in range(2,x))
def main(a, b):
    if a is b: return [a]
    num_list = [num_factors(i) for i in range(a,b)]
    max_num = max(num_list)
    final_list = []
    for num in range(a, b):
        if num_list[num-a] is max_num:
            final_list.append(num)
    return final_list
