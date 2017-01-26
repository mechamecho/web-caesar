import string 


def alphabet_position(letter):
	alphabet = string.ascii_lowercase
	if letter.isalpha():
		letter = letter.lower()
		letter_position0= alphabet.index(letter)-alphabet.index("a")
		return letter_position0

def rotate_character(rot, char):
	new_char=char
	alphabet=string.ascii_lowercase
	if char.isalpha():
		new_position_char = (alphabet_position(char)+rot)%len(alphabet)
		new_char=alphabet[new_position_char]
		if char.isupper():
			new_char = new_char.upper()
	return new_char

def encrypt(text, rot):
	new_text = ""
	for letter in text:
		new_letter=rotate_character(rot, letter)
		new_text=new_text+new_letter
	return new_text