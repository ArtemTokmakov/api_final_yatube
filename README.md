Проект API социальной сети Yatube

Разработчик:

Токмаков Артем Михайлович

О проекте:

Проект Yatube представляет собой социальную сеть, в которой пользователи имеют возможность создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи. В данном проекте реализован интерфейс для обмена данными социальной сети Yatube. Он предоставляет клиентам доступ к базе данных. Данные передаются в формате JSON.

Примененные технологии:

Python 3

Django Rest Framework

Git


Описание

Данное API позволяет использовать следующий функционал:

1. Публикации

Получать список всех публикаций

Создавать новую публикацию

Полностью или частично редактировать публикацию

Удалять публикацию

2. Сообщества

Получение списка доступных сообществ

Получение информации о сообществе

3. Комментарии

Получение всех комментариев к публикации

Получение конкретного комментария к публикации

Добавление нового комментария к публикации

4. Подписка

Получение списка своих подписчиков

Подписка на публикации других пользователей



Клонирование репозитория и переход в него в командной строке:
```

git clone git@github.com:ArtemTokmakov/api_final_yatube.git

cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
pyhton -m venv venv
```
Если у вас Linux/MacOS
```
source venv/bin/activate
```
Если у вас windows
```
source venv/scripts/activate
```
Установка зависимостей из файла requirements.txt:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запуск проекта:
```
python manage.py runserver
```

