
import flet as ft

def validar_entrada(e):
    # Permitir apenas números
            # Permitir apenas números
    allow = str((0,2,3,4,5,6,7,8,9, "."))
    print(allow, e.control.value.digit)
    print(e.control.value not in allow)
    if e.control.value not in allow:
        e.control.value = ''.join(filter(str.isdigit, e.control.value))
        e.control.update()
        
def textField(title:str, ref: ft.Ref) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text(
                value=title,
                font_family="Roboto Regular",
                size=15,
                color="#A7B4BF",
                ),
                ft.TextField(
                    value=1,
                    ref= ref,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    bgcolor="#111D2B",
                    # border=ft.InputBorder.NONE,
                    border_color=ft.Colors.TRANSPARENT,
                    text_align=ft.TextAlign.END,
                    border_radius=ft.border_radius.all(5),
                    text_style=ft.TextStyle(
                        font_family="Inter SemiBold"
                        ),
                    tooltip="Insira apenas números",
                )
            ]   
    )