import logging
import os
import sys

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# === Путь к файлу app.log рядом с .exe или .py ===
if getattr(sys, 'frozen', False):
    # Программа запущена из .exe
    base_dir = os.path.dirname(sys.executable)
else:
    # Программа запущена как скрипт
    base_dir = os.path.dirname(__file__)

log_file_path = os.path.join(base_dir, "app.log")

# === Обработчики ===
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(log_file_path, encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
