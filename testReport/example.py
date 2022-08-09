from testReport import *

def main():
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

    Report.print()

    print(Report.data)

if __name__ == '__main__':
    main()
