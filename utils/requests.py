import json
from urllib.parse import urljoin
from deco import RequestDecorator
import requests
from dotenv import load_dotenv, find_dotenv
import os


if not find_dotenv():
    exit('Переменные окружения не загружены, т.к отсутствует файл .env')
else:
    load_dotenv()

API_URL = os.getenv('API_URL')


class RequestHandler:
    """ Класс для выполнения запросов к API сайта """

    def __call__(self, *args, **kwargs):
        """
        Магический метод для вызова класса как функции
        :param args: кортеж параметров (url, params, headers)
        :return: статус-код ответа API сайта, тело ответа API сайта.
        """
        response = requests.get(
            url=args[0],
            params=args[1],
            headers=args[2]
        )
        try:
            response_json = response.json()
        except:
            response_json = json.loads(response.text)
        return response.status_code, response_json


class FactoryRequest:
    """ Класс-фабрика запросов к API сайта """

    API_URL = API_URL

    def __init__(self, path_deco: RequestDecorator, request_handler: RequestHandler):
        """
        Конструктор класса-фабрики.
        :param path_deco: класс-декоратор хэндлера, формирующий строку запроса.
        :param request_handler: оборачиваемый класс, выполняющий запрос.
        """
        self.path_deco = path_deco
        self.request_handler = request_handler

    def interface(self, endpoint: str, headers: dict, params: dict | None, endpoint_params: dict = None):
        """
        Метод класса-фабрики, служащий интерфейсом для основной программы.
        :param endpoint: имя эндпойнта.
        :param headers: заголовки запроса.
        :param endpoint_params: дополнительные параметры для включения в основные параметры эндпойнта.
        :param params: основные параметры эндпойнта.
        :return: результат выполнения запроса.
        """
        deco_obj = self.path_deco
        deco_obj.url = urljoin(self.API_URL, endpoint)
        deco_obj.headers = headers
        if endpoint_params:
            params.update(**endpoint_params)
        deco_obj.params = params

        return deco_obj(self.request_handler)
