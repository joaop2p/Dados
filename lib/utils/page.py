from flet import Page

from ..UI.default import Default

from .singleton import Singleton

@Singleton
class MainPage:
    _main_page: Page
    
    def __init__(self) -> None:
        self._main_page = None

    def __str__(self):
        return self.__class__.__name__

    def config(self):
        self._main_page.window.resizable = False
        self._main_page.window.maximizable = False
        self._main_page.views.clear()
        self._main_page.window.height = 1024
        self._main_page.window.width = 1024
        self._main_page.fonts = {
            "Montserrat Bold": "assets/fonts/montserratbold.ttf",
            "Poppins Medium": "assets/fonts/poppins-medium.ttf",
            "Roboto Regular": "assets/fonts/roboto-regular.ttf",
            "Inter SemiBold": "assets/fonts/inter-18pt-bold.ttf"
            }
        # self._main_page.on_route_change = self.new_page

    def new_page(self, obj: Default)-> None:
        if obj not in self._main_page.views:
            page = obj.getPage()
            self._main_page.views.append(page)
        self._main_page.go(obj.route)
        self._main_page.update()
        

    def setPage(self, page) -> None:
        self._main_page = page

    def getPage(self) -> Page:
        self.config()
        self._main_page.update()
        return self._main_page
        