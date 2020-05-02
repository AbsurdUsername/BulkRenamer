import os
import sys
import tkinter
from tkinter.filedialog import askopenfilenames

def RenameFileName():
    tkinter.Tk().withdraw()
    #main list with file names and path
    Files = askopenfilenames(title='Choose the files you want to rename')

    FilesTuple = tuple()
    FilesList = list()
    index = 0

    for x in Files:
        #tuple with file names without path
        FilesTuple = os.path.split(x)
        #using a list for file names without path for convience
        FilesList.append(FilesTuple[1])
        
    for y in FilesList:
        print('File picked ► ' + FilesList[index])
        index += 1

    oldName = input('Write the part of the name of the files you want to change [CASE SENSITIVE]: ')

    index = 0
    for k in FilesList:
        strtest = FilesList[index]
        if not (oldName in strtest):
            print(' ! It appears that one of the files you selected does not contains: ' + oldName)
            print('Do you want to remove the element? No will exit the program (y/n)')
            pick = input('>> ')
            if pick == 'n' or pick == 'no' or pick == 'No' or pick == 'NO':
                sys.exit()
            elif pick == 'y' or pick == 'yes' or pick == 'Yes' or pick == 'YES':
                FilesList.pop(index)
        index += 1

    newName = input('Write how you want to rename the files: ')

    for z in FilesList:
        discard, keep = z.split(oldName)
        result = newName + keep
        os.rename(os.path.join(FilesTuple[0], z), os.path.join(FilesTuple[0], result))

def RenameFileExtension():
    tkinter.Tk().withdraw()
    #main list with file names and path
    Files = askopenfilenames(title='Choose the files you want to rename')

    FilesTuple = tuple()
    FilesList = list()
    index = 0

    for x in Files:
        #tuple with file names without path
        FilesTuple = os.path.split(x)
        #using a list for file names without path for convience
        FilesList.append(FilesTuple[1])
        
    for y in FilesList:
        print('File picked ► ' + FilesList[index])
        index += 1

    newName = input('Write how you want to change the extension [DOT NOT INCLUDED]: ')

    for z in FilesList:
        keep, discard = z.split('.')
        result = keep + '.' + newName
        os.rename(os.path.join(FilesTuple[0], z), os.path.join(FilesTuple[0], result))


print('Welcome!')
print('Enter 1 to rename the files names')
print('Enter 2 to rename the files extensions')
choice = int(input('>>'))
if choice == 1:
    RenameFileName()
elif choice == 2:
    RenameFileExtension()