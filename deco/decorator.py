class RequestDecorator:
    """ Класс-декоратор для оборачивания класса и передачи ему строки запроса """

    def __init__(self, url: str = "", params=None,
                 headers=None):
        """
        Конструктор класса-декоратора.
        :param url: url-адрес запроса
        :param params: параметры запроса
        :param headers: заголовки запроса.
        """
        headers = headers or {}
        params = params or {}
        self.url = url
        self.params = params
        self.headers = headers

    def __call__(self, obj, *args, **kwargs):
        """
        Метод для вызова декоратора как функции.
        :param obj: оборачиваемый класс.
        :return: результат вызова оборачиваемого класса.
        """
        return obj(self.url, self.params, self.headers)
