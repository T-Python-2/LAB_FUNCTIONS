def numbers(number: int):
    '''   This function takes 1 parameters of type int and returns decreasing sequence in each round '''
    round = 1
    decreaseNumber = number
    while round <= number:
        print("\n")
        
        for n in range(decreaseNumber, 0 , -1):
            print(n, end= ' ')
             
        round +=1
        decreaseNumber-=1
        
numbers(5)
print()
print(numbers.__doc__)