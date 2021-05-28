import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

n=int(input("輸入:"))
mode_list=[0,1,2]

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

# 置頂視窗--button 形式
class SubWindow(QDialog,QWidget):

     def __init__(self):
          super().__init__()
          self.title = 'Mode show'
          self.left = 1500
          self.top = 50
          self.width = 200
          self.height = 100
          self.initUI()
          self.createHorizontalLayout


     def initUI(self):
          self.setWindowTitle(self.title)
          
          self.setGeometry(self.left, self.top, self.width, self.height)
          
          #置頂參數
          self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
          
          self.createHorizontalLayout()

          #設定圖示，QIcon物件接收一個我們要顯示的圖片路徑作為引數。
          # self.setWindowIcon(QIcon('web3.png'))

          # windowLayout = QVBoxLayout()
          # windowLayout.addWidget(self.horizontalGroupBox)
          # self.setLayout(windowLayout)

          self.show()

     def createHorizontalLayout(self):

          hbox = QHBoxLayout()

          if n == mode_list[0]:
               hbox.addWidget(QLabel("0:Rest"))
          elif n == mode_list[1]:
               hbox.addWidget(QLabel("1:Keyboard"))
          elif n == mode_list[2]:
               hbox.addWidget(QLabel("2:Mouse"))
          # self.setGeometry(self.left, self.top, self.width, self.height)
          self.setWindowTitle('Showing')
          self.setLayout(hbox)
          self.show()
          """
          self.horizontalGroupBox = QGroupBox("Showing")
          
          layout = QHBoxLayout()
          change_mode = "rest"
          buttonBlue = QPushButton(change_mode, self)
          buttonBlue.clicked.connect(self.on_click)
          layout.addWidget(buttonBlue) 

          buttonRed = QPushButton('keyboard', self)
          buttonRed.clicked.connect(self.on_click)
          layout.addWidget(buttonRed) 

          buttonGreen = QPushButton('mouse', self)
          buttonGreen.clicked.connect(self.on_click)
          layout.addWidget(buttonGreen) 

          self.horizontalGroupBox.setLayout(layout)

     @pyqtSlot()
     def on_click(self):
          print('PyQt5 button click')
"""

if __name__ == '__main__':
     app = QApplication([])
     window = MainWindow()
     window.show()
     
     sys.exit(app.exec_())