from time import sleep
import flet as ft

# AGGIUNGE CONTROLLO ALLA PAGE
def main(page: ft.Page):
    txtIn = ft.Text(value="Buongiorno TdP 2024!", color="red")
    page.controls.append(txtIn)
    page.update()

# AGGIUNGE CONTROLLO ALLA PAGE
#    txtOut = ft.Text(value="Counter:", color="red",size=24)
#    page.add(txtOut)

# CREA TIMER VISIBILE
#    for i in range(1,100):
#         txtOut.value = "Counter: " + str(i)
#         txtOut.update()
#         sleep(1) #simula lo scorrere del tempo

# CREA UNA CONSEGUENZA DI UN BOTTONE
    def handleBottone(e):
        lv.controls.append(ft.Text("Tasto Cliccato!"))
        lv.update()

# BOTTONE VA INSERITO IN UN CONTROLLO DELLA PAGINA
    btn = ft.ElevatedButton(text="Premimi", on_click=handleBottone)
    row = ft.Row([btn])
    page.add(row)

# expand=1: indica che l'oggetto ListView deve espandersi per occupare tutto lo spazio disponibile all'interno del suo contenitore.
# spacing=10: specifica lo spazio tra gli elementi nella vista.
# padding=20: determina il riempimento (spazio) tra il bordo dell'oggetto ListView e i suoi elementi interni.
# auto_scroll=True: abilita la funzionalità di scorrimento automatico della ListView quando vengono aggiunti nuovi elementi.
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    page.add(lv)

# AVVIA UN'APPLICAZIONE CON "MAIN" E IMPOSTA LA VISUALIZZAZIONE DELL'APPLICAZIONE COME "FLET_APP".
ft.app(target=main, view=ft.AppView.FLET_APP)