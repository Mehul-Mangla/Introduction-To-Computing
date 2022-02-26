# Assignment 4


# Question 1
print("\n           Question 1\n")

# defining a function for Tower of Hanoi problem
def TowerOfHanoi(n, source="A", destination="C", extra_rod="B"):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    TowerOfHanoi(n - 1, source, extra_rod, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    TowerOfHanoi(n - 1, extra_rod, destination, source)


# taking input form user for number of disks
n = int(input("Enter the number of disks : "))
print()  # just to print empty line

if n == 0:
    pass
else:
    TowerOfHanoi(n)

###############################################################################

# Question 2
print("\n           Question 2\n")


# taking input from user for number of rows
n = int(input("Enter the number of rows : "))

# By Loop Method
print("\nBy Loop Method - \n")
for i in range(1, n + 1):

    # printing spaces on the left side
    print("  " * (n - i), end="")

    # since first number is always 1
    x = 1
    for j in range(1, i + 1):

        print(x, end="   ")

        # using formula for binomial coefficients
        # nCr = n!/((n-r)!*r!)
        x = x * (i - j) // j

    print()  # just to print empty line


# By Recursion Method
print("\nBy Recursion Method - \n")

# defining pascal function for pascal's triangle
def pascal(n, actual_n=n):
    if n == 0:
        return

    pascal(n - 1, actual_n)

    # printing spaces on the left side
    print("  " * (actual_n - n), end="")

    # since first number is always 1
    num = 1
    for i in range(1, n + 1):

        print(num, end="   ")

        # using formula for binomial coefficients
        # nCr = n!/((n-r)!*r!)
        num = num * (n - i) // i

    print()  # just to print empty line


# calling pascal function
pascal(n)


################################################################################

# Question 3
print("\n           Question 3\n")

# defining a function to print quotient & remainder
def qnr():

    # using built-in function 'divmod' to assign values to c,d
    c, d = divmod(a, b)

    # built-in function to ensure remainder is never negative
    d = abs(d)

    # printing the result
    print("\nQuotient is : ", c)
    print("Remainder is : ", d)


# taking input from user
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# to ensure that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non-zero number : "))

# calling the function
qnr()


# Q3 (a)
print("\nQ3 (a)")

# using the built-in function 'callable'
print(callable(qnr))

# --------------------------------------------------------

# Q3 (b)
print("\nQ3 (b)")

c, d = divmod(a, b)

# built-in function to ensure remainder is never negative
d = abs(d)

l = [c, d]
print(all(l))

# --------------------------------------------------------

# Q3 (c)
print("\nQ3 (c)")

l.extend([4, 5, 6])
print("After adding 4,5,6 : ", l)

filtered = filter(lambda n: n > 4, l)

print("Values greater than 4 are : ", list(filtered))


# --------------------------------------------------------

# Q3 (d)
print("\nQ3 (d)")

s = set(l)
print(s)

# --------------------------------------------------------

# Q3 (e)
print("\nQ3 (e)")

fs = frozenset(s)
print("Immutable set : ", fs)

# --------------------------------------------------------

# Q3 (f)
print("\nQ3 (f)")
m = max(fs)
print(hash(str(m)))


################################################################################

# Question 4
print("\n           Question 4\n")

# creating class student
class Student:

    # defining init function
    def __init__(self, Name, Roll_No):
        self.Name = Name
        self.Roll_No = Roll_No
        print("Student created")

    # defining del function
    def __del__(self):
        print("Student deleted")


# storing data in class
s1 = Student("abc", 5001)
s2 = Student("lmn", 5004)
s3 = Student("xyz", 5007)

print()  # just to print empty line

# calling del function to destroy an object
del s2

################################################################################

# Question 5
print("\n           Question 5\n")

# creating class called Employees
class Employees:

    # defining init function
    def __init__(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary

    # defining a function to print the details of all employees
    def record(self):
        print("Employee Name : ", self.Name)
        print("Employee Salary : ", self.Salary)
        print("\n")


# storing data of all employees
e1 = Employees("Mehak", 40000)
e2 = Employees("Ashok", 50000)
e3 = Employees("Viren", 60000)

# printing thr record
print("Record of all employees\n")
e1.record()
e2.record()
e3.record()


# Q5 (a)
print("Q5 (a)")

# updating salary of Mehak
print("Updated record of employee Mehak\n")
e1.Salary = 70000
e1.record()

# --------------------------------------------------------

# Q5 (b)
print("Q5 (b)")

# deleting record of Vivek
del e3
print("Record of Vivek deleted")

################################################################################

# Question 6
print("\n           Question 6\n")


# defining a function
def friendship(w1, w2):

    # making all letters lowercase
    w1 = w1.lower()
    w2 = w2.lower()

    # checking whether all the same letters are used in both words
    if sorted(w1) == sorted(w2):
        print("Your friendship is real")
    else:
        print("Your friendship is fake")


# taking input from users
w1 = input("Friend 1, please enter your word : ")
w2 = input("Friend 2, please enter your word : ")

print()  # just to print empty line

# calling function
friendship(w1, w2)
