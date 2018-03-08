import random
import tkinter


class MakeWords:
    def __init__(self):
        self.consents, self.vowels = [], []

        self.structure = {}

    def read_file(self, file_name):
        try:
            file = open("{}.txt".format(file_name), 'r')

        except FileNotFoundError or IOError:
            print("Couldn't find the file")

            exit(1)

        self.set_up(file)

        file.close()

    def set_up(self, file):
        """
        Uses the file to set up the the rules of the language.
            1. key is for the structure dictionary.
            2. i is used in the list so only one loops runs
        :param file: the opened file with the correct format
        :return: sets the rules defined by the user
        """
        key = 1
        i = 0

        dummy = [self.structure[key], self.consents, self.vowels]

        for line in file:
            for word in line.strip().split(","):
                if i == 0:
                    dummy[i] = word

                    key += 1

                elif i in (1, 2):
                    dummy[i].append(word)
            i += 1

    def hard_code(self):
        """
        My understanding of the necessary letters for language stuff
        :return: sets default if there is no file input
        """
        self.consents = ['b', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']

        self.vowels = ['a', 'i', 'o', 'u', 'y']

        self.structure = {1: "CVC", 2: "CV", 3: "CCV", 4: "VC"}

    def io(self):
        """
         Console output at the moment.
        :return: N/A
        """
        while True:
            length = int(input("how many consents? "))

            struct = input("what kind of word structure? ")

            for key, name in self.structure.items():
                if name == struct:
                    self.individual_word(key, length)

            answer = input("Would you like another word?")

            if "N" in answer.upper()[0]:
                break

    def individual_word(self, key, count):
        """
        This is used to output a single word of the language.

        :param key: The key for the structure dictionary.
        :param count: The number of consents
        :return: N/A
        """
        new_word = ""

        while count > 0:
            for let in self.structure[key]:

                if let is "C":
                    if count == 0:
                        break

                    else:
                        new_word += random.choice(self.consents)

                        count -= 1

                elif let is "V":
                    new_word += random.choice(self.vowels)

                else:
                    print("Error fell out of structure.")

                    exit(1)
        print(new_word)


if __name__ == '__main__':
    words = MakeWords()

    top = tkinter.Tk()
    top.mainloop()

    setup = input("Do you have a language file?")

    if "Y" in setup.upper()[0]:
        filename = input("what is the file's name? ")

        words.read_file(filename)

    else:
        words.hard_code()

        words.io()
