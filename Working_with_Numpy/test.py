import numpy as np
#function that takes a 2D NumPy array as input and returns a new array where: All even numbers are squared. All odd numbers are replaced by -1. 
def squared_even_odd_1(arr):
    print(f"\nThe new array is: \n {np.where(arr%2==0,arr**2,-1)}")
# function to generate random array
def gen_random_array():
    gen_row=int(input("How many rows is your array?: "))
    gen_col=int(input("How many colums is your array?: "))
    # gen_col=input("What is the range value of your element? e.g (Range btw 1 to 51) many colums is your array?: ")
    array= np.random.randint(1,51,size=(gen_row,gen_col))
    print(f"\nYour Generated Array is: \n{array}")
    return array

# function to enter your Array elements yourself
def input_your_element():
    gen_row=int(input("How many rows is your array?: "))
    gen_col=int(input("How many colums is your array?: "))
    # define array
    array = np.zeros((gen_row, gen_col), dtype=int)
    for row in range(gen_row):
        for col in range(gen_col):
            # loop to make sure only integer is inserted
            while True:
                try:
                    value=int(input(f"Enter element for row:{row}, col:{col} is your array?: ") )
                    array[row,col]= value
                    break
                except ValueError:
                    print("Please enter only integer numbers")
            # end of while loop
    print(f"\nYour Array is: \n{array}")
    return array

#  Driver code 
while True:
    print("========================================")
    print("Do your want to use random array or enter your own elements?: ")
    print("1. Generate")
    print("2. Input your owner element")
    print("3. Exit")
    print("")
    choice= input("Enter your choice: ")
    print("")

    if choice =='1':
        array=gen_random_array()
        squared_even_odd_1(array)
    elif choice=='2':
        array=input_your_element()
        squared_even_odd_1(array)
    elif choice== "3":
        break
    else:
        print("Enter valid choice between 1 to 3: ")
   

print("")
print("========================================")
print("========Closing... Thank you============")
print("========================================")

   
