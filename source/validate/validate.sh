#!/bin/bash

# Requires jq and usfm-grammar (https://github.com/Bridgeconn/usfm-grammar) to be installed globally already

# Assumes both git repositories are in the same directory. Modify if necessary
BIBLE_PATH=../../../OEOCV/source

for current_book in $BIBLE_PATH/*.usfm; do
		[ -e "$current_book" ] || continue
		JSON_OUT=$(usfm-grammar $current_book) # TODO: Show only the error messages to make this easier to read
		#echo $JSON_OUT
		JSON_PARSED=$(echo $JSON_OUT | jq -M '.. | ._warnings? //empty')
		if [ "$JSON_PARSED" != '[]' ] && [ ! -z "$JSON_PARSED" ]
		then
			echo $current_book
			echo $JSON_PARSED
		fi
done
