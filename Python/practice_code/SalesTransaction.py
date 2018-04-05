

class ClassWork:
    def __init__(self):
        pass

    def Employee(self):
        name = input("what is their name?")
        salary = float(input("what is the salary"))
        hours = float(input("how many hours worked?"))

        gross = salary * hours
        taxed = gross * .025
        net = gross - taxed

        print("{} makes {} an hour for {} hours making their gross pay {} and net pay {}".format(name, hours, salary, gross, net))


if __name__ == '__main__':
    test = ClassWork()
    test.Employee()
