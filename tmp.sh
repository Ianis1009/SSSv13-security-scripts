#!/usr/bin/env bash

mode=$(stat -c '%a' /tmp 2>/dev/null) || exit 2

if [[ "$mode" == "1777" ]]; then
    echo "OK"
else
    echo "WARN: /tmp permissions: $mode"
    exit 1
fi