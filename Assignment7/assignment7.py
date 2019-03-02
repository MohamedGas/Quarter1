#This Program Will Find  The Prime Number
#assignment7.py
def main():
    #promptin values from the users
    user_input=eval(input("Please Enter Any  Number That Is Greater Than 1 : "))
    #checking whether the number is greater than 2 or not 
    if user_input<=1:
        print("You Should Enter A number that is greater than 1")
    else:
        #Creating lists of numbers
        numbers_list=[]
        #creating list of prime numbers 
        list_of_prime=[]
        #adding the numbers to the numbers_list and it starts from 2
        for i in range(2,user_input+1):
            numbers_list.append(i)

        while numbers_list!=[]:
            #remove the firstname and add to the list of primes 
            first_number=numbers_list.pop(0)
            list_of_prime.append(first_number)
            #Removing the numbers that divided by first_number  
            for numbers in numbers_list:
                if numbers % first_number==0 :
                    numbers_list.remove(numbers)
        #Reporting to the user Allt the prime numbers of the that number 
        print("The List Of  Prime Number of  ",user_input," are ")        
        for i in range(len(list_of_prime)):
            print(list_of_prime[i]," Is Prime Number")
            
    return list_of_prime
        


main()


