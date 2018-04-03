

class BMI:
    def __init__(self):
        self.weight = int(input("what is your weight? "))
        self.height = 12 * int(input("what is your height in feet? "))

    def calcBmi(self):
        result = (self.weight * 703) / self.height ** 2

        print("your BMI is {}".format(result))

        if result < 18.5:
            print("under weight")

        elif result > 25:
            print("over weight")

        else:
            print("optimal weight range")


if __name__ == '__main__':
    bmi = BMI()
    bmi.calcBmi()
