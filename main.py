
def pattern(rows:int):
    '''print number as halve pyramid'''
    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        
        print("\n")

#not working but try to use recrsive function
'''
def pattern2(rows:int):
    while rows>=0:
        if rows == 0:
            break
        for i in range(1, rows):
            print(i, end=" ")
        print("\n")
        pattern2(rows-1)
        
'''
            
        
    
rows = int(input("Enter number of rows:"))
pattern(rows)
print(pattern.__doc__)

