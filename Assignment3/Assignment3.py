#this program will display list of students with firstname , lastname, grade of the student from 
#-> file in a directory using of the name of the file 
#-> it allows to add the grades when user get the student data

def main():
    
    #this a display message 
    print('<:-Welcome this program will display list of students name and their grade from a file and You Will'+
     ' Add Grades :->','\n')
    #requirements 
    print('!!-<>- It Requires To Know The Name of The File With Extension .dat -<>-!!','\n')
    ######## READING DATA ################
    #GRADING SCORE
    grade_range=[]
    #from 0-60 its gonna be F
    for n in range(60):
	    grade_range.append('F') 
    #from 60-69 its gonna be D
    for n in range(60,70):
	    grade_range.append('D') 
    #from 70-69 its gonna be C
    for n in range(70,80):
	    grade_range.append('C') 
    #from 80-89 its gonna be B
    for n in range(80,90):
	    grade_range.append('B') 
    #from 90-100 its gonna be A
    for n in range(90,101):
	    grade_range.append('A') 
    

    #prompt user from the file name
    filename=input('Please Enter Name Of The File With Thr Extension Of The File-: ')
    #Opening The File with the mode
    input_file=open(filename,'r')
    #open another score file  
    list_students_with_grade=[]
    
    
    for students in input_file.readlines():
        #get the scores
        grd=int(students[-3:].strip())
       
        x=students+grade_range[grd]
       #adding to the list
        
        list_students_with_grade.append(x.replace("\n"," "))
        
    #print record after graded
    print (list_students_with_grade)
    
    #close the files
    input_file.close()
    

    ########### WRITING DATA #############################

     
    #opening grade.dat file to able write a data of the students    
    grade_fname='grade.dat' 
    outfile_grade=open(grade_fname,'w')
    #Creating an empty accumalate variable to hold new data
    
    
    #Writing the data on the file
    outfile_grade.writelines(list_students_with_grade)      
    #Closing the file
    outfile_grade.close()
    #report to user that data has been successfully submitted
    print("Successfully Saved Data")

 
main()

