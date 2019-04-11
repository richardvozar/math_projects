# bekér egy számot
# mondja meg a helyi értékeit
# kérdezze meg, melyik helyi értéken melyik szám áll

from tkinter import *
from math import log10 as logaritmus

def valaszt():
    global math
    global eredmeny
    szamocska_list = list(szamocska)
    szamocska_list.reverse()
    pista = lista.get(ACTIVE)
    pisti = int(logaritmus(pista))
    lista.destroy()
    eredmeny = Label(ablak1, text='A '+ str(szamocska)+' számnak a(z) '+ str(pista)+'-s helyi értéke: '+ str(szamocska_list[pisti]), fg='red', bg='black')
    eredmeny.pack()
    val.destroy()

def szam_e():
    global szamocska
    global lista
    global val
    szamocska = mezo1_e.get()
    lista = Listbox(ablak1)
    for i in range(len(szamocska)):
        lista.insert(i, int(10**(i)))
    lista.pack()
    val = Button(ablak1, text='Választ', command = valaszt)
    val.pack()
    eredmeny.destroy()

ablak1 = Tk()
eredmeny = Label(ablak1, text='')
mezo1 = Label(ablak1, text='Írj be egy számot!')
mezo1.pack()
mezo1_e = Entry(ablak1)
mezo1_e.pack()
mezo2 = Button(ablak1, text='Bevitel', command = szam_e)
mezo2.pack()
mezo66 = Button(ablak1, text='Kilépés', command = ablak1.destroy)
mezo66.pack()

ablak1.mainloop()
