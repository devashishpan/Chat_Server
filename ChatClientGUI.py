import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(100, 100, 500, 500)
    win.setWindowTitle("PING")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
