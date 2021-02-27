# TCMB sitesinden efektif dolar satış fiyatını çekelim.
# https://www.turkiye.gov.tr/doviz-kurlari

from tkinter import *
from bs4 import *
import requests


# gui oluşturuyoruz.

root = Tk()
root.title('Döviz Çevirici - TCMB')
root.configure(background='light blue')
root.resizable(width=False, height=False)

dolar_label = Label(root, text='Dolar:', background='light blue', font='Arial 12 bold')
dolar_label.grid(row=0, column=0, padx=10, pady=(10,0))

# Entry
dolar_text = DoubleVar()
dolar_entry = Entry(root, width=15, textvariable=dolar_text)
dolar_entry.grid(row=0, column=1, sticky="")


# TL

tl_label = Label(root, text='TL:', background='light blue', font='Arial 12 bold')
tl_label.grid(row=1, column=0, padx=10, pady=(5,0), sticky=E)

# Entry
tl_text = DoubleVar()
tl_entry = Entry(root, width=15, textvariable=tl_text)
tl_entry.grid(row=1, column=1, sticky='E')

def dolar_cevir():
    sayfa = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")

    #print(sayfa.text)

    soup = BeautifulSoup(sayfa.text, "html.parser")

    efektif_dolar_satis = soup.find('td', text='1 ABD DOLARI')\
                              .find_next_sibling('td')\
                              .find_next_sibling('td')\
                              .find_next_sibling('td')\
                              .find_next_sibling('td')\
                              .text

    tl_miktar = dolar_text.get() * float(efektif_dolar_satis)
    tl_text.set(round(tl_miktar, 2))


# buton ekliyoruz.

cevir_btn = Button(root, text='Çevir', bg='blue', fg='white',
                   font='Arial 12 bold', width=7, command=dolar_cevir)
cevir_btn.grid(row=2, column=0, columnspan=2)

# ekranı ortala
def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(280, 150)



# GUI'yi gösterelim.
root.mainloop()



