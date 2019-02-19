import random,pickle,os
from Record import *

nRecords = 100 
def createFile(nRecords):
    '''
    Objective : To create a file having nRecords Record() objects
                each with unique key
    Input:
        nRecord: Number of records to write in a file
    Return: None
    '''

    f = open("File.txt",'wb')
    keys = []

    #Create nRecords each with a random and unique key
    for i in range(nRecords):
        key = random.randint(1000000,2000000)

        #Check for duplicate keys
        while key in keys:
            key = random.randint(1000000,2000000)
        keys.append(key)
        pickle.dump(Record(key),f)
    f.close()

    #Read file 
##    f = open('records.txt','rb')
##    for i in range(nRecords):
##        print(pickle.load(f).getKey())
##    f.close()


def readFileR(fname,upper,lower = 0):
    '''
    Objective : To display the records of file between upper and lower limits.
    Input:
        fname : Name of file in which records are stored
        upper : Upper limit
        lower : Lower limit
    Return Value : None
    '''
    try:
        f = open(fname)
    except FileNotFoundError:
        print("No file exist. Please create the file first")
        return

    #Read file 
    f = open(fname,'rb')
    pickle.load(f)
    size = f.tell()

    f.seek((lower-1)*size)
    print(lower,upper)
    
    for i in range(lower,upper+1):
        try:
            print(pickle.load(f))
        except:
            print("NOT SUFFICIENT RECORDS")
            break
    f.close()


def readFile(fname):
    '''
    Objective : To display all the records of file.
    Input:
        fname : Name of file in which records are stored
    Return Value : None
    '''
    try:
        f = open(fname)
    except FileNotFoundError:
        print("No file exist. Please create the file first")
        return

    #Read file 
    f = open(fname,'rb')

    while True:
        try:
            print(pickle.load(f))
        except:
            break
        
    f.close()

if __name__ == "__main__":
    while True:
        print("*********** CREATE FILE ***************")
        print("1. Create file again.")
        print("2. Read the whole file.")
        print("3. Read records in a particular range.")
        print("4. Exit")
        ch = int(input("\nEnter your choice:"))

        if ch == 1:
            #nRecords = int(input('Enter the number of records you want to create:'))
            print('Creating files again with '+str(nRecords)+' records...')
            createFile(nRecords)
            print('Records created')

        elif ch == 2:
            readFile("File.txt")

        elif ch == 3:
            lower,upper = int(input('Enter the range of records \n Lower limit:')),int(input(" Upper limit:"))
            if upper<1 or lower<1:
                print("Limits should be more than 1")
                continue
            readFileR("File.txt",upper,lower)
        elif ch == 4:
            print("\n ADIOS!")
            break
        else:
            print("Invalid choice")
