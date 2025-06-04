import threading
import time

import flet as ft
import pyautogui
import keyboard


from utils import load_settings


clicking = False
click_thread = None
keyboard_hooks = []


def click_loop():
    global clicking
    while clicking:
        pyautogui.mouseDown()
        pyautogui.keyDown("w")
        time.sleep(0.1)


def load_home_tab(page: ft.Page):
    settings = load_settings()

    status_text = ft.Text("Status: Stopped", size=18)
    log_text = ft.Text(f"Press  {settings.get('start')} — start\n"
                       f"Press {settings.get('stop')} — stop\n"
                       f"Press {settings.get('exit')} — exit", size=14)

    def start_clicking(e):
        nonlocal status_text
        global clicking, click_thread
        if not clicking:
            clicking = True
            click_thread = threading.Thread(target=click_loop, daemon=True)
            click_thread.start()
            status_text.value = "Status: Running"
            page.update()

    def stop_clicking(e):
        nonlocal status_text
        global clicking
        if clicking:
            clicking = False
            pyautogui.mouseUp()
            pyautogui.keyUp(settings.get('go'))
            status_text.value = "Status: Stopped"
            page.update()

    def exit_program(e):
        stop_clicking(None)
        keyboard.unhook_all()
        page.window.close()

    # Привязка клавиш
    h1 = keyboard.on_press_key(settings.get('start'), start_clicking)
    h2 = keyboard.on_press_key(settings.get('stop'), stop_clicking)
    h3 = keyboard.on_press_key(settings.get('exit'), exit_program)

    # Сохраняем хендлы
    keyboard_hooks.extend([h1, h2, h3])

    return ft.Container(
        content=ft.Column(
            [
                status_text,
                ft.Divider(),
                log_text
            ]
        )
    )
