# Mapping of morse letters with Latin letters.
morse = {
  '.-': 'A',
  '-...': 'B',
  '-.-.': 'C',
  '----': 'CH',
  '-..': 'D',
  '.': 'E',
  '..-.': 'F',
  '--.': 'G',
  '....': 'H',
  '..': 'I',
  '.---': 'J',
  '-.-': 'K',
  '.-..': 'L',
  '--': 'M',
  '-.': 'N',
  '--.--': 'Ñ',
  '---': 'O',
  '.--.': 'P',
  '--.-': 'Q',
  '.-.': 'R',
  '...': 'S',
  '-': 'T',
  '..-': 'U',
  '...-': 'V',
  '.--': 'W',
  '-..-': 'X',
  '-.--': 'Y',
  '--..': 'Z',
  '.----': '1',
  '..---': '2',
  '...--': '3',
  '....-': '4',
  '.....': '5',
  '-....': '6',
  '--...': '7',
  '---..': '8',
  '----.': '9',
  '-----': '0',
  '.-.-.-': '.',
  '-.-.--': ',',
  '..--..': '?',
  '.-..-.': '"',
  '--..--': '!'
}

morse_code = input("Escriba el código morse: ")

# Decode the morse code.
morse_words = morse_code.split()

decoded_words = ''
for morse_word in morse_words:
  morse_letters = morse_word.split('|')

  decoded_word = ''
  for letter in morse_letters:
    decoded_word = decoded_word + morse[letter]

  decoded_words = decoded_words + decoded_word + ' '

print(decoded_words)
