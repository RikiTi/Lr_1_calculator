class GUI:
    _user_choose = None
    _menu_text = "Выберите операцию:\n1.Суммирование\n2.Умножножение\n3.Деление\n4.Вычитание\n5.Выход\n:"

    def __init__(self, calculator):
        """Constructor for base values and realization DI by constructor"""
        self.calculator = calculator

    def show_menu(self):
        '''Отображение меню пользователя'''
        self._user_choose = int(input(self._menu_text))

    def run_command(self):
        '''Запуск основных команд для работы с калькулятором'''
        answer = None
        self.show_menu()
        if self._user_choose > 5:
            print("Такого  варианта операции не существует!\nПовторите операцию.")
            return self.run_command(self.calculator)
        else:
            if self._user_choose == 5:
                exit(0)
            numbers = list(map(lambda x: int(x), self.get_numbers()))
            if self._user_choose == 4:
                answer = self.calculator.subtraction(numbers[0], numbers[1])
            if self._user_choose == 3:
                answer = self.calculator.division(numbers[0], numbers[1])
            if self._user_choose == 2:
                answer = self.calculator.multiplication(numbers[0], numbers[1])
            if self._user_choose == 1:
                answer = self.calculator.addition(numbers[0], numbers[1])
            return answer

    def get_numbers(self):
        '''Запрос данных у пользователя'''

        return input("Введите через пробел два числа: ").split()
