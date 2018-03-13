from string import ascii_lowercase

def caesar_decoder(encoded):
    letters_in_input = [(i in ascii_lowercase and ascii_lowercase.index(i) + 1 or 0) - 1 for i in encoded.lower()] # index in alphabet for letters, -1 for anything else
    scores, letter_frequencies = [], [8.12, 1.49, 2.71, 4.32, 12.02, 2.30, 2.03, 5.92, 7.31, 0.10, 0.69, 3.98, 2.61, 6.95, 7.68, 1.82, 0.11, 6.02, 6.28, 9.10, 2.88, 1.11, 2.09, 0.17, 2.11, 0.07]  
    
    for i in range(26):
        scores.append(0)

        for i in range(26):
            scores[-1] += abs(letters_in_input.count(i) / len(letters_in_input) - letter_frequencies[i]) ** 2 # Calculates the average error

        letters_in_input = [i == -1 and -1 or (i + 1) % 26 for i in letters_in_input]
        
    return "".join([i == -1 and " " or ascii_lowercase[(i + scores.index(min(scores))) % 26] for i in letters_in_input])
