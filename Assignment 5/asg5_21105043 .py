from tkinter import *
import calendar

# I HAVE CREATED A MAIN WINDOW CALLED 'APP' AND WHEN YOU CLICK ON THE BUTTON OF THE
# RESPECTIVE QUESTION IN IT A NEW WINDOW WILL OPEN SHOWING YOU THE OUTPUT OF THAT QUESTION

# Question 1 - GST Calculator
def Q1():

    # configuring the window
    Q1 = Tk()
    Q1.title("Q1 GST Calculator")  # changing title
    Q1.geometry("300x400")  # changing size
    Q1.resizable(False, False)  # making window non-resizable
    Q1.config(bg="black")  # making background black

    # initial GST Calculator label
    l1 = Label(
        Q1, text="GST Calculator", fg="cyan", bg="black", font=("calibre", 20, "bold")
    )
    l1.pack()

    # original cost label
    l2 = Label(
        Q1, text="Original Cost", fg="white", bg="black", font=("calibre", 10, "bold")
    )
    l2.place(x=10, y=100)

    # net price label
    l3 = Label(
        Q1, text="Net Price", fg="white", bg="black", font=("calibre", 10, "bold")
    )
    l3.place(x=10, y=150)

    # defining a function for the command of button
    def gst_rate():

        # since denominator (original cost) cannot be zero
        if oc.get() == 0:
            l4["text"] = "Error!\nOriginal Cost\ncannot be zero"

        else:
            gst = (np.get() - oc.get()) * 100 / oc.get()
            # changing text of the empty label to display the result
            l4["text"] = f"GST Rate = {gst}"

    # empty label which will not be displayed until user enters values and clicks calculate button
    l4 = Label(Q1, text="", fg="red", bg="black", font=("bold"))
    l4.place(x=100, y=200)

    # taking entry from user and storing in 'float' data type
    oc = DoubleVar(Q1)  # np refers to net price
    e1 = Entry(Q1, textvariable=oc)
    e1.place(x=125, y=100)

    # taking entry from user and storing in float data type
    np = DoubleVar(Q1)  # oc refers to original cost
    e2 = Entry(Q1, textvariable=np)
    e2.place(x=125, y=150)

    # making a calculate button for the user to click after entering the values
    b1 = Button(Q1, text="  CALCULATE   ", command=gst_rate)
    b1.place(x=125, y=300)

    Q1.mainloop()


# Question 2 - Calendar
def Q2():
    # configuring the window
    Q2 = Tk()
    Q2.title("Q2 Calendar")  # changing title
    Q2.config(bg="black")  # making background black

    # initial label to ask user for input of year
    l1 = Label(
        Q2,
        text="Please enter the year for which you want to view the calendar",
        fg="white",
        bg="black",
        font=("arial", 10),
    )
    l1.pack(side=TOP)

    # taking entry from user and storing it in 'int' data type
    year = IntVar()
    e1 = Entry(Q2, textvariable=year)
    e1.pack(side=TOP)

    # empty label to separate entry and submit button
    l2 = Label(Q2, text="", bg="black")
    l2.pack(side=TOP)

    # defining submit function for the submit button
    def submit():
        yyyy = int(year.get())

        # changing text of the empty label to display the calendar
        l3["text"] = calendar.calendar(yyyy)

    # empty label which will display the calendar after user clicks submit button
    l3 = Label(Q2, text="", fg="white", bg="black", font=("consolas", 10, "bold"))
    l3.pack(side=BOTTOM)

    # submit button
    b1 = Button(Q2, text="Submit", command=submit)
    b1.pack(side=TOP, ipadx=10)

    Q2.mainloop()


