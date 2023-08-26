from loader import factory
from loader import PATH_TO_JSON
from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit('Переменные окружения не загружены, т.к отсутствует файл .env')
else:
    load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

HEADERS = {
    "X-API-KEY": API_TOKEN,
    "Content-Type": "application/json"
}


def save_info(text):
    """ Функция для сохранения информации в файл """
    with open(PATH_TO_JSON, "a+", encoding="utf-8") as file:
        file.write(str(text))


def get_info(is_action=True):
    """ Функция для выдачи справки по доступным командам """
    text = """
Здравствуйте! Вас приветствует парсер для Кинопоиска.
Вам доступны следующие действия:
0 - получить справку
1 - получить информацию о случайном фильме
2 - получить информацию о фильме по его id
3 - получить информацию о выходе сезонов и серий
4 - получить отзывы о фильме
5 - выход из программы\n
"""
    print(text)
    if is_action:
        while True:
            try:
                action_num = int(input("\nВыберите номер действия: "))
                if not 0 <= action_num <= 5:
                    raise ValueError
                break
            except ValueError:
                print("Ошибка! Введите число от 0 до 5.")
            except TypeError:
                print("Ошибка! Необходимо ввести число от 0 до 5.")
        return action_num


def get_random_film():
    """ Хендлер для получения рандомного фильма """
    endpoint = "v1/movie/random"
    params = None
    print("Отправка запроса...\n")
    status_code, response = factory.interface(endpoint=endpoint,
                                              headers=HEADERS,
                                              params=params)
    answer = {
        "Имя фильма": response.get("name") or "не указано",
        "Второе имя": response.get("alternativeName") or "не указано",
        "ID": response.get("id"),
        "Тип тайтла": response.get("type") or "не указан",
        "Год премьеры": response.get("year") or "не указан",
        "Описание фильма": response.get("description") or "не найдено",
        "Короткое описание": response.get("shortDescription") or "не найдено",
        "Слоган": response.get("slogan") or "не указан",
        "Рейтинг": response.get("rating", {}).get("kp", "не найден"),
        "Продолжительность": response.get("movieLength") or "не указана" + " мин.",
        "Трейлеры": ''.join(["\n\t{trailer_name} - {trailer_url}".format(
            trailer_name=trailer.get("name") or "нет",
            trailer_url=trailer.get("url") or "нет"
        ) for trailer in response.get("videos", {}).get("trailers", {})]
        ) or "не найдены",
        "Актеры": ', '.join([
            person.get("name") or "имя не найдено"
            for person in response.get("persons", {})
            if person.get("profession") == "актеры"
        ]),
        "Жанр": ', '.join([genre.get("name") for genre in response.get("genres", {})])
    }
    save_info(answer)
    print('\n'.join([f"{key}: {val}" for key, val in answer.items()]))


def get_film_info_by_id():
    """ Хендлер для получения информации о фильме по его id """
    try:
        film_id = int(input("Хорошо, введите id фильма: "))
    except:
        print("Необходимо ввести число, id фильма. Попробуйте еще раз.")
        return None
    endpoint = f"v1/movie/{film_id}"
    params = None
    print("Запрос отправлен.\n")
    status_code, response = factory.interface(endpoint=endpoint,
                                              headers=HEADERS,
                                              params=params)
    if response.get("id") is None:
        print("К сожалению, фильм с таким ID не найден.")
        return
    answer = {
        "Имя фильма": response.get("name") or "не указано",
        "Второе имя": response.get("alternativeName") or "не указано",
        "ID": response.get("id"),
        "Тип тайтла": response.get("type") or "не указан",
        "Год премьеры": response.get("year") or "не указан",
        "Описание фильма": response.get("description") or "не найдено",
        "Короткое описание": response.get("shortDescription") or "не найдено",
        "Слоган": response.get("slogan") or "не указан",
        "Рейтинг": response.get("rating", {}).get("kp", "не найден"),
        "Продолжительность": response.get("movieLength") or "не указана" + " мин.",
        "Трейлеры": ''.join(["\n\t{trailer_name} - {trailer_url}".format(
            trailer_name=trailer.get("name") or "нет",
            trailer_url=trailer.get("url") or "нет"
        ) for trailer in response.get("videos", {}).get("trailers", {})]
        ) or "не найдены",
        "Актеры": ', '.join([
            person.get("name") or "имя не найдено"
            for person in response.get("persons", {})
            if person.get("profession") == "актеры"
        ]),
        "Жанр": ', '.join([genre.get("name") for genre in response.get("genres", {})])
    }
    save_info(answer)

    print('\n'.join([f"{key}: {val}" for key, val in answer.items()]))


