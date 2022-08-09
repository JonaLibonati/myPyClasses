# testReport.py
This library is useful for creating test reports. It could be used to print the report on the terminal or export it as a list of dictionaries.

The following code is used as example:
```
Report = TestReport('Report title')

section = Section('Section Title')

section.addResult(Result('comment message\n', 'comment'))

for i in [0,1,2,3,4]:
    if i > 2:
        r = Result('Result message', 'success')
    elif i == 0:
        r = Result('Result message', 'warning')
    else:
        r = Result('Result message', 'fail')
    section.addResult(r)

subsection = Subsection('Subsection title').addResult(Result('Subsection Result Message', 'success'))
section.addSubSection(subsection)

Report.addSection(section)
```

## Class Result(description: str, result = 'comment')
This class creates a Result object. The first parameter is the result description as string. The second parameter is the result it self and it can take four values which are 'success', 'fail', 'warning' or 'comment'

### description
Contains the description as string.

### result
Contains the result as string.

### data
Contains the result data as a dictionary.

### line
Contains the result line as string.

### print()
Prints the result on the terminal.

## Class Section(name: str)

### name
Contains the section name as string.

### data
Contains the section data as a list of dictionaries.

### subsection
Contains the Subsection object added to the report as a list.

### results
Contains the Result object added to the report as a list.

### lines
Contains the section lines as a list.

### addResult(*args: Result)
Adds the Result objects to the report.

### addSubSection(*args: Subsection)
Adds the Subsection objects to the report.

### setName(new_name: str)
Set the section name.

### print()
Prints the section on the terminal.

## Class Subsection(name: str)
This class creates a Subsection object which inherits from Section object, therefore it has the same properties and methods.

## Class TestReport(name: str)
This class creates a TestReport object. The parameter is the name of the resport as string.
The report is empty when it is created. By using addSection(*args: Section), the diferent section are included in the report.

### name
Contains the report name as string.
```
print(Report.name)

Result:
Report title
```

### data
Contains report data as list of dictionaries.
```
print(Report.data)

Result:
[
    {'type': 'title', 'data': 'Report title'},
    {'type': 'subtitle', 'data': 'Section Title'},
    {'type': 'result', 'data': 'comment message\n', 'result': 'comment'},
    {'type': 'result', 'data': 'Result message', 'result': 'warning'},
    {'type': 'result', 'data': 'Result message', 'result': 'fail'},
    {'type': 'result', 'data': 'Result message', 'result': 'fail'},
    {'type': 'result', 'data': 'Result message', 'result': 'success'},
    {'type': 'result', 'data': 'Result message', 'result': 'success'},
    {'type': 'subtitle', 'data': 'Subsection title'},
    {'type': 'result', 'data': 'Subsection Result Message', 'result': 'success'}
]
```

### section
Contains the section object added to the report as a list.
```
print(Report.sections)

Result:
[<testReport.Section object>]
```

### lines
Contains the report lines as a list.
```
[
    '\n-------------------- REPORT TITLE --------------------\n', \
    '\n------------ SECTION TITLE ------------\n',
    'comment message\n',
    '🟡 - Result message',
    '🔴 - Result message',
    '🔴 - Result message',
    '🟢 - Result message',
    '🟢 - Result message',
    '\n-- SUBSECTION TITLE --\n',
    '🟢 - Subsection Result Message'
]
```

### addSection(*args: Section)
Adds the section objects to the report.

### setName(new_name: str)
Set the report name.
```
Report.setName('new report name')

print(Report.name)

Result:
new report name
```

### print()
Prints the report on the terminal.
```
Report.print()

Result:
-------------------- REPORT TITLE --------------------


------------ SECTION TITLE ------------

comment message
🟡 - Result message
🔴 - Result message
🔴 - Result message
🟢 - Result message
🟢 - Result message

-- SUBSECTION TITLE --

🟢 - Subsection Result Message
```