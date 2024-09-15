import sys

# dictionary to convert English to braille
braille_alphabet = { 
    'a' : 'O.....', 'b' : 'O.O...', 'c' : 'OO....', 'd' : 'OO.O..', 'e' : 'O..O..',
    'f' : 'OOO...', 'g' : 'OOOO..', 'h' : 'O.OO..', 'i' : '.O.O..', 'j' : '.OOO..',
    'k' : 'O...O.', 'l' : 'O.O.O.', 'm' : 'OO..O.', 'n' : 'OO.OO.', 'o' : 'O..OO.',
    'p' : 'OOO.O.', 'q' : 'OOOOO.', 'r' : 'O.OOO.', 's' : '.OO.O.', 't' : '.OOOO.',
    'u' : 'O...OO', 'v' : 'O.O.OO', 'w' : '.OOO.O', 'x' : 'OO..OO', 'y' : 'OO.OOO',
    'z' : 'O..OOO', ' ' : '......',
}

# dictionary to convert numbers to braille
braille_numbers = {
    '1' : 'O.....', '2' : 'O.O...', '3' : 'OO....', '4' : 'OO.O..', '5' : 'O..O..',
    '6' : 'OOO...', '7' : 'OOOO..', '8' : 'O.OO..', '9' : '.OO...', '0' : '.OOO..',
}  

# leading dots for capital and number following
capital_follows = '.....O'
number_follows = '.O.OOO'

# reverse the dictionaries for braille to English/numbers
english_alphabet = {value: key for key, value in braille_alphabet.items()}
english_numbers = {value: key for key, value in braille_numbers.items()}

def is_braille(input):
    # check if the input is braille (only contains O and .)
    return all(char in ['O', '.'] for char in input)


def english_to_braille(input_str):
    result = []
    is_number = False  # flag to check if a number is following

    for char in input_str:
        if char.isupper():  # check if the character is a capital letter
            result.append(capital_follows)
            result.append(braille_alphabet[char.lower()])
            is_number = False
        elif char.isdigit():  # check if the character is a number
            if not is_number:
                result.append(number_follows)
                is_number = True
            result.append(braille_numbers[char])
        else:  # check if the character is a letter
            result.append(braille_alphabet[char])
            is_number = False

    return ''.join(result)



def braille_to_english(input):
    result = []
    i = 0
    is_capital = False # flag to check if a capital letter is following
    is_number = False # flag to check if a number is following

    while i < len(input):
        braille_char = input[i:i+6] # get the next 6 characters

        if braille_char == capital_follows:
            is_capital = True
        elif braille_char == number_follows:
            is_number = True
        else:
            if is_number:
                result.append(english_numbers[braille_char]) 
            else:
                if is_capital:
                    result.append(english_alphabet[braille_char].upper())
                    is_capital = False
                else:
                    result.append(english_alphabet[braille_char])
                    is_number = False

        i += 6 # increment i by 6 to go to next braille character

    return ''.join(result)


def main():
    input = ' '.join(sys.argv[1:]) # take in all args as a string separated with a space

    if is_braille(input[0]): # check if the input is in braille
        print(braille_to_english(input))
    else: 
        print(english_to_braille(input))


if __name__ == '__main__':
    main()