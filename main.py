import sys
import random

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Случайные окружности')
        self.add_circle = QPushButton('Нарисовать круг', self)
        self.add_circle.resize(300, 20)
        self.add_circle.move(0, 200)


class RandomCircles(UI):
    def __init__(self):
        super().__init__()
        self.add_circle.clicked.connect(self.draw_circle)
        self.circles = []
        self.draw = False

    def paintEvent(self, event):
        if self.draw:
            self.draw = False
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(0, 0, 0, 0))
            for c in self.circles:
                qp.setBrush(c[1])
                qp.drawEllipse(*c[0])
            qp.end()

    def draw_circle(self):
        radius = random.randint(1, 100)
        self.circles.append(((random.randint(0, 300 - radius), random.randint(0, 200 - radius), radius, radius), (QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255))))
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()

    sys.exit(app.exec())