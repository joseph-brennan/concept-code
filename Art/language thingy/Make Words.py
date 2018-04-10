import random

"""
now czecha
"""
class WordGenerator:
    def __init__(self):
        self.vowel_choices = []
        self.consonant_choices = []
        self.syllable_choices = []

    def syllable(self):
        self.syllable_choices = ["CV", "VC", "CVC"]

        # return random.choice(choices)

    def vowel(self):
        self.vowel_choices = "a"

        # return random.choice(choices)

    def consonant(self):
        self.consonant_choices = "b"

        # return random.choice(choices)

    def word(self, numsyll):
        length = numsyll

        word, temp = "", ""

        # hard coded for now to use the options above
        self.syllable()
        self.consonant()
        self.vowel()

        for i in range(0, length):

            temp += random.choice(self.syllable_choices)

            print("temp {}".format(temp))

        # this says for each letter in the "word" template. where letter is the C or V
        for letter in temp:
            if letter == 'C':
                word += random.choice(self.consonant_choices)

                print("C {}".format(word))

            else:
                word += random.choice(self.vowel_choices)

                print("V {}".format(word))

        return word

    def run(self):
        while True:
            numsyll = int(input("Enter number of syllables: "))

            if numsyll == -1:
                break

            else:
                word = self.word(numsyll)
                print("{}\n".format(word))


if __name__ == '__main__':
    word = WordGenerator()
    word.run()
