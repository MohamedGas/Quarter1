#This program will compute the fuel effiency 
#assignment6.py

def main():
        print(" This Program Will Calculate the fuel Efficiency ")
        # Prompt inital odometer from the user 
        initial_odometer=eval(input("Please enter the initial odometer reading : "))
        #Holds list of miles 
        list_of_miles=[] 
        # holds list of gas per leg
        list_of_gas=[]
        total_miles=0 # accumulate the miles
        total_gas=0 # accumlate the gas
        #prompt user odometer with gas 
        user_input=input("Please Enter the odometer and gas seperated by a space : ")

        while user_input!="":
                # splitting with comma
                final_odometer,gas=user_input.split()
                #assigning  the values we have splitted
                final_odometer,gas=eval(final_odometer),eval(gas)
               
                #appending listt of miles to list
                list_of_miles.append(final_odometer-initial_odometer)
                # adding  list of gas to list
                list_of_gas.append(gas)
                
                # reassging the initial values again
                initial_odometer=final_odometer
                # ask if there is another leg trip that user want to calculate  
                user_input=input("Please Enter the odometer and gas seperated by a space : ")

        # reporting the MPG of each leg
        print("Leg       MPG")
        for i in range(len(list_of_miles)):
                #accumalting the total of miles
                total_miles=total_miles+list_of_miles[i]
                #accumluating the total of gas belongs to this the mile of the trip 
                total_gas=total_gas+list_of_gas[i]
                #Calculate MPG 
                Mile_per_gallon=list_of_miles[i]/list_of_gas[i]
                print(i+1,"       " ,Mile_per_gallon)

        #Computing the final MPG
        final_total=total_miles/total_gas
        # seperate upper data and the fi
        print(35*'-')
        #reporting final total
        print("Total MPG for The Trip is : ", final_total)



        

main()