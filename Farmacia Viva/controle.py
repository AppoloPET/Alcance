from PyQt5  import uic, QtWidgets


class JanelaPrincipal:
    def __init__(self, app, janela) -> None:
        self.app = app
        self.janela = janela

        self.botoes_principais()

        janela.show()
        self.app.exec()

    def botoes_principais(self):
        self.janela.botao_editar.clicked.connect(self.frame_editar)
        self.janela.botao_ler.clicked.connect(self.frame_ler)
        self.janela.botao_escrever.clicked.connect(self.frame_escrever)

    def frame_editar(self):
        self.janela.frame_escrever.close()
        self.janela.frame_editar.show()

    def frame_ler(self):
        self.janela.frame_editar.close()
        self.janela.frame_escrever.close()

    def frame_escrever(self):
        self.janela.frame_editar.show()
        self.janela.frame_escrever.show()
    

class FrameEditar:
    def __init__(self) -> None:
        pass


class FrameEscrever:
    def __init__(self) -> None:
        pass


class FrameLer:
    def __init__(self) -> None:
        pass



JanelaPrincipal(app=QtWidgets.QApplication([]), janela=uic.loadUi("Farmacia.ui"))









