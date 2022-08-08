from menu import *

def main ():
#creating options
    option1 = Option('option 1', lambda : print('Hello from option 1'), 'optional message')
    option2 = Option('option 2', lambda : print('Hello from option 2'))
    option3 = Option('option 3', lambda : print('Hello from option 3'))
    option4 = Option('option 4', lambda : print('Hello from option 4'))

    #e.g. Numeric Menu
    menu = NumericMenu('Choose mode Menu\n', 'This is a trial menu\n')
    menu.addOptions(option1, option2, option3, option4)
    menu.ask()

    #e.g. Binary Menu
    BinaryMenu('', 'Do you want to continue?').addOptions(option1, option2).ask()

    print('')

    #e.g. Command Menu
    def help():
        print('This is a help message ')

    option1 = Option('-h', lambda: help())
    option2 = Option('--help', lambda: help())
    option3 = Option('', lambda: print('Hello from option 3'))

    menu = CommandMenu().addOptions(option1, option2, option3)
    menu.ask('-h')
    menu.ask('--help')
    menu.ask('')


if __name__ == '__main__':
    main()