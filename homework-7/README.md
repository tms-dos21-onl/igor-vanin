Выполнял задание на VPS серверы, разворачивал приложение следующим способом:

1. Клонировал проекты:
```
git clone https://github.com/bezkoder/django-rest-api.git
git clone https://github.com/bezkoder/django-rest-api.git
```
2. Установил виртуальное окружение для python и пакетный менеджер pip 
```
 python -m virtualenv django_ven
 sudo apt-get install python3-pip
```

3. Проект на djangorestframework:
Комады выполняем в папке проекта где лежит файл manage.py

Устанавливаем нужные пакеты
```
pip install djangorestframework
pip install django-cors-headers
pip install django
pip install gunicorn
```

Настраиваем конфиг проекта для удаленного сервера и БД:
~./DjangoRestApi/settings.py
```
ALLOWED_HOSTS = ['123.123.123.123'] указываем хост сервера (свой скрыл)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' // требуется для запуска и миграций, чтобы избежать ошибку 
Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
) // Разрешаем доступ из других источников к нашему приложению (указываем порт клиентского приложения)
```
Создаем миграцию:
```
python manage.py migrate tutorials
manage.py migrate
```
Разрешаем соединение на 8080 порт используя ufw
```
sudo ufw allow 8080
```

Проверяем работоспособность gunicorn
```
gunicorn --bind 0.0.0.0:8080 DjangoRestApi.wsgi // DjangoRestApi название проекта.
Если ошибки отсутствуют, gunicorn работает 
```
Запускаем приложение:
```
python manage.py runserver 123.123.123.123:8080 // указываем ip нашего сервера
```

4. Настраиваем клиентстую часть:
Устанавливаем пакетный менеджер и зависимости:

```
sudo apt-get install npm
npm install bootstrap
npm install react-router-dom
npm install axios
```
Настраиваем конфиг для доступа к бэкенду:
~./src/http-common.js
```
Указываем адрес удаленного сервера 
baseURL: "http://123.123.123.123:8080/api"
```
Запускаем приложение:
```
npm start
```
