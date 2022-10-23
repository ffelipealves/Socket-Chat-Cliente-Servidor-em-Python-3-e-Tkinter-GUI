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

conexoes_jogadores = []

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
*       **************************************************************
*  ~~~ Codigos das ações e variáveis do Socket do Servidor na aplicação ~~~
*       **************************************************************
*
"""
def servidor(text_area):    
    IP_SERVIDOR =  str(extrai_IP_da_maquina()) #<---- IP DO SERVIDOR, AQUI É PEGUE O IP DA MÁQUINA DO TIPO IPv4! (Ou seja, operamos um esquema de endereçamento IPv4)
    PORTA_SERVIDOR = 12000 #<---- PORTA INSTANCIADA DO SERVIDOR (Usamos uma porta de valor muito alto pois portas de valores pequenos são usadas pelo SO e podem causar conflitos na aplicação)
    
    try:

        #Criamos um 'stream based socket' ou 'soquete baseado em fluxo' (ou seja, um soquete TCP) para o Servidor.
        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #<---- SOCKET DO SERVIDOR*****
        #socket_servidor.bind(('', PORTA_SERVIDOR)) # << [USO DE SOCKETS NO CÓDIGO]
        socket_servidor.bind((IP_SERVIDOR, PORTA_SERVIDOR)) # << [USO DE SOCKETS NO CÓDIGO

        """
        * O método listen geralmente recebe um número como parâmetro,
        * indicando a quantidade de conexões que serão enfileiradas
        * pelo protocolo TCP até que o servidor realize o próximo passo,
        * ou seja o comando accept. Essa é a função que determina esse
        * socket como o servidor dentre os outros. Aqui optei por não
        * definir um parâmetro para ele pois minha aplicação nõ necessitava
        * de tal controle.
        """
        socket_servidor.listen(5) #<---- Mais é explicado no seguinte link: https://stackoverflow.com/questions/2444459/python-sock-listen

        text_area.insert(tk.INSERT,"Servidor conectado!\n")

        IP_SERVIDOR =  str(extrai_IP_da_maquina())
        PORTA_SERVIDOR = '12000'

        # Printo aqui o IPv4 usado pelo servidor para que se possa ser informado aos Jogadores para poderem se conectar ao Servidor caso esteja em outra máquina,
        # claro, isso deve ser informado aos jogadores e eles irão entrar esse dado antes de iniciarem suas aplicações, foi decidido pelo aluno fazer a aplicação
        # assim ao invés de se conseguir esse IP do servidor de uma forma mais automática (Na verdade eu não tinha conhecimento de como fazer isso pois fiz de
        # um jeito que o servior precisa ser iniciado para poder os jogadores entrarem kkkkk).
        text_area.insert(tk.INSERT, "\n>> [IP do Servidor]: "+IP_SERVIDOR+"\n>> [PORTA do Servidor]: "+PORTA_SERVIDOR+"\n", 'dados_servidor')  # <-- tagging `name`
        text_area.tag_config('dados_servidor', foreground='black')
        
        while True:
            # -----> *Aceitamos a tentativa de conexão do cliente:
            conexao_socket_servidor, endereco = socket_servidor.accept() # << [USO DE SOCKETS NO CÓDIGO]
            # -----> *Adicionamos a conexão aceita na nossa lista que vai armazená-la
            conexoes_jogadores.append(conexao_socket_servidor)
            # -----> *Começamos nossa primeira thread que vai gerenciar a conexão de cada 
            #         cliente recebendo suas mensagens e transmitindo-as aos outros clientes,
            #         que aqui é apenas a troca de mensagens dos 2 jogadores rsrsrs:
            threading.Thread(target=recebe_msg_jogadores, args=[conexao_socket_servidor, text_area]).start() #<---- THREAD 'recebe_msg_jogadores' *****

    except Exception as e:
        text_area.insert(tk.INSERT,f"\n>> An error has occurred when instancing socket: {e}.\n--------------------------------------------------\n")

    # palavra-chave ''finally''
    # Python fornece uma palavra-chave finalmente, que é sempre executada
    # após os blocos try e except. O bloco finally sempre é executado após
    # o término normal do bloco try ou após o término do bloco try devido
    # a alguma exceção. 
    finally:
        # Em caso de algum problema, limpamos todas as conexões e fechamos a conexão do servidor:
        if len(conexoes_jogadores) > 0:
            for conn in conexoes_jogadores:
                remove_conexao(conn)

        socket_instance.close() # << [USO DE SOCKETS NO CÓDIGO]

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

    gif_bg_asset_url = resource_path('recursos/img_AVISO_DESCONECTAR_SERVIDOR_bg.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.place(x=0, y=0)
    lbl_with_my_gif.start()
    
    sim_button = Button(newWindow, text='Sim', width=12, command=lambda:fecha_APLICACAO(newWindow))
    sim_button.place(x=124, y=154)

    nao_button = Button(newWindow, text='Não', width=12, command=lambda:fecha_janela_TOPLEVEL(newWindow))
    nao_button.place(x=240, y=154)

def mostra_janela_SERVIDOR():    
    newWindow = Toplevel(root)
    newWindow.title("Socket: Servidor")

    newWindow.geometry("476x220")

    newWindow.protocol("WM_DELETE_WINDOW", mostra_janela_AVISO_FECHAR_SERVIDOR)

    gif_bg_asset_url = resource_path('recursos/img_SERVIDOR_CONECTADO_bg.gif')    
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.place(x=0, y=0)
    lbl_with_my_gif.start()
    
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
    threading.Thread(target=mostra_janela_SERVIDOR).start() #<---- THREAD 'mostra_janela_SERVIDOR' *****
    root.mainloop()
