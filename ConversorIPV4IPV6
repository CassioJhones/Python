import ipaddress
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 30
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 30
        self.segundoContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
//Cássio Jhones
//Sandro Junior
        self.titulo = Label(self.primeiroContainer, text=" CONVERSOR IPV4 / IPV6")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="IPV4: ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.converter = Button(self.quartoContainer)
        self.converter["text"] = " CONVERTER "
        self.converter["font"] = ("Calibri", "12", "bold")
        self.converter["width"] = 12
        self.converter["command"] = self.converteIPV4
        self.converter.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    # Método verificar IP
    def converteIPV4(self):
        try:
            ipaddress.IPv6Address('2002::' + self.nome.get()).exploded
            self.mensagem["text"] = '\nIP Válido: ' + ipaddress.IPv6Address('2002::' + self.nome.get()).exploded
        except:
            self.mensagem["text"] = "Digite um IP válido!!!"



root = Tk()
root.wm_title("CONVERSOR")
Application(root)
root.mainloop()
