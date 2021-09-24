import sys
sys.path.append('.')
sys.path.append('lib/')

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtGui import QIcon
from time import sleep as delay
import base64
import libQemu

qemu = libQemu.Qemu()




class loadingPage(QWidget):
    #loading gif widget/page
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint) #| Qt.WindowStaysOnTopHint | Qt.SplashScreen)
        self.setAttribute(Qt.WA_TranslucentBackground, True) #100% transparent
        self.setStyleSheet( """
                color: rgba(237,174,28,100%);
                background-color: #181B1D;
                padding: 55px;
                text-align: center;
                border-radius: 15px;
                padding: 0px;
                """)


        self.label = QLabel()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(self.vbox)
        
        self.gif = QMovie('loader.gif')
        self.gif.setScaledSize(QSize().scaled(300, 300, Qt.KeepAspectRatio))
        self.label.setMovie(self.gif)
        self.gif.start()

        



class App(QWidget):
    #main GUI class
    def __init__(self):
        super().__init__()
        self.loadingPage = loadingPage()
        self.title = 'Open Image'
        self.width = 640#280
        self.height = 480#80
        self.left = 100
        self.top = 100
        self.statusbar = QStatusBar()
        #self.setStatusBar(self.statusBar)
        self.progressBar = QProgressBar(self)
        self.statusbar.addWidget(self.progressBar)
        self.loader()
        self.frontCheckDep()
        self.initUI()
        exit()
        
    def Handle_Progress(self, blocknum, blocksize, totalsize):
 
        ## calculate the progress
        readed_data = blocknum * blocksize
 
        if totalsize > 0:
            download_percentage = readed_data * 100 / totalsize
            self.progressBar.setValue(download_percentage)
            QApplication.processEvents()

    def frontCheckDep(self):
        if not qemu.checkDep():
            reply = QMessageBox.question(self, 'Qemu Not Found', 'Do you want to install it?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.loadingPage.show()
                if not qemu.install(self.Handle_Progress):
                    exit()
                self.loadingPage.hide()
            else:
                exit()

    def loader(self):
        #splashscreen. Stored in b64, converted to PNG.
        b64_data = '''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'''
        pm = QPixmap()
        pm.loadFromData(base64.b64decode(b64_data), 'png')
        self.splash = QSplashScreen(pm)
        self.splash.show()
        QTimer.singleShot(2000, self.splash.close)
        delay(2)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        qemu.run(self.openFileNameDialog())
        #self.openFileNamesDialog()
        #self.saveFileDialog()
        self.show()
    
    def openFileNameDialog(self):
        #Open File Dialog. Self explanatory
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PokePi Image (*.pimg);; All Files (*.*)", options=options)
        if fileName:
            return fileName
        else:
            exit()
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)
    
    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
