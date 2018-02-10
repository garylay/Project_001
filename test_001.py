'''print ("lai qianwei")
print ("1978-04-22")

print ("1+1=",1+1)
print ("3-1=",3-1)
print ("2*5=",2*5)
print ("12/2=",12/2)
print ("12//5=", 12//5)
print ("3**3=",3**3)
print ("13%4=",13%4)


print ("test")
my_input = input("what is your name ?\n")
print ("my name is ",my_input)


number = float(input("type in a number :"))
integer = int(input("type in a integer :"))
test = input("type in a string :")

print("number type =",type(number))
print("integer type =",type(integer))
print("test type =",type(test))

print("test**3 =",test*3)
print("test**3 =",test+'444')


str1 = input("str1:")
str2 = input("str2:")
num1 = float(input("num 1:"))
num2 = float(input("num 2:"))

print ("str1 = ",str1)
print ("str2 = ",str2)
print ("num1 = ",num1)
print ("num2 = ",num2)
print (str1+str2)
print (num1*num2)

a = 0
while a < 10 :
    a+=2
    print(a)


mypassword = "test"
password = str()
count = 1
while count < 5 :
    password = input("password:")
    count+=1
    if password == mypassword :
        print ("password is correct")
    else :
        print ("xxxx")

logname=input("logname:")
password=input("password:")

command = None
input1 = None
input2 = None
while command != "lock" :
    command = input("input your command:")
while input1 != logname :
    input1 =input("what is your name :")
while input2 != password :
    input2 = input("what is your password")

print ("welcome back")'''


    name = input("your name :")

    if name == 'lai' :
        print("this is a nice name")
    elif name == 'one' :
        print("one is no.1")
    elif name == "two" :
        print("tow is no.2")
    else :
        print ("you have a nice name")