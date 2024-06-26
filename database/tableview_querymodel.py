import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("chinook.sqlite")
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)
        query = QSqlQuery("SELECT Name, Composer FROM track ", db=db)
        self.model.setQuery(query)
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
