from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def the_button_was_clicked():
    print("Clicked!")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(the_button_was_clicked)
        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
