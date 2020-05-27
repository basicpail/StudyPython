import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow,QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('cat.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        button = QPushButton('Quit',self)
        button.move(50,50)
        button.resize(button.sizeHint())
        #button.clicked.connect(QCoreApplication.instance().quit)
        button.clicked.connect(self.btn_clicked)

        #self.move(200,200)
        #self.resize(640, 400)
        #self.setGeometry(200,200,640,400)
        #self.show()

        self.setWindowTitle('My Qt App')
        self.setWindowIcon(QIcon('cat.png'))
        self.setGeometry(100,100,640,400)
        self.show()
    def btn_clicked(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    exit(app.exec_())