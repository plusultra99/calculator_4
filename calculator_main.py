import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_equation = QFormLayout()
        layout_operation = QGridLayout()
        layout_number = QGridLayout()
        

        #equation 구간#

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("")
        self.equation = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation.addRow(label_equation, self.equation)

        #operation 구간#

        ### clear 버튼
        button_clear = QPushButton("Clear")
        button_clear.clicked.connect(self.button_clear_clicked)
        layout_operation.addWidget(button_clear,0,1)

        ### backspace 버튼
        button_backspace = QPushButton("Backspace")
        button_backspace.clicked.connect(self.button_backspace_clicked)
        layout_operation.addWidget(button_backspace,0,3)
        
        # / 버튼
        button_division = QPushButton("/")
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        layout_operation.addWidget(button_division,1,3)

        #number 구간#
        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0,10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                if x==2:
                    x=0
                elif x==0:
                    x=2
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        ### = 버튼
        button_equal = QPushButton("=")
        button_equal.clicked.connect(self.button_equal_clicked)
        layout_number.addWidget(button_equal, 3, 3)

        ### + 버튼
        button_plus = QPushButton("+")
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        layout_number.addWidget(button_plus, 2,3)

        ### - 버튼
        button_minus = QPushButton("-")
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        layout_number.addWidget(button_minus,1,3)

        ### x
        button_product = QPushButton("x")
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        layout_number.addWidget(button_product,0,3)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        equation = eval(equation)
        self.equation.setText(str(equation))

    def button_clear_clicked(self):
        self.equation.setText("")
        

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
