import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLabel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.acceptDrops()
        # set the title
        self.setWindowTitle("qrcode link")

        # setting  the geometry of window
        self.setGeometry(1300, 150, 540, 575)


        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap('myqr.png')

        # adding image to label
        self.label.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())


        # lineedit to get the link copied to clipboard
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Link:')
        self.textLabel = QLabel(self)
        self.line = QLineEdit(self)
        self.line.insert("copy your link here ")

        self.line.move(60, 530)
        self.line.resize(450, 32)
        self.nameLabel.move(20, 530)
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())