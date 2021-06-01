from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class DrecPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drec Player")
        self.setMinimumSize(500,200)

        window = QWidget()
        self.setCentralWidget(window)

        self.hbox = QHBoxLayout()
        window.setLayout(self.hbox)

        

if __name__ == "__main__":
    app = QApplication([])
    myapp = DrecPlayer()
    myapp.show()
    sys.exit(app.exec_())
