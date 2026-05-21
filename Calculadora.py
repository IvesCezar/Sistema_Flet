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
     
     if operacao == "+":
         res = n1 + n2
     elif operacao == "-":
         res = n1 - n2
     elif operacao == "x":
         res = n1 * n2
     elif operacao == "÷":
         res = n1 / n2
     else:
         resultado.value = "Resultado: Selecione uma operação"
         page.update()
         return

     resultado.value = f"Resultado: {res}"
     page.update()


    operacoes = ft.Dropdown(
        label = "Escolha a operação",
        options =[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("x"),
            ft.dropdown.Option("÷"),             
            ]
         )

    button_calcular = ft.ElevatedButton("Calcular", on_click=calcular)
    page.update()
    page.add(numero1, numero2,operacoes, button_calcular,resultado )

ft.app(target=main)