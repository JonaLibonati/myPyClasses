from menu import *

def main ():
#creating options
    option0 = Menu.Option('option 1', lambda : print('Hello from option 1'), 'optional message')
    option1 = Menu.Option('option 2', lambda : print('Hello from option 2'))
    option2 = Menu.Option('option 3', lambda : print('Hello from option 3'))
    option3 = Menu.Option('option 4', lambda : print('Hello from option 4'))

    #e.g. Numeric Menu
    menu1 = NumericMenu('Choose mode Menu\n', 'Este es un menu de prueba\n')
    menu1.addOptions(option0, option1, option2, option3)
    menu1.ask()

    #e.g. Binary Menu
    BinaryMenu().addOptions(option0, option1).ask()

if __name__ == '__main__':
    main()