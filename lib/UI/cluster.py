import flet as ft

from ..src.cluster import getCluster

from ..utils.page import MainPage
from .default import Default

class CategoriaClientes(Default):
    def __init__(self):
        self.page = MainPage().getPage()
        self.route = "/cluster"

    def enviar_dados_api(self, e):

        dados = {key: self.inputs[key].value for key in self.inputs}


        response = getCluster(dados)


        if "erro" in response:
            self.page.open(ft.SnackBar(
                ft.Text(f"Erro: {response['erro']}"),
                bgcolor=ft.colors.RED
            ))
        else:
            descricao = response["descricao"]
            self.page.open(ft.SnackBar(
                ft.Text(f"Cluster identificado: {descricao}"),
                bgcolor=ft.colors.GREEN
            ))
        self.page.update()


    def getPage(self) -> ft.View:
        self.inputs = {
            "idade": ft.TextField(label="Idade", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "sexo": ft.Dropdown(label="Sexo", options=[ft.dropdown.Option("M"), ft.dropdown.Option("F"), ft.dropdown.Option("Outro")]),
            "estado_civil": ft.Dropdown(label="Estado Civil", options=[ft.dropdown.Option("Solteiro"), ft.dropdown.Option("Casado"), ft.dropdown.Option("Divorciado")]),
            "renda_mensal": ft.TextField(label="Renda Mensal", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "cidade": ft.TextField(label="Cidade", expand=True),
            "estado": ft.Dropdown(label="Estado", options=[ft.dropdown.Option(uf) for uf in ["SP", "RJ", "MG", "BA", "PR"]]),
            "frequencia_compra_mensal": ft.TextField(label="Frequência de Compra (mensal)", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "ticket_medio": ft.TextField(label="Ticket Médio", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "categoria_preferida": ft.Dropdown(label="Categoria Preferida", options=[ft.dropdown.Option(cat) for cat in ["Roupas", "Eletrônicos", "Alimentos", "Cosméticos", "Utilidades"]]),
            "tempo_cliente": ft.TextField(label="Tempo como cliente (meses)", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "utiliza_app": ft.Dropdown(label="Usa App?", options=[ft.dropdown.Option("Sim"), ft.dropdown.Option("Não")]),
            "participa_programa_fidelidade": ft.Dropdown(label="Participa do Programa de Fidelidade?", options=[ft.dropdown.Option("Sim"), ft.dropdown.Option("Não")]),
            "ultima_compra_dias": ft.TextField(label="Dias desde última compra", keyboard_type=ft.KeyboardType.NUMBER, expand=True),
            "forma_pagamento_preferida": ft.Dropdown(label="Forma de Pagamento Preferida", options=[ft.dropdown.Option(pag) for pag in ["Crédito", "Débito", "Pix", "Dinheiro", "Boleto"]]),
            "canal_compra_preferido": ft.Dropdown(label="Canal de Compra Preferido", options=[ft.dropdown.Option(can) for can in ["Loja Física", "Site", "App"]])
        }

        enviar_btn = ft.ElevatedButton(
            text="Enviar para API",
            on_click=self.enviar_dados_api, 
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
        )

        card = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Classificação de Clientes por Cluster", size=26, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    *[self.inputs[key] for key in self.inputs],
                    ft.Divider(),
                    enviar_btn
                ],
                spacing=15,
                tight=True
            ),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.03, ft.Colors.ON_SURFACE),
            alignment=ft.alignment.center,
            width=600
        )

        return ft.View(
            route=self.route,
            controls=[
                ft.Row(
                    controls=[card],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            scroll=ft.ScrollMode.AUTO
        )
