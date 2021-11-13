from gui import  GUI
from calculators import EconomicalCalculator
calculator = EconomicalCalculator()
gui_interface = GUI(calculator)
while True:
    answer = gui_interface.run_command()
    print(f' Результат вычислений: {answer}')