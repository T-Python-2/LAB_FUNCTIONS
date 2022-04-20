
def decrement_function(x:int):
    ''' This function takes one parameter of type int and print each row in decrementation till number 1, then decrement the number by 1
    and print it in the next line '''
    for i in range(0, x + 1):
        for j in range(x - i, 0, -1):
            print(j, end=' ')
        print()

    for i in range(x + 1, 0, -1):    
        for j in range(0, i - 1):  
            print("*", end=' ')  
        print(" ")  

decrement_function(5)
print(decrement_function.__doc__)




