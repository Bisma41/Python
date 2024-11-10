#########USE OF TYPE##########
'''
x=10
print(type(x))
y="bisma"
print(type(y))
z=10+20j
print(type(z))
xx=2.3+4.5j
print(type(xx))
a=["apple","mango"]
print(type(a))
b=("tea","Coffee")
print(type(b))
L=[10,20,30,40]
L=bytes(L)
print(type(L))#bytes must be in range of 0-256 and strings canot be added in this type
m=bytearray(L)#baytearray is mutable while bytes is immutable
print(type(m))
name=None
print(type(name))
#del name
print(name)
s={10,"candy",0.5}
print(type(s))
f=frozenset({10,"candy",0.5})
print(type(f))
'''

###########USE OF ID##########
'''
x=input()
print(id(x))
'''
########### BINARY FORM##########
'''
x=10
bin(x)
'''
###########OCTAL FORM##########
'''
x=7
oct(x)
'''
###########HEXADECIMAL FORM##########
'''
x=10
bin(x)
'''
###########COMPLEX DATA TYPE##########
'''
z=10+20j
print(type(z))
print(z)
##########PRINT CODE OF REAL AND IMAGINARY PARTS##########
real=z.real
print(real)
imag=z.imag
print(imag)
############################################################
xx=2.3+4.5j
print(type(xx))
print(xx)
r=xx.real
print(r)
i=xx.imag
print(i)
############ADDITION AND SUBRACTION OF COMPLEX NUMBERS##########
add=z+xx
print(add)
sub=z-xx
print(sub)
a=10
sum=a+z
print(sum)
'''
##########BOOLEAN DATATYPE##########
'''
a=True
b=False
print(type(a))
print(type(b))
##########TRUE REPRESENTS 1 AND FALSE REPRESENTS 0##########
#SO IF WE ADD TRUE+TRUE THEN I WILL BE 2 AND IF WE ADD TRUE +FALSE THEN IT WILL BE 1
x=True+True
print(x)
y=False+True
print(y)
z=False+False
print(z)
'''

############RANGE####################
'''
x=list(range(1,10))
print(x)
'''
#############DICTIONARIES##############
'''
D={'brand':'ford','model':'Mustang','year':1964}
print(D)
print(D["brand"])
print(type(D))
x=D.items()
print(x)
y=D.keys()
z=D.values()
print(y)
print(z)
D.update({"year":2000})
print(D)
#TO ADD VALUE IN DICTIONARY
D["color"]="red"
print(D)
#to remove value from dictionary
D.pop("year")
print(D)
'''
###################eval() function##########
#The eval() function is used to evaluate and execute the Python expression passed as a string.
'''
result = eval("2 + 3 * 4")
print(result)
'''
#############MULTIPLE INPUTS USING .SPLIT()#########
'''
string = input("Enter three numbers separated by spaces: ")#if wanna put comma among three of them then use .split(',')
num1, num2, num3 = string.split()
n=num1, num2, num3
print(num1, num2, num3)
'''






