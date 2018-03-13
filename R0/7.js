const en_letter_freqs = [8,1,2,4,12,2,2,6,6,0,0,4,2,6,7,1,0,5,6,9,2,0,2,0,1,0]
//calculate the cross-entropy by summing the frequency for each letter
const entropy = str => str.reduce((a, e) => a + ~~en_letter_freqs[e], 0)
//guess the right decryption by testing all possible keys
const decrypt = str => en_letter_freqs.map((_, key) =>
        //decrypt with each key by adding it to the char code (if not a space)
        str.split('').map(e => e == " " ? -65 : (e.charCodeAt(0) + key) % 26))
    //sort the decrypted messages by entropy and get the one with lowest entropy
    .sort((a, b) => entropy(b) - entropy(a))[0]
    .map(e => String.fromCharCode(e + 97)).join('') //key codes to string again
