from ast import Continue
import os
from shutil import copyfile

def cls():
    print('\n'*100)

# Replace the value for source and destination
Source='/home/Example/Documents/Test/Source/'
Destination='/home/Example/Documents/Test/Destination/'


def Backup(root,name):
    SourcePath=os.path.join(root, name)
    DestPath=SourcePath.replace(Source,Destination)
    if not os.path.exists(SourcePath.replace(Source,Destination)):
        print('Creating Directory:',DestPath)
        if os.path.isdir(SourcePath):
            os.mkdir(DestPath)
        elif os.path.isfile(SourcePath):
            copyfile(SourcePath,DestPath)
        else:
            print('Error Not a file or a Directory')
            exit()
        if os.path.exists(DestPath):
            print(DestPath,' Created Successfully')
        else:
            print('Error Creating:',DestPath)
            exit()
        print('')

def Deleting(root,name): 
    DestPath=os.path.join(root,name)
    SourcePath=DestPath.replace(Destination,Source)
    print(DestPath)
    if Destination == DestPath:
        print('NOT Deleting Root')
    else:
        if not os.path.exists(SourcePath):
            print('Deleting:',DestPath)
            if os.path.isdir(DestPath):
                os.rmdir(DestPath)
            elif os.path.isfile(DestPath):
                os.remove(DestPath)
            else:
                print('Error Not a file or a Directory')
                exit()
            if not os.path.exists(DestPath):
                print(DestPath,' Deleted Successfully')
            else:
                print('Error Deleting:',DestPath)
                exit()
            print('')


cls()
print('Are you sure you want to Sync files')
print('From here:',Source)
print('To here:',Destination)
print('This will delete any files ONLY here:',Destination)
print('')
Continue=input('Press Enter To Continue, Anything Else to Cancel')
if Continue == '':

    #Removing Files from Destination that aren' in Source
    for root, dirs, files in os.walk(Destination,topdown=False):
        #Removing Files
        for name in files:
            Deleting(root,name)

        #Removing Direcotires
        for name in dirs:
            Deleting(root,name)


    #Backing up files and Directories
    for root, dirs, files in os.walk(Source, topdown=True):
        #Backing up Directories
        for name in dirs:
            Backup(root,name)

        #Backing up Files
        for name in files:
            Backup(root,name)