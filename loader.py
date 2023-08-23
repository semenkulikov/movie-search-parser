from deco import RequestDecorator
from utils.requests import RequestHandler, FactoryRequest
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_JSON = os.path.join(BASE_DIR, "info.json")

deco = RequestDecorator()
handler = RequestHandler()
factory = FactoryRequest(path_deco=deco, request_handler=handler)
