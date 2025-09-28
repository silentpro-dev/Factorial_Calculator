def test_factorial(): 
    assert factorial(5) == 120 
    assert factorial(0) == 1 
    assert factorial(7) == 5040 
    print("All tests passed!") 

def factorial(n): 
    if n == 0: 
        return 1 
    else: 
        return n * factorial(n-1) 
    
def get_factorial_input(): 
    """ 
    Prompts the user for a non-negative integer and returns it. 
    Keeps prompting until a valid non-negative integer is provided. 
    """ 
    while True: 
        try: 
            # Get input from the user 
            num = int(input("Enter a non-negative integer for factorial computation: ")) 

            # Check if the number is non-negative 
            if num >= 0: 
                return num 
            else: 
                print("Please enter a non-negative integer.") 
        except ValueError: 
            print("Invalid input. Please enter a non-negative integer.") 

test_factorial()

number = get_factorial_input() 
print(f"The factorial of {number} is {factorial(number)}") 

