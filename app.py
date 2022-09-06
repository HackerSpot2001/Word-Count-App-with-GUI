from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel, QMessageBox,QPushButton,QPlainTextEdit
from PyQt5.uic import loadUi
import sys

class win(QMainWindow):
    def __init__(self):
        super(win,self).__init__()
        loadUi("untitled.ui",self)
        self.label_2 = self.findChild(QLabel,"label_2")
        self.plainText = self.findChild(QPlainTextEdit,"plainTextEdit")
        self.pushBtn = self.findChild(QPushButton,"pushButton")
        self.pushBtn.clicked.connect(self.getText)
    
    def getText(self):
        text = str(self.plainText.toPlainText())
        if text == None:
            QMessageBox.warning(self,"Warning","Please fill text field.")
        
        else:
            self.label_2.setText("Word Count: {}".format(str(len(list(text.split(" "))))))
            self.plainText.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = win()
    window.show()
    sys.exit(app.exec())