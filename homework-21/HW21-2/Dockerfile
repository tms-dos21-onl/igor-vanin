FROM php:apache as dev

RUN docker-php-ext-install pdo_mysql

WORKDIR /var/www/html
COPY /simple-lamp .
COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

EXPOSE 80

CMD ["apache2-foreground"]