#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Utilizare: $0 <fisier>"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "Fisierul nu exista."
    exit 1
fi

CHECKSUM=$(sha256sum "$FILE" | awk '{print $1}')

echo "Fisier: $FILE"
echo "SHA-256: $CHECKSUM"