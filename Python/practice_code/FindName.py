class FindName:
    def __init__(self):
        pass

    def findname(self):
        names = ['David', 'Adam', 'Mary', 'Jill', 'Jack']

        newName = input('Enter a name ')

        if newName in names:
            print("{} is in the list".format(newName))

        else:
            print("{} is not in the list".format(newName))
    # Write the code to test if newName is in the list
    # of names (names). It should display an appropriate
    # message in the output.


if __name__ == '__main__':
    name = FindName()
    name.findname()
