#!/usr/bin/env bash

value=$(sshd -T 2>/dev/null | awk '$1 == "permitrootlogin" {print $2}')

[[ "$value" == "no" ]] && echo "OK" || {
    echo "WARN: PermitRootLogin=$value"
    exit 1
}