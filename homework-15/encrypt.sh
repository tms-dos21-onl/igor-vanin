#!/bin/bash

if [ ! -f "public.pem" ]; then
    echo "Ошибка: Файл public.pem не найден."
    exit 1
fi

openssl pkeyutl -pubin -inkey public.pem -encrypt
