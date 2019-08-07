#Week 3 Day 1: Importing Data from a File

import csv #importing the csv library allows us to read files

#CSV: Commas Separated Values
#RECORDS: row of the file, different types of data
#FIELDS: columns of the file, sets of same type of data (name, age, etc)

total_records = 0 #you should ALWAYS have a total records var and value (holds total # of records in the file)

total_salary = 0 #this holds the total salaries of all employees (this is a sum total variable)

#FIELD HEADER HINT below:
name = "NAME"
age = "AGE"
sal = "SALARY"

#if printed before loop, will only print ... before the loop :D
print("{0:5} \t\t {1:5} \t\t ${2:8}".format(name, age, sal))



#CONNECT TO THE ACTUAL FILE
#right click the file in folder view --> "Properties" and copy file location
#NOTE: this will NOT include the file name. you need to add that on your own
#these file locations are cAsE sEnSiTiVe and character/space sensitive

#flip '\' to '/'
#OPENING OF FILE------------------------------------------------------------
with open("C:/Users/KTRUCHON/Downloads/example.csv") as csvfile:

    #notice the ':' and minimize button next to with -- everything must be INDENTED now (until we are ready to "close" / "leave" the file)

    file = csv.reader(csvfile) #now the file we have connected is known in the program as 'file' (var .. sortof)

    #below is a FOR LOOP
    #for loops are loops -- repeated sequence of code
    #they continue based on a range instead of a condition

    for rec in file:
        
        total_records += 1 #total_records = total_records + 1
        #print("TOTAL RECORDS = ", total_records)
        #print the records of the file to see the for loop run
        #print(rec) #prints each record as a list ['Sam', '18', '32000'] 

        #TRICK OF THE TRADE below:
        name = rec[0]
        age = rec[1]
        salary = float(rec[2])

        #after above lines (storing field data into their own vars) you can now use/process the variables instead of rec[#]




        #print each field item for each record (not as a list, as their own values ... to print indiv value from list you must know the field position of the value: 0, 1, 2, 3, 4...)

        print("{0:5} \t\t {1:5} \t\t ${2:8.2f}".format(rec[0], rec[1], float(rec[2])))
        #**ALL DATA coming into a Python program is treated as STRING unless otherwise cast (why we are casting rec[2] so it appears as $$)

        #print("{0:5} \t\t {1:5} \t\t ${2:8.2f}".format(name, age, salary))

        #Process data within the file to add each employee's salary to total_salary
        
        total_salary += float(rec[2]) 
        #total_records = total_records + float(rec[2])
        #MUST CAST NUMERIC DATA! see line 42 above for "trick of the trade"

    
#END OF FILE---------------------------------------------------------------

#all processing of file must be done before the end of the for loop. if trying to process after the end, it will only handle the last record's data
#print("{0:5} \t\t {1:5} \t\t ${2:8.2f}".format(rec[0], rec[1], float(rec[2])))          
        
print("\n\nFinished Processing.\n\n\n")
print("-------------------------------\n")
print("TOTAL RECORDS: ", total_records)
print("ANNUAL PAYROLL: ${0:.2f}\n".format(total_salary))
print("-------------------------------\n\n\n\n")


    
