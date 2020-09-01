
class AutomataFileReader:

    def openFile(self):
        fileName = input("Enter file name end .txt -")
        if len(fileName) < 1: fileName = 'automatafile.txt'
        try:
            fileHandle = open(fileName)
        except ValueError:
            print('Error: file name not found')

        for line in fileHandle:
            print(line.rstrip())
