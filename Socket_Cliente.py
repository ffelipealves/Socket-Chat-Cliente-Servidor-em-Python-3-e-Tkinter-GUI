
"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

#Bibliotecas para manipulação dos dados via Socket com o uso de Threads:
import socket, threading
import ipaddress

#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

# Uso para a criação dos gifs e animações da interface, todo o crédito desse código para o github e seu autor: https://github.com/olesk75/AnimatedGIF
from AnimatedGIF import *

"""
 Abaixo o método que utilizo para armazenar todos os caminhos de imagens usadas aqui nesse código para poder transformá-lo em um .exe.

 *** Caso esteja interessado, eu segui o procedimento do seguinte link do Stackoverflow para converter meus códigos em um .exe todo o
     crédito aos que falam desse método nas respostas do Stackoverflow: https://stackoverflow.com/questions/54210392/how-can-i-convert-pygame-to-exe
"""
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

"""
Cria objeto "Tkinter"/"Tk"
"""
root = Tk()

"""
Aqui escondemos a janela 'default' do Tkinter que chamamos de 'Root' (Faço isso pois vou trabalhar com muitas janelas e só a root não dá conta.)
"""
root.withdraw()

path_botao_ENVIA_MSG_JOGADOR_asset = resource_path('recursos/button_img_mandar_msg.png')
botao_ENVIA_MSG_JOGADOR_asset = PhotoImage(file=path_botao_ENVIA_MSG_JOGADOR_asset, master=root)
path_label_INSERE_DADOS_IP_SERVIDOR_bg_asset = resource_path('recursos/img_INSERE_DADOS_IP_SERVIDOR_bg.png')
label_INSERE_DADOS_IP_SERVIDOR_bg_asset = PhotoImage(file=path_label_INSERE_DADOS_IP_SERVIDOR_bg_asset, master=root)
path_label_DADOS_IP_INVALIDOS_bg_asset = resource_path('recursos/img_DADOS_IP_INVALIDOS_bg.png')
label_DADOS_IP_INVALIDOS_bg_asset = PhotoImage(file=path_label_DADOS_IP_INVALIDOS_bg_asset, master=root)
path_JANELA_PRINCIPAL_asset = resource_path('recursos/img_JANELA_PRINCIPAL_bg.png')
JANELA_PRINCIPAL_asset = PhotoImage(file=path_JANELA_PRINCIPAL_asset, master=root)
path_imagem_OK_BUTTON_asset = resource_path('recursos/button_img_OK.png')
imagem_OK_BUTTON_asset = PhotoImage(file=path_imagem_OK_BUTTON_asset, master=root)

def fecha_APLICACAO_2(Toplevel):
    Toplevel.destroy()
    Toplevel.quit()
    root. destroy()
    os._exit(1) 

def fecha_janela_TOPLEVEL(Toplevel):
    Toplevel.destroy()

def fecha_janela_TOPLEVEL(Toplevel):
    Toplevel.destroy()

def aviso_dados_IP_ERRADOS():
    newWindow = Toplevel(root)
    newWindow.title("Jogador-01: Aviso!")
    newWindow.geometry("280x155")
    insere_dados_IP_SERVIDOR_label.place(x=0, y=0)

def checa_ip(endereco_ip,Toplevel_entry):
    try:
        ipaddress.ip_address(endereco_ip)
    except Exception as erro:
        aviso_dados_IP_ERRADOS()
    else:
        fecha_janela_TOPLEVEL(Toplevel_entry)
        inicia_aplicacao_jogador(endereco_ip)

def pede_dados_IP_SERVIDOR():
    newWindow = Toplevel(root)
    newWindow.title("Socket: Jogador-01")
    newWindow.geometry("280x155")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO_2(newWindow))

    jogador_text_input = Entry(newWindow,width = 27)
    jogador_text_input.place(x=98, y=62)

    continuar_button = Button(newWindow, text='Conectar ...', font='sans 11 bold', width=12, height=int(1.5), command=lambda:checa_ip(str(jogador_text_input.get()),newWindow))
    continuar_button.place(x=140, y=96)

def inicia_aplicacao_jogador(ip_servidor):
    
    #Ajudar colocando o resto do código aqui <-----

"""
*
*       **********************************
*  ~~~ Inicializando a aplicação do Jogador ~~~
*       **********************************
*
"""

if __name__ == "__main__":
    root.mainloop()     
