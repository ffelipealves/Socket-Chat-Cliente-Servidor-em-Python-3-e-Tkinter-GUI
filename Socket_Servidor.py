"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

from tkinter import *
from AnimatedGIF import *

"""
*
*       ******************************************************
*  ~~~ Construção de Interface Gráfica com a biblioteca Tkinter ~~~
*       ******************************************************
*
"""

root = Tk()
root.withdraw()

def fecha_APLICACAO(Toplevel):
    Toplevel.destroy()      
    Toplevel.quit()
    root. destroy()
    os._exit(1) 

def fecha_janela_TOPLEVEL(Toplevel):
    Toplevel.destroy()

def mostra_janela_AVISO_FECHAR_SERVIDOR():
    newWindow = Toplevel(root)
    newWindow.title("Servidor: Aviso!")
    newWindow.geometry("360x205")

    sim_button = Button(newWindow, text='Sim', width=12, command=lambda:fecha_APLICACAO(newWindow))
    sim_button.place(x=124, y=154)

    nao_button = Button(newWindow, text='Não', width=12, command=lambda:fecha_janela_TOPLEVEL(newWindow))
    nao_button.place(x=240, y=154)

def mostra_janela_SERVIDOR():    
    newWindow = Toplevel(root)
    newWindow.title("Socket: Servidor")

    newWindow.geometry("476x220")

    newWindow.protocol("WM_DELETE_WINDOW", mostra_janela_AVISO_FECHAR_SERVIDOR)

    text_area = ScrolledText(newWindow,wrap = WORD, fg='blue', width = 42,height = 7,font = ("Callibri",9))
    text_area.place(x=120, y=79)
    text_area.focus()

    servidor(text_area)

"""
*
*       ***********************************
*  ~~~ Inicializando a aplicação do Servidor ~~~
*       ***********************************
*
"""

if __name__ == "__main__":
    root.mainloop()
