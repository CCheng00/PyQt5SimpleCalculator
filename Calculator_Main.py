from Calculator import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5 import QtCore

current = 0
stored = 0
operator = ''
pressed = False

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        global current
        global stored
        global operator
        global fakeZero
        global pressed
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.display(current)

        self.zero.clicked.connect(lambda:self.number(0))
        self.one.clicked.connect(lambda:self.number(1))
        self.two.clicked.connect(lambda:self.number(2))
        self.three.clicked.connect(lambda:self.number(3))
        self.four.clicked.connect(lambda:self.number(4))
        self.five.clicked.connect(lambda:self.number(5))
        self.six.clicked.connect(lambda:self.number(6))
        self.seven.clicked.connect(lambda:self.number(7))
        self.eight.clicked.connect(lambda:self.number(8))
        self.nine.clicked.connect(lambda:self.number(9))

        self.backspace.clicked.connect(lambda:self.bckspace())

        self.equals.clicked.connect(lambda:self.equls())
        self.plus.clicked.connect(lambda:self.pls())
        self.minus.clicked.connect(lambda:self.mins())
        self.divide.clicked.connect(lambda:self.divid())
        self.times.clicked.connect(lambda:self.tmes())

        self.clear.clicked.connect(lambda:self.clr())

    def display(self, current):
        self.outputText.setText(str(int(current)))

    def number(self, input):
        global current
        global pressed
        if(pressed == True):
            self.store()
        current = (current * 10) + input #appends 'input' to displayed number
        self.display(current)

    def bckspace(self):
        global current
        global pressed
        current = int((current - (current % 10)) / 10)
        self.display(current)

    def store(self):
        global stored
        global current
        global pressed
        pressed = False
        stored = current
        current = 0


#TODO
    def equls(self):
        global stored
        global current
        global operator
        if (operator == 'times'):
            current = stored * current
            operator = ''
        if (operator == 'divide'):
            current = stored / current
            operator = ''
        if (operator == 'plus'):
            current = stored + current
            operator = ''
        if (operator == 'minus'):
            current = stored - current
            operator = ''
        self.display(current)
        current = 0
        stored = 0


    def helper(self):
        global stored
        global operator
        global current
        if (operator == 'times'):
            current = stored * current
        if (operator == 'divide'):
            current = stored / current
        if (operator == 'plus'):
            current = stored + current
        if (operator == 'minus'):
            current = stored - current

        self.display(current)

    def pls(self):
        global operator
        global pressed
        self.helper()
        operator = 'plus'
        pressed = True
    def mins(self):
        global operator
        global pressed
        self.helper()
        operator = 'minus'
        pressed = True
    def divid(self):
        global operator
        global pressed
        self.helper()
        operator = 'divide'
        pressed = True
    def tmes(self):
        global operator
        global pressed
        self.helper()
        operator = 'times'
        pressed = True
    def clr(self):
        global current
        global stored
        current = 0
        stored = 0
        self.display(current)



import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
