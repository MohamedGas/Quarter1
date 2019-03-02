#this program will calculate the sum , square of a list of numbers as well as 
# it converts string to number , it also compute the square number from the file
#MOHAMED GAS

#Sum of the squared number Method
def sumList(nums):
    #initializing acculamtive variable 
    sum_of_list=0
    #iterating the list 
    for n in range(len(nums)):
        #calculating the sum of the number of list
        sum_of_list+=nums[n]
    #Return the sum of the list 
    return sum_of_list

#Square Method 
def squareEach(nums):
    #empty list using to append the squared number from the list
    squarednumber=[]
    #iterating the list 
    for n in range(len(nums)):        
        #holding square number
        square=nums[n]**2
        #append squared number to sqaurenumber list 
        squarednumber.append(square)
    #return the list of the squared number 
  
    return squarednumber
    

#toNumbers Method
def toNumbers(strList):
    for n in range(len(strList)):
        strList[n]=float(strList[n])
        print(type(strList[n]))
    return strList

#Reading number from the file 
def Read_from_file(fname):
    
    #opening the file
    infile= open(fname,'r')  
    #holding the data into data field  
    data=infile.readlines()
    #folding the data list into file_num_list
    file_num_list=[]
    #iterating the data and get each value in the file
    for line in data:
        #converting type into integer
        x=int(line)   
        #adding list into new list variable called file_num_list    
        file_num_list.append(int(x))
    #square each value using squareech method
    square=squareEach(file_num_list)
    #report the sum of the square values    
    print('Sum is :', sumList(square))

def main():
    '''
    if you want to  test each function i write some sample data of list below you should uncomment 
    otherwise the works on reading file and you can see the functionality of 
    squareEach and sumList method in read_file method 
    '''
    #Testing toNumber Method
    #print(toNumbers(['1','1.2','3.33']))

    #testting sumList Method
    #print(sumList([1,2,3,4]))

    #testting squareEach Method
    #print(squareEach([1,2,3,4]))
    #prompting user from the file name
    fname=input("Please Enter The File Name With it's Extention : ")

    #invoking readfile method
    Read_from_file(fname)

main()
