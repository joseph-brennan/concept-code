class test:
	def __init__(self):
		self.dummy = ""

	def printer(self):
		self.dummy = "it worked yay"
		print(self.dummy)


if __name__ == '__main__':
	foo = test()
	foo.printer()
