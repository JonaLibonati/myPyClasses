# menu.py
This library is useful to create menus for scripts which run on the terminal.

## Class Option(name: str, funtion: function, message = '')
This class creates an Option object which contains its name, function and message(optional).
```
option1 = Option('option 1', lambda : print('Hello from option 1'), 'optional message')
```

## Class NumericMenu(name = '', message = '')
This class creates a Numeric Menu. Name and message are optional parameter. The numeric menu allows an indeterminate quantity of option.

### addOptions(*args: Option)
Adds options to the numeric menu. The order is important because it defines the number that corresponds to each option.

### ask()
Asks to the user which option is executed and it executes.

```
option1 = Option('option 1', lambda : print('Hello from option 1'), 'optional message')
option2 = Option('option 2', lambda : print('Hello from option 2'))
option3 = Option('option 3', lambda : print('Hello from option 3'))
option4 = Option('option 4', lambda : print('Hello from option 4'))

menu = NumericMenu('Choose mode Menu\n', 'This is a trial menu\n')
menu.addOptions(option1, option2, option3, option4)
menu.ask()

Result:
Choose mode Menu

This is a trial menu

1) option 1 optional message
2) option 2
3) option 3
4) option 4

You choose: 3
Hello from option 3
```

## Class BinaryMenu(name = '', message = '')
This class creates a Binary Menu. Name and message are optional parameter. The binary menu allows only two option, yes or no.

### addOptions(optionYES: Option, optionNO: Option)
Adds options to the numeric menu. The order is important because the first one defines the "yes" option and the second one defines the "no".

### ask()
Asks to the user which option is executed and it executes.

```
option1 = Option('option 1', lambda : print('Hello from option 1'), 'optional message')
option2 = Option('option 2', lambda : print('Hello from option 2'))

BinaryMenu().addOptions(option1, option2).ask()

Result:
Do you want to continue?
Y) Yes
N) No

You choose: y
Hello from option 1
```

## Class CommandMenu()
This class creates a Command Menu. This menu uses a string as a command to run a specific option. It could be useful when the option is passed as a paremeter in the terminal when a script is executed.

### addOptions(*args: Option)
Adds options to the Command menu. The order is not important.

### ask(cmdOption: str)
Executes the option which name matchs with cmdOption.

```
def help():
        print('This is a help message ')

option1 = Option('-h', lambda: help())
option2 = Option('--help', lambda: help())
option3 = Option('', lambda: print('Hello from option 3'))

menu = CommandMenu().addOptions(option1, option2)
menu.ask('-h')
menu.ask('--help')
menu.ask('')

Result:
This is a help message
This is a help message
Hello from option 3
```