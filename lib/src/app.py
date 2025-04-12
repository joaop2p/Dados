from flet import Page

from ..UI.cluster import CategoriaClientes

from ..UI.home import Home
from ..utils.page import MainPage


class MyApp:
    page: Page
    def __init__(self):
        self.page = None
        self.main_page:MainPage

    def config(self, page: Page):
        self.main_page:MainPage = MainPage()
        self.main_page.setPage(page)
        self.page = self.main_page.getPage()

    def run(self, page):
        self.config(page)
        new_page = CategoriaClientes()
        self.main_page.new_page(new_page)
        self.page.update()
        
       