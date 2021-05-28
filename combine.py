import os
import cv2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap

n=int(input("輸入:"))
mode_list=[0,1,2]

# class MainWindow(QMainWindow):
class MainWindow(QWidget):
     def __init__(self):
          super(MainWindow, self).__init__()
          # self.resize(400, 300)

          # Button
          # self.button = QPushButton(self)
          # self.button.setGeometry(0, 0, 400, 300)
          # self.button.setText('Main Window')
          # self.button.setStyleSheet('font-size:40px')

          # Sub Window
          self.sub_window = SubWindow()

          # Button Event
          # self.button.clicked.connect(self.sub_window.show)

          #CV
          self.timer_camera = QTimer()  # 初始化定时器
          self.cap = cv2.VideoCapture()  # 初始化摄像头
          self.CAM_NUM = 0
          self.set_ui()
          self.slot_init()
          self.__flag_work = 0
          self.x = 0
          self.count = 0

     def set_ui(self):
          self.__layout_main = QHBoxLayout()  # 采用QHBoxLayout类，按照从左到右的顺序来添加控件
          self.__layout_fun_button = QHBoxLayout()
          self.__layout_data_show = QVBoxLayout()  # QVBoxLayout类垂直地摆放小部件

          self.button_open_camera = QPushButton(u'打开相机')
          self.button_close = QPushButton(u'退出')

          # button颜色修改
          button_color = [self.button_open_camera, self.button_close]
          for i in range(2):
               button_color[i].setStyleSheet("QPushButton{color:black}"
                                             "QPushButton:hover{color:red}"
                                             "QPushButton{background-color:rgb(78,255,255)}"
                                             "QpushButton{border:2px}"
                                             "QPushButton{border_radius:10px}"
                                             "QPushButton{padding:2px 4px}")

          self.button_open_camera.setMinimumHeight(50)
          self.button_close.setMinimumHeight(50)

          # move()方法是移动窗口在屏幕上的位置到x = 500，y = 500的位置上
          self.move(500, 500)

          # 信息显示
          self.label_show_camera = QLabel()
          self.label_move = QLabel()
          self.label_move.setFixedSize(100, 100)

          self.label_show_camera.setFixedSize(641, 481)
          self.label_show_camera.setAutoFillBackground(False)

          self.__layout_fun_button.addWidget(self.button_open_camera)
          self.__layout_fun_button.addWidget(self.button_close)
          self.__layout_fun_button.addWidget(self.label_move)

          self.__layout_main.addLayout(self.__layout_fun_button)
          self.__layout_main.addWidget(self.label_show_camera)

          self.setLayout(self.__layout_main)
          self.label_move.raise_()
          self.setWindowTitle(u'摄像头')

          '''
          # 设置背景颜色
          palette1 = QPalette()
          palette1.setBrush(self.backgroundRole(),QBrush(QPixmap('background.jpg')))
          self.setPalette(palette1)
          '''

     def slot_init(self):  # 建立通信连接
          self.button_open_camera.clicked.connect(self.button_open_camera_click)
          self.timer_camera.timeout.connect(self.show_camera)
          self.button_close.clicked.connect(self.close)

     def button_open_camera_click(self):
          if self.timer_camera.isActive() == False:
               flag = self.cap.open(self.CAM_NUM)
               if flag == False:
                    msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                                       buttons=QMessageBox.Ok,
                                                       defaultButton=QMessageBox.Ok)
                    # if msg==QtGui.QMessageBox.Cancel:
                    #                     pass
               else:
                    self.timer_camera.start(30)
                    self.button_open_camera.setText(u'关闭相机')
          else:
               self.timer_camera.stop()
               self.cap.release()
               self.label_show_camera.clear()
               self.button_open_camera.setText(u'打开相机')

     def show_camera(self):
          flag, self.image = self.cap.read()
          show = cv2.resize(self.image, (640, 480))
          show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
          showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
          self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

     def closeEvent(self, event):
          ok = QPushButton()
          cancel = QPushButton()
          msg = QMessageBox(QMessageBox.Warning, u'关闭', u'是否关闭！')
          msg.addButton(ok, QMessageBox.ActionRole)
          msg.addButton(cancel, QMessageBox.RejectRole)
          ok.setText(u'确定')
          cancel.setText(u'取消')
          if msg.exec_() == QMessageBox.RejectRole:
               event.ignore()
          else:
               if self.cap.isOpened():
                    self.cap.release()
               if self.timer_camera.isActive():
                    self.timer_camera.stop()
               event.accept()








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
          self.setWindowFlags(Qt.WindowStaysOnTopHint)
          
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
          # 按鈕事件
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