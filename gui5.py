from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QFormLayout, QGroupBox, QLabel, \
    QScrollArea, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize, QRect


class Window(QMainWindow):
    def __init__(self, val):
        super().__init__()

        self.title = "PyQt5 Scroll Area"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250
        self.iconName = 'capture.png'

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        formLayout = QFormLayout()
        groupBox = QGroupBox('This is group box')

        label_list = []
        button_list = []

        for i in range(val):
            label_list.append(QLabel('Label'))
            button_list.append(QPushButton('Click Me'))
            formLayout.addRow(label_list[i], button_list[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)
        # self.
        self.show()


App = QApplication(sys.argv)
window = Window(20)
sys.exit(App.exec())

