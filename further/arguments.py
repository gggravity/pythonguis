from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for arg in sys.argv:
            l = QLabel(arg)
            layout.addWidget(l)

        self.setLayout(layout)
        self.setWindowTitle("Arguments")


app = QApplication(sys.argv)
w = Window()
w.show()
app.exec()
