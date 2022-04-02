import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


def the_button_was_clicked():
    print("Clicked!")


def the_button_was_toggled(checked):
    print("Checked?", checked)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(the_button_was_clicked)
        button.clicked.connect(the_button_was_toggled)
        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
