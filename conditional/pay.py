#pay.py
# this program calculates the how much you earn if you worked over 40 hrs
def main(): 
    hour=eval(input("Please enter the hours you worked := "))
    rate=float(input("Please enter hourly rate:= "))
    total=rate*hour
    if hour>40:
        total=total + (rate+rate/2)*(hour-40)
        print(" The amount is : ", total)
    else:
        print(" Your Amount is : ",total)


main()
