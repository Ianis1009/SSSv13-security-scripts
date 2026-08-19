#!/usr/bin/env bash

mode=$(stat -c '%a' /etc/passwd 2>/dev/null) || exit 2

if [[ "$mode" != "644" ]]; then
    echo "WARN: /etc/passwd permissions: $mode"
    exit 1
fi

echo "OK"