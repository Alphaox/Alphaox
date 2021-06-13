#Create a program that asks the user for a number 
#and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, 
#it is a number that divides evenly into another number. /#

num = int(input("please enter a num to divide: "))
listrange = list(range(1,num+1))
dividelist = []

for number in listrange:
  if num % number == 0:
    dividelist.append(number)
print(dividelist)
