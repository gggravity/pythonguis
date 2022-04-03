import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("chinook.sqlite")
db.open()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        # tag::sortTable[]
        self.model.setTable("Track")
        idx = self.model.fieldIndex("Milliseconds")
        self.model.setSort(idx, Qt.SortOrder.DescendingOrder)
        self.model.select()
        # end::sortTable[]
        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
