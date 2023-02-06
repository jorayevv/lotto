from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Application(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(1366, 768)
        self.setWindowTitle("Lotto")
        self.setWindowIcon(QIcon(QPixmap("./icon.png")))
        self.setStyleSheet("""
            background-color: rgb(255, 213, 128);
            font-size: 15px;
        """)

        # radio buttons
        self.radio1 = QRadioButton("Omad (36/5)", self)
        self.radio1.setGeometry(20, 50, 170, 50)
        self.radio2 = QRadioButton("Sharqona (36/6)", self)
        self.radio2.setGeometry(190, 50, 170, 50)
        self.radio3 = QRadioButton("Super (36/7)", self)
        self.radio3.setGeometry(340, 50, 170, 50)

        # input
        self.input = QLineEdit(self)
        self.input.setGeometry(20, 100, 400, 50)
        self.input.setStyleSheet("""
            background-color: white;
            border-radius: 20px;
            border: 3px solid blue;
        """)

        self.button = QPushButton("+", self)
        self.button.setGeometry(430, 100, 80, 50)
        self.button.setStyleSheet("""
            background-color: grey;
            border-radius: 20px;
            border: 3px solid red;
            font-size: 30px;
        """)

        # buttons
        self.btn1 = QPushButton("1", self)
        self.btn1.setGeometry(20, 170, 70, 70)
        self.button_style(self.btn1)

        self.btn2 = QPushButton("2", self)
        self.btn2.setGeometry(100, 170, 70, 70)
        self.button_style(self.btn2)

        self.btn3 = QPushButton("3", self)
        self.btn3.setGeometry(180, 170, 70, 70)
        self.button_style(self.btn3)

        self.btn4 = QPushButton("4", self)
        self.btn4.setGeometry(260, 170, 70, 70)
        self.button_style(self.btn4)

        self.btn5 = QPushButton("5", self)
        self.btn5.setGeometry(340, 170, 70, 70)
        self.button_style(self.btn5)

        self.btn6 = QPushButton("6", self)
        self.btn6.setGeometry(420, 170, 70, 70)
        self.button_style(self.btn6)

        self.btn7 = QPushButton("7", self)
        self.btn7.setGeometry(20, 250, 70, 70)
        self.button_style(self.btn7)

        self.btn8 = QPushButton("8", self)
        self.btn8.setGeometry(100, 250, 70, 70)
        self.button_style(self.btn8)

        self.btn9 = QPushButton("9", self)
        self.btn9.setGeometry(180, 250, 70, 70)
        self.button_style(self.btn9)

        self.btn10 = QPushButton("10", self)
        self.btn10.setGeometry(260, 250, 70, 70)
        self.button_style(self.btn10)

        self.btn11 = QPushButton("11", self)
        self.btn11.setGeometry(340, 250, 70, 70)
        self.button_style(self.btn11)

        self.btn12 = QPushButton("12", self)
        self.btn12.setGeometry(420, 250, 70, 70)
        self.button_style(self.btn12)

        self.btn13 = QPushButton("13", self)
        self.btn13.setGeometry(20, 330, 70, 70)
        self.button_style(self.btn13)

        self.btn14 = QPushButton("14", self)
        self.btn14.setGeometry(100, 330, 70, 70)
        self.button_style(self.btn14)

        self.btn15 = QPushButton("15", self)
        self.btn15.setGeometry(180, 330, 70, 70)
        self.button_style(self.btn15)

        self.btn16 = QPushButton("16", self)
        self.btn16.setGeometry(260, 330, 70, 70)
        self.button_style(self.btn16)

        self.btn17 = QPushButton("17", self)
        self.btn17.setGeometry(340, 330, 70, 70)
        self.button_style(self.btn17)

        self.btn18 = QPushButton("18", self)
        self.btn18.setGeometry(420, 330, 70, 70)
        self.button_style(self.btn18)

        self.btn19 = QPushButton("19", self)
        self.btn19.setGeometry(20, 410, 70, 70)
        self.button_style(self.btn19)

        self.btn20 = QPushButton("20", self)
        self.btn20.setGeometry(100, 410, 70, 70)
        self.button_style(self.btn20)

        self.btn21 = QPushButton("21", self)
        self.btn21.setGeometry(180, 410, 70, 70)
        self.button_style(self.btn21)

        self.btn22 = QPushButton("22", self)
        self.btn22.setGeometry(260, 410, 70, 70)
        self.button_style(self.btn22)

        self.btn23 = QPushButton("23", self)
        self.btn23.setGeometry(340, 410, 70, 70)
        self.button_style(self.btn23)

        self.btn24 = QPushButton("24", self)
        self.btn24.setGeometry(420, 410, 70, 70)
        self.button_style(self.btn24)

        self.btn25 = QPushButton("25", self)
        self.btn25.setGeometry(20, 490, 70, 70)
        self.button_style(self.btn25)

        self.btn26 = QPushButton("26", self)
        self.btn26.setGeometry(100, 490, 70, 70)
        self.button_style(self.btn26)

        self.btn27 = QPushButton("27", self)
        self.btn27.setGeometry(180, 490, 70, 70)
        self.button_style(self.btn27)

        self.btn28 = QPushButton("28", self)
        self.btn28.setGeometry(260, 490, 70, 70)
        self.button_style(self.btn28)

        self.btn29 = QPushButton("29", self)
        self.btn29.setGeometry(340, 490, 70, 70)
        self.button_style(self.btn29)

        self.btn30 = QPushButton("30", self)
        self.btn30.setGeometry(420, 490, 70, 70)
        self.button_style(self.btn30)

        self.btn31 = QPushButton("31", self)
        self.btn31.setGeometry(20, 570, 70, 70)
        self.button_style(self.btn31)

        self.btn32 = QPushButton("32", self)
        self.btn32.setGeometry(100, 570, 70, 70)
        self.button_style(self.btn32)

        self.btn33 = QPushButton("33", self)
        self.btn33.setGeometry(180, 570, 70, 70)
        self.button_style(self.btn33)

        self.btn34 = QPushButton("34", self)
        self.btn34.setGeometry(260, 570, 70, 70)
        self.button_style(self.btn34)

        self.btn35 = QPushButton("35", self)
        self.btn35.setGeometry(340, 570, 70, 70)
        self.button_style(self.btn35)

        self.btn36 = QPushButton("36", self)
        self.btn36.setGeometry(420, 570, 70, 70)
        self.button_style(self.btn36)

    @staticmethod
    def button_style(object):
        object.setStyleSheet("""
            background-color: rgb(255, 114, 118);
            border: 2px solid crimson;
            font-size: 30px;
        """)


app = QApplication(sys.argv)
application = Application()
application.show()
sys.exit(app.exec_())