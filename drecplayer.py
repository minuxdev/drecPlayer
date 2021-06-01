from PyQt5.QtGui import QIcon, QPicture, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# from pygame import mixer
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drec Player")
        self.setMinimumSize(250,300)

        self.setStyleSheet("QMainWindow {background-color: green}")
        window = QWidget()
        self.vbox = QVBoxLayout()
        window.setLayout(self.vbox)
        self.setCentralWidget(window)

        # Creating basic widgets
        imageLoader = QLabel()
        imageLoader.setPixmap(QPixmap("music.png"))
        imageLoader.setAlignment(Qt.AlignCenter)
        # imageLoader.setText("IMAGE HERE")
        self.vbox.addWidget(imageLoader)

        labThems = "QLabel {font-size: 13px; color: white}"
        self.fileName = QLabel()
        self.fileName.setStyleSheet(labThems)
        self.fileName.setMaximumHeight(10)
        self.fileName.setText("File Name")
        self.fileName.setAlignment(Qt.AlignCenter)
        self. vbox.addWidget(self.fileName)

        # Creating a buttonGroup
        them = "QPushButton {border-radius: 30px; background-color: white}"

        buttonGroup = QGroupBox()
        buttonGroup.setMaximumHeight(50)
        hbox = QHBoxLayout()
        buttonGroup.setLayout(hbox)

        self.back = QPushButton()
        self.back.setStyleSheet(them)
        self.back.setIcon(QIcon("back.icon"))
        self.back.setStyleSheet(them)
        hbox.addWidget(self.back)

        self.play = QPushButton()
        self.play.setStyleSheet(them)
        self.play.setIcon(QIcon("play.icon"))
        hbox.addWidget(self.play)

        self.pause = QPushButton()
        self.pause.setStyleSheet(them)
        self.pause.setIcon(QIcon("pause.icon"))
        hbox.addWidget(self.pause)

        self.Next = QPushButton()
        self.Next.setStyleSheet(them)
        self.Next.setIcon(QIcon("next.icon"))
        hbox.addWidget(self.Next)

        self.vbox.addWidget(buttonGroup)
    

class Player(Window):
    def __init__(self):
        super().__init__()
        self.win = Window()
        
        
        self.win.play.clicked.connect(self.Play)

    def Play(self):
        print("Im Playing")



if __name__ == "__main__":
    app = QApplication([])
    # myapp = Window()
    # myapp.show()
    myapp = Player()
    myapp.win.show()
    sys.exit(app.exec_())
