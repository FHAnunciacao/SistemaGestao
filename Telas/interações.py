from Telas.TelaPadrao import *

# AQUI É ONDE PRETENDO DEIXAR TODAS AS INTERAÇÕES DO ARQUIVO Telafunções.py


class CadastroProduto(Padrao):
    def __init__(self, geometry="1000x600", title="Cadastro de Produto"):
        super().__init__(geometry, title)

    def iniciar(self):
        ReferenciaLabel = Label(self.Padrao, text='Referencia', font=('Century Gothic', 10, 'bold'), bg=azulescuro,
                                fg=branco)
        ReferenciaLabel.place(x=5, y=10)
        ReferenciaEntry = ttk.Entry(self.Padrao, width=20)
        ReferenciaEntry.place(x=8, y=30)

        DescricaoLabel = Label(self.Padrao, text='Descrição do Produto', font=('Century Gothic', 10, 'bold'),
                               bg=azulescuro, fg=branco)
        DescricaoLabel.place(x=200, y=10)
        DescricaoEntry = ttk.Entry(self.Padrao, width=100)
        DescricaoEntry.place(x=200, y=30)

        UnidadeLabel = Label(self.Padrao, text='Unidade de Medida', font=('Century Gothic', 10, 'bold'),
                             bg=azulescuro, fg=branco)
        UnidadeLabel.place(x=850, y=10)
        UnidadeEntry = ttk.Entry(self.Padrao, width=20)
        UnidadeEntry.place(x=853, y=30)

        MarcaLabel = Label(self.Padrao, text='Marca', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        MarcaLabel.place(x=5, y=70)
        MarcaEntry = ttk.Entry(self.Padrao, width=30)
        MarcaEntry.place(x=6, y=90)

        TipoItemLabel = Label(self.Padrao, text='Tipo de Item', font=('Century Gothic', 10, 'bold'),
                              bg=azulescuro, fg=branco)
        TipoItemLabel.place(x=220, y=70)
        TipoItemEntry = ttk.Entry(self.Padrao, width=20)
        TipoItemEntry.place(x=220, y=90)

        GtinLabel = Label(self.Padrao, text='GTIN', font=('Century Gothic', 10, 'bold'), bg=azulescuro, fg=branco)
        GtinLabel.place(x=400, y=70)
        GtinEntry = ttk.Entry(self.Padrao, width=25)
        GtinEntry.place(x=400, y=90)

        ConfirmarButton = ttk.Button(self.Padrao, text='Confirmar', command=self.confirmarcadastro)
        ConfirmarButton.place(x=400, y=500)

        CancelarButton = ttk.Button(self.Padrao, text='Cancelar', command=self.Padrao.destroy)
        CancelarButton.place(x=500, y=500)

        self.Padrao.mainloop()  # Esse padrão é o atributo da Class Padrao

    def confirmarcadastro(self):
        pass






abrir = CadastroProduto()
abrir.iniciar()
