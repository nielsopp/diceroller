# -*- coding: utf-8 -*-
"""
Created on Thu Apr 02 08:04:58 2020

@author: NOppermann
"""

NumDice = 5
MaxRoll = 3


import sys
import numpy as np
from PyQt5 import QtWidgets


class DiceRoller(QtWidgets.QWidget):
    
    def __init__(self):
        super(DiceRoller, self).__init__()
        self.results = np.zeros(NumDice)*np.nan
        self.count = 0
        self.initUI()
        return

    def initUI(self):
        #add roll count line
        roll_label = QtWidgets.QLabel('You have rolled 0 times.',self)
        roll_label.move(20,10)
        self.roll_label = roll_label
        
        #add result labels
        res_labels = [QtWidgets.QLabel('',self) for ii in range(NumDice)]
        for ii in range(NumDice):
            res_labels[ii].move(30 + ii*35,30)
        self.res_labels = res_labels
        
        #add checkboxes
        boxes = [QtWidgets.QCheckBox(self) for ii in range(NumDice)]
        for ii in range(NumDice):
            boxes[ii].move(27 + ii*35,50)
            boxes[ii].setChecked(True)
        self.boxes = boxes
        
        #add reset button
        reset_button = QtWidgets.QPushButton('Reset',self)
        xpos = np.max([165,27 + NumDice*35])
        reset_button.move(xpos,10)
        reset_button.clicked[bool].connect(self.reset)
        
        #add roll button
        roll_button = QtWidgets.QPushButton('Roll',self)
        roll_button.move(xpos,40)
        roll_button.clicked[bool].connect(self.roll)

        #set window parameters
        self.setGeometry(300, 100, xpos + 90, 90)
        self.setWindowTitle('DiceRoller - %i dice, %i rolls'%(NumDice,MaxRoll))
        self.show()
        return

    def reset(self):
        self.roll_label.setText('You have rolled 0 times.')
        self.results = np.zeros(NumDice)*np.nan
        self.count = 0
        for ii in range(NumDice):
            self.res_labels[ii].setText('')
            self.boxes[ii].setChecked(True)
        return
    
    def roll(self):
        if self.count < MaxRoll:
            self.count += 1
            self.roll_label.setText('You have rolled %i time%s.'%(self.count,'s'*(self.count != 1)))
            select = np.array([self.boxes[ii].isChecked() for ii in range(NumDice)])
            self.results[select] = np.random.choice(np.arange(1,6),int(np.sum(select)))
            for ii in range(NumDice):
                self.res_labels[ii].setText('%i'%self.results[ii])
        return


def run():    
    app = QtWidgets.QApplication(sys.argv)
    dr = DiceRoller()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
