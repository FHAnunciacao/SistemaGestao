from tkinter import *
from Telas import *

class Padrao:
    def __init__(self, geometry="400x300", title="Padrão"):
        self.Padrao = Tk()
        self.Padrao.title(title)
        self.Padrao.geometry(geometry)
        self.Padrao.resizable(height=False, width=False)
        self.Padrao.configure(background=azulescuro)



