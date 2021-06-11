from PyQt5  import uic, QtWidgets, QtGui


class JanelaPrincipal:
    def __init__(self, app, janela) -> None:
        self.app = app
        self.janela = janela
        
        # self.janela.gui_farmacia_viva.setPixmap(QtGui.QPixmap('Logo Farmacia Viva.png'))

        self.botoes_principais()

        Escrever(self.janela)

        janela.show()
        self.app.exec()

    def botoes_principais(self):
        # self.janela.botao_editar.clicked.connect(lambda: Editar(self.janela));
        self.janela.botao_editar.clicked.connect(self.print)
        self.janela.botao_ler.clicked.connect(lambda: Ler(self.janela))
        self.janela.botao_escrever.clicked.connect(lambda: Escrever(self.janela))

    def print(self):
        print('oi')

class Editar:
    def __init__(self, janela) -> None:
        self.janela = janela

        self.janela.frame_escrever.close()
        self.janela.frame_ler.close()
        self.janela.frame_editar.show()  
        

class Escrever:
    def __init__(self, janela) -> None:
        self.janela = janela
        self.janela.frame_editar.close()
        self.janela.frame_ler.close()
        self.janela.frame_escrever.show()
        
        self.janela.botao_salvar.clicked.connect(self.salvar)
        self.janela.botao_excluir.clicked.connect(self.excluir)

    def colheita(self):
        pass

    def corte(self):
        pass

    def secagem(self):
        pass

    def controle(self):
        pass

    def cor(self):
        pass

    def odor(self):
        pass

    def embalagem(self):
        pass

    def salvar(self):
        lote = self.janela.linha_colheita_lote.text()
        print(lote)
        print(1)

    def excluir(self):
        print('cara de pau')
 


class Ler:
    def __init__(self, janela) -> None:
        self.janela = janela

        self.janela.frame_editar.close()
        self.janela.frame_escrever.close()
        self.janela.frame_ler.show()

        self.colheita()


    def colheita(self):

        # redimensinando o tamanho de todas as colunas
        for i in range(0, 5):
            self.janela.tabela_colheita.setColumnWidth(i, 250)

        self.carregando_dados()

    def carregando_dados(self):
        colheita = [{"Lote": "0001",
                    "Data": "05/04/2021",
                    "Hora": "16:00",
                    "Peso Fresco": "500",
                    "Profissional": "Guilherme"
                    }, {"Lote": "0002",
                    "Data": "05/04/2021",
                    "Hora": "16:00",
                    "Peso Fresco": "5050",
                    "Profissional": "Guilherme"
                    }, {"Lote": "0003",
                    "Data": "05/04/2021",
                    "Hora": "16:00",
                    "Peso Fresco": "500",
                    "Profissional": "Guilherme"
                    }, {"Lote": "0001",
                    "Data": "05/04/2021",
                    "Hora": "16:00",
                    "Peso Fresco": "5040",
                    "Profissional": "Guilherme"
                    }]

        row = 0
        self.janela.tabela_colheita.setRowCount(len(colheita))
        for data in colheita:
            self.janela.tabela_colheita.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Lote"]))
            self.janela.tabela_colheita.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Data"]))
            self.janela.tabela_colheita.setItem(row, 2, QtWidgets.QTableWidgetItem(data["Hora"]))
            self.janela.tabela_colheita.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Peso Fresco"]))
            self.janela.tabela_colheita.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Profissional"]))
            row += 1


JanelaPrincipal(app=QtWidgets.QApplication([]), janela=uic.loadUi("Farmacia.ui"))








