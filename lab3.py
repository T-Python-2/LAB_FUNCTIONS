

'''
#1 Create a function that takes 1 parameter of type int ,
 then it prints out the result formatted like the following patter (if we give it 5 for example):
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1 
'''

def patterns(row:int):
   ''' this function takes one parameter type of int and print the numbers in reverse pattern  '''


   for i in range(0, row+1):
    for j in range(row-i , 0,-1):
        print(j, end=' ')
            #new line
    print(" ")
    

patterns(5)
#2 Document the newly created function. describe what it does, then print the documentation.
print(patterns.__doc__)

