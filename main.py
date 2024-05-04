import flet as ft
import constants as const
import mainPage as mainPage
import sqlite3 as sql

def main(page: ft.Page):
    page.title = const.TITLE + '- Регистрация'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_height = const.WINDOW_HEIGHT
    page.window_width = const.WINDOW_WIDTH
     
    def signIn(e):
        db = sql.connect('my_thesis_project')
        
        cur = db.cursor()
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS Users (
                        int IDENTITY(1,1) PRIMARY KEY,
                        FirstName VARCHAR(255) NOT NULL,
                        LastName VARCHAR(255) NOT NULL,
                        Login VARCHAR(50) NOT NULL,
                        Password VARCHAR(50) NOT NULL
                    )''');
        
        print('Create table')
        
        cur.execute(f'''
                    INSERT INTO Users (FirstName, LastName, Login, Password) 
                    VALUES ('test', 
                            'testov', 
                            '{user_login.value}', 
                            '{user_password.value}')
                    ''')
        
        print('Insert')
        
        cur.execute(f'''
                    SELECT 1 
                    FROM Users
                    WHERE Login = '{user_login.value}'
                      AND Password = '{user_password.value}'
                    ''')

        print('select')
        
        if (cur.rowcount != 0):
            db.close()
            mainPage.mainPage(page)
        
    def validate(e):
        if all([user_login.value, user_password.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()
        
    user_login = ft.TextField(label = 'Логин', width = 200, on_change=validate)
    user_password = ft.TextField(label = 'Пароль', width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text='Вход', width=200, on_click=signIn, disabled=True)
        
    page.add(
        ft.Row([
            ft.Column([
                ft.Text('Вход'),
                user_login,
                user_password,
                btn_reg
            ])], 
            alignment= ft.MainAxisAlignment.CENTER
        )
    )
        
ft.app(target=main)