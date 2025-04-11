from flet import app

from lib.src.app import MyApp

my_app = MyApp()
app(my_app.run, assets_dir="assets")