#This project just for fun :)

english_to_morse = {
    # Alphabets
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..',
    
    #space
    ' ': '/',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.',
}
user_input = input("enter your text: ")
def text(text):
    result = ""
    text = text.upper()
    for i in text:
        if (i in english_to_morse):
            result+= english_to_morse[i]+" "

    return result
print('this is your text: '+ user_input + "\n and this is the morse code: "+text(user_input))