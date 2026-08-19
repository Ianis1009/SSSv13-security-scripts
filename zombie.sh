#!/usr/bin/env bash

ps -eo stat= \
    | awk '$1 ~ /^Z/ {count++} END {print count+0}'