def get_info_releases():
    """ Хендлер для получения информации о выходе сезонов и серий """
    endpoint = "v1/season"
    params = None
    print("Запрос отправляется...\n")
    status_code, response = factory.interface(endpoint=endpoint,
                                              headers=HEADERS,
                                              params=params)
    answer = {
        "Общее количество результатов": response.get("total"),
        "Количество результатов на странице": response.get("limit"),
        "Сколько страниц всего": response.get("pages"),
        "Текущая страница": response.get("page"),
        "Сезоны": ''.join(["\n\tID фильма: {movie_id}"
                           "\n\tНомер: {number}"
                           "\n\tКоличество эпизодов: {episodes_count}"
                           "\n\tЭпизоды: {episodes}\n".format(movie_id=season.get("movieId") or "нет",
                                                              number=season.get("number") or "не указан",
                                                              episodes_count=season.get("episodesCount") or "нет",
                                                              episodes=''.join(["\n\t\tНомер: {number}"
                                                                                "\n\t\tНазвание: {name}"
                                                                                "\n\t\tВторое название: {en_name}"
                                                                                "\n\t\tОписание: {description}"
                                                                                "\n\t\tДата: {date}\n".format(
                                                                  number=episode.get("number") or "не указан",
                                                                  name=episode.get("name") or "не указано",
                                                                  en_name=episode.get("enName") or "не указано",
                                                                  description=episode.get("description") or "нет",
                                                                  date=episode.get("date") or "не найдена")
                                                                  for episode in season.get("episodes", {})
                                                              ])) or "не найдены"
                           for season in response.get("docs", {})]
                          ) or "не найдены",
    }
    save_info(answer)
    print('\n'.join([f"{key}: {val}" for key, val in answer.items()]))


def get_movie_reviews():
    """ Хендлер для получения отзывов о фильме """
    endpoint = "v1/review"
    try:
        film_id = input("Введите id фильма (по желанию). Чтобы пропустить, нажмите Enter: ")
        if film_id != '':
            film_id = int(film_id)
        else:
            film_id = None
    except:
        print("Необходимо ввести число, id фильма. Попробуйте еще раз.")
        return None
    params = {"movieId": film_id} if film_id is not None else None
    print("Запрос отправлен.\n")
    status_code, response = factory.interface(endpoint=endpoint,
                                              headers=HEADERS,
                                              params=params)
    answer = {
        "Общее количество результатов": response.get("total"),
        "Количество результатов на странице": response.get("limit"),
        "Сколько страниц всего": response.get("pages"),
        "Текущая страница": response.get("page"),
        "Отзывы": ''.join(["\n\tID отзыва: {id}"
                           "\n\tID фильма: {movie_id}"
                           "\n\tЗаголовок: {title}"
                           "\n\tТип: {type}"
                           "\n\tОтзыв: {review}"
                           "\n\tДата: {date}"
                           "\n\tАвтор: {author}"
                           "\n\tID автора: {author_id}"
                           "\n\tРейтинг: {user_rating}\n".format(id=season.get("id") or "нет",
                                                                 movie_id=season.get("movieId") or "не указан",
                                                                 title=season.get("title") or "нет",
                                                                 type=season.get("type") or "не указан",
                                                                 review=season.get("review") or "нет",
                                                                 date=season.get("date") or "не найдена",
                                                                 author=season.get("author") or "не найден",
                                                                 author_id=season.get("authorId") or "нет",
                                                                 user_rating=season.get("userRating") or "нет")
                           for season in response.get("docs", {})]
                          ) or "не найдены",
    }
    save_info(answer)

    print('\n'.join([f"{key}: {val}" for key, val in answer.items()]))
