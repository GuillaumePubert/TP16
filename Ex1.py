from PySide2.QtWidgets import *
import random
class Premier(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500,300)
        self.setWindowTitle("Cycles de l'ISEN")
        self.b1=QPushButton("Changer le cycle")
        self.obj1=QLabel("CSI")
        self.layoutV=QVBoxLayout()
        self.layoutV.addWidget(self.obj1)
        self.layoutV.addWidget(self.b1)
        self.b1.clicked.connect(self.Bouton)
        self.setLayout(self.layoutV)

    def Bouton(self):
        liste=["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        choix=random.choice(liste)
        self.obj1.setText(choix)

if __name__ == "__main__":
    app = QApplication([])
    win = Premier()
    win.show()
    app.exec_()
