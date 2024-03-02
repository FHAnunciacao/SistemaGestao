from Telas import *
import Database


class TelaCadastro:
    def __init__(self):
        self.Cadastro = Toplevel(None)
        self.Cadastro.title('Cadastro de Usuário')
        self.Cadastro.geometry('450x300')
        self.Cadastro.configure(background=azulescuro)
        self.Cadastro.resizable(width=False, height=False)

        # Cria os campos de entrada na nova janela

        def salvardatabase():
            try:
                Nome = NomeEntry.get().title().strip()
                Email = EmailEntry.get()
                CPF = CpfEntry.get()
                # Quis validar algumas informações para preencher corretamente
                if CPF.isnumeric():
                    pass
                else:
                    messagebox.showerror(title='CPF', message='CPF DEVE SER NÚMEROS')
                Usuario = UserEntry.get().strip()
                Senha = SenhaEntry.get()
                if Nome == "" or Email == "" or CPF == "" or Usuario == "" or Senha == "":
                    messagebox.showerror(title='AVISO', message='CAMPOS DEVEM SER PREENCHIDOS')
                    self.Cadastro.destroy()
                    return
                Database.cursor.execute("""
                            INSERT INTO Users (Nome, Email, CPF, Usuario, Senha) VALUES (?, ?, ?, ?, ?)
                            """, (Nome, Email, CPF, Usuario, Senha))
                Database.conn.commit()
                messagebox.showinfo(title='Aviso', message='Cadastro Concluído')
                self.Cadastro.destroy()  # fecha a tela depois de salvar os arquivos

            except sqlite3.IntegrityError:
                messagebox.showerror(title='AVISO', message='CPF ja Cadastrado ou Usuário')
                self.Cadastro.destroy()

        Label(self.Cadastro, text='Nome:', font=('Century Gothic', 15), bg='#344A53', fg='white').place(x=15, y=10)
        NomeEntry = ttk.Entry(self.Cadastro, width=50)
        NomeEntry.place(x=90, y=15)
        Label(self.Cadastro, text='Email:', font=('Century Gothic', 15), bg='#344A53', fg='white').place(x=21, y=40)
        EmailEntry = ttk.Entry(self.Cadastro, width=50)
        EmailEntry.place(x=90, y=45)
        Label(self.Cadastro, text='CPF:', font=('Century Gothic', 15), bg='#344A53', fg='white').place(x=35, y=70)
        CpfEntry = ttk.Entry(self.Cadastro, width=50)
        CpfEntry.place(x=90, y=75)
        Label(self.Cadastro, text='Usuário:', font=('Century Gothic', 15), bg='#344A53', fg='white').place(x=2, y=100)
        UserEntry = ttk.Entry(self.Cadastro, width=50)  # Variável com o mesmo nome da tela de início
        UserEntry.place(x=90, y=105)
        Label(self.Cadastro, text='Senha:', font=('Century Gothic', 15), bg='#344A53', fg='white').place(x=10, y=130)
        SenhaEntry = ttk.Entry(self.Cadastro, width=50, show='•')  # Variável com o mesmo nome da tela de início
        SenhaEntry.place(x=90, y=135)

        # Criando os botões que vai confirmar a operação e gravar no banco de dados
        Confirmar_Registro_Button = ttk.Button(self.Cadastro, text='Registrar', width=20, command=salvardatabase)
        Confirmar_Registro_Button.place(x=80, y=200)

        Voltar_Button = ttk.Button(self.Cadastro, text='Voltar', width=15, command=self.Cadastro.destroy)
        Voltar_Button.place(x=220, y=200)

        self.Cadastro.mainloop()
