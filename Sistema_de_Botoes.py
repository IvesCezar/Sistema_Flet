#Tela com Botão utilizando a biblioteca Flet
import flet as ft


def main(page: ft.Page):
    def clicar():
        if texto.value == "Utilizando o Flet":
            texto.value = "App Flet Operacional"
        else:
            texto.value = "Utilizando o Flet"
        page.update()

    
    
    texto = ft.Text("Utilizando o Flet")
    botao = ft.ElevatedButton("Clique aqui", on_click=clicar)
    
    

    page.add(texto, botao)


ft.app(target=main)

