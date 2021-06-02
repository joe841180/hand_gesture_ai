import os
import cv2
import sys

from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon,QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets


# n=int(input("輸入:"))
# mode_list=[0,1,2]

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







# QDialog,QWidget。
# 置頂視窗--button 形式
class SubWindow(QMainWindow):
     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.setWindowTitle('Showing')
          # self.resize(100, 50)
          self.setGeometry(1600, 30, 50, 50)
          self.initUI()
 

          ##### 创建界面 ######
          self.centralwidget = QWidget()
          self.setCentralWidget(self.centralwidget)
          self.Layout = QVBoxLayout(self.centralwidget)

          # 设置顶部三个按钮
          self.topwidget = QWidget()
          self.Layout.addWidget(self.topwidget)
          self.buttonLayout = QHBoxLayout(self.topwidget)

          self.pushButton1 = QPushButton()
          self.pushButton1.setText("rest")
          self.buttonLayout.addWidget(self.pushButton1)

          self.pushButton2 = QPushButton()
          self.pushButton2.setText("keyboard")
          self.buttonLayout.addWidget(self.pushButton2)

          self.pushButton3 = QPushButton()
          self.pushButton3.setText("mouse")
          self.buttonLayout.addWidget(self.pushButton3)



          # 设置stackedWidget
          self.stackedWidget = QStackedWidget()
          self.Layout.addWidget(self.stackedWidget)

          # 设置第一个面板
          self.form1  = QWidget()
          self.formLayout1 = QHBoxLayout(self.form1)
          self.label1 = QLabel()
          self.label1.setText("rest mode")
          self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
          self.label1.setAlignment(Qt.AlignCenter)
          self.label1.setFont(QFont("Roman times", 15, QFont.Bold))
          self.formLayout1.addWidget(self.label1)


          # 设置第二个面板
          self.form2  = QWidget()
          self.formLayout2 = QHBoxLayout(self.form2)
          self.label2 = QLabel()
          self.label2.setText("keyboard mode")
          self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
          self.label2.setAlignment(Qt.AlignCenter)
          self.label2.setFont(QFont("Roman times", 15, QFont.Bold))
          self.formLayout2.addWidget(self.label2)

          # 设置第三个面板
          self.form3  = QWidget()
          self.formLayout3 = QHBoxLayout(self.form3)
          self.label3 = QLabel()
          self.label3.setText("mouse mode")
          self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
          self.label3.setAlignment(Qt.AlignCenter)
          self.label3.setFont(QFont("Roman times", 15, QFont.Bold))
          self.formLayout3.addWidget(self.label3)

          # 将三个面板，加入stackedWidget
          self.stackedWidget.addWidget(self.form1)
          self.stackedWidget.addWidget(self.form2)
          self.stackedWidget.addWidget(self.form3)


          
          # 设置状态栏
          self.statusBar().showMessage("当前用户：")

          # 窗口最大化
     #    self.showMaximized()
          ###### 三个按钮事件 ######
          self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
          self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
          self.pushButton3.clicked.connect(self.on_pushButton3_clicked)


     # 按钮一：打开第一个面板
     def on_pushButton1_clicked(self):
          self.stackedWidget.setCurrentIndex(0)


     # 按钮二：打开第二个面板
     def on_pushButton2_clicked(self):
          self.stackedWidget.setCurrentIndex(1)


     # 按钮三：打开第三个面板
     def on_pushButton3_clicked(self):
          self.stackedWidget.setCurrentIndex(2)


          


     def initUI(self):

          
          #置頂參數
          self.setWindowFlags(Qt.WindowStaysOnTopHint)
          

          #設定圖示，QIcon物件接收一個我們要顯示的圖片路徑作為引數。
          # self.setWindowIcon(QIcon('web3.png'))

          # windowLayout = QVBoxLayout()
          # windowLayout.addWidget(self.horizontalGroupBox)
          # self.setLayout(windowLayout)

          self.show()


if __name__ == '__main__':
     app = QApplication([])
     window = MainWindow()
     window.show()
     
     sys.exit(app.exec_())