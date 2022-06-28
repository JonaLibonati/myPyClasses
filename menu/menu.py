from __future__ import annotations
#Menu Object - Father
class Menu():

    def __init__(self, name='', message = '') -> None:
        self.name = name
        self.message = message
        self.options = []
        self.answer = -1

    #Method to add options
    def addOptions(self) -> Menu:
        pass

    #Method to ask the menu options
    def ask(self) -> None:
        pass

    # Option object
    class Option:
        def __init__(self, name: str, function: function, message = '') -> None:
            self.name = name
            self.message = message
            self.function = function

# Numeric Menu Object- Menu child
class NumericMenu(Menu):
    def addOptions(self, *args: Menu.Option) -> NumericMenu:
        for arg in args:
            self.options.append(arg)
        return self

    def ask(self) -> None:
        print(self.name)
        print(self.message)
        if self.options != []:
            for i, option in enumerate(self.options):
                print(f'{i + 1}) {option.name} {option.message}')
            while not self.inRange():
                try:
                    self.answer = int(input('\nYou choose: ').strip())
                    if not self.inRange():
                        print("\nInvalid input. The number is not a valid option.")
                except ValueError:
                    print("\nInvalid input, please enter a number")
            self.options[self.answer - 1].function()
        else:
            print('\nCODE ERROR: There are not options to show. Please instantiate Menu.Option() and add it using MenuObject().addOptions before ask()')

    def inRange(self) -> bool:
        return self.answer > 0 and self.answer <= len(self.options)


# Binary Menu - Menu child
class BinaryMenu(Menu):

    def addOptions(self, optionYES: Menu.Option, optionNO: Menu.Option) -> BinaryMenu:
            self.options.append(optionYES)
            self.options.append(optionNO)
            return self

    def ask(self) -> None:
        print(self.name)
        print(self.message)
        if self.options != []:
            print(f'Y) {self.options[0].name}')
            print(f'N) {self.options[1].name}')
            while not (self.isyes() or self.isno()):
                self.answer = input('\nYou choose: ').lower().strip()
                if not (self.isyes() or self.isno()):
                    print('\nInvalid input')
                    print('Valid inputs: [y, n], [yes, no], [1, 0]')
            if self.isyes():
                self.options[0].function()
            else:
                self.options[1].function()
        else:
            print('\nCODE ERROR: There are not options to show. Please instantiate Menu.Option() and add it using MenuObject().addOptions before ask()')

    def isyes(self) -> bool:
        return self.answer == 'y' or self.answer == 'yes' or self.answer == '1'

    def isno(self) -> bool:
        return self.answer == 'n' or self.answer == 'no' or self.answer == '0'