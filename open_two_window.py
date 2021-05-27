import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
     def __init__(self):
          super(MainWindow, self).__init__()
          self.resize(400, 300)

          # Button
          self.button = QPushButton(self)
          self.button.setGeometry(0, 0, 400, 300)
          self.button.setText('Main Window')
          self.button.setStyleSheet('font-size:40px')

          # Sub Window
          self.sub_window = SubWindow()

          # Button Event
          self.button.clicked.connect(self.sub_window.show)


class SubWindow(QWidget):
     def __init__(self):
          super(SubWindow, self).__init__()
          self.resize(400, 300)

         # Label
        
          self.label = QLabel(self)
          self.label.setGeometry(10, 0,50, 100)
          self.label.setText('0:rest')
          self.label.setAlignment(Qt.AlignCenter)
          self.label.setStyleSheet('font-size:20px')

          self.labe2 = QLabel(self)
          self.labe2.setGeometry(10, 0, 100, 200)
          self.labe2.setText('1:keyboard')
          self.labe2.setAlignment(Qt.AlignCenter)
          self.labe2.setStyleSheet('font-size:20px')

          self.labe3 = QLabel(self)
          self.labe3.setGeometry(10, 0, 150, 300)
          self.labe3.setText('2:mouse')
          self.labe3.setAlignment(Qt.AlignCenter)
          self.labe3.setStyleSheet('font-size:20px')
        
        


if __name__ == '__main__':
     app = QApplication([])
     window = MainWindow()
     window.show()
     
     sys.exit(app.exec_())