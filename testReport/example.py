from testReport import *

def main():
    Report = TestReport('Report title')

    section = Section('Section Title')

    for i in [0,1,2,3,4]:
        if i > 2:
            r = Result('Result message')
        elif i == 0:
            r = Result('Result message', 'warning')
        else:
            r = Result('Result message', 'fail')
        section.addResult(r)

    subsection = Subsection('Subsection title').addResult(Result('Subsection Result Message'))
    section.addSubSection(subsection)
    Report.addSection(section)

    Report.print()

if __name__ == '__main__':
    main()