# Question 3 - Calculator
def Q3():
    # configuring the window
    Q3 = Tk()
    Q3.title("Q3 Calculator")  # changing title
    Q3.geometry("170x230")  # changing size
    Q3.resizable(False, False)  # making the window non-resizable
    Q3.config(bg="black")  # making th background black

    # entry which will display the input and result
    ent = Entry(Q3, width=16, borderwidth=2)
    ent.grid(pady=10, row=0, sticky="w", padx=15)

    # defining function for delete or 'del' button
    def delete():
        a = ent.get()
        ent.delete(first=len(a) - 1, last="end")

    # defining function for equals or '=' button
    def result():
        if ent.get() == "":
            pass
        elif ent.get()[0] == "0":
            ent.delete(0, "end")
        else:
            exp = ent.get()
            exp = eval(
                exp
            )  # built-in 'eval' function will evaluate the expression in the input field/entry
            clear()
            ent.insert("end", exp)

    # defining function for clear or 'C' button
    def clear():
        ent.delete(0, "end")

    # 'C' button
    clean = Button(Q3, text="C", width=4, command=clear, bg="light blue", fg="black")
    clean.grid(row=0, sticky="w", padx=125)

    # '9' button
    button_nine = Button(
        Q3,
        text="9",
        width=3,
        command=lambda: ent.insert("end", "9"),
        borderwidth=2,
    )
    button_nine.grid(row=1, sticky="w", padx=15)

    # '8' button
    button_eight = Button(
        Q3,
        text="8",
        width=3,
        command=lambda: ent.insert("end", "8"),
        borderwidth=2,
    )
    button_eight.grid(row=1, sticky="w", padx=50)

    # '7' button
    button_seven = Button(
        Q3,
        text="7",
        width=3,
        command=lambda: ent.insert("end", "7"),
        borderwidth=2,
    )
    button_seven.grid(row=1, sticky="w", padx=85)

    # '+' button
    button_plus = Button(
        Q3,
        text="+",
        font=("calibre", 10),
        width=3,
        command=lambda: ent.insert("end", "+"),
        borderwidth=2,
    )
    button_plus.grid(row=1, sticky="e", padx=125)

    # '6' button
    button_six = Button(
        Q3,
        text="6",
        width=3,
        command=lambda: ent.insert("end", "6"),
        borderwidth=2,
    )
    button_six.grid(row=2, sticky="w", padx=15, pady=5)

    # '5' button
    button_five = Button(
        Q3,
        text="5",
        width=3,
        command=lambda: ent.insert("end", "5"),
        borderwidth=2,
    )
    button_five.grid(row=2, sticky="w", padx=50, pady=5)
    # '4' button
    button_four = Button(
        Q3,
        text="4",
        width=3,
        command=lambda: ent.insert("end", "4"),
        borderwidth=2,
    )
    button_four.grid(row=2, sticky="w", padx=85, pady=5)

    # '-' button
    button_minus = Button(
        Q3,
        text="--",  # added 2'-' to increase the size without distorting the whole column
        font=("calibre", 10),
        width=3,
        command=lambda: ent.insert("end", "-"),
        borderwidth=2,
    )
    button_minus.grid(row=2, sticky="e", padx=125, pady=5)

    # '3' button
    button_three = Button(
        Q3,
        text="3",
        width=3,
        command=lambda: ent.insert("end", "3"),
        borderwidth=2,
    )
    button_three.grid(row=3, sticky="w", padx=15, pady=5)

    # '2' button
    button_two = Button(
        Q3,
        text="2",
        width=3,
        command=lambda: ent.insert("end", "2"),
        borderwidth=2,
    )
    button_two.grid(row=3, sticky="w", padx=50, pady=5)

    # '1' button
    button_one = Button(
        Q3,
        text="1",
        width=3,
        command=lambda: ent.insert("end", "1"),
        borderwidth=2,
    )
    button_one.grid(row=3, sticky="w", padx=85, pady=5)

    # 'X' button
    button_multiply = Button(
        Q3,
        text="X",
        font=("calibre", 10),
        width=3,
        command=lambda: ent.insert("end", "*"),
        borderwidth=2,
    )
    button_multiply.grid(row=3, sticky="e", padx=125, pady=5)

    # '0' button
    button_zero = Button(
        Q3,
        text="0",
        width=3,
        command=lambda: ent.insert("end", "0"),
        borderwidth=2,
    )
    button_zero.grid(row=4, sticky="w", padx=15, pady=5)

    # '00' button
    button_double_zero = Button(
        Q3,
        text="00",
        width=3,
        command=lambda: ent.insert("end", "00"),
        borderwidth=2,
    )
    button_double_zero.grid(row=4, sticky="w", padx=50, pady=5)

    # '.' button
    button_dot = Button(
        Q3,
        text=".",
        width=3,
        command=lambda: ent.insert("end", "."),
        borderwidth=2,
    )
    button_dot.grid(row=4, sticky="w", padx=85, pady=5)

    # '/' button
    button_divide = Button(
        Q3,
        text="/",
        font=("calibre", 10),
        width=3,
        command=lambda: ent.insert("end", "/"),
        borderwidth=2,
    )
    button_divide.grid(row=4, sticky="e", padx=125, pady=5)

    # '=' button
    result = Button(
        Q3,
        text="=",
        width=8,
        command=result,
        bg="light blue",
        fg="black",
        borderwidth=2,
    )
    result.grid(row=5, sticky="w", padx=15, pady=5)

    # '%' button
    button_modulus = Button(
        Q3,
        text="%",
        font=("calibre", 10),
        width=3,
        command=lambda: ent.insert("end", "%"),
        borderwidth=2,
    )
    button_modulus.grid(row=5, sticky="e", padx=125, pady=5)

    # 'del' button
    delete = Button(Q3, text="del", width=3, command=delete, borderwidth=2)
    delete.grid(row=5, sticky="w", padx=85, pady=5)

    Q3.mainloop()


