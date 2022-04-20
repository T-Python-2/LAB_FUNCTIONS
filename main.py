

def numbers(rows:int):
    ''' This function takes 1 parameter of type int and print out the result in reversed number pattern '''
    for i in range (0 ,rows+1):
        for j in range(rows-i ,0,-1):
            print(j, end=" ")
        print()

numbers(5)
#acces the documentation of a function
print(numbers.__doc__)
 
