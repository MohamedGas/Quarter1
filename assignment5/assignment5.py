#this program will determine the level of student at college 
#this program gives your level of education whether
# freshman ,sophomore , junior, senior

def main():
    #try except block
    try:
        #prompting the number of credit from user
        Ncredits=eval(input("Please enter the number of the credits you earned: "))
        gradelevel=""
        #this block checks if the number of credit earned is less thans 0
        if Ncredits<0:
            print("Number Of Credits Can't Less Than Zero ")
        else :
            #checking freshman 
            if Ncredits>=0 and Ncredits<=6:
                gradelevel="Freshman" 
            #checking sophonmore 
            elif Ncredits>=7 and Ncredits<=15:
                gradelevel="Sophomore" 
            #checking junior
            elif Ncredits>=16 and Ncredits<=25:
                gradelevel="Junior" 
            #checking Senior
           
            elif Ncredits>=26:
                gradelevel="Senior" 
            #reporting tothe user
            print("You're a ", gradelevel)

        
    # Excepting and catching errors
    except NameError as e :
        print (e)
    except ValueError as e :
        print(e)
    except SyntaxError as e:
        print(e)
    # because of zerodivisionerror is if the user accidentally input 5/0
    #5/5=1 also its fresh man but we have to restrict 5/0
    except ZeroDivisionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    
main()