import sys
from PyQt6 import QtWidgets, QtCore
import pyqtgraph as pg  # import PyQtGraph after Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graphWidget.setBackground("w")
        # pen = pg.mkPen(color=(255, 0, 0))
        # pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.PenStyle.DashLine)
        # self.graphWidget.plot(hour, temperature, pen=pen)
        # self.graphWidget.plot(hour, temperature, symbol='+', pen=pen)
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.PenStyle.DashLine)
        # self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        self.graphWidget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")

        # styles = {'color':'r', 'font-size':'30pt'}
        # self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        # self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

        self.graphWidget.setLabel('left', "<span style=\"color:red;font-size: 30px\">Temperature (°C)</span>")
        self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size: 30px\">Hour (H)</span>")

        self.graphWidget.addLegend()
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setXRange(5, 20, padding=0)
        self.graphWidget.setYRange(30, 40, padding=0)
        self.graphWidget.plot(hour, temperature, name="Sensor 1", pen=pen, symbol='+', symbolSize=30,
                              symbolBrush=('b'))


        # self.graphWidget.plot(hour, temperature, pen=pen, symbol='+', symbolSize=30, symbolBrush=('b'))


app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
app.exec()
