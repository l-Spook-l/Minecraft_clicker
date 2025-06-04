import flet as ft

from utils import load_settings, save_settings


def load_settings_tab(page: ft.Page):
    settings = load_settings()
    change_key = True

    # Текст, который будет отображать нажатую клавишу
    key_display = ft.Text("Press the button to start")

    # Добавляем текстовые поля для каждого действия
    start_key_field = (
        ft.TextField(label="Start key", value=settings["start"], width=80, text_align=ft.TextAlign.CENTER, max_length=2,
                     read_only=True))
    stop_key_field = (
        ft.TextField(label="Stop key", value=settings["stop"], width=80, text_align=ft.TextAlign.CENTER, max_length=2,
                     read_only=True))
    exit_key_field = (
        ft.TextField(label="Exit key", value=settings["exit"], width=80, text_align=ft.TextAlign.CENTER, max_length=2,
                     read_only=True))
    go_key_field = (
        ft.TextField(label="Go key", value=settings["go"], width=80, text_align=ft.TextAlign.CENTER, max_length=2,
                     read_only=True))

    def change_button_clicked(e, key: str):
        # Переменная для хранения "сохранённых данных"
        saved_data = ""
        nonlocal change_key  # Используем состояние переменной change_key

        if change_key:
            key_display.value = "Press any key"
            page.on_keyboard_event = on_key  # Включаем обработчик клавиш
            change_key = False  # Переключаем режим на "Сохранить"

            match key:
                case "start":
                    change_start_key.icon = ft.Icons.CHECK_CIRCLE_OUTLINED
                case "stop":
                    change_start_key.icon = ft.Icons.CHECK_CIRCLE_OUTLINED
                case "exit":
                    change_start_key.icon = ft.Icons.CHECK_CIRCLE_OUTLINED
                case "go":
                    change_start_key.icon = ft.Icons.CHECK_CIRCLE_OUTLINED

        else:
            # Сохранение данных в переменную и отображение
            saved_data = key_display.value[-1]
            key_display.value = f"Data saved: {saved_data}"
            page.on_keyboard_event = None  # Отключаем отслеживание клавиш
            change_key = True  # Переключаем режим на "Изменить"

            match key:
                case "start":
                    change_start_key.icon = ft.Icons.CHANGE_CIRCLE
                    start_key_field.value = saved_data
                case "stop":
                    change_start_key.icon = ft.Icons.CHANGE_CIRCLE
                    stop_key_field.value = saved_data
                case "exit":
                    change_start_key.icon = ft.Icons.CHANGE_CIRCLE
                    exit_key_field.value = saved_data
                case "go":
                    change_start_key.icon = ft.Icons.CHANGE_CIRCLE
                    go_key_field.value = saved_data
            settings[key] = saved_data

            save_changes()

        page.update()

    # Обработчик нажатия клавиш
    def on_key(e: ft.KeyboardEvent):
        key_display.value = f"Key pressed: {e.key}"
        page.update()

    change_start_key = ft.IconButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        on_click=lambda e: change_button_clicked(e, "start"),
    )
    change_stop_key = ft.IconButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        on_click=lambda e: change_button_clicked(e, "stop"),
    )
    change_exit_key = ft.IconButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        on_click=lambda e: change_button_clicked(e, "exit"),
    )
    change_go_key = ft.IconButton(
        icon=ft.Icons.CHANGE_CIRCLE,
        on_click=lambda e: change_button_clicked(e, "go"),
    )

    def save_changes():
        save_settings(settings)

        page.open(ft.SnackBar(ft.Text("Settings saved!")))
        page.update()

    # Добавляем элементы на страницу
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Hotkey settings", size=20),
                key_display,
                ft.Row([
                    ft.Column([
                        ft.Row([
                            change_start_key,
                            start_key_field
                        ]),
                        ft.Row([
                            change_stop_key,
                            stop_key_field,
                        ]),
                    ]),
                    ft.Column([
                        ft.Row([
                            change_exit_key,
                            exit_key_field
                        ]),
                        ft.Row([
                            change_go_key,
                            go_key_field,
                        ]),
                    ])
                ], spacing=20),
            ]
        )
    )
