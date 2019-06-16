import sys
import os
from random import randint
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox,
    QPushButton, QGridLayout, QLineEdit, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

class GameWindow(QWidget):

    def __init__(self,name,min,max):
        super().__init__()
        self.name = name
        self.min = min
        self.max = max
        self.initUI(name,min,max)

    def initUI(self,name,min,max):

        self.resize(400,200)
        self.setWindowTitle(name)
        icon_name = 'coin_stack.png'
        self.setWindowIcon(QIcon(icon_name))

        grid = QGridLayout()
        self.setLayout(grid)

        self.player_prompt = QLabel()
        self.player_prompt.setText('Your turn, Player 1!')
        self.player_prompt.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.player_prompt,0,0,1,3)

        self.instruction = QLabel()
        self.instruction.setText('Input the amount you would like to remove:')
        grid.addWidget(self.instruction,1,0,1,2)

        self.change = QLineEdit(self)
        grid.addWidget(self.change,1,2,1,2)



        self.button1 = QPushButton('Take from 1', self)
        self.button1.clicked.connect(self.on_click1)
        self.button1.clicked.connect(self.win_check)
        self.button1.clicked.connect(self.next_player)
        grid.addWidget(self.button1,2,0)

        self.button2 = QPushButton('Take from 2', self)
        self.button2.clicked.connect(self.on_click2)
        self.button2.clicked.connect(self.win_check)
        self.button2.clicked.connect(self.next_player)
        grid.addWidget(self.button2,2,1)

        self.button3 = QPushButton('Take from 3', self)
        self.button3.clicked.connect(self.on_click3)
        self.button3.clicked.connect(self.win_check)
        self.button3.clicked.connect(self.next_player)
        grid.addWidget(self.button3,2,2)

        self.score_label = QLabel()
        self.score_label.setText('Current Pile Values:')
        grid.addWidget(self.score_label,3,0)

        self.score_display1 = QLineEdit(self)
        self.score_display1.setReadOnly(False)
        self.score_display1.setText(str(randint(min,max)))
        grid.addWidget(self.score_display1,4,0)

        self.score_display2 = QLineEdit(self)
        self.score_display2.setReadOnly(False)
        self.score_display2.setText(str(randint(min,max)))
        grid.addWidget(self.score_display2,4,1)

        self.score_display3 = QLineEdit(self)
        self.score_display3.setReadOnly(False)
        self.score_display3.setText(str(randint(min,max)))
        grid.addWidget(self.score_display3,4,2)

        self.show()

    @pyqtSlot()
    def win_check(self):

        win1 = int(self.score_display1.text()) == 0
        win2 = int(self.score_display2.text()) == 0
        win3 = int(self.score_display3.text()) == 0

        if win1 and win2 and win3:
            current_player = self.player_prompt.text()[-2]

            win_notice = QMessageBox.question(self, 'Winner!',
            f'Player {current_player} is the winner! Thanks for playing!',
            QMessageBox.Ok)

            if win_notice == QMessageBox.Ok:
                self.player_prompt.setText('Your turn, Player 1!')
                self.score_display1.setText(str(randint(min,max)))
                self.score_display2.setText(str(randint(min,max)))
                self.score_display3.setText(str(randint(min,max)))


    @pyqtSlot()
    def next_player(self):

        change_val = self.change.text()

        current_player = int(self.player_prompt.text()[-2])

        if change_val.isdigit() and int(change_val) != 0:

            if current_player == 1:
                self.player_prompt.setText('Your turn, Player 2!')
            else:
                self.player_prompt.setText('Your turn, Player 1!')

        self.change.setText('')

    @pyqtSlot()
    def on_click1(self):

        score = int(self.score_display1.text())
        change = self.change.text()

        if change.isdigit():

            change = int(change)

            if score > change:
                new_score = score - change

            else:
                new_score = 0

        else:
            new_score = score

        #print('New Score ='+str(new_score))

        self.score_display1.setText(str(new_score))

    @pyqtSlot()
    def on_click2(self):

        score = int(self.score_display2.text())
        change = self.change.text()

        if change.isdigit():

            change = int(change)

            if score > change:
                new_score = score - change

            else:
                new_score = 0

        else:
            new_score = score

        #print('New Score ='+str(new_score))

        self.score_display2.setText(str(new_score))

    @pyqtSlot()
    def on_click3(self):

        score = int(self.score_display3.text())
        change = self.change.text()

        if change.isdigit():

            change = int(change)

            if score > change:
                new_score = score - change

            else:
                new_score = 0

        else:
            new_score = score

        #print('New Score ='+str(new_score))

        self.score_display3.setText(str(new_score))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow('The Game of NIM',10,100)
    sys.exit(app.exec_())
