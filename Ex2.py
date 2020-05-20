from PySide2.QtWidgets import *

class Deuxieme(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layoutH=QHBoxLayout()
        self.barre=QProgressBar()
        self.slider=QSlider()
        self.layoutH.addWidget(self.barre)
        self.layoutH.addWidget(self.slider)
        self.slider.valueChanged.connect(self.Signal)
        self.setLayout(self.layoutH)

    def Signal(self):
        self.Slot(self.slider.value())

    def Slot(self,value):
        self.barre.setValue(value)

if __name__ == "__main__":
    app = QApplication([])
    win = Deuxieme()
    win.show()
    app.exec_()
