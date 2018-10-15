import random


class Encryption:
    def __init__(self):
        try:
            self.mod = int(input("mod number: ")) % 26

        except ValueError:
            print("not a number picking random one")

            self.mod = random.randint(0, 24)

        while True:
            answer = input("would you like to encrypt or decrypt? ")

            if answer[0].lower() == "e":
                self.type = 1
                break

            elif answer[0].lower() == "d":
                self.type = 0
                break

            else:
                print("either Encrypt/Decrypt")

        self.scheme = {}

    def setup(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        reverse = "zyxwvutsrqponmlkjihgfedcba"

        if self.type is 1:
            for letter in alphabet:
                self.scheme[letter] = alphabet[self.mod]

                self.mod = (self.mod + 1) % 26

        elif self.type is 0:
            for letter in reverse:
                self.scheme[letter] = reverse[self.mod]

                self.mod = (self.mod + 1) % 26

    def message(self):
        ciphered = ""
        sentence = input("what would you like encrypted/decrypted? ")

        for letter in sentence:
            if letter not in list(self.scheme.values()):
                ciphered += letter

            else:
                ciphered += self.scheme[letter]

        print("{} \nthat is the new message.".format(ciphered))

    def run(self):
        self.setup()

        while True:
            self.message()

            again = input("Another message with the current scheme? ")

            if again[0].lower() in "y":
                pass

            else:
                break


if __name__ == '__main__':
    test = Encryption()
    test.run()
