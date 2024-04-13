#!/bin/sh

number="$1"

if ! echo "$number" | grep -qE '^[0-9]+$'; then
    echo "Not number"
    exit 1
fi

if [ "$(( number % 2 ))" -eq 0 ]; then
    echo "Even"
else
    echo "Not Even"
fi
