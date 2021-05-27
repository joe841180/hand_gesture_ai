from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QPainter, QColor, QPen)
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel)

class Example(QWidget):
    def __init__(self):
       super(Example, self).__init__()
       self.initUi()
       #預設情況下禁用滑鼠跟蹤， 如果啟用滑鼠跟蹤，即使沒有按鈕被按下，小部件也會接收滑鼠移動事件。
        #當然你也可以不寫，只需要在執行的過程中按照滑鼠左鍵也行
       self.setMouseTracking(True)
       #置頂參數
       self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def initUi(self):
         self.setGeometry(400,300,400,300)
         self.setWindowTitle("鍵盤響應事件")
         self.lab1 = QLabel("方向",self)
         self.lab1.setGeometry(200,150,100,100)
         self.lab2 = QLabel("顯示滑鼠座標", self)
         self.lab2.setGeometry(200, 80, 100, 100)

    """重定義鍵盤事件"""
    def keyPressEvent(self,e ):
         if e.key() == Qt.Key_Up:
             self.lab1.setText("↑")
         elif e.key() == Qt.Key_Down:
             self.lab1.setText("↓")
         elif e.key() == Qt.Key_Left:
             self.lab1.setText("←")
         else:
             self.lab1.setText("→")

    """重定義滑鼠單擊事件"""
    def mousePressEvent(self, event):
         if event.button() == Qt.LeftButton:
             self.lab1.setText("滑鼠左鍵點選！")
             # print(event.pos().x(),event.pos().y())
         if event.button() == Qt.RightButton:
             self.lab1.setText("滑鼠右鍵點選！")

    """當滑鼠左鍵點選拖動時觸發事件,有無if判斷條件效果都一樣"""
    def mouseMoveEvent(self, event):
         # if event.buttons() == Qt.LeftButton:
         #     # print(type(event.pos().x()))    #<class 'int'>
         #     self.lab2.setText(str(event.pos().x())+","+str(event.pos().y()))
         self.pos = event.pos()
         print(self.pos)
         self.lab2.setText(str(event.pos().x()) + "," + str(event.pos().y()))
         self.update()



if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     ex.show()
     sys.exit(app.exec_())