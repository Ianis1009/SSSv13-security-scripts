#!/bin/bash

# strace -> urmareste ce apeluri de sistem face un program Linux
# ne intereaseaza syscalls pentru a vedea interactiunea cu OS-ul

strace -f -s 256 "$1" 2>&1 | grep "SSS"

