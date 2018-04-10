class WordGenerator:
    def __init__(self):
        pass

    def syllable(self):
        choices = "CV"

        return choices

    def vowel(self):
        choices = "a"

        return choices

    def consonant(self):
        choices = "b"

        return choices

    def word(self, numsyll):
        length = numsyll

        word, temp = "", ""

        for i in range(0, length):
            temp += self.syllable()

            print("temp {}".format(temp))

        for i in range(0, len(temp)):
            if temp[i] == 'C':
                word += self.consonant()

                print("C {}".format(word))

            else:
                word += self.vowel()

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
