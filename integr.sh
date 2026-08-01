#!/bin/bash

if ["$#" -ne 1]; then
    echo "Utilizare: $0 <fisier>"
    exit 1

fi 

FILE = "$1"

#TODO