import os
import json
import sys

from logging_config import logger

DEFAULT_SETTINGS = {
    "start": "9",
    "stop": "0",
    "exit": "Del",
    "go": "w"
}


def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def get_settings_path():
    return os.path.join(get_app_dir(), "settings.json")


def ensure_settings():
    path = get_settings_path()
    if not os.path.exists(path):
        logger.info("Файл settings.json не найден. Создаём с настройками по умолчанию.")
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4, ensure_ascii=False)
            logger.info(f"успешно создан -  settings.json")
        except Exception as e:
            logger.error(f"Ошибка при создании settings.json: {e}")


def load_settings() -> dict:
    data = {}  # значение по умолчанию

    if os.path.exists("settings.json"):
        with open("settings.json", "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                logger.info("⚠️ Файл повреждён. Создаём заново.")

    logger.info(f'path - {os.path.exists("settings.json")}')
    logger.info(f'data - {data}')

    return data


def save_settings(settings):
    with open("settings.json", "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)
