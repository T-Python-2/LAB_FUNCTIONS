
def pattern(rows:int):
    for i in range(rows, 0, -1):
        for j in range(1, i+1):
            print(j, end=" ")
        
       




rows = int(input("Enter number of rows:"))
pattern(rows)
