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

        # column headers
        self.model.setTable("Track")
        column_titles = {
            "Name": "Name",
            "AlbumId": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
            "Composer": "Composer",
        }
        for n, t in column_titles.items():
            idx = self.model.fieldIndex(n)
        self.model.setHeaderData(idx, Qt.Orientation.Horizontal, t)
        self.model.select()

        # Remove unwanted columns
        columns_to_remove = ['Bytes', 'TrackId']
        for cn in columns_to_remove:
            idx = self.model.fieldIndex(cn)
            self.model.removeColumns(idx, 1)

        self.setMinimumSize(QSize(1024, 600))
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
