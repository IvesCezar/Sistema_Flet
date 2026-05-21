#Calculadora utilizando a biblioteca Flet
import flet as ft
def main(page: ft.Page):
    
    page.title = "Calculadora "
    numero1 = ft.TextField(label="Primeiro Valor")
    numero2 = ft.TextField(label="Segundo Valor")
    resultado = ft.Text("Resultado: ")

    def calcular ():
     n1 = float(numero1.value)
     n2 = float(numero2.value)
     r = n1 + n2
     resultado.value = f"Resultado: {r}"
    botao_calcular = ft.ElevatedButton("Calcular", on_click=calcular)
    
    page.add(numero1, numero2, resultado, botao_calcular)

ft.app(target=main)