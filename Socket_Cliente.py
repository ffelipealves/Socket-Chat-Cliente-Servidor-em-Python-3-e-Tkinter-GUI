
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

# Variavel que irá receber o socket do jogador:
global socket_jogador
global flag_estado_do_socket

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
    insere_dados_IP_SERVIDOR_label = Label(newWindow,image = label_DADOS_IP_INVALIDOS_bg_asset, width=276, height=151)
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

    insere_dados_IP_SERVIDOR_label = Label(newWindow,image = label_INSERE_DADOS_IP_SERVIDOR_bg_asset, width=276, height=151)
    insere_dados_IP_SERVIDOR_label.place(x=0, y=0)
    
    jogador_text_input = Entry(newWindow,width = 27)
    jogador_text_input.place(x=98, y=62)

    continuar_button = Button(newWindow, text='Conectar ...', font='sans 11 bold', width=12, height=int(1.5), command=lambda:checa_ip(str(jogador_text_input.get()),newWindow))
    continuar_button.place(x=140, y=96)

def inicia_aplicacao_jogador(ip_servidor):
    global socket_jogador
    global flag_estado_do_socket

    # Ambos são os mesmos que o do servidor para poder possibilitara conexão em máquinas diferentes, ambas, dentro de um mesma rede é claro.
    ENDERECO_JOGADOR = ip_servidor
    PORTA_JOGADOR = 12000 # <--- Um valor alto para não dar conflitos no SO. Decidi fazer ela instanciada no código para evitar mais ainda problemas
                          #      de porta com valores problemáticos caso o usuário pudesse instanciá-la também e colocasse um valor que conflitasse
                          #      com os usados pela máquina.

    flag_estado_do_socket = 0

    try:
        socket_jogador = socket.socket()  # << [USO DE SOCKETS NO CÓDIGO]
        socket_jogador.connect((ENDERECO_JOGADOR, PORTA_JOGADOR))  # << [USO DE SOCKETS NO CÓDIGO]

        msg_de_entrada = '<Jogador-01 conectou-se ao servidor!>'
        socket_jogador.send(msg_de_entrada.encode())

        flag_estado_do_socket = 1

        mostra_janela_PRINCIPAL()
        
    except Exception as erro:
        print(erro)
        mostra_janela_SERVIDOR_CAIU()
        socket_jogador.close()  # << [USO DE SOCKETS NO CÓDIGO]

def mostra_janela_PRINCIPAL():
    global flag_estado_do_socket
    global socket_jogador
    
    newWindow = Toplevel(root)
    newWindow.title("Socket: Jogador-01")
    newWindow.geometry("309x382")

    bg_label = Label(newWindow,image = JANELA_PRINCIPAL_asset)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/chat_bubble_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.place(x=80, y=31)
    lbl_with_my_gif.start()

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO_2(newWindow))

    # Abaixo instanciamos o widget aonde as mensagens são mostradas no chat.
    text_area = ScrolledText(newWindow,wrap = WORD,width = 38,height = 12,font = ("Callibri",8))
    text_area.place(x=28, y=152)
    text_area.focus()
    
    jogador_text_input = Entry(newWindow,width = 30)
    jogador_text_input.place(x=100, y=352)
    envia_mensagem_jogador_button = Button(newWindow, image=botao_ENVIA_MSG_JOGADOR_asset,command=lambda:envia_mensagem(str(jogador_text_input.get()),text_area))
    envia_mensagem_jogador_button.place(x=17, y=334)

    text_area.insert(tk.INSERT, "<Você entrou> Bem vindo ao chat!~\n", 'msg')
    text_area.tag_config('msg', foreground='blue')

    if flag_estado_do_socket == 1:
        msg = '<Jogador-01 entrou no chat!>'
        socket_jogador.send(msg.encode()) # << [USO DE SOCKETS NO CÓDIGO]

    threading.Thread(target=recebe_mensagens, args=(text_area,socket_jogador)).start() #<---- THREAD 'recebe_mensagens' *****

    """
*
*       *******************************************************************************************
*  ~~~ Codigos das ações e variáveis do Socket de comunicação do Jogador com o Servidor na aplicação ~~~
*       *******************************************************************************************
*
"""

"""
Funções utilizadas pelos Sockets jogador
"""

def mostra_janela_SERVIDOR_CAIU():
    newWindow = Toplevel(root)
    newWindow.title("Jogador-01: Aviso!")
    newWindow.geometry("280x155")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO_2(newWindow))

    gif_bg_asset_url = resource_path('recursos/img_AVISO_SERVIDOR_DESCONECTADO_jogador_bg.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.place(x=0, y=0)
    lbl_with_my_gif.start()

    ok_button = Button(newWindow, image=imagem_OK_BUTTON_asset,command=lambda:fecha_APLICACAO_2(newWindow))
    ok_button.place(x=127, y=107)
        
"""
*
*       **********************************
*  ~~~ Inicializando a aplicação do Jogador ~~~
*       **********************************
*
"""

if __name__ == "__main__":
    pede_dados_IP_SERVIDOR()
    root.mainloop()     
