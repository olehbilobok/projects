"""English PL RU
Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase."""

MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    data = []
    final = []
    for x in code.split(' '):
        data.append(x)
    count = 0
    for x in data:
        if x == '':
            count += 1
            if count == 2:
                final.append(' ')
                count = 0
        if x in MORSE:
            final.append(MORSE[x])
    return ''.join(final).capitalize()


print(morse_decoder("... --- -- .   - . -..- -"))
print(morse_decoder("..--- ----- .---- ---.."))
print(morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--"))
