request = __import__("urllib.request").request.urlopen("https://goo.gl/Qc7ZJb")         #request a file with 20k words from github
words = [line.decode("utf-8")[:-1] for line in request]                                 #read lines from request, convert from bytes to str, then remove the ending newline

weights = [6.51, 1.89, 3.06, 5.08, 17.4, 1.66, 3.01, 4.76, 7.55, 0.27, 1.21, 3.44, 2.53, 9.78, 2.51, 0.29, 0.02, 7.00, 7.27, 6.15, 4.35, 0.67, 1.89, 0.03, 0.04, 1.13]
def weight(char): return weights[ord(char)-97] if char != ' ' else 0                    #use frequency of characters in english to score a character.

def caesar_ch(char, key): return chr((ord(char)+key-97)%26+97) if char != ' ' else ' '  #caesar of a single character. turns a-z into 0-26, adds i, modulos 26.
def caesar(base, key): return ''.join([caesar_ch(char, key) for char in base])          #caesar of a string. calls caesar_ch on each character in the string.

def main(encoded):                                                                      #call this function to decipher.
    arr = [sum([int(word in words) for word in caesar(encoded,i).split()])+1 for i in range(26)]#for each possible key, look at the caesar of s for that key. arr[key] is the number of common words in the sentence.
    arr = [a*b for a,b in zip(arr,[sum([weight(char) for char in caesar(encoded,i)]) for i in range(26)])]#multiply by the letter weight of each string.
    return caesar(encoded, arr.index(max(arr)))                                         #find the max of arr, then find the key used to generate it with index. use that key with caesar() to get our best candidate.