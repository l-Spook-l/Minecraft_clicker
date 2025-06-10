import flet as ft

from app import app
from logging_config import logger


def main():
    ft.app(target=app)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Application has stopped.")
