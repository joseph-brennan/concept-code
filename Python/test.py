import math


class Test:
    def __init__(self):
        self.dummy = ""

    def printer(self):
        self.dummy = "it worked yay"
        print(self.dummy)
        mysum = 0
        for i in range(5, 11, 2):
            mysum += i
            print("this is i {}".format(i))
            print("this is sum {}".format(mysum))

        print(mysum)

    def gcd(self, x, y):
        gcd = 1

        if x % y == 0:
            return y

        for k in range(int(y / 2), 0, -1):
            if x % k == 0 and y % k == 0:
                gcd = k
                break
        return gcd

    def replace(self):
        out = ""
        replacement = {"a": "u", "e": "o", "u": "a"}
        string = input("input ")
        for letter in string:
            if letter in replacement.keys():
                out += replacement[letter]

            else:
                out += letter
            print(out)


if __name__ == '__main__':
    foo = Test()
    foo.replace()
