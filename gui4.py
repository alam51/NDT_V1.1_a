from functools import partial

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5 import QtWidgets, QtGui \
    # , uic
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # action method
    def clickme(self, val):
        # printing pressed
        print(f"pressed {val}")

    def initUI(self):
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1, 2):
            # object = QLabel("TextLabel")
            object = QPushButton('Click Me')
            object.setGeometry(QRect(0, 150, 200, 300))
            object.setObjectName("PB_Percent")
            font = QtGui.QFont()
            font.setPointSize(26)
            object.setFont(font)
            object.setStyleSheet("background-color : green")
            self.vbox.addWidget(object)
            object.clicked.connect(partial(self.clickme, i))

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 500, 600)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
