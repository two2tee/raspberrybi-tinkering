from time import sleep
from gpiozero import LED
from gpiozero import Buzzer

led = LED(4)
buzzer = Buzzer(17)

# seconds
dot = 0.05
dash = dot * 3
time_between_letters = dash
time_between_words = dot * 7

morse_alphabet = {
    "A": [dot, dash],
    "B": [dash, dot, dot, dot],
    "C": [dash, dot, dash, dot],
    "D": [dash, dot, dot],
    "E": [dot],
    "F": [dot, dot, dash, dot],
    "G": [dash, dash, dot],
    "H": [dot, dot, dot, dot],
    "I": [dot, dot],
    "J": [dot, dash, dash, dash],
    "K": [dash, dot, dash],
    "L": [dot, dash, dot, dot],
    "M": [dash, dash],
    "N": [dash, dot],
    "O": [dash, dash, dash],
    "P": [dot, dash, dash, dot],
    "Q": [dash, dash, dot, dash],
    "R": [dot, dash, dot],
    "S": [dot, dot, dot],
    "T": [dash],
    "U": [dot, dot, dash],
    "V": [dot, dot, dot, dash],
    "W": [dot, dash, dash],
    "X": [dash, dot, dot, dash],
    "Y": [dash, dot, dash, dash],
    "Z": [dash, dash, dot, dot]
}


def convert_to_morse_word(wordStr):
    characters = [char for char in wordStr.upper()]
    word_morse = [
        morse_alphabet[char]
        for char in characters
    ]

    return word_morse

def convert_paragraf_to_morse(paragraf):
    words = paragraf.split(' ')
    morse_words = [convert_to_morse_word(word) for word in words]
    return morse_words

def blink(on_time, off_time):
    led.on()
    buzzer.on()
    sleep(on_time)
    led.off()
    buzzer.off()
    sleep(off_time)

def blink_morse_letter(morse_letter):
    for morse_unit in morse_letter:
        blink(on_time = morse_unit, off_time = time_between_letters)

def blink_morse_word(morse_word):
    for morse_letter in morse_word:
        blink_morse_letter(morse_letter)

def blink_morse(morse_words):
    for morse_word in morse_words:
        blink_morse_word(morse_word)
        sleep(time_between_words)



## main

input = "sos"
print(f'input: {input}')

morse = convert_paragraf_to_morse(input)

print(f'morse: {morse}')

while True:
    blink_morse(morse)
    sleep(time_between_words)