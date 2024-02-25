from Telas import *
from Database import *


class TelaDeFuncoes:
    def __init__(self):
        self.telafuncoes = Tk()
        self.telafuncoes.configure(background=azulescuro)
        self.telafuncoes.geometry('1000x600')
        self.telafuncoes.title('Funcionalidade do Sistema')
        self.telafuncoes.resizable(width=False, height=False)
        HeightFrame = Frame(self.telafuncoes, width=1000, height=30, bg=azulcinza)
        HeightFrame.pack(side=TOP)
        TituloLabel = Label(HeightFrame, text='Gestão Contábil', font=('Century Gothic', 15, 'bold'), bg=azulcinza,
                            fg=branco)
        TituloLabel.place(x=5, y=0)
        self.telafuncoes.mainloop()



