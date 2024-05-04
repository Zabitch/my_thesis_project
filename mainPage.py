import flet as ft
import constants as const

def mainPage(page: ft.Page):
    page.clean()
    page.title = const.TITLE + '- Главная страница'
    
    navBar =  ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.BACKUP_TABLE, label="Товары"),
            ft.NavigationDestination(icon=ft.icons.SHOPPING_BASKET, label="Корзина", ),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Настройки",),
        ]
    )
    
    
    page.add(ft.Row(
        [
                ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("First name")),
                    ft.DataColumn(ft.Text("Last name")),
                    ft.DataColumn(ft.Text("Age"), numeric=True),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("John")),
                            ft.DataCell(ft.Text("Smith")),
                            ft.DataCell(ft.Text("43")),
                        ],
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Jack")),
                            ft.DataCell(ft.Text("Brown")),
                            ft.DataCell(ft.Text("19")),
                        ],
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("Alice")),
                            ft.DataCell(ft.Text("Wong")),
                            ft.DataCell(ft.Text("25")),
                        ],
                    ),
                ],
                width = ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        ],
        alignment= ft.MainAxisAlignment.SPACE_BETWEEN
    ))
            #ft.Row([navBar])

ft.app(target=mainPage)
