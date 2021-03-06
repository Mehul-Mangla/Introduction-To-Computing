#           Question 1
print("Question 1\n")
string= str(input("Enter a string \n"))

#To check whether user has entered a word or sentence
new_str=string.lower().split(" ")
occ = {}

#If user has entered a word
if len(new_str)==1:
    for i in string.lower():
        if i in occ: 
            occ[i] += 1
        else: 
            occ[i] = 1
    # Printing result  
    print ("Occurrence of all characters in the given string is :\n "+ str(occ))

#If user has entered a sentence
elif len(new_str)>1:
    for i in new_str:
        if i in occ: 
            occ[i] += 1
        else: 
            occ[i] = 1
    # Printing result  
    print ("Occurrence of all words in the given string is :\n "+ str(occ))



#           Question 2
print("\nQuestion 2\n")
# Input from user
date=str(input("Please enter a date from 1st Jan 1800 to 31st Dec 2025 \nin the format dd/mm/yyyy: "))
nd = date.split("/")

day=int(nd[0])
month=int(nd[1])
year=int(nd[2])

# Loop to check if date>28 in February when year is not a leap year
while year%4!=0 and month==2 and day>28:
    date=str(input("Please enter a valid date: "))
    nd = date.split("/")
    day=int(nd[0])
    month=int(nd[1])
    year=int(nd[2])

#Special case for 1800 and 1900 because within our range they are the only years which are divisible by 4 but are still not a leap year
while month==2 and day>28 and year == 1800 or year == 1900:
    date=str(input("Please enter a valid date: "))
    nd = date.split("/")
    day=int(nd[0])
    month=int(nd[1])
    year=int(nd[2])
    
# Loop to check if date is valid and in the given range        
while day not in range(1,32) or month not in range(1,13) or year not in range(1800,2026):
    date=str(input("Please enter a valid date in the range given above: "))
    nd = date.split("/")
    day=int(nd[0])
    month=int(nd[1])
    year=int(nd[2])

# For leap year
if year %4 and year %400 == 0:
    leap_year = True
else:
    leap_year = False

# For months with 31 days
if month in (1,3,5,7,8,10,12):
    month_length = 31
# Special case for February
elif month == 2:
    if leap_year:
        month_length = 29
    else:
        month_length = 28
# For months with 30 days
else:
    month_length = 30

# For dates less than 31
if day < month_length:
    day+=1
# If date is 31
else:
    day = 1

#Special case for 31st December
    if month == 12:
        month = 1
        year+=1
# Next month if date is 31 and any month except December
    else:
        month+=1

print("The next date is %d/%d/%d "%(day,month,year))



#        Question 3
print("\nQuestion 3\n")

#Input from user and storing in a list
l1=list(input("Please enter the numbers separated by spaces \n").split())
l2=list()
l3=list()
#Loop to store each element and its square in two different lists
for i in l1:
    l2.append(int(i))
    l3.append(int(i)**2)
#Using zip function and printing list with elements as (z,z^2) [z^2 means square of z]
print(list(zip(l2,l3)))


    

#           Question 4
print("\nQuestion 4\n")

#Ask user to enter their grades
g=int(float(input("Please enter your grade points: ")))

#Check if entered grade is within range
if g<4 or g>10:
    print("Error! Please enter grade between 4 and 10")

#Creating a dictionary and storing values in it
d=dict()
d[10]= "Your Grade is 'A+' and Outstanding Performance"
d[9]="Your Grade is 'A' and Excellent Performance"
d[8]="Your Grade is 'B+' and Very Good Performance"
d[7]="Your Grade is 'B' and Good Performance"
d[6]="Your Grade is 'C+' and Average Performance"
d[5]="Your Grade is 'C' and Below Average Performance"
d[4]="Your Grade is 'D' and Poor Performance"

#Print the result for the given grade
print(d[g])
    
    
        
#           Question 5
print("\nQuestion 5\n")
s='ABCDEFGHIJK'

#Initialize variables for the loop
i=13
j=1

#Creating a loop to print the inverted pyramid
while i>1:
    print(" "*j,s[:i-2]) #print(" "*j) is used to add the required spaces

    #Updating values
    i-=2
    j+=1



#           Question 6
print("\nQuestion 6")

#Asking if user wants to enter their details
x=str(input("\nDo you want to enter your details?\nUse Y for Yes & N for No\n"))
d1=dict()
#d2=dict()

#Loop if user enters yes
while "Y" in x or "y" in x:
    name = str(input("Enter your name: "))
    sid = int(input("Enter your SID: "))
    d1[name] = sid #Dictionary with name as key & sid as value
    #d2[sid] = name #Dictionary with sid as key & name as value

    #Asking if the user wants to enter details again
    x=str(input("\nDo you want to enter your details?\nUse Y for Yes & N for No\n"))

#Q6 (a)
print("\nQ6 (a)\n",d1)

#Q6 (b)
print("\nQ6 (b)\n",sorted(d1.items()))

#Q6 (c)
lst=sorted((value, key) for (key,value) in d1.items())
d1=dict([(k,v) for v,k in lst])
print("\nQ6 (c)\n",d1)

#Q6 (d)
#Define a function to return key(name) from value(SID)
def key_from_value(stud):
    for key, value in d1.items():
         if stud == value:
             return key
 
    return "SID doesn't exist"

#Asking the user for sid of student whose details have to be found
stud=int(input("\nPlease enter the SID of the student: ")) 
print("Name: ",key_from_value(stud),"\nSID: ",stud)



#           Question 7
print("\nQuestion 7\n")
nt = int(input("Please enter the number of terms: ")) #nt stands for number of terms
l=list()
# First two terms
a1, a2 = 0, 1
count = 0

# Check if the number of terms is valid
while nt <= 0:
   nt=int(input("Please enter a positive integer: "))
# If there is only one term
if nt == 1:
   print("Fibonacci sequence upto %d term(s) is"%nt)
   print(a1)


# Generate fibonacci sequence
else:
   print("Fibonacci sequence upto %d term(s) is"%nt)
   while count < nt:
       print(a1)
       a_n = a1 + a2
       l = l + [a1]
       #Updating values
       a1 = a2
       a2 = a_n
       count += 1

#Printing average
if nt==1:
   print("Average is: 0")
else:
   print(f'Average is: {sum(l)/len(l):.2f}') #.2f is used to print output upto 2 decimal places



#           Question 8
print("\nQuestion 8\n")
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

# Q8 (a)
print("\nQuestion 8(a)")
print(set1^set2)

# Q8 (b)
print("\nQuestion 8(b)")
# Union of all sets - Elements which are common in any 2
set4=(set1|set2|set3)-(set1&set2)-(set2&set3)-(set1&set3) 
print(set4)

# Q8 (c)
print("\nQuestion 8(c)")
set5=((set1&set2)|(set2&set3)|(set3&set1))
print(set5)

# Q8 (d)
print("\nQuestion 8(d)")
set6 = set()
for i in range(1,11):
    if i not in set1:
        set6 = set6 | {i}
print(set6)

# Q8 (e)
print("\nQuestion 8(e)")
set7 = set()
for i in range(1,11):
    if i not in set1|set2|set3:
        set7 = set7 | {i}
print(set7)



    
