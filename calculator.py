from PyQt6.QtWidgets import QGridLayout,QVBoxLayout,QHBoxLayout,QMainWindow,QWidget,QApplication,QLabel,QPushButton,QLineEdit,QCheckBox,QMessageBox
import sys
from PyQt6.QtGui import QPixmap,QFont
from PyQt6.QtCore import Qt


class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()
  
  def initUI(self):
    self.setWindowTitle("Calculator App")

    self.current_input = "0"
    self.previous_input = ""
    self.current_operator = ""

    layout = QGridLayout()
    self.setLayout(layout)

    self.display = QLabel("0")
    self.display.setAlignment(Qt.AlignmentFlag.AlignRight)

    layout.addWidget(self.display,0,0,1,4)

    buttons = [QPushButton(str(i)) for i in range(10)]

    for i,button in enumerate(buttons):
      layout.addWidget(button,1+i//3,i%3)

    for button in buttons:
      button.clicked.connect(self.number_button_clicked)

    operators = ["+", "-", "*", "/"]
    operator_buttons = [QPushButton(op) for op in operators]

    for i,op_button in enumerate(operator_buttons):
      layout.addWidget(op_button,1+i,3)
    
    for op_button in operator_buttons:
      op_button.clicked.connect(self.operator_button_clicked)

    self.equals_button = QPushButton("=")
    layout.addWidget(self.equals_button,4,1)
    self.equals_button.clicked.connect(self.calculate)

    self.clear_button = QPushButton("C")
    layout.addWidget(self.clear_button,4,2)
    self.clear_button.clicked.connect(self.clear)
  
  def number_button_clicked(self):
    digit = self.sender().text()

    if self.current_input == "0":
      self.current_input = digit
    else:
      self.current_input += digit

    self.display.setText(self.current_input)
  
  def operator_button_clicked(self):
    operator = self.sender().text()

    if self.current_operator == "":
      self.current_operator = operator
      self.previous_input = self.current_input
      self.current_input = "0"
    else:
      self.calculate()
      self.current_operator = operator
      self.previous_input = self.current_input
      self.current_input = "0"

  def clear(self):
    self.current_input = "0"
    self.current_operator = ""
    self.previous_input = ""
    self.display.setText(self.current_input)

  def calculate(self):
       
    if self.current_operator == "+":
      result = float(self.previous_input) + float(self.current_input)
    elif self.current_operator == "-":
      result = float(self.previous_input) - float(self.current_input)
    elif self.current_operator == "*":
      result = float(self.previous_input) * float(self.current_input)
    elif self.current_operator == "/":
      if self.current_input == "0":
        result = "Error"
      else:
        result = float(self.previous_input) / float(self.current_input)
    else:
      result = self.current_input
    
    if result == "Error":
      msg = QMessageBox.warning(self, "Error", "An error has occured!, kindly clear the input and start again.")
      self.clear()
      return
    else:  
      self.display.setText(str(result))
      self.current_input = str(result)
      self.current_operator = ""


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())