import flet as ft

from utils import ensure_settings


def app(page: ft.Page) -> None:
    ensure_settings()

    page.title = "Minecraft - копатель"
    page.window.width = 450
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0

    # Запрещаем изменение размера окна
    page.window.resizable = False

    # Контейнер для отображения текущего содержимого
    content_container = ft.Container(
        bgcolor=ft.Colors.YELLOW_200,
        padding=10,
    )

    # Добавляем на страницу боковое меню и основной контент
    page.add(
        ft.Row(
            [
                # nav,
                ft.VerticalDivider(width=1),
                content_container,  # Контейнер с динамическим контентом
            ],
            expand=True,
        )
    )
