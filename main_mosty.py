import random
import tkinter as tk
import random

win = tk.Tk()
canvas = tk.Canvas(win,width =400 , height = 400,bg = "pink")
canvas.pack()

voda = []
zem = []
piczem = tk.PhotoImage(file="images/ostrov0.png")
picvoda = tk.PhotoImage(file = "images/ostrov3.png")
obrazky = [tk.PhotoImage(file="images/ostrov_kruh0.png"), tk.PhotoImage(file="images/ostrov_kruh1.png")]
mosty = [tk.PhotoImage(file="images/ostrov1.png"), tk.PhotoImage(file="images/ostrov2.png")]


sirobr = 50
vysobr = 50
peniaze = 60


def clik_switcher(e):
    print(canvas.itemcget("switcher", "image"))
    if canvas.itemcget("switcher", "image") == "pyimage3":
        canvas.itemconfig("switcher", image=obrazky[1])

    elif canvas.itemcget("switcher", "image") == "pyimage4":
        canvas.itemconfig("switcher", image=obrazky[0])


pocitadlo = 0
def clik_switcher_teacher(e):
    global pocitadlo
    pocitadlo +=1
    canvas.itemconfig("switcher", image = obrazky[pocitadlo%2])

mosty_idecka= []
def most_maker(e):
    global peniaze
    if canvas.itemcget("switcher", "image") == "pyimage3":
        x = (e.x//50) *50
        y = (e.y//50)*50
        if canvas.itemcget("current", "image") == "pyimage5":
            canvas.itemconfig("current", image = mosty[1], tags = "most")
        elif canvas.itemcget("current", "image") == "pyimage6":
            canvas.itemconfig("current", image = mosty[0], tags = "most")

        elif canvas.itemcget("current", "image") == "pyimage2" and peniaze>=10:
            peniaze -=10
            canvas.create_rectangle(345,65,400,115, fill  = "pink",outline = "pink")
            canvas.create_text(375,80, text = str(peniaze), font=('Helvetica','30','bold'))
            canvas.create_image(x,y, image = mosty[0], tags = "most", anchor = "nw")


    elif  canvas.itemcget("switcher", "image") == "pyimage4" and peniaze>=50:
        x = (e.x//50) *50
        y = (e.y//50)*50
        idecko= canvas.find_withtag("current")[0]
        canvas.delete(idecko)
        print(x,y)
        canvas.create_image(x, y, image= piczem,  anchor="nw")
        peniaze -=50
        canvas.create_rectangle(345, 65, 400, 115, fill="pink", outline="pink")
        canvas.create_text(375, 80, text=str(peniaze), font=('Helvetica', '30', 'bold'))



#TODO Musime zariadit, aby ked je switcher hnedy,tak sa menia polia na tem, ak modry, tak sa menia polia na mosty
# TODO Musime zariadit, aby ked sa klikne n amost, tak sa otoci
# TODO POriesit aby sa odratavali peniaze

def create_screen():
    global zem
    m = random.randint(4,6)
    n = random.randint(3,9)
    for stlpec in range(n):
        for riadok in range(m):
            ran = random.randint(0,5)
            if ran == 1:
                temp = canvas.create_image(riadok * sirobr, stlpec * vysobr, image=piczem, anchor="nw")
                zem.append(temp)
            else:
                temp = canvas.create_image(riadok *sirobr,stlpec*vysobr, image = picvoda,anchor = "nw", tags= "water")
                voda.append(temp)
    canvas.create_image(400,10,anchor = "ne",image = obrazky[0], tags = "switcher")

# TODO def zmen(e):
    # idecko
#item c get - dostat property image, ak 1 TAK ZMENIT. AJ NAOPAK
#GET ITEM CGET do if , potom item config

create_screen()
canvas.tag_bind("switcher","<Button-1>", clik_switcher) #pripíname udalosť na objekty s konkrétnym tagom
canvas.tag_bind("water","<Button-1>", most_maker)
canvas.tag_bind("most", "<Button-1>", most_maker)


win.mainloop()


#DOMACA ULOHA - ked most klik tak sa otoci, podla stavu pocitadla,ak je parne pridaj zem, inak pridaj most(u nas to pojde na pyimage 3 a pyimagw4
#peniaze , odovzdat do utorka
# piatok  prví traja kucerovia, 1 sa nahodne vyberie- 2,4,5- textove subory


#znicit vodu , najst suradnicu danej vody, natvrdo create novy obrazok - suradnice vody, image = novy obrazok
#