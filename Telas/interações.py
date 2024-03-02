from Telas.TelaPadrao import *

# AQUI É ONDE PRETENDO DEIXAR TODAS AS INTERAÇÕES DO ARQUIVO Telafunções.py


class CadastroProduto(Padrao):
    def __init__(self, geometry="1000x600", title="Cadastro de Produto"):
        super().__init__(geometry, title)

    def iniciar(self):
        self.Padrao.mainloop()  # Esse padrão é o atributo da Class Padrao
