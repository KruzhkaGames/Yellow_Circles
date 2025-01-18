import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor

from PyQt6 import uic


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Жёлтые окружности')
        self.add_circle.clicked.connect(self.draw_circle)

        self.draw = False
        self.circles = []

    def paintEvent(self, event):
        if self.draw:
            self.draw = False
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0, 255))
            qp.setPen(QColor(0, 0, 0, 0))
            for c in self.circles:
                qp.drawEllipse(*c)
            qp.end()

    def draw_circle(self):
        radius = random.randint(1, 100)
        self.circles.append((random.randint(radius, 300 - radius), random.randint(radius, 200 - radius), radius, radius))
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()

    sys.exit(app.exec())