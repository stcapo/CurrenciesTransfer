from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

import requests
# 获取实时汇率数据
def get_exchange_rates():
    api_key = '11b95e588508d54e2eaf7ea7'  # 替换成你的API密钥
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD' 
    response = requests.get(url)
    if response.status_code == 200:
        a = response.json()['conversion_rates']
        response.close()
        return a
    else:
        print("Failed to fetch exchange rates.")
        response.close()
        return None

# 进行货币转换
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency in exchange_rates and to_currency in exchange_rates:
        rate = exchange_rates[to_currency] / exchange_rates[from_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        print("Invalid currencies.")
        return None

# 主函数
def con(data,from_currency,to_currency,exchange_rates):
    if exchange_rates:
        amount = float(data)
        converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    else:
        print("无法获取汇率数据。")
    return converted_amount

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()#继承父类
        self.exchange_rates = get_exchange_rates()
        if self.exchange_rates is None:
            print("无法获取汇率数据。")
            sys.exit()
        l = self.exchange_rates.keys()
        self.setFixedSize(QSize(900,300))
        self.setWindowTitle("My App")
        layout1 = QVBoxLayout()#定义布局控件
        top = QHBoxLayout()
        mid = QHBoxLayout()
        bottom = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()
        label_from = QLabel("请选择要转换的货币代码", self)
        label_to = QLabel("请选择转换目标的货币代码",self)
        label_from.setStyleSheet("font-size: 22px;")
        label_to.setStyleSheet("font-size: 22px;")
        """
        font = label_from.font()  # Get the current font
        font.setPointSize(13)  # Set the font size to 14
        label_from.setFont(font)
        font = label_to.font()  # Get the current font
        font.setPointSize(13)  # Set the font size to 14
        label_to.setFont(font)
        """
        self.label_obj_amount=QLabel(self)

        self.label_obj_amount.setStyleSheet("border: 1px solid black;font-size: 22px;") #结果样式选择
        self.label_obj_amount.setFixedSize(QSize(200,40))

        self.firstBox = QComboBox(self)#下拉列表填充
        self.firstBox.setFixedSize(200, 40)  # 设置组合框的大小
        
        # 设置字体样式表来改变字体大小
        self.firstBox.setStyleSheet("font-size: 22px;")
        self.firstBox.addItems(l)
        
        self.secondBox = QComboBox(self)
        self.secondBox.setFixedSize(200, 40)  # 设置组合框的大小
        
        # 设置字体样式表来改变字体大小
        self.secondBox.setStyleSheet("font-size: 22px;")
        self.secondBox.addItems(l)
        self.input_amount = QLineEdit(self)
        self.input_amount.setFixedSize(200,40)
        self.input_amount.setStyleSheet("font-size: 22px;")
        self.button = QPushButton("转换",self)
        self.button.setFixedSize(200,40)
        self.button.setStyleSheet("font-size: 22px;background: #ffffff")

        layout1.setContentsMargins(50,0,50,80)#设置边距
    
        top.setSpacing(280)
        bottom.setContentsMargins(0,0,0,0)
        left.setSpacing(10)
        right.setSpacing(10)
        top.addWidget(label_from)
        top.addWidget(label_to)
        mid.addWidget(self.button)
        bottom.addLayout(left)
        bottom.addLayout(mid)
        bottom.addLayout(right)
        left.addWidget(self.firstBox)
        left.addWidget(self.input_amount)
        right.addWidget(self.secondBox)
        right.addWidget(self.label_obj_amount)
        layout1.addLayout(top)
        layout1.addLayout(bottom)
        widget = QWidget()
        widget.setStyleSheet("background:#add8e6")
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        self.button.clicked.connect(self.getPrice)
        
    def getPrice(self):
        try:
            value = con(self.input_amount.text(),self.firstBox.currentText(),self.secondBox.currentText(),self.exchange_rates)
            self.label_obj_amount.setText(str(value))
        except ValueError:
            self.label_obj_amount.setText("Invalid Input")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()