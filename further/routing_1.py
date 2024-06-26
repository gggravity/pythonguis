import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in this window")
        self.status = self.statusBar()

        self.setFixedSize(QSize(200, 100))
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        button = e.button()
        pos = e.position()
        if button == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
            if pos.x() < 100:
                self.status.showMessage("Left click on left")
                self.move(self.x() - 10, self.y())
            else:
                self.status.showMessage("Left click on right")
                self.move(self.x() + 10, self.y())
        elif button == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif button == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")
            if pos.x() < 100:
                self.status.showMessage("Right click on left")
                print("Something else here.")
                self.move(10, 10)
            else:
                self.status.showMessage("Right click on right")
                self.move(400, 400)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