app = Tk()
app.title("Asg")
app.config(bg="black")
app.geometry("300x400")
button_Q1 = Button(app, text="Q1", command=Q1).pack(padx=15, pady=5, ipadx=15, ipady=5)
button_Q2 = Button(app, text="Q2", command=Q2).pack(padx=15, pady=5, ipadx=15, ipady=5)
button_Q3 = Button(app, text="Q3", command=Q3).pack(padx=15, pady=5, ipadx=15, ipady=5)
app.mainloop()


# Question 4 - Quick Sort
print("\n           Question 4\n")

# defining a function to divide the array into partitions
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    # creating a loop
    while True:

        # moving the high pointer to one lower value
        while low <= high and array[high] >= pivot:
            high -= 1

        # moving the low pointer to one higher value
        while low <= high and array[low] <= pivot:
            low += 1

        # swapping the low & high values
        if low <= high:
            array[low], array[high] = array[high], array[low]

        # exit the loop if low>=high
        else:
            break

    # swapping the start/low & high values
    array[start], array[high] = array[high], array[start]

    return high


# defining 'quick_sort' function
def quick_sort(array, start, end):
    if start >= end:
        return

    # partitioning the array
    p = partition(array, start, end)

    # implementing quick sort function for array before 'pivot' value
    quick_sort(array, start, p - 1)

    # implementing quick sort function for array after 'pivot' value
    quick_sort(array, p + 1, end)


s = input("Enter the marks of students separated by commas \n")
l = s.split(",")

# creating an empty list 'nl'
nl = []  # nl refers to new list

# creating a loop to store all elements in 'int' type in the empty list
for i in l:
    nl.append(int(i))

# calling the quick_sort function
quick_sort(nl, 0, len(nl) - 1)

print(f"\nSorted List : {nl}")


# Q5 - Binary Search
print("\n           Question 5\n")


def binsearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # if x is greater than middle value, then check x in right half
        if arr[mid] < x:
            low = mid + 1

        # if x is smaller than middle value, then check x in left half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at the middle of the array
        else:
            return mid

    # just to print error message if element is not present
    return -1


inp = input("Enter the marks of students separated by commas \n")
input_arr = inp.split(",")

# creating an empty list 'new_arr'
new_arr = []

# creating a loop to store all elements in 'int' type in the empty list
for i in input_arr:
    new_arr.append(int(i))

# Q5 (a)
print("\nQ5 (a)")

# Sorting the arr
sorted_arr = sorted(new_arr)
print("Sorted Array : ", sorted_arr)

# Q5 (b)
print("\nQ5 (b)")

# Taking input of element from user
n = int(input("Please enter the number whose index & occurrence you want to find : "))

# calling function 'binsearch'
result = binsearch(sorted_arr, n)

# print index / error message
if result != -1:
    print("Element is present at index : ", result)
else:
    print("Error! Element is not present in array")


# Q5 (c)
print("\nQ5 (c)")

# print number of occcurrences of element entered by user
print(f"Number of occurrences of element {n} is : ", new_arr.count(n))
