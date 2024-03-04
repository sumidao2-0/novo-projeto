import tkinter
from tkinter import *
from tkinter import ttk

# importando pillow
from PIL import Image, ImageTk

#cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('Pedra papel tesoura')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row = 0, column = 0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row = 1, column = 0, sticky=NW)
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima

app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1,fg=co0)
app_1.place(x=25,y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0,fg=co0)
app_1_linha.place(x=0,y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1,fg=co0)
app_1_pontos.place(x=50,y=20)

app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1,fg=co0)
app_.place(x=120,y=20)

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1,fg=co0)
app_2_pontos.place(x=170,y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1,fg=co0)
app_2.place(x=205,y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0,fg=co0)
app_2_linha.place(x=255,y=0)

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Ivy 1 bold'), bg=co0,fg=co0)
app_linha.place(x=0,y=95)

# configurando o frame baixo

icon_1 = Image.open('images/pedra.png')
icon_1 = icon_1.resize((50,50))
icon_1 = ImageTk.PhotoImage(icon_1)
b_icon_1 = Button(frame_baixo, width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
b_icon_1.place(x=15, y=60)

icon_2 = Image.open('images/papel.png')
icon_2 = icon_2.resize((50,50))
icon_2 = ImageTk.PhotoImage(icon_2)
b_icon_2 = Button(frame_baixo, width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
b_icon_2.place(x=95, y=60)

icon_3 = Image.open('images/tesoura.png')
icon_3 = icon_3.resize((50,50))
icon_3 = ImageTk.PhotoImage(icon_3)
b_icon_3 = Button(frame_baixo, width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='flat')
b_icon_3.place(x=170, y=60)

b_jogar = Button(frame_baixo, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief='raised', overrelief='ridge')
b_jogar.place(x=5, y=151)



janela.mainloop()