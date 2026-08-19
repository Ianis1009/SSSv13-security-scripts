#!/usr/bin/env bash

find / \
    -type d \
    -perm -0002 \
    -print 2>/dev/null