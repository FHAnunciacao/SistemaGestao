import os.path
from Telas import *
from Telas.interações import *


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

        # Daqui para cima foi criado apenas o layout da tela, as imagens e texto é apartir daqui

        # Primeira utilidade adicionada ao meu menu principal podemos dizer
        CadastrarProdutoLabel = Label(DonwFrame, text='Cadastrar Produto',
                                      font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg='white', cursor="hand2")
        CadastrarProdutoLabel.place(x=20, y=100)

        # Irei criar várias funções chamando as telas de cada item do menu principal

        # None para que só abra quando clicar
        def abrir_cadastro(event=None):
            cadastrar_produto = CadastroProduto()
            cadastrar_produto.iniciar()

        caminho_foto_cadastar = os.path.dirname(os.path.abspath(__file__))
        caminho_foto_cadastar_final = os.path.join(caminho_foto_cadastar, 'cadastrarproduto.png')
        ImagemCadastrarProduto = PhotoImage(file=caminho_foto_cadastar_final)
        FotoProdutoLabel = Label(DonwFrame, image=ImagemCadastrarProduto, bg=azulescuro, cursor='hand2')
        FotoProdutoLabel.place(x=45, y=10)
        FotoProdutoLabel.bind("<Button-1>", abrir_cadastro)
        # O bind não aceita retorno de class por isso foi feito função para chamar class

        self.telafuncoes.mainloop()
