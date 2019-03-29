import sys
from PyQt4 import QtGui, QtCore
import sqlite3
import pygame

pygame.mixer.init()
pygame.init()
black=(0,0,0)


conn=sqlite3.connect('project.db')
c=conn.cursor()


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100,100, 600, 400)
        self.setWindowTitle("MUSIC PLAYER!")
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.text_field = QtGui.QPlainTextEdit(self)
        self.text_field.setMinimumSize (600,400)
        self.text_field.setStyleSheet("background-image: url(tut.png); background-attachment: fixed")
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        btn1 = QtGui.QPushButton("p@u$e", self)
        btn2 = QtGui.QPushButton('Re$uMe', self)
        btn1.setIcon(QtGui.QIcon('play.png'))
        btn2.setIcon(QtGui.QIcon('res.png'))
        btn1.setStyleSheet("background-color: rgb(150,150,150)")
        btn2.setStyleSheet("background-color: rgb(150,150,150)")
        btn1.clicked.connect(self.pau)
        btn2.clicked.connect(self.res)
        btn1.resize(btn1.minimumSizeHint())
        btn1.move(150,200)
        btn2.resize(btn2.minimumSizeHint())
        btn2.move(375,200)
        #self.play = QtGui.QLabel("SONGS", self)
        #self.play.move(50,150)
        self.scrol()

  

    def scrol(self):
        comboBox=QtGui.QComboBox(self)
        c.execute('select song_name from song')
        data=c.fetchall()
        for row in data:
             comboBox.addItem(row[0])
        comboBox.resize(100,30)
        comboBox.move(250,100)
        comboBox.activated[str].connect(self.play)
        self.show()

    def play(self,text):
        t=text
        text=text+".mp3"
        pygame.mixer.music.load(text)
       # self.play.setText(t)
        #QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(t))
        pygame.mixer.music.play()


    def pau(self):
        pygame.mixer.music.pause()

    def res(self):
        pygame.mixer.music.unpause()

    def close_application(self):
        print("NICE TRY BOI!!!")
        sys.exit()
    
                
    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
