"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

#Bibliotecas para manipulação dos dados via Socket comm o uso de Threads:
import socket, threading


#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os


#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

from AnimatedGIF import *

#
#   Abaixo o método que utilizo para armazenar todos os caminhos de imagens usadas aqui nesse código para poder transformá-lo em um .exe.
#
#   *** Caso esteja interessado, eu segui o procedimento do seguinte link do Stackoverflow para converter meus códigos em um .exe todo o
#       crédito aos que falam desse método nas respostas do Stackoverflow: https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe
#
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
