import Database
from Telas.TelaPadrao import *

# AQUI É ONDE PRETENDO DEIXAR TODAS AS INTERAÇÕES DO ARQUIVO Telafunções.py


class CadastroProduto(Padrao):
    def __init__(self, geometry="1000x600", title="Cadastro de Produto"):
        super().__init__(geometry, title)

        # Referencia
        ReferenciaLabel = Label(self.Padrao, text='Referencia', font=('Century Gothic', 10, 'bold'), bg=azulescuro,
                                fg=branco)
        ReferenciaLabel.place(x=5, y=10)
        self.ReferenciaEntry = ttk.Entry(self.Padrao, width=20)
        self.ReferenciaEntry.place(x=8, y=30)

        # Descrição do Produto
        DescricaoLabel = Label(self.Padrao, text='Descrição do Produto', font=('Century Gothic', 10, 'bold'),
                               bg=azulescuro, fg=branco)
        DescricaoLabel.place(x=200, y=10)
        self.DescricaoEntry = ttk.Entry(self.Padrao, width=100)
        self.DescricaoEntry.place(x=200, y=30)

        # Unidade de Medida
        UnidadeLabel = Label(self.Padrao, text='Unidade de Medida', font=('Century Gothic', 10, 'bold'),
                             bg=azulescuro, fg=branco)
        UnidadeLabel.place(x=850, y=10)
        self.UnidadeEntry = ttk.Entry(self.Padrao, width=20)
        self.UnidadeEntry.place(x=853, y=30)

        # Marca do Produto
        MarcaLabel = Label(self.Padrao, text='Marca', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        MarcaLabel.place(x=5, y=70)
        self.MarcaEntry = ttk.Entry(self.Padrao, width=30)
        self.MarcaEntry.place(x=8, y=90)

        # Tipo de Produto
        TipoItemLabel = Label(self.Padrao, text='Tipo de Item', font=('Century Gothic', 10, 'bold'),
                              bg=azulescuro, fg=branco)
        TipoItemLabel.place(x=220, y=70)
        self.TipoItemEntry = ttk.Entry(self.Padrao, width=20)
        self.TipoItemEntry.place(x=220, y=90)

        # Gtim do Produto
        GtinLabel = Label(self.Padrao, text='GTIN', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        GtinLabel.place(x=400, y=70)
        self.GtinEntry = ttk.Entry(self.Padrao, width=25)
        self.GtinEntry.place(x=400, y=90)

        # Grupo
        GrupoLabel = Label(self.Padrao, text='Grupo', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        GrupoLabel.place(x=600, y=70)
        self.GrupoEntry = ttk.Entry(self.Padrao, width=25)
        self.GrupoEntry.place(x=603, y=90)

        # SubGrupo
        SubGrupoLabel = Label(self.Padrao, text='SubGrupo', font=('Century Gothic', 10, 'bold'),
                              bg=azulescuro, fg=branco)
        SubGrupoLabel.place(x=5, y=140)
        self.SubGrupoEntry = ttk.Entry(self.Padrao, width=25)
        self.SubGrupoEntry.place(x=8, y=160)

        # NCM
        NcmLabel = Label(self.Padrao, text='NCM', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        NcmLabel.place(x=200, y=140)
        self.NcmEntry = ttk.Entry(self.Padrao, width=30)
        self.NcmEntry.place(x=203, y=160)

        # CST
        CstLabel = Label(self.Padrao, text='CST', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        CstLabel.place(x=415, y=140)
        self.CstEntry = ttk.Entry(self.Padrao, width=10)
        self.CstEntry.place(x=418, y=160)

        # ALÍQUOTA IPI
        AliquotaLabel = Label(self.Padrao, text='Alíquota IPI', font=('Century Gothic', 10, 'bold'),
                              bg=azulescuro, fg=branco)
        AliquotaLabel.place(x=550, y=140)
        self.AliquotaEntry = ttk.Entry(self.Padrao, width=10)
        self.AliquotaEntry.place(x=553, y=160)

        ConfirmarButton = ttk.Button(self.Padrao, text='Confirmar', command=self.confirmarcadastro)
        ConfirmarButton.place(x=400, y=500)

        CancelarButton = ttk.Button(self.Padrao, text='Cancelar', command=self.Padrao.destroy)
        CancelarButton.place(x=500, y=500)

        self.Padrao.mainloop()  # Esse padrão é o atributo da Class Padrao

    def confirmarcadastro(self):
        try:
            Referencia = self.ReferenciaEntry.get()
            Descricao = self.DescricaoEntry.get()
            Unidade = self.UnidadeEntry.get()
            Marca = self.MarcaEntry.get()
            Tipo = self.TipoItemEntry.get()
            Ncm = self.NcmEntry.get()
            Gtin = self.GtinEntry.get()
            Grupo = self.GrupoEntry.get()
            Subgrupo = self.SubGrupoEntry.get()
            Cst = self.CstEntry.get()
            Aliquota = self.AliquotaEntry.get()
            Database.cursor.execute("""
                        INSERT INTO Produtos (Referencia, [Descrição do Produto], [Unidade de Medida], Marca,
                        [Tipo de Item], NCM, GTIN, Grupo, SubGrupo, CST, [Alíquota de IPI]) VALUES (?, ?, ?, ?, ?,
                         ?, ?, ?, ?, ?, ?)""", (Referencia, Descricao, Unidade, Marca, Tipo, Ncm, Gtin, Grupo,
                                                Subgrupo, Cst, Aliquota))
            Database.conn.commit()
            messagebox.showinfo(title='Cadastro', message='Produto cadastrado com sucesso')
            self.Padrao.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror(title='ERRO!!', message='Algo deu errado, tente novamente mais tarde!')
            self.Padrao.destroy()
