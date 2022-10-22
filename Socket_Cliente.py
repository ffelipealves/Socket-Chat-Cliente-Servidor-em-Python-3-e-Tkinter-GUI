
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
