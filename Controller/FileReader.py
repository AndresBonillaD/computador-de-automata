# code to generate autoamata from a text file
import re

fileName = input("Enter file name end .txt -")
if len(fileName) < 1: fileName = 'automatafile.txt'
fileHandle = open(fileName)

# patterns to use regular expresions
typePattern = re.compile('^(#!)(nfe|dfa|nfa)$')
alphabetPattern = re.compile('^([^#\n\t\r$])$|^([^\n\t$\r])-([^\n\t$\r])$')
statePattern = re.compile('^([^#;>\r\n\t ])([^;>\r\n\t]*)$')
transitionsPattern = re.compile('^([^#;>\r\n\t ])([^;>\r\n\t]*):'
                                '([^#\n\t\r])>([^#;>\r\n\t ])([^;>\r\n\t]*)(;([^;>\r\n\t ])([^;>\r\n\t]*))*$')

# funtions to compute the elements of the automata
def addToAlphabet(line):
    print('input line ' + line)
    m = alphabetPattern.match(line)
    if m :
        print('correct alphabet line')
    else:
        print('incorrect alphabet line')

def addToStates(line):
    print('input line ' + line)
    m = statePattern.match(line)
    if m :
        print('correct states line')
    else:
        print('incorrect states line')

def addToInitial(line):
    print('input line ' + line)
    m = statePattern.match(line)
    if m :
        print('correct state line')
    else:
        print('incorrect state line')

def addToAccepting(line):
    print('input line ' + line)
    m = statePattern.match(line)
    if m :
        print('correct state line')
    else:
        print('incorrect state line')

def addToTransitions(line):
    print('input line ' + line)
    m = transitionsPattern.match(line)
    if m :
        print('correct transition line')
    else:
        print('incorrect transition line')

# select the correct type and create the automata
def generateAutomata(type):
    if type == '#!dfa':
        print('Generating deterministic finite automata')
    elif type == '#!nfa':
        print('Generating Non-deterministic finite automata')
    elif type == '#!nfe':
        print('Generating Non-deterministic finite automata with lambda transitions')

element = ''
print()
typeMatch = typePattern.match(fileHandle.readline())
if typeMatch:
    for line in fileHandle:
        line = line.rstrip()
        # set the element flag to clacify the lines
        if line.startswith('#'):
            element = line
            continue
        #print(element)
        if element == '#alphabet':
            addToAlphabet(line)
        elif element == '#states':
            addToStates(line)
        elif element == '#initial':
            addToInitial(line)
        elif element == '#accepting':
            addToAccepting(line)
        elif element == '#transitions':
            addToTransitions(line)
        #print(line)
else:
    print('incorrect automata Type')
print('-- Done --')
#print(lines)
