import os
import sys
from PyQt6.QtCore import QUrl, QSize, Qt
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QLabel, QFileDialog, QDialog, \
    QDialogButtonBox, QVBoxLayout


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        QBtn = QDialogButtonBox.StandardButton.Ok  # No cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Mozzarella Ashbadger")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join("icons", "ma-icon-128.png")))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 23.35.211.233232"))
        layout.addWidget(QLabel("Copyright 2015 Mozzarella Inc."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignmentFlag.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(nav_toolbar)

        back_btn = QAction(QIcon(os.path.join("icons", "arrow-180.png")), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        nav_toolbar.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join("icons", "arrow-000.png")), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        nav_toolbar.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join("icons", "arrow-circle-315.png")), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        nav_toolbar.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join("icons", "home.png")), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        nav_toolbar.addAction(home_btn)

        self.https_icon = QLabel()  # Yes, really!
        self.https_icon.setPixmap(QPixmap(os.path.join("icons", "locknossl.png")))
        nav_toolbar.addWidget(self.https_icon)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.url_bar)

        stop_btn = QAction(QIcon(os.path.join("icons", "cross-circle.png")), "Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(self.browser.stop)
        nav_toolbar.addAction(stop_btn)

        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

        file_menu = self.menuBar().addMenu("&File")
        open_file_action = QAction(QIcon(os.path.join("icons", "disk--arrow.png")), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join("icons", "disk--pencil.png")), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join("icons", "printer.png")), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)

        help_menu = self.menuBar().addMenu("&Help")
        about_action = QAction(QIcon(os.path.join("icons", "question.png")), "About Mozzarella Ashbadger", self, )
        about_action.setStatusTip("Find out more about Mozzarella Ashbadger")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)
        navigate_mozzarella_action = QAction(QIcon(os.path.join("icons", "lifebuoy.png")),
                                             "Mozzarella Ashbadger Homepage", self, )
        navigate_mozzarella_action.setStatusTip("Go to Mozzarella Ashbadger Homepage")
        navigate_mozzarella_action.triggered.connect(self.navigate_mozzarella)
        help_menu.addAction(navigate_mozzarella_action)

        # Create our system printer instance.
        self.printer = QPrinter()

        self.setCentralWidget(self.browser)
        self.show()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):  # Does not receive the Url
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
            self.browser.setUrl(q)

    def update_urlbar(self, q):
        if q.scheme() == "https":
            # Secure padlock icon
            self.https_icon.setPixmap(QPixmap(os.path.join("icons", "lock-ssl.png")))
        else:
            # Insecure padlock icon
            self.https_icon.setPixmap(QPixmap(os.path.join("icons", "lock-nossl.png")))

        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - Mozzarella Ashbadger" % title)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;" "All files",
                                                  )
        if filename:
            with open(filename, "r") as f:
                html = f.read()

            self.browser.setHtml(html)
            self.urlbar.setText(filename)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;" "All files (*. *)",
                                                  )
        if filename:
            # Define callback method to handle the write.
            def writer(html):
                with open(filename, "w") as f:
                    f.write(html)

            self.browser.page().toHtml(writer)

    def print_page(self):
        page = self.browser.page()

        def callback(*args):
            pass

        dlg = QPrintDialog(self.printer)
        dlg.accepted.connect(callback)

        if dlg.exec() == QDialog.Accepted:
            page.print(self.printer, callback)

    def navigate_mozzarella(self):
        self.browser.setUrl(QUrl("https://www.pythonguis.com/"))

    def about(self):
        dlg = AboutDialog()
        dlg.exec()


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
