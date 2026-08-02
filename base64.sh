#!/usr/bin/env bash

set -euo pipefail

if (( $# != 1 )); then
    echo "Use: $0 file.txt"
    exit 1
fi 

file="$1"

if [[ ! -f "$file" ]]; then
    echo "Error: '$file' does not exist."
    exit 1
fi 

code=$(base64 < "$file")
decode=$(printf '%s' "$code" | base64 --decode)

cat -- "$file"
echo
echo "$code"
echo
echo "$decode"
