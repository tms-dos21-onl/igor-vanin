#!/bin/bash

if [ ! -f "private.pem" ]; then
    echo "Ошибка: Файл private.pem не найден."
    exit 1
fi

openssl pkeyutl -inkey private.pem -decrypt
