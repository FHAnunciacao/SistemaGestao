import os.path

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
        DonwFrame = Frame(self.telafuncoes, width=1000, height=570, bg=azulescuro)
        DonwFrame.pack(side=BOTTOM)
        TituloLabel = Label(HeightFrame, text='Gestão Contábil', font=('Century Gothic', 15, 'bold'), bg=azulcinza,
                            fg=branco)
        TituloLabel.place(x=5, y=0)

        CadastrarProdutoLabel = Label(DonwFrame, text='Cadastrar Produto',
                                      font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg='white', cursor="hand2")
        CadastrarProdutoLabel.place(x=20, y=100)

        caminho_foto_cadastar = os.path.dirname(os.path.abspath(__file__))
        caminho_foto_cadastar_final = os.path.join(caminho_foto_cadastar, 'cadastrarproduto.png')
        ImagemCadastrarProduto = PhotoImage(file=caminho_foto_cadastar_final)
        FotoProdutoLabel = Label(DonwFrame, image=ImagemCadastrarProduto, bg=azulescuro, cursor='hand2')
        FotoProdutoLabel.place(x=45, y=10)
        self.telafuncoes.mainloop()
