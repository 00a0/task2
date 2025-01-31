import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class CustomButton(QPushButton):
    rightClicked = pyqtSignal()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        if event.button() == Qt.RightButton:
            self.rightClicked.emit()

class Task1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.a = int(input("a: "))
        self.b = int(input("b: "))
        self.colors = ["white", "gray", "green", "red"]
        self.buttons = []
        self.anton()

    def change_color(self):
        button = self.sender()
        currentIdx = button.property("currentIdx")
        nextIdx = (currentIdx + 1) % len(self.colors)
        nextColor = self.colors[nextIdx]
        
        if nextColor in ("green", "red"):
            for row in self.buttons:
                for btn in row:
                    idx = btn.property("currentIdx")
                    if self.colors[idx] == nextColor:
                        btn.setStyleSheet("background-color: white;")
                        btn.setProperty("currentIdx", 0)

        button.setStyleSheet(f"background-color: {nextColor};")
        button.setProperty("currentIdx", nextIdx)

    def reset_color(self):
        button = self.sender()
        button.setStyleSheet("background-color: white;")
        button.setProperty("currentIdx", 0)

    def anton(self):
        self.setWindowTitle("Button Matrix")
        self.setFixedSize(500, 500)
        
        container = QWidget()
        self.setCentralWidget(container)
        layout = QGridLayout(container)
        
        for i in range(self.a):
            row = []
            for j in range(self.b):
                button = CustomButton()
                button.setStyleSheet("background-color: white;")
                button.setProperty("currentIdx", 0)
                
                button.clicked.connect(self.change_color)
                button.rightClicked.connect(self.reset_color)
                
                button.setFixedSize(int(500/self.b - 5), int(500/self.a - 5))
                layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task1()
    window.show()
    sys.exit(app.exec_())