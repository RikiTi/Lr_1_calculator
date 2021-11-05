from gui import  GUI
from calculators import EconomicalCalculator
calculator = EconomicalCalculator()
gui_interface = GUI()
while True:
    answer = gui_interface.run_command(calculator)
    print(f' Результат вычислений: {answer}')