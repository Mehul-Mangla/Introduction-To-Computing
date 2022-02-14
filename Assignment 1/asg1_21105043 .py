#Assignment 1


# Question 1
print("           Question 1")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
avg = (num1+num2+num3)/3
print("Average of the three numbers = ",avg)
print() #Just to add a blank line

# Question 2
print("           Question 2")
g_i = float(input("Enter your Gross Income: ")) #g_i stands for gross income
n_d = int(input("Enter the number of dependents: ")) #n_d stands for number of dependents
txb_i = g_i - 10000 - (3000 * n_d) #txb_i stands for taxable income
tax = (txb_i * 0.2)
print("Tax = ", tax)
print() #Just to add a blank line

# Question 3
print("           Question 3")
print("Student= [SID, Name, Gender, Dept. Name, CGPA]")
std=[123,'Ajay', 'M', 'ECE', 8.7] 
print("Student=",std)
print() #Just to add a blank line

# Question 4
print("           Question 4")
print("Marks of five students")
marks= [89,53,18,45,56]
print("List before sorting ", marks)
marks.sort()
print("List after sorting ", marks)
print() #Just to add a blank line

# Question 5
print("           Question 5")
color= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Original List: ", color)
print() #Just to add a blank line
#Q5 (a)
print("Q5 (a)")
color.pop(3)
print(color)
print() #Just to add a blank line

#Q5 (b)
print("Q5 (b)")
color[3:5]=['Purple']
print(color)
