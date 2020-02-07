import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import threading
 
 
class YoutubeVideoDownload(QtGui.QMainWindow):
 
    def __init__(self):
        super(YoutubeVideoDownload, self).__init__()
 
        self.initUI()

    def onInputFileButtonClicked(self):
        pass
 
    def initUI(self):
        # Setting label
        self.lbl1 = QtGui.QLabel(self)
        self.lbl1.move(10, 20)
        self.lbl1.setText("Video Link : ")

        # Setting link of video
        self.qle = QtGui.QLineEdit(self)
        self.qle.move(170, 20) # re
        self.qle.setMaxLength(100)
        self.qle.setFixedWidth(430)

        # Setting label
        self.lbl2 = QtGui.QLabel(self)
        self.lbl2.move(10, 100)
        self.lbl2.setText("File Name : ")

        # Setting destination folder
        self.browse = QtGui.QLineEdit(self)
        self.browse.move(170, 100) # re
        self.browse.setMaxLength(100)
        self.browse.setFixedWidth(430)

        # Setting OK button
        self.btn = QtGui.QPushButton("Ok", self)
        self.btn.move(160, 200)
        self.btn.clicked.connect(self.oKClicked)

        # Setting Reset button
        self.btn = QtGui.QPushButton("Reset", self)
        self.btn.move(260, 200)
        self.btn.clicked.connect(self.resetClicked)

        # Setting Close button
        self.btn = QtGui.QPushButton("Close", self)
        self.btn.move(360, 200)
        self.btn.clicked.connect(self.closeClicked)

        # Setting console output on the qt screen
        self.log = QtGui.QTextEdit(self)
        self.log.move(20, 240)
        self.log.setMinimumHeight(220)
        self.log.setMinimumWidth(600)
        self.log.setReadOnly(True)

        self.resize(640, 480)
        self.setWindowTitle('Youtube Window Downloader')
        self.show()
 
    def oKClicked(self):
        self.command = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --no-playlist --merge-output-format mp4 \'" + self.qle.text() + "\' -o " + self.browse.text() + "/video"
        #self.command = "youtube-dl -F --no-playlist \'" + self.qle.text() + "\' -o " + self.browse.text() + "/video"
        print(self.command)
        stdout = os.popen4(str(self.command))[1].read()
        self.log.setText(str(stdout))
    
    def resetClicked(self):
        self.qle.setText("")
        self.browse.setText("")
        self.log.setText("")
    
    def closeClicked(self):
        QCoreApplication.exit(0)

def main():
    try:
        app = QtGui.QApplication(sys.argv)
        ex = YoutubeVideoDownload()
    except:
        print("You must install the following applications in order to run the application :- \n1. Pyqt\n2. ffmpeg\n3. youtube-dl")
        raise
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()