## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):
'''
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
'''
### Document the newly created function. describe what it does, then print the documentation. 

def tr(rows:int):
    
   
    for i in range(0, rows + 1):
        for a in range(rows - i, 0, -1):
            print(a, end=' ')
        print()
tr(5)










