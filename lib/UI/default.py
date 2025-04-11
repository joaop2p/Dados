from flet import Page, View
from abc import ABC, abstractmethod

class Default(ABC):
    page: Page
    route: str

    @abstractmethod
    def getPage(self) -> View:
        pass