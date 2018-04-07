class VowelCount:
    def __init__(self):
        self.sentence = input("what word or sentence would you like to get the total number of vowels? ").strip()

    def count(self):
        count = 0

        for letter in self.sentence:

            if letter.lower() in ("a", "e", "i", "o", "u", "y"):
                count += 1

        self.printer(count)

    def printer(self, count):
        check = self.sentence.partition(" ")

        if check[2]:
            print("For the sentence: {} \nThere are {} vowels".format(self.sentence, count))

        else:
            if count is 1:
                print("For your word: {} \nThere is {} vowel".format(self.sentence, count))

            else:
                print("For your word: {} \nThere are {} vowels".format(self.sentence, count))


if __name__ == '__main__':
    vowel = VowelCount()
    vowel.count()
