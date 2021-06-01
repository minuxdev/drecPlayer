from PyQt5.QtGui import QIcon, QPicture, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pygame
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drec Player")
        self.setMinimumSize(250,300)

        self.setStyleSheet("QMainWindow {background-color: black}")
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
        # hbox.addStretch(5)

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

        # hbox.addStretch(5)
        self.vbox.addWidget(buttonGroup)
    

class Player(Window):
    def __init__(self):
        super().__init__()
        self.win = Window()
    
        pygame.init()
        pygame.mixer.music.load('1. Oh Boy.wav')
        # self.pymodule = mixer.music()
        self.win.play.clicked.connect(self.Main)
        self.win.pause.clicked.connect(self.Main)
        self.win.Next.clicked.connect(self.Main)
        self.win.back.clicked.connect(self.Main)


    def Main(self):
        src = self.win.sender()

        if src == self.win.play:
            print("Play button was triggered")
            self.Play()

        elif src == self.win.pause:
            # print("Pause button was triggered")
            self.status = pygame.mixer.music.get_busy()

            if self.status == 0:
                print("Unpausing")
                self.UnPause()
            else:
                print("Pausing")
                self.Pause()
        
        elif src == self.win.back:
            print("Back button was triggered")

        else:
            print("Next button was triggered")


    def Play(self): 
        pygame.mixer.music.play()
        
    def Pause(self):
        pygame.mixer.music.pause()

    def UnPause(self):
        pygame.mixer.music.unpause()
             


if __name__ == "__main__":
    app = QApplication([])
    # myapp = Window()
    # myapp.show()
    myapp = Player()
    myapp.win.show()
    sys.exit(app.exec_())
