import Database
from Telas import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class RecuperarSenha:
    def __init__(self):
        self.telarecuperar = Toplevel(None)
        self.telarecuperar.title('Recuperação de Senha')
        self.telarecuperar.geometry('450x300')
        self.telarecuperar.configure(background=azulescuro)
        self.telarecuperar.resizable(width=False, height=False)

        def confirmar():
            try:
                CPF = CpfEntry.get()
                if CPF.isnumeric():
                    pass
                else:
                    messagebox.showerror(title='ERRO', message='CPF deve ser apenas Numero')
                Database.cursor.execute("""
                SELECT Usuario, Senha, Email FROM Users
                WHERE (CPF = ?)
                """, (CPF,))
                Verificador = Database.cursor.fetchone()
                if Verificador is not None:
                    messagebox.showinfo(title='Aviso', message=f'Usuario e Senha enviado para o email:'
                                                               f'***{Verificador[2][3:]}')
                    # Configurando o envio de email
                    remetente = 'Seuemail@gmail.com'
                    senha = 'senha liberada do APP google'

                    # Confiuração do destinatario e email
                    destinatario = Verificador[2]
                    assunto = 'Recuperar Senha'
                    corpo = Verificador
                    mensagem = MIMEMultipart()
                    mensagem['From'] = remetente
                    mensagem['To'] = destinatario
                    mensagem["Subject"] = assunto

                    mensagem.attach(MIMEText(f'Login: {corpo[0]}\nSenha: {corpo[1]} ', "plain"))

                    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
                    servidor_smtp.starttls()
                    servidor_smtp.login(remetente, senha)

                    servidor_smtp.send_message(mensagem)
                    servidor_smtp.quit()

                    self.telarecuperar.destroy()

                else:
                    messagebox.showerror(title=CPF, message='CPF NÃO CADASTRADO NO SISTEMA')
                    self.telarecuperar.destroy()
            except sqlite3.IntegrityError:
                messagebox.showerror(title='SQL', message='PROBLEMA DE CONEXÃO! TENTE NOVAMENTE MAIS TARDE')

        MensagemLabel = Label(self.telarecuperar, text='RECUPERAÇÃO DE LOGIN E SENHA',
                              font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg='white')
        MensagemLabel.place(x=120, y=50)
        CpfLabel = Label(self.telarecuperar, text='CPF:', bg=azulescuro, fg=branco)
        CpfLabel.place(x=25, y=80)

        CpfEntry = Entry(self.telarecuperar, width=50)
        CpfEntry.place(x=70, y=80)

        ConfirmeButton = Button(self.telarecuperar, text='Confirmar!', command=confirmar)
        ConfirmeButton.place(x=200, y=120)

        self.telarecuperar.mainloop()
