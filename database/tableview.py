import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableView
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()
        # self.model = ?
        # self.table.setModel(self.model)
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
