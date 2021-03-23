from PyQt5  import uic, QtWidgets


class JanelaPrincipal:
    def __init__(self, app, janela) -> None:
        self.app = app
        self.janela = janela

        self.botoes_principais()
        janela.show()
        self.app.exec()

    def botoes_principais(self):
        self.janela.botao_editar.clicked.connect(lambda: Editar(self.janela))
        self.janela.botao_ler.clicked.connect(lambda: Ler(self.janela))
        self.janela.botao_escrever.clicked.connect(lambda: Escrever(self.janela))


class Editar:
    def __init__(self, janela) -> None:
        self.janela = janela

        self.janela.frame_escrever.close()
        self.janela.frame_editar.show()  
          

class Escrever:
    def __init__(self, janela) -> None:
        self.janela = janela

        self.janela.frame_editar.show()
        self.janela.frame_escrever.show()


class Ler:
    def __init__(self, janela) -> None:
        self.janela = janela

        self.janela.frame_editar.close()
        self.janela.frame_escrever.close() 


JanelaPrincipal(app=QtWidgets.QApplication([]), janela=uic.loadUi("Farmacia.ui"))








