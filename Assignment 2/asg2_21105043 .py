#Assignment 2


# Question 1
print("           Question 1\n")
sen= 'Python is a case sensitive language'
print(sen)
#Q1 (a)
print('Length= ',len(sen))
#Q1 (b)
print('Reverse= ',sen[::-1])
#Q1 (c)
new_sen= sen[10:26]
#Q1 (d)
print(sen[:9],'object oriented',sen[27:])
#Q1 (e)
index= sen.find('a')
print('Index= ',index)
#Q1 (f)
print(sen.replace(' ',''))

#Question 2
print("\n           Question 2\n")
name = 'Mehul Mangla'
sid = 21105043
c = 'ECE'
d = 9.9
name1='Hey, %s here!'%(name)
print(name1)
print('My SID is %d'%(sid))
print('I am from %s department and my CGPA is %f'%(c,d))

#Question 3
print("\n           Question 3\n")
a = 56
b = 10
print('a&b= ', a&b)
print('a|b= ', a|b)
print('a^b= ', a^b)
print('a<<2= ', a<<2)
print('b<<2= ', b<<2)
print('a>>2= ', a>>2)
print('b>>4= ', b>>4)

#Question 4
print("\n           Question 4\n")
x = int(input('1st number=? '))
y = int(input('2nd number=? '))
z = int(input('3rd number=? '))

if (x>y) and (x>z):
    print('Greatest number: ',x)
elif (y>x) and (y>z):
    print('Greatest number: ',y)
elif (z>x) and (z>y):
    print('Greatest number: ',z)

#Question 5
print("\n           Question 5\n")
sentence = str(input('Enter a sentence: '))
if 'name' in sentence:
    print('Yes')
else:
    print('No')

#Question 6
print("\n           Question 6\n")
l= int(input('Enter first side length '))
m= int(input('Enter second side length '))
n= int(input('Enter third side length '))
if (l+m)<n or (m+n)<l or (l+n)<m:
    print('No')
else:
    print('Yes')

