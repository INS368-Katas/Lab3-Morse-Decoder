letter_to_morse = {
  '.-': 'A',
  '-..': 'B',
  '-.-.': 'C',
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
}
converted_phrase = ''
morse_code = input("Escriba el código morse: ")

# Separate letters by |
words = morse_code.split()

for word in words:
  converted_word = ''
  letters = word.split('|')

  for letter in letters:
    converted_word = converted_word + letter_to_morse[letter]

  converted_phrase = converted_phrase + converted_word + ' '

print(f'converted_prhase: {converted_phrase}')