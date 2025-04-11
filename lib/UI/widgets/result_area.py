from typing import Literal
import flet as ft

def result(icon, color, tip):
    text = "Com base no dados fornecidos, a recomendação é "
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    ft.Column(
                        controls=[
                            ft.Container(
                                ft.Icon(
                                    name=icon,
                                    color=color,
                                    size=70
                                    ),
                            alignment=ft.alignment.center,
                            ),
                            ft.Container(
                                ft.Text(
                                    tip.upper(),
                                    color=color,
                                    weight=ft.FontWeight.BOLD,
                                    size=40
                                    ),
                                alignment=ft.alignment.center,
                                )
                            ],
                        width=250,
                        spacing=0
                        ),
                    alignment=ft.alignment.center,
                    ),
                ft.Container(
                    content=ft.Container(
                        ft.Text(
                            text,
                            font_family="Roboto Regular",
                            size=15,
                            color="#A7B4BF",
                            text_align=ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan(
                                    tip,
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE
                                        )
                                    )
                                ]
                            ),
                        width=250,
                        alignment=ft.alignment.center,
                        ),
                    alignment=ft.alignment.center,
                    )
                ],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        )

def area(tip: Literal["comprar", "manter", "vender"] = "") -> ft.Container:
    print(tip)
    match(tip):
        case "comprar":
            return result(icon = ft.Icons.CALL_MADE_ROUNDED, color = "#37A384", tip=tip)
        case "manter":
            return result(icon = ft.Icons.HORIZONTAL_RULE_SHARP, color = "#E09B24", tip=tip)
        case "vender":
            return result(icon = ft.Icons.CALL_RECEIVED, color = "#A71118", tip=tip)
        case _:
            return ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Container(
                                ft.Text(
                                    "Os resultados aparecerão aqui.",
                                    font_family="Roboto Regular",
                                    size=15,
                                    color="#A7B4BF",
                                    text_align=ft.TextAlign.CENTER,
                                    ),
                                width=250,
                                alignment=ft.alignment.center,
                                ),
                            alignment=ft.alignment.center,
                            )
                        ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                )
            