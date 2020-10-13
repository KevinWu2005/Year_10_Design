import math


number1 = int(input("Enter a value: "))
number2 = int(input("Enter another value: "))
#we will learn techniques to get the right input
numbers = [5,2,8,1,3,7]

print (numbers)
print (numbers[2]) #prints 8

for i in numbers: 
	print (i, end=" ") #prints all numbers in the list
print()

answer = number1 * number2
print(answer)

answer = number1 / number2
print(answer)
print(math.floor(answer))
print(math.ceil(answer))
print(math.trunc(answer))

if number1 % number2 == 0:
	print (str(number1) + ' is a multiple of ' + str(number2))
elif number2 % number1 == 0:
	print (str(number2) + ' is a multiple of ' + str(number1))
else:
	print (str(number1) + ' is not a multiple of ' + str(number2))

counter = 0
while counter < 10:
	print (counter)
	counter += 2

for counter in range (10,0,-2): #if you wanted to include 0 change 0 to -1
	print(counter)






