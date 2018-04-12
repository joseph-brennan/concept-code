import random
import tkinter


class WordGenerator:
    def __init__(self):
        self.vowel_choices = []
        self.consonant_choices = []
        self.syllable_choices = {}
        self.numsyll = 0

    def set_up(self):
        try:
            self.numsyll = int(input("Enter number of syllables: "))

        except ValueError:
            self.numsyll = input("Please enter an actual number: ")

            if self.numsyll.isdigit():
                self.numsyll = int(self.numsyll)

            else:
                print("Still not a number aborting.")
                exit(-1)

    def syllable(self):
        self.syllable_choices = {1: "CV", 2: "VC", 3: "CVC"}

        # return random.choice(choices)

    def vowel(self):
        self.vowel_choices = ["a", "e", "i", "o", "u"]

        # return random.choice(choices)

    def consonant(self):
        self.consonant_choices = ["b", "c", "d", "f", "h", "j", "k", "l", "m", "n", "p", "q", "r", "t", "v", "x", "z"]

        # return random.choice(choices)

    def word(self):
        word, temp = "", ""

        for i in range(0, self.numsyll):

            temp += random.choice(list(self.syllable_choices.values()))

        # this says for each letter in the "word" template. where letter is the C or V
        for letter in temp:
            if letter in 'C':
                word += random.choice(self.consonant_choices)

            elif letter in 'V':
                word += random.choice(self.vowel_choices)

            else:
                print("how? fell out of word building")
                exit(1)

        return word

    def run(self):
        # hard coded for now to use the options above
        self.syllable()
        self.consonant()
        self.vowel()

        while True:
            self.set_up()

            if self.numsyll is -1:
                break

            elif self.numsyll is 0:
                self.numsyll = random.randint(1, 4)

            else:
                pass

            word = self.word()

            print("{}\n".format(word))


if __name__ == '__main__':
    tk = tkinter
    tk.Tk()
    tk.mainloop()

    words = WordGenerator()
    words.run()
