import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff",
]


class QPaletteButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self._pixmap = QtGui.QPixmap(600, 300)
        self._pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self._pixmap)
        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor("#000000")

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        pos = e.position()
        if self.last_x is None:  # First event.
            self.last_x = pos.x()
            self.last_y = pos.y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self._pixmap)
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(int(self.last_x), int(self.last_y), int(pos.x()), int(pos.y()))
        painter.end()
        self.setPixmap(self._pixmap)

        # Update the origin for next time.
        self.last_x = pos.x()
        self.last_y = pos.y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda color=c: self.canvas.set_pen_color(color))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
