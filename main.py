import flet as ft

from app import app

"""
при сборке - exe файла
flet pack main.py --icon assets/icon.png
"""


def main():
    ft.app(target=app)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Приложение остановлено")
