import sys
from random import randint, choice

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        painter = QtGui.QPainter(self.canvas)

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor("green"))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily("Times")
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)
        painter.drawText(100, 100, 100, 100, Qt.AlignmentFlag.AlignHCenter,
                         'Hello, world!')
        # painter.drawText(100, 100, "Hello, world!")
        painter.end()
        self.label.setPixmap(self.canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
