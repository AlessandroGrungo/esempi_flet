import flet as ft

def main(page: ft.Page):

    def addCheckbox(e):
        strToAdd = txtIn.value
        txtIn.value = ""
        if strToAdd == "":
            return
        page.add(ft.Checkbox(label=strToAdd)) # ft.Checkbox aggiunge le caselline da spuntare con il nome = strToAdd

    # Row 1
    txtIn = ft.TextField(label="Aggiungi un elemento.")
    # CLICK SUL BOTTONE = AVVIA LA FUNZIONE addCheckbox
    btnAdd = ft.CupertinoButton(text="Add",on_click=addCheckbox)
    # PER ALLINEARE AL CENTRO LA RIGA:
    row1 = ft.Row([txtIn,btnAdd],alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

# AVVIA UN'APPLICAZIONE CON "MAIN"
ft.app(target=main)