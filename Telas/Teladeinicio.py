from Telas.Telacadastro import *
from Telas.Telafuncoes import *
from Telas.Recuperarsenha import *


class TelaDeAcesso:
    def __init__(self):
        #  Criando a janela que vai ser base para as divisões
        self.janela = Tk()
        self.janela.geometry('1000x600')
        self.janela.configure(background='white')
        self.janela.title('SISTEMA GERENCIADOR')
        self.janela.resizable(width=False, height=False)
        self.janela.iconbitmap(default="Telas/icon.ico")
        # aqui inseri a variavel logo para usar no frame da direita que irei criar para usar quando criar os Frame
        logo = PhotoImage(file="Telas/caduceu.png")
        # Separação da janela principal em dois Frame
        LeftFrame = Frame(self.janela, width=200, height=600, bg=cyan)
        LeftFrame.pack(side=LEFT)
        RightFrame = Frame(self.janela, width=799, height=600, bg=azulescuro)
        RightFrame.pack(side=RIGHT)
        LogoLabel = Label(LeftFrame, image=logo, bg=cyan)
        LogoLabel.place(x=30, y=150)

        def acessarsistema():

            UsuarioLogin = UserEntry.get()
            SenhaLogin = SenhaEntry.get()
            Database.cursor.execute("""
                        SELECT * FROM Users
                        WHERE (Usuario = ? and Senha = ?)
                        """, (UsuarioLogin, SenhaLogin))
            Verificador = Database.cursor.fetchone()
            if Verificador is not None:
                messagebox.showinfo(title='Aviso', message='Acesso Liberado')
                self.janela.destroy()
                TelaDeFuncoes()
            else:
                messagebox.showerror(title='Aviso', message='Acesso Negado')

        # Criando os botões e os campos para futuramente usar o get()

        UserLabel = Label(RightFrame, text='Usuário:', font=('Century Gothic', 15), bg='#344A53', fg='white')
        UserLabel.place(x=290, y=290)
        UserEntry = ttk.Entry(RightFrame, width=26)
        UserEntry.place(x=375, y=295)

        SenhaLabel = Label(RightFrame, text='Senha:', font=('Century Gothic', 15), bg='#344A53', fg='white')
        SenhaLabel.place(x=297, y=325)
        SenhaEntry = ttk.Entry(RightFrame, width=26, show='•')
        SenhaEntry.place(x=374, y=330)

        LogarButton = ttk.Button(RightFrame, text='Logar', command=acessarsistema)
        LogarButton.place(x=375, y=360)

        CadastrarButton = ttk.Button(RightFrame, text='Cadastrar', command=TelaCadastro)
        CadastrarButton.place(x=460, y=360)

        RecuperarButton = ttk.Button(RightFrame, text='Esqueceu a senha? Clique aqui!', command=RecuperarSenha)
        RecuperarButton.place(x=375, y=390)

        self.janela.mainloop()

