#!/bin/bash

# Requires jq

if [ -z "$1" ]  # File path is the first argument
then
  echo 'Must use the file path as an argument'
  exit 1
fi

JSON_OUT=$(usfm-grammar $1)
JSON_PARSED=$(echo $JSON_OUT | jq -M '.. | ._warnings? //empty')
if [ "$JSON_PARSED" != '[]' ] && [ ! -z "$JSON_PARSED" ]
then
  echo $current_book
  echo $JSON_PARSED
fi
