#Calculadora utilizando a biblioteca Flet
import flet as ft
def main(page: ft.Page):
    
    page.title = "Calculadora"
    numero1 = ft.TextField(label="Primeiro Valor")
    numero2 = ft.TextField(label="Segundo Valor")
    resultado = ft.Text("Resultado: ")

    def calcular ():
     n1 = float(numero1.value)
     n2 = float(numero2.value)
     
     operacao = operacoes.value
     
     
    operacoes = ft.Dropdown(
        label = "Escolha a operação",
        options =[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("x"),
            ft.dropdown.Option("/"),             
            ]
         )

    page.update()
    page.add(numero1, numero2, resultado, operacoes)

ft.app(target=main)