#Functions_LAB

def print_triangle(len:int) -> str :
    '''This function takes an integer number as an input, and outputs a pattern (triangle) of a specific length based on the entered input.'''
    track = len
    while track > 0 :
        for num in reversed(range(track+1)):
            if num == 0:
                print()
                break
            print(num,end=" ")
        track -=1
            
print_triangle(int(input("enter the length of the triangle ")))
print(print_triangle.__doc__)