import re

def main():
	book = '\v 1 \w The|strong="G3588"\w* \w elder|strong="G4245"\w* \w to|strong="G1722"\w* \w Gaius|strong="G1050"\w* \w the|strong="G3588"\w* \w beloved|strong="G27"\w*, \w whom|strong="G3739"\w* \w I|strong="G1473"\w* \w love|strong="G25"\w* \w in|strong="G1722"\w* \w truth|strong="G225"\w*.'
	new_book = re.sub(r'\b(\|strong)\b[^"]+"([^"]*)"', "", book)  # Uses a raw string for the regex pattern
	new_book = re.sub(r'(\\w\*|\\w )', "", new_book)
	print(new_book)

if __name__ == "__main__":
	main()
