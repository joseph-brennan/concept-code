class ID:
    def __init__(self):
        self.first = input("what is your first name? ")
        self.last = input("what is your last name? ")

    def output(self):
        full = self.first + self.last

        print("your full name is {} with initials {} {} with length of {}".format(
            full, self.first[0], self.last[0], len(full)))


if __name__ == '__main__':
    idname = ID()
    idname.output()
