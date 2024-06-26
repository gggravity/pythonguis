from PyQt6.QtWidgets import (
    QApplication,
    QSystemTrayIcon,
    QMainWindow,
    QTextEdit,
    QMenu,
)
from PyQt6.QtGui import QIcon, QAction
import sys

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("animal-penguin.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        self.load()  # Load up the text from file.

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")

        self.reset = QAction("&Reset")
        self.reset.triggered.connect(self.editor.clear)
        file_menu.addAction(self.reset)

        self.quit = QAction("&Quit")
        self.quit.triggered.connect(app.quit)
        file_menu.addAction(self.quit)

        self.setCentralWidget(self.editor)
        self.setWindowTitle("PenguinNotes")

    def load(self):
        with open("notes.txt", "r") as f:
            text = f.read()
            self.editor.setPlainText(text)

    def save(self):
        text = self.editor.toPlainText()

        with open("notes.txt", "w") as f:
            f.write(text)

    # def activate(self, reason):
    #     if reason == QSystemTrayIcon.ActivationReason.Trigger:  # Icon clicked.
    #         self.show()

    def activate(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # Icon clicked.
            if self.isVisible():
                self.hide()
            else:
                self.show()


w = MainWindow()
tray.activated.connect(w.activate)
app.aboutToQuit.connect(w.save)
app.exec()
