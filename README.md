# Проект "Парсер для Кинопоиска"

## Описание 
Эта программа-парсер для запросов к API Кинопоиска. Может выполнять следующие действия:
* Получать информацию о случайном фильме;
* Получать полную информацию по id фильма; 
* Запрашивать информацию о выходе сезонов и серий;
* Парсить отзывы о фильме. 

Чтобы запустить программу, потребуется:
1. Скачать код парсера
2. Установить все зависимости командой `pip install -r requirements.txt`
3. Переименовать файл .env.template в .env, добавить туда свой API Токен (получить можно [здесь](https://kinopoisk.dev/))
4. Запустить парсер командой `python main.py`

## Стек

* Python
* requests
* dotenv

## Техническое задание «Работа со сторонним API»
### Что нужно сделать
Чтобы подключиться к API «Кинопоиска», перейдите на [сайт](https://kinopoisk.dev/) и следуйте инструкциям. Для работы используйте бесплатный тариф Demo. В конце успешной регистрации вы получите ключ для работы с API. 

Внимательно [изучите документацию API](https://api.kinopoisk.dev/v1/documentation) и напишите программу, которая выводит на экран (и в JSON-файл): 

* информацию о случайном фильме;
* полную информацию по id фильма; 
* информацию о выходе сезонов и серий;
* отзывы о фильме. 

### Требования к коду
* Нельзя использовать функциональный стиль программирования, кроме функции main(), где собирается логика программы. Используйте ООП.
* Нельзя использовать библиотеки вне курса, кроме pprint, http.
* Преобразование типов выполняйте только на вводе (some_variable = int(input("Enter some number")).
* Работайте строго в рамках пройденного материала на курсе «Основы Python», части 1 и 2.
* Не используйте циклы, за исключением функции main() для зацикливания логики кода:
```
def main():
    while True:
        pass
```

Код должен соответствовать РЕР 8.


### Эндпойнты
* Выбрать из базы рандомный фильм: /v1/movie/random
* Получить всю информацию о фильме: /v1/movie/{id}
* Получить все сезоны и эпизоды: /v1/season
* Отзывы пользователей: /v1/review

### Структура
**Директория common**

Корневая директория:

* модуль с декоратором (deco) - скорее показательный, чем обязательный;
* модуль с основной логикой запросов (utils); 
* модуль с сообщениями (messages);
* модуль общих настроек (settings).


## Movie Search Parser Project

## Description 
This is a parser program for requests to the Kinopoisk API. It can perform the following actions:
* Get information about a random movie;
* Get full information on movie id; 
* Request information about seasons and series release;
* Parsing movie reviews. 

To run the program, you will need:
1. Download the parser code
2. Install all dependencies with the command `pip install -r requirements.txt`.
3. Rename the .env.template file to .env, add your API Token there (you can get it [here](https://kinopoisk.dev/)).
4. Run the parser with the `python main.py` command

## Stack

* Python
* requests
* dotenv

### Terms of Reference "Working with third-party API"
### What you need to do
To connect to the Kinopoisk API, go to [site](https://kinopoisk.dev/) and follow the instructions. To work, use the free Demo tariff. At the end of successful registration, you will receive a key to work with the API. 

Carefully [study the API documentation](https://api.kinopoisk.dev/v1/documentation) and write a program that outputs to the screen (and to a JSON file): 

* information about a random movie;
* complete movie id information; 
* season and series release information;
* movie reviews. 

### Code requirements
* Do not use functional programming style, except main() function, where the program logic is assembled. Use OOP.
* Do not use off-course libraries except pprint, http.
* Do type conversions only on input (some_variable = int(input("Enter some number")).
* Work strictly within the framework of the material covered in Python Fundamentals, Parts 1 and 2.
* Do not use loops, except for main() to loop the code logic:
```
def main():
    while True:
        pass
```

The code must conform to RER 8.


### Endpoints
* Select a random movie from the database: /v1/movie/random
* Get all movie information: /v1/movie/{id}
* Get all seasons and episodes: /v1/season
* Get user reviews: /v1/review

### Structure
**Directory common**

Root directory:

* module with decorator (deco) - indicative rather than mandatory;
* module with basic query logic (utils); 
* module with messages;
* common settings module.