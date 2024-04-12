import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #ALLINEAMENTO PAGINA AL CENTRO

# AGGIUNGE 1 AL VALORE CORRENTE QUANDO VIENE CHIAMATA
    def handleAdd(e):
        currentVal = txtOut.value # Ottiene il valore corrente del campo di testo txtOut
        txtOut.value = currentVal + 1 # Aggiorna il valore di txtOut
        txtOut.update()

# TOGLIE 1 AL VALORE CORRENTE QUANDO VIENE CHIAMATA
    def handleRemove(e):
        currentVal = txtOut.value # Ottiene il valore corrente del campo di testo txtOut
        txtOut.value = currentVal - 1 # Aggiorna il valore di txtOut
        txtOut.update()

# CREA PULSANTE CON "-" CHE ATTIVA UNA FUNZIONE QUANDO VIENE CLICCATO
    btnMinus = ft.IconButton(icon = ft.icons.REMOVE,
                             icon_color="blue",
                             icon_size= 24, on_click= handleRemove)

# CREA PULSANTE CON "+" CHE ATTIVA UNA FUNZIONE QUANDO VIENE CLICCATO
    btnAdd = ft.IconButton(icon = ft.icons.ADD,
                             icon_color="red",
                             icon_size= 24, on_click= handleAdd)

# CREA un CAMPO di TESTO con LARGHEZZA 100, DISABILITATO, CON VALORE INIZIALE A 0
    txtOut = ft.TextField(width=100, disabled=True,
                          value=0, text_align=ft.TextAlign.CENTER)

# CREA LINEA AL CENTRO CON I TASTI CHE MI SERVONO
    row1 = ft.Row([btnMinus, txtOut, btnAdd], alignment=ft.MainAxisAlignment.CENTER)
    page.add(row1)

# AVVIA UN'APPLICAZIONE CON "MAIN"
ft.app(target=main)