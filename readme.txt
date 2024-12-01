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
POST запрос записывает результат выполненного квиза. Принимает на вход id квиза и ответы на вопросы квиза в формате {"(id вопроса)": "(ответ)"}. В теле ответа в поле "res" будет хранится количество набранных за квиз баллов. В случае, если превышено количество попыток пользователя или предыдущая попытка набрала больше или 50 баллов, возвращается пустой HTTP ответ с кодом 460. Пример запроса и ответа:
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

main/question/ принимает только GET запросы и возвращает список вопросов к конкретному квизу. Ожидает на вход параметр "quiz", в котором будет указан айди квиза. На выходе также ты получаешь ссылку варианты ответа в качестве видео. При подгрузке обязательно нужно приписывать в качестве src адрес бэкенда перед самой ссылкой, тогда src будет выглядеть следующим образом: src=`(адрес сервера с бэком)://${json['video']}`. Пример запроса и ответа:
GET REQUEST http://example.com/main/question/2
RESPONSE:
[
    {
        "id": 19,
        "content": "Какой жест означает: \"Университет\"?",
        "right_answer": "/media/videos/university.mp4",
        "wrong_answer1": "/media/videos/office.mp4",
        "wrong_answer2": "/media/videos/school.mp4",
        "wrong_answer3": "/media/videos/college.mp4"
    }
]








