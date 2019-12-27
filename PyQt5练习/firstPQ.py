import sys

#qtwidgets模块包含创造经典桌面风格的用户界面提供了一套UI元素的类
from PyQt5.QtWidgets import QApplication,QWidget


#只能直接运行，不能调用
if __name__ == '__main__':
    #每个pyqt5应用程序必须创建一个应用程序对象.sys.argv参数是一个列表，从命令行输入参数
    app = QApplication(sys.argv)
    #QWidget部件是pyqt5所有用户界面对象的基类。他为QWidget提供默认构造函数。默认构造函数没有父类
    w = QWidget()
    #resize()方法调整窗口大小
    w.resize(1900,1000)
    #move()方法移动窗口在屏幕上的位置。（0，0）在左上角
    w.move(0,0)
    #setWindowTitle()设置窗口标题
    w.setWindowTitle('Simple')
    #显示在屏幕上
    w.show()

    
    #系统exit()方法确保应用程序干净退出
    #exec_()方法有下划线。因为执行是一个Python关键词。因此，exec_()代替
    sys.exit(app.exec_())
