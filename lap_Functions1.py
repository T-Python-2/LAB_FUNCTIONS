#Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter 
# (if we give it 5 for example):

def numbers(x:int):
    
    '''This function takes 1 parameter of type int , then it prints out the result  '''

    while x != 0 :
        for i in range(x, 0, -1):
            print(i, end=" ")
        x = x - 1
        print("\n")


numbers(5)

print(numbers.__doc__)