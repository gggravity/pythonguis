import sys
from datetime import datetime  # <1>

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
          '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DecorationRole:
            value = self._data[index.row()][index.column()]

            if isinstance(value, datetime):
                return QtGui.QIcon("calendar.png")

            if isinstance(value, bool):
                if value:
                    return QtGui.QIcon("tick.png")
                else:
                    return QtGui.QIcon("cross.png")

        if role == Qt.ItemDataRole.ForegroundRole:
            value = self._data[index.row()][index.column()]
            if (isinstance(value, int) or isinstance(value, float)) and value < 0:
                return QtGui.QColor("red")

        if role == Qt.ItemDataRole.TextAlignmentRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                # Align right, vertical middle.
                return Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight

        if role == Qt.ItemDataRole.BackgroundRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, int) or isinstance(value, float):
                value = int(value)  # Convert to integer for indexing.
                # Limit to range -5 ... +5, then convert to 0..10
                value = max(-5, value)  # values < -5 become -5
                value = min(5, value)  # valaues > +5 become +5
                value = value + 5  # -5 becomes 0, +5 becomes + 10
                return QtGui.QColor(COLORS[value])

        if role == Qt.ItemDataRole.DisplayRole:
            # Get the raw value
            value = self._data[index.row()][index.column()]

            # Perform per-type checks and render accordingly.
            if isinstance(value, datetime):
                # Render time to YYY-MM-DD.
                return value.strftime("%Y-%m-%d")

            if isinstance(value, float):
                # Render float to 2 dp
                return "%.2f" % value

            if isinstance(value, str):
                # Render strings with quotes
                return '"%s"' % value

            # Default (anything not captured above: e.g. int)
            return value

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        data = [
            [True, 9, 2],
            [1, -1, "hello"],
            [3.023, 5, -5],
            [3, 3, datetime(2017, 10, 1)],
            [7.555, 8, False],
        ]

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
        self.setGeometry(600, 100, 400, 200)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
