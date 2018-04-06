class Gcd:
    def __init__(self):
        self.first = int(input("your first number "))
        self.second = int(input("your second number "))

    def gcd(self):
        gcd_result = 1

        if self.first % self.second == 0:
            return self.second

        for k in range(int(self.second / 2), 0, -1):
            if self.first % k == 0 and self.second % k == 0:

                gcd_result = k

                break

        return gcd_result


if __name__ == '__main__':
    run = Gcd()
    print(run.gcd())
