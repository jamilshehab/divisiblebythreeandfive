#enter the number assigned as a variable x 
x=int(input("enter a number : "))

#we run through the numbers by creating a loop 
for number in range(1,x):
    #check the numbers if they are divisible by 3 and 5
    if number % 3==0 and number % 5 == 0:    
       #display them on the output
       print("the numbers that are divisible by 3 and 5 are : ", number)
