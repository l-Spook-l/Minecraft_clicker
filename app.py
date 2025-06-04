import flet as ft

from utils import ensure_settings
from home_tab import load_home_tab
from settings_tab import load_settings_tab


def app(page: ft.Page) -> None:
    ensure_settings()

    page.title = "MineClicker"
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
        width=350
    )

    # Функция для загрузки контента в зависимости от выбранного пункта меню
    def load_menu_content(menu_index):
        match menu_index:
            case 0:
                content_container.content = load_home_tab(page)
            case 1:
                content_container.content = load_settings_tab(page)

        content_container.update()

    #
    # Функция для обработки изменения выбранного пункта в навигации
    def on_nav_change(e):
        load_menu_content(nav.selected_index)
        update_navigation_rail(nav.selected_index)

    # Обновление боковой навигации
    def update_navigation_rail(active_index):
        """Обновляет боковое меню, делая активный пункт неактивным."""
        nonlocal nav
        nav.destinations = [
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.HOME, size=25),
                selected_icon=ft.Icon(ft.Icons.HOME, size=30),
                label="Home",
                disabled=active_index == 0  # Отключаем, если активен
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_SUGGEST_OUTLINED,
                label="Settings",
                disabled=active_index == 1
            ),
        ]
        page.padding = 0
        page.update()

    # Боковое меню
    nav = ft.NavigationRail(
        selected_index=0,
        destinations=[],
        on_change=on_nav_change,
        width=100,
        bgcolor=ft.Colors.LIGHT_GREEN_ACCENT_200
    )

    update_navigation_rail(0)

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

    load_menu_content(0)
