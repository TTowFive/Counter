import sys
from PyQt5 import QtWidgets
from counter_ui import Ui_MainWindow
import time
import sys

display_num_store = [] # 数字中转
FinallNum = []
FinallNum_fomal = []    #前一位数
Final_result = 0
i = 0
k = 0
SYMBOL = ''     #定义符号的存储

class counter(Ui_MainWindow,QtWidgets.QMainWindow):

    def __init__(self):
        super(counter,self).__init__()
        self.setupUi(self)
        self.result.setText('0')
        self.Event_solve()

    def Equal(self):        #用户按下“=”时实现数据运算
        global FinallNum
        global SYMBOL
        global FinallNum_fomal

        if SYMBOL != '' and display_num_store != 0:
            try:        #通过异常判断用户输入的数据类型
                FinallNum_fomal = int (FinallNum_fomal)
                FinallNum = int (FinallNum)
            except:
                try:
                    FinallNum_fomal = float (FinallNum_fomal)
                    FinallNum = float(FinallNum)
                except:
                    print('continue')
            if SYMBOL == '+':   #加
                re = FinallNum_fomal + FinallNum
                self.result.setText(str(re))
                self.symbol.setText('')
                FinallNum_fomal = re
                print(FinallNum_fomal)
            if SYMBOL == '-':       #减
                re = FinallNum_fomal - FinallNum
                self.result.setText(str(re))
                self.symbol.setText('')
                FinallNum_fomal = re
            if SYMBOL == 'X':       #乘
                re = FinallNum_fomal * FinallNum
                self.result.setText(str(re))
                self.symbol.setText('')
                FinallNum_fomal = re
            if SYMBOL == '/':       #除
                if FinallNum == 0:
                    QtWidgets.QMessageBox.question(self, u'警告', u'"零不能作为被除数"',
                                                   QtWidgets.QMessageBox.Yes |
                                                   QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.Yes)
                else:
                    re = FinallNum_fomal / FinallNum
                    #print(type(re))
                    self.result.setText(str(re))
                    self.symbol.setText('')
                    FinallNum_fomal = re

        else:
            QtWidgets.QMessageBox.question(self, u'警告', u'请输入数字！',
                                           QtWidgets.QMessageBox.Yes |
                                           QtWidgets.QMessageBox.No,
                                           QtWidgets.QMessageBox.Yes)

    def store(self,symbol = ''):        #暂时储存输入符号
        global FinallNum
        global SYMBOL
        global FinallNum_fomal
        global display_num_store
        if FinallNum_fomal == [] and display_num_store != 0:
            FinallNum_fomal = FinallNum

        if  symbol != '':
            SYMBOL = symbol
            self.symbol.setText(SYMBOL) #显示符号
            display_num_store = []
            self.result.setText('0')


#_________________________________符号规定____________________________-
    def SUB(self):
        sub = '-'
        self.store(sub)
    def ADD(self):
        plug = '+'
        self.store(plug)
    def MUL(self):
        mul = 'X'
        self.store(mul)
    def S(self):
        s = '/'
        self.store(s)

#

    def Write_num_in_label(self,NUM):       #写入数字到lable_result
        global i
        global FinallNum
        global display_num_store
        global k
        i = len(display_num_store)
        NUM = str(NUM)
        #print(display_num_store)
        if i != 9:          #限制数据长度
            display_num_store.append(NUM)
            FinallNum = ''.join(display_num_store)
            self.result.setText(FinallNum)
        else:
            self.TIP()

    def TIP(self):      #提示
        reply = QtWidgets.QMessageBox.question(self,'警告！','数字已达上限！是否清除？',
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No,QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.Clear_button()

    def Event_solve(self):      #事件解决
        self.clean_num.clicked.connect(self.Clear_button)
        self.NUM_0.clicked.connect(self.ZERO)
        self.NUM_1.clicked.connect(self.ONE)
        self.NUM_2.clicked.connect(self.TWO)
        self.NUM_3.clicked.connect(self.THREE)
        self.NUM_4.clicked.connect(self.FOUR)
        self.NUM_5.clicked.connect(self.FIVE)
        self.NUM_6.clicked.connect(self.SIX)
        self.NUM_7.clicked.connect(self.SEVEN)
        self.NUM_8.clicked.connect(self.EIGHT)
        self.NUM_9.clicked.connect(self.NINE)
        self.dot.clicked.connect(self.DOT)
        self.subnum.clicked.connect(self.SUB) #减
        self.addnum.clicked.connect(self.ADD) #加
        self.mulnum.clicked.connect(self.MUL) #乘
        self.snum.clicked.connect(self.S)   #除
        self.equal.clicked.connect(self.Equal) #等于

    def Clear_button(self):         #初始化计算器 C
        global display_num_store
        global i
        global FinallNum,FinallNum_fomal
        global SYMBOL
        i = 0
        display_num_store = []
        FinallNum = []
        SYMBOL = ''
        if SYMBOL =='':
            FinallNum_fomal = []
        self.result.setText('0')
        self.symbol.setText('')
        SYMBOL = ''

    """
        写出0~9数字行为
    """

    def ZERO(self):     #数字零的行为
        zero = '0'
        global FinallNum,FinallNum_fomal
        if FinallNum_fomal == [] and FinallNum == []:
            self.Clear_button()
        else:
            self.Write_num_in_label(zero)

    def ONE(self):  #数字一的行为
        one = 1
        self.Write_num_in_label(one)
    def TWO(self):
        two = 2
        self.Write_num_in_label(two)
    def THREE(self):
        three = 3
        self.Write_num_in_label(three)
    def FOUR(self):
        four = 4
        self.Write_num_in_label(four)
    def FIVE(self):
        five = 5
        self.Write_num_in_label(five)
    def SIX(self):
        six = 6
        self.Write_num_in_label(six)
    def SEVEN(self):
        seven = 7
        self.Write_num_in_label(seven)
    def EIGHT(self):
        eight = 8
        self.Write_num_in_label(eight)
    def NINE(self):
        nine = 9
        self.Write_num_in_label(nine)
    def DOT(self):
        dot = '.'
        self.Write_num_in_label(dot)

    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self, '信息', '确认退出吗？',
                                               QtWidgets.QMessageBox.Yes |
                                               QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def __repr__(self):
        return 'yes'

if __name__ == '__main__':
    ACCEPT = 1
    LUNCH_RIGHT = 1
    if LUNCH_RIGHT == ACCEPT:
        app = QtWidgets.QApplication(sys.argv)
        window = counter()
        window.show()
        sys.exit(app.exec_())
