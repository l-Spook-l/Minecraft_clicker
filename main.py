import flet as ft

from app import app
from logging_config import logger

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
        logger.info("Application has stopped.")
