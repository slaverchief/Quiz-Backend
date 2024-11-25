Запросы:
Все запросы делятся на категории запросов:

- Запросы, начинающиеся с "auth/" касаются всего, что связано с пользователями и их аутентификацией
- Запросы, начинающиеся с "main/" касаются всего, что связано с данными квизов.


Пользователи и аутентификация:

auth/login/ запрашивает JWT токен. В теле запроса надо передать 2 параметра: имя пользователя и его пароль через параметры "username" и "password". Принимает только POST запросы. Пример запроса:
POST REQUEST http://example.com/auth/login
json_body:
{
"username": "butakova_pizda", 
"password": "da_da_yapizda"
}
RESPONSE
{
"access": (токен), 
"refresh": (рефреш-токен, но он нам не нужен)
}

auth/user/ принимает 2 типа запроса: GET и POST. GET запрос не принимает никаких параметров, а лишь возвращает 2 значения: id и username авторизованного пользователя. POST запрос принимает на вход 2 значения: username и password, в результате будет создан новый пользователь с указанным именем и паролем. Ответ со статусом 200 будет сигнализировать об успешно созданном пользователе. Пример запроса и ответа:

GET REQUEST http://example.com/auth/user
RESPONSE
{
    "id": 1,
    "username": "admin"
}

POST REQUEST http://example.com/auth/user
json_body:
{
    "username": "some_user",
    "password": "userpass"
}
RESPONSE
{
    "id": 1,
    "username": "admin"
}


Квиз:

main/quiz/ принимает GET и POST запросы:
GET запрос возвращает список, состоящий из id и name квизов. Пример запроса и ответа:
GET REQUEST http://example.com/main/quiz
RESPONSE json_type 
[
    {
        "id": 1,
        "name": "HTML"
    },
    {
        "id": 2,
        "name": "CSS"
    },
    {
        "id": 3,
        "name": "JS"
    }
]
POST запрос записывает результат выполненного квиза. Принимает на вход id квиза и ответы на вопросы квиза в формате {"(id вопроса)": "(ответ)"}. В теле ответа в поле "res" будет хранится количество набранных за квиз баллов. Пример запроса и ответа:
POST REQUEST http://example.com/main/quiz
json_type
{
    "quiz": 2,
    "7": "Cascading Style Sheets",
    "8": "background-color: #FF5733;",
    "9": "font-family: Arial;",
    "10": "font-size: 16px;",
    "11": "text-align: center;",
    "12": "Применяет флексбокс к контейнеру"
}
RESPONSE
json_type
{
    "res": 100
}

main/question/ принимает только GET запросы и возвращает список вопросов к конкретному квизу. Ожидает на вход параметр "quiz", в котором будет указан айди квиза. Пример запроса и ответа:
GET REQUEST http://example.com/main/question/2
RESPONSE:
[
    {
        "id": 7,
        "content": "Что означает аббревиатура CSS?",
        "right_answer": "Cascading Style Sheets",
        "wrong_answer1": "Creative Style Sheets",
        "wrong_answer2": "Computer Style Sheets",
        "wrong_answer3": "Colorful Style Sheets"
    },
    {
        "id": 8,
        "content": "Как задать цвет фона элемента в CSS?",
        "right_answer": "background-color: #FF5733;",
        "wrong_answer1": "color: #FF5733;",
        "wrong_answer2": "border-color: #FF5733;",
        "wrong_answer3": "font-color: #FF5733;"
    },
    {
        "id": 9,
        "content": "Как изменить шрифт текста в CSS?",
        "right_answer": "font-family: Arial;",
        "wrong_answer1": "text-font: Arial;",
        "wrong_answer2": "font-style: Arial;",
        "wrong_answer3": "font-type: Arial;"
    },
    {
        "id": 10,
        "content": "Как изменить размер шрифта в CSS?",
        "right_answer": "font-size: 16px;",
        "wrong_answer1": "text-size: 16px;",
        "wrong_answer2": "font-width: 16px;",
        "wrong_answer3": "text-style: 16px;"
    },
    {
        "id": 11,
        "content": "Как выровнять текст по центру с помощью CSS?",
        "right_answer": "text-align: center;",
        "wrong_answer1": "text-position: center;",
        "wrong_answer2": "align-text: center;",
        "wrong_answer3": "center-text: true;"
    },
    {
        "id": 12,
        "content": "Что делает свойство display: flex;?",
        "right_answer": "Применяет флексбокс к контейнеру",
        "wrong_answer1": "Скрывает элемент",
        "wrong_answer2": "Устанавливает фиксированную ширину элемента",
        "wrong_answer3": "Задает фоновый цвет для элемента"
    }
]








