from PySide2.QtWidgets import *

class Troisieme(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.layoutV=QVBoxLayout()
        self.b1=QPushButton("Change mon texte !")
        self.layoutV.addWidget(self.b1)
        self.valeur=0
        #self.b1.clicked.connect(self.Fermer)
        self.b1.clicked.connect(self.ChgtTexte)
        self.setLayout(self.layoutV)

    # def Fermer(self):
    #     self.close()
    def ChgtTexte(self):
        self.valeur+=1
        self.b1.setText("Click"+str(self.valeur))

if __name__ == "__main__":
    app = QApplication([])
    win = Troisieme()
    win.show()
    app.exec_()
