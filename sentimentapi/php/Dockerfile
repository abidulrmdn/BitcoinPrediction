FROM php:7.0-fpm
RUN apt-get update

RUN docker-php-ext-install pdo_mysql mysqli
RUN apt-get install -y software-properties-common
RUN apt-get install -y python3 python3-dev python3-pip python3-virtualenv && \
  rm -rf /var/lib/apt/lists/*

