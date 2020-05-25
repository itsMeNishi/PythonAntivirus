from DirectoryExplorer import *

#dirList = DirectoryExplorer("/home/fractaluser/Desktop")

#print(dirList.list_dir())

class Main:
	
	def __init__(self):
		self.OptionList = []
		

	def initOptions(self):
		
		self.OptionList.append("Press 1 if you want to scan a directory")
		self.OptionList.append("Press 2 if you want to scan a file")
		self.OptionList.append("Press 3 if you want to scan a URL")
		self.OptionList.append("Press 4 to exit")
	def printOption(self):
		for item in self.OptionList:
			print(item)

	def takeUserInput(self):
		userInput = input("Your input :")
		return userInput

	def directoryScanner(self):
		pass
		
	def fileScanner(self):
		pass
	
	def urlScanner(self):
		pass

	def handleUserInput(self,userInput):
		if userInput == 1:
			self.directoryScanner()
		elif userInput == 2:
			self.fileScanner()
		elif userInput == 3:
			self.urlScanner()
		else:	
			return False
		return True


	def run(self):
		self.initOptions()
		self.printOption()
		while self.handleUserInput(self.takeUserInput()) == True:
			self.printOption()
			


Main().run()
		

		


