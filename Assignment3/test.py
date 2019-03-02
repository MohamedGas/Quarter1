#promt user from the file name

def main():

    fname=input("please input the name of the file that you want to read")

    #opening the file
    infile=open(fname,'r')

    #holding the data that we have read from the file

    for line in infile.readline():
       print(line)
        

    #closing the file

    infile.close()

    #report to the user

    



main()

