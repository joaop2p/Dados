
import flet as ft
from flet.core.view import View

from ..src.predictor import Predictor

from .widgets.result_area import area

from .widgets.textfield import textField

from .default import Default

from ..utils.page import MainPage

class Home(Default):
    content_area: ft.Ref[ft.Container]
    precitor: Predictor
    
    def __init__(self):
        main_page = MainPage()
        self.route = "/home"
        self.precitor = Predictor()
        self.page = main_page.getPage()

    def __str__(self):
        return self.route

    def _check_fields(self, field: ft.TextField):
        try:
            return float(field.value)
        except (ValueError, TypeError):
            return None

    def loading_page(self):
        loading_view = ft.View(
            route="/temp",
            controls=[
                ft.Container(
                    content=ft.ProgressRing(),
                    alignment=ft.alignment.center
                    )
                ],
            vertical_alignment=ft.MainAxisAlignment.CENTER
            )
        self.page.views.append(loading_view)
        self.page.update()

    def loading_end(self):
        self.page.views.pop(-1)
        self.page.update()

    def start_predictor(self):
        self.precitor = Predictor()

    def check_fields(self, inputs: dict):
        for key in inputs.keys():
            field:ft.Ref = inputs.get(key)["ref"]
            new_value = self._check_fields(field.current)
            if new_value is None:
                return False
            inputs.get(key)["valor"] = new_value
        return True

    def send(self, inputs: dict[dict]):
        if not self.check_fields(inputs):
            print("dados inválidos")
            return
        package = {}
        for key in inputs.keys():
            package[key] = inputs[key]["valor"]
        self.update_content(area(self.precitor.predict(package).lower()))

    def update_content(self, content: ft.Control):
        self.content_area.current.content = content
        self.content_area.current.update()

    def getPage(self) -> View:
        self.loading_page()
        self.precitor.start()
        self.loading_end()
        inputs = {
            "valor_mercado_bilhoes": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "Valor de Mercado (Bilhões)",
                "valor": None
            },
            "lucro_liquido_milhoes": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "Lucro Líquido (Milhões)",
                "valor": None
            },
            "receita_milhoes": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "Receita (Milhões)",
                "valor": None
            },
            "divida_milhoes": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "Dívida (Milhões)",
                "valor": None
            },
            "pl": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "P/L",
                "valor": None
            },
            "roe": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "ROE (%)",
                "valor": None
            },
            "margem_liquida": {
                "ref": ft.Ref[ft.TextField](),
                "Label": "Margem Líquida (%)",
                "valor": None
            },
        }
        self.content_area = ft.Ref[ft.Container]()
        return View(
            route= self.route,
            appbar=ft.AppBar(
                bgcolor="#121E2F"
                ),
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Container(
                                        content=ft.Image(
                                            src="assets/images/logo.png",
                                            width=50,
                                            height=50,
                                            scale=1.2
                                            ),
                                        margin=ft.Margin(0,0,10,0),
                                        ),
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Text(
                                                    value="Assistente de investimentos".upper(),
                                                    font_family="Montserrat Bold",
                                                    style=ft.TextStyle(
                                                        size=30,
                                                        weight=ft.FontWeight.W_500,
                                                        color="#ECF3F7"
                                                        )
                                                    ),
                                                ft.Text(
                                                    value="Recomendações baseadas em dados reais.",
                                                    size=18,
                                                    color="#A7B4BF",
                                                    font_family="Poppins Medium"
                                                    )
                                                ],
                                            spacing=0.3
                                            )
                                        )
                                    ]
                                )
                            )
                        ]
                    ),
                ft.Container(
                    content=ft.Text(
                        value="Insira os valores abaixo.",
                        size=20,
                        font_family="Roboto Regular",
                        color="#ECF3F7"
                        ),
                    margin=ft.Margin(0,20,0,20)
                    ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.Column(
                                                controls=[
                                                    textField(
                                                        title=inputs.get(key)["Label"],
                                                        ref=inputs.get(key)["ref"]
                                                        )
                                                    for key in inputs.keys()
                                                    ] 
                                                ),
                                            )
                                        ]
                                    ),
                                # bgcolor="white",
                                width=512
                                ),
                            ft.Container(
                                ft.Column(
                                    controls=[
                                        ft.Container(
                                            ft.Container(
                                                ref=self.content_area,
                                                bgcolor="#13202D",
                                                width=350,
                                                height=350,
                                                border_radius=ft.border_radius.all(10),
                                                content= area(),
                                                alignment=ft.alignment.center,
                                                ),
                                            padding=ft.padding.all(20),
                                            alignment=ft.alignment.center,
                                            ),
                                        ft.Container(
                                            ft.Container(
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Icon(
                                                            name=ft.Icons.TRENDING_UP,
                                                            size=30,
                                                            color="white"
                                                            ),
                                                        ft.Text(
                                                            value="Gerar Recomendação.",
                                                            size=20
                                                            )
                                                        ],
                                                    alignment=ft.MainAxisAlignment.CENTER
                                                    ),
                                                bgcolor="#36A383",
                                                width=350,
                                                height=50,
                                                alignment=ft.alignment.center,
                                                border_radius=ft.border_radius.all(10),
                                                on_hover=lambda e: (e.control.scale),
                                                on_click=lambda _: self.send(inputs)
                                                ),
                                            alignment=ft.alignment.center,
                                            ),
                                        ],
                                    spacing=100
                                    ),
                                alignment=ft.alignment.center,
                                width=512
                                ),
                            ]
                        )
                    )
                ],
            bgcolor="#0A131F",
            padding=20
            )