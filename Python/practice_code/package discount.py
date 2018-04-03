class Discount:
    def __init__(self):
        self.total = int(input("how many packages did you buy? "))

    def softwarediscount(self):
        if self.total >= 100:
            print("your discount is 50%")

        elif self.total >= 50 or self.total <= 99:
            print("your discount is 40%")

        elif self.total >= 20 or self.total <= 49:
            print("your discount is 30%")

        elif self.total >= 10 or self.total <= 19:
            print("your discount is 20%")

        else:
            print("there is no discount")


if __name__ == '__main__':
    dis = Discount()
    dis.softwarediscount()
