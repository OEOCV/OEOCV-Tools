""" Strong's Remover
Removes references to Strong's Concordance from USFM files in order to
keep the text consistent with the Septuagint version
and to simplify the editing process.
"""

import os
import re
import sys


def remove_text(book):
	new_book = re.sub(r'\b(\|strong)\b[^"]+"([^"]*)"', "", book)  # Uses a raw string for the regex pattern
	new_book = re.sub(r'(\\w\*|\\w )', "", new_book)
	return new_book

def main():
	if len(sys.argv) == 1:
		print("Error: Enter the path to either a file or a directory")
		sys.exit()
	current_path = sys.argv[1]
	if os.path.isdir(current_path):
		print("Directory")
		os.chdir(current_path)
		for current_book in os.listdir():
			if os.path.splitext(current_book)[-1] != ".usfm":  # Only works for USFM files
				continue
			file = open(current_book, 'r+')
			text = file.read()
			new_text = remove_text(text)
			file.seek(0)
			file.truncate(0)
			file.write(new_text)
			file.close()
	else:
		print("File")
		if os.path.splitext(current_path)[-1] != ".usfm":  # Only works for USFM files
			print("Error: Only compatible with USFM files")
			sys.exit()
		file = open(current_path, 'r+')
		text = file.read()
		new_text = remove_text(text)
		file.seek(0)
		file.truncate(0)
		file.write(new_text)
		file.close()

if __name__ == "__main__":
	main()
