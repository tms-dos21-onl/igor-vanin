FROM php:apache as dev

RUN apt-get update && apt-get install -y libmemcached-dev libmemcached11 zlib1g-dev libssl-dev

RUN docker-php-ext-install pdo_mysql \ 
    && yes '' | pecl install -f memcached-3.2.0 \
    && docker-php-ext-enable memcached

WORKDIR /var/www/html
COPY /simple-lamp .

COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh
RUN chmod +x /usr/local/bin/wait-for-it.sh

EXPOSE 80

CMD ["apache2-foreground"]