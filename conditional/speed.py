# Speed.py 
# this program will calculate the speed of ticket fine penalt at podunksivile city
def main():
    #catching the error
    try:

        mile=0
        #prompting speed limit from the user
        speed=eval(input("Please Enter the speed  := "))
        limit=eval(input("Please Enter the speed limit := "))
        #restricting negative values
        if speed<0:
            print("Cannot accept negative values ")
        #checking  if the speed is illegal
        elif speed>limit:
            Total_fine=5*(speed-limit)+250
            #report to over speed limit
            print(" Your Speed Limit Was Illegal","\n"
                "The Amount of fine is : $", Total_fine 
                )
        else:
            print("Your speed limit is legal thanks")
     
    except NameError:
        print(" Something Error")


main()

    