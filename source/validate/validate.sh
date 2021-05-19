#!/bin/bash

# Requires usfm-grammar (https://github.com/Bridgeconn/usfm-grammar) to be installed globally already

# Assumes both git repositories are in the same directory. Modify if necessary
BIBLE_PATH=../../../OEOCV/source

for current_book in $BIBLE_PATH/*.usfm; do
		[ -e "$current_book" ] || continue
		usfm-grammar $current_book # TODO: Show only the error messages to make this easier to read
done
