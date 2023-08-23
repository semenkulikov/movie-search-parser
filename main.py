from messages import get_info
from settings.config import COMMANDS


def main():
    while True:
        action = get_info()
        handler = COMMANDS[action]
        if action == 5:
            print("Всего доброго!")
        handler()


if __name__ == '__main__':
    main()
