MORSE_DICTIONARY = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ': '$',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

TEXT_DICTIONARY = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..': 'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
     	'...': 'S',    '-': 'S',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'W',
        '-.--': 'Y',   '--..': 'Z',   '$': ' ',
        
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9' 
        }
"""stop char is |
1 | between letters
$ between words"""

def translate_to_morse_code( text ):
        morse_code = ""
        
        capital_text = text.upper()         
        
        for index in range(len(capital_text)):  
                character = capital_text[index]  
                if( not character.isalnum() and not character.isspace() ):
                        return "Error text must be alpha numeric"            
                morse_code += MORSE_DICTIONARY[character] + "|"
        return morse_code
        
def translate_to_text( morse_code ):
        text = ""
        
        parsed_morse_code = morse_code.split("|")
        
        for index in range(len(parsed_morse_code)):
                code = parsed_morse_code[index]
                if(code in TEXT_DICTIONARY):
                        text += TEXT_DICTIONARY[code]
                elif(code == ""):
                        pass #add nothing
                else:
                        return "Error Morse code does not exist " + code
                
        return text