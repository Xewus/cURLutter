# cURLutter
One more url cutter fot a test task

***
- Python 3.10
- Django 4.1
***
### Инструкция по применению  
Качаем:
```
https://github.com/Xewus/cURLutter.git
```
Виртуальное окружение:
```
python3.10 -m venv venv && . venv/bin/activate
```
Скачать Django:
```
pip install django
```
Миграции:
```
python app/manage.py makemigrations && python app/manage.py migrate
```
Можно создать суперпользователя:
```
python app/manage.py createsuperuser
```
Запустить:
```
python app/manage.py runserver
```
Дальше по адресу:
```
<hоst>:8000/link/help/
```
***

### Задача:
**Необходимо спроектировать сервис-«укорачиватель ссылок», с
возможностью выбора времени жизни укороченной ссылки.
Авторизация и фронт часть не требуются.**  


**Дополнительная задача(Необязательная):
Реализовать хранение данных об устройствах пользователя и его IP, а
так же возможность выхода со всех устройств при сбросе пароля.**

***

*У постановщика задачи в стеке заявлен Django.*